from bs4 import BeautifulSoup as soup
import requests
import  time

year = '2022' #str(input("Enter the year : "))
month = '02' #str(input("Enter the month : "))
start_time = time.time()

url = "https://www.imdb.com/movies-coming-soon/"+year+"-"+month+"/"
html_page = soup(requests.get(url).text , 'lxml')
for x in html_page.find_all('div',class_='image'):
    link = "https://www.imdb.com/"+x.a['href']+"?ref_=cs_ov_i"
    title = x.a.div.img['title']
    poster = x.a.div.img['src']
    output = [title,link,poster]
    print(output)
print("--- %s seconds ---" % (time.time() - start_time))

"""



url = 'https://paytm.com/movies/upcoming-movies'
page = soup(requests.get(url).text, 'lxml')
links_with_text = []
for a in page.find_all('a', href=True):
    if a.text:
        links_with_text.append(a['href'])

linfil = links_with_text[14:246]
linfil = [i.split('/') for i in linfil]
linfil = [[i[-1]] for i in linfil]
for i in range(0,len(linfil)):
    for j in linfil[i]:
        linfil[i] = j.split('-')

for i in range(0,len(linfil)):
    linfil[i] = [linfil[i][:-3],linfil[i][-1]]

for i in range(0,len(linfil)):
    linfil[i][0] = " ".join(linfil[i][0])
"""



