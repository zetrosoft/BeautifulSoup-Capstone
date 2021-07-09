from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests
from datetime import datetime

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.exchange-rates.org/history/IDR/USD/T')
soup = BeautifulSoup(url_get.content,"html.parser")

table = soup.find('table')

#for i in range(1, len(tr)):
#insert the scrapping process here
    
    #temp.append((____,____)) 

temp = [] #initiating a tuple
baris = table.find_all('tr')

for tr in baris:
    td = tr.find_all('td')
    row =[i.text for i in td]
    temp.append(row)
    
temp

temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp,columns =['ExchangeDate','DayName','Price','Remarks'])

#insert data wrangling here
#cleaning data
df = df.dropna(how='any')
#TODO :
# Change ExchangeDate to datetime64 data type
df['ExchangeDate'] = df['ExchangeDate'].astype('datetime64')
# Change DayName to Category data type
df['DayName'] = df['DayName'].astype('category')
# # Remove or split Price column for IDR and change Price to float64 data type
df['Price'] = df['Price'].str.replace('IDR','')
df['Price'] = df['Price'].str.replace(',','')
df['Price'] = df['Price'].astype('float64')

#for visualisation only
df['ExDate'] = df['ExchangeDate'].dt.strftime('%d-%m-%Y')
# Drop remark columns - not used data
df=df.drop('Remarks',axis=1)

#wrangling
#Create Exchangedate as column index
df = df.set_index('ExchangeDate')
#end of data wranggling 

@app.route("/")
def index(): 

	#for fill card column
	idr_mean = '{:,.2f}'.format(df["Price"].mean().round(2))
	card_data = f'$1 USD = {idr_mean} IDR'

	#for fill Report Periode 
	periode_from = datetime.strptime (f'{df.reset_index()["ExchangeDate"].min()}',"%Y-%m-%d %H:%M:%S")
	periode_to = datetime.strptime(f'{df.reset_index()["ExchangeDate"].max()}',"%Y-%m-%d %H:%M:%S")
	periode = f'Periode : {periode_from.strftime("%d %b %Y")} to {periode_to.strftime("%d %b %Y")}'
	# generate plot
	min_rate	= df.min()[['Price','ExDate']].to_list()
	min_val 	= '{:,.2f}'.format(min_rate[0])
	avg_rate 	= df.agg('mean').to_list()
	avg_val		= '{:,.2f}'.format(avg_rate[0])
	max_rate	= df.max()[['Price','ExDate']].to_list()
	max_val 	= '{:,.2f}'.format(max_rate[0])
	xLabel = f'Min = {min_val}({min_rate[1]}) - Avg = {avg_val} - Max ={max_val}({max_rate[1]})'
	ax = df.plot(
		x='ExDate',
		y='Price',
		figsize = (20,9),
		xlabel=xLabel,
		ylabel='Exchange Rate',
		grid=True,
		color='Red'
	)
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	df['Periode'] 	= df.index.to_period('M')
	last_period		= df.index.max()
	df_30 = df[df.index >= (last_period + pd.Timedelta(days=-60))]
	#generate plot2
	min_rate	= df_30.min()[['Price','ExDate']].to_list()
	min_val 	= '{:,.2f}'.format(min_rate[0])
	avg_rate 	= df_30.agg('mean').to_list()
	avg_val		= '{:,.2f}'.format(avg_rate[0])
	max_rate	= df_30.max()[['Price','ExDate']].to_list()
	max_val 	= '{:,.2f}'.format(max_rate[0])
	xLabel = f'Min = {min_val}({min_rate[1]}) - Avg = {avg_val} - Max ={max_val}({max_rate[1]})'
	ax2 = df_30.plot(
		x='ExDate',
		y='Price',
		figsize = (20,10),
		xlabel=xLabel,
		ylabel='Exchange Rate',
		grid=True,
		color='Blue',
		kind='line'
	)

	figfile2 = BytesIO()
	plt.savefig(figfile2, format='png', transparent=True)
	figfile2.seek(0)
	figdata_png2 = base64.b64encode(figfile2.getvalue())
	plot_result2 = str(figdata_png2)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data,
		plot_result=plot_result,
		plot_result2=plot_result2,
		periode = periode
		)


if __name__ == "__main__": 
    app.run(debug=True)
