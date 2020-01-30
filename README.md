# Web-Scrapping using Beautifulsoup

This is developed as one of Algoritma Academy Data Analytics Specialization using capstone Projects. The deliverables of this project is doing a simple web scrapping to extract some information from a table. For step by step guide, you can check out my git [Click here](https://github.com/t3981-h/Webscrapping-with-BeautifulSoup "Webscrapping with Beautiful Soup"). We will also utilize the simple flask dashboard to do a simple visualisation from the data we got.

## Dependencies

- beautifulSoup4
- pandas
- flask
- matplotlib

or you can simply install using the requirements.txt

```python
pip install -r requirements.txt
```

## Rubics

- Environment preparation (2 points)
- Finding the right key to scrap the data  & Extracting the right information (6 points)
- Creating data frame & Data wrangling (6 points)
- Implement it on flask dashboard (2 points)


## What You Need to Do

* You can clone this repo.
* File in this repo is a skeleton that you can use for making a simple flask dashboard.
* You can fill the blank part at the skeleton.
* You can try to scrap the information from this sites : (link)
* fill function `scrap` with scrapping process. You need fill this part with the key to get the infromation from the webpage.

```python
table = soup.find(...)
tr = table.find_all(...)
```

* Then you can extract the infromation per row with looping.
* Save here to save your scrapping data as csv.

```python
df = pd.DataFrame(name of your tupple, columns = (name of the columns))
```

* Lastly you can use your scrap function at function for making table and chart. Fill the parameter with the link.

```python
df = scrap(...) #insert url here
```

* You also can play with the ui at `index.html` which you can follow the comment to know which part you can change.

### The Final Mission 

Pada captsone kali ini, Bapak Ibu bisa memilih beberapa website ini untuk discrapping. 

- Data inflasi Indonesia dari bi.go.id/id/moneter/inflasi/data

- Data Harga kereta api dari Jakarta menuju ke Bandung hari ini dari tiket.com/kereta-api

- Data product lipstik dari Bukalapak.com

Silahkan pilih 1 aspek yang Bapak Ibu ingin visualisasikan. 

Happy learning~
