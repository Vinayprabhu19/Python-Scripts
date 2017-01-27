from bs4 import BeautifulSoup
import requests
import re
url='in.bookmyshow.com/bengaluru/movies'
movie=str(input('Enter the movie\n')).title().strip()
data=requests.get("http://in.bookmyshow.com/bengaluru/movies")
soup=BeautifulSoup(data._content,'html.parser')
d=soup.find_all('a',{'class':'__movie-name'})
for i in d:
    if(i.string==movie):
        movie_link=i.get('href')
        movie=movie.replace(' ','-')
        m=re.search((movie.lower()),movie_link)
        if(m!=None):
            movie_link=movie_link[m.end()+1:]
try:
    date=input('Enter date: yyyymmdd\n')
    url_new='https://in.bookmyshow.com/buytickets/'+movie+'-bengaluru/movie-bang-'+movie_link+'-MT/'+date
    print(url_new)
    data=requests.get(url_new)
    soup=BeautifulSoup(data._content,'html.parser')
    soup.prettify()
    p=soup.find_all('a',{'class':'__venue-name'})
    c=soup.find_all('div',{'class':'__showtime-link _unpaid-showtime'})
    for m in c:
        print(m)
    for i in p:
        print(i.find('strong').string)
except:
    print('Invalid Movie Name.\n')

