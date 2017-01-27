from bs4 import BeautifulSoup
import requests
import re
data=requests.get('http://www.fastvturesults.com/check_new_results/')
soup=BeautifulSoup(data._content,'html.parser')
usn=input('Enter the usn\n')
print()
usn='http://www.fastvturesults.com/check_new_results/'+usn
print(usn)
results=[]
try:
    data=requests.get(usn)
    soup=BeautifulSoup(data._content,'html.parser')
    soup.prettify()
    x=(soup.find('div',{'class':"table-responsive"}))
    p=x.find_all('a',{'class':'btn btn-danger'})
    for i in p:
        results.append(i.get('href'))
    count=len(results)
    for i in results:
        total=0
        data=requests.get(i)
        soup=BeautifulSoup(data._content,'html.parser')
        soup.prettify()
        x=soup.find('meta',{'property':"og:title"})
        print("\t\t"+x['content'])
        x=soup.find('p',{'class':"text-center"})
        print("\t\t\t\t"+x.string)
        x=soup.find_all('tr',{'class':'success'})
        for i in x:
            p=i.find_all('td')
            for j in range(6):
                string=str(p[j].string).strip()
                print(string,end='   ')
                if(j==4):
                    total=total+int(string)
            print()
        print('\n\n')
except:
    print("Invalid USN")
