
import requests
from bs4 import BeautifulSoup
from csv import writer
import time
URL = "https://www.talabat.com/uae/restaurants"
page=requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
soup_body=soup.find("body")
soup_resturent_page=soup_body.find("div",class_="paginationstyles__PaginationContainer-wz3rb7-0")
find_page=soup_resturent_page.find_all("a")
b=[]
b.append(str(1))
for x in find_page:
    if x.text != "":
        b.append(x.text)
print(b)
resturent_name=[]
resturent_type=[]
r_data=[]
not_scraped=[]
rest_file=open("resturent_talabat_final.csv",'a')
writer_object = writer(rest_file)
writer_object.writerow(['restaurant name','cuisines','rating','rated by people','review','country'])
error=[]
error1=[]
error2=[]
error3=[]
error4=[]
error5=[]
error6=[]
data=[]
pending_resturant=[]
for x in b[18:]:
    try:
        time.sleep(1)
        URL_with_page = f"https://www.talabat.com/uae/restaurants?page={x}"
        rest_page=requests.get(URL_with_page)
        rest = BeautifulSoup(rest_page.content, "html.parser")
        rest_body=soup.find("body")
    except:
        try:
            time.sleep(1)
            URL_with_page = f"https://www.talabat.com/uae/restaurants?page={x}"
            rest_page=requests.get(URL_with_page)
            rest = BeautifulSoup(rest_page.content, "html.parser")
            rest_body=soup.find("body")
        except:
            try:
                URL_with_page = f"https://www.talabat.com/uae/restaurants?page={x}"
                rest_page=requests.get(URL_with_page)
                rest = BeautifulSoup(rest_page.content, "html.parser")
                rest_body=soup.find("body")
            except:
                try:
                    URL_with_page = f"https://www.talabat.com/uae/restaurants?page={x}"
                    rest_page=requests.get(URL_with_page)
                    rest = BeautifulSoup(rest_page.content, "html.parser")
                    rest_body=soup.find("body")
                except:
                    URL_with_page = f"https://www.talabat.com/uae/restaurants?page={x}"
                    rest_page=requests.get(URL_with_page)
                    rest = BeautifulSoup(rest_page.content, "html.parser")
                    rest_body=soup.find("body")
    print(URL_with_page)     
    soup_resturent=rest_body.find_all("div",class_="vendorstyles__VendorContainer-eu6e2y-0")
    for y in soup_resturent:
        rest_data=[]
        data=y.find("div",class_="description")
        rest_data.append(data.find_all("p")[0].text)
        rest_data.append(data.find_all("p")[1].text)
        rest_name=data.find_all("p")[0].text.lower().replace("- ","-").replace(".","").replace("& ","").replace(" ","-")
        resturent_slug_url=f"https://www.talabat.com/uae/{rest_name}"
        try:
            resturent_slug_url_page=requests.get(resturent_slug_url)
            if resturent_slug_url_page.status_code == 200:
                    find_resturent_rating=BeautifulSoup(resturent_slug_url_page.content, "html.parser")
                    resturent_rating=find_resturent_rating.find("div",class_="rating-number")
                    resturnet_rating_by_people=find_resturent_rating.find("div",class_="ratings-count")
                    resturnet_rating_by_people_review=find_resturent_rating.find("span",class_="f-500")
                    rest_data.append(resturent_rating.text)
                    rest_data.append(resturnet_rating_by_people.text.split(" ")[1])
                    rest_data.append(resturnet_rating_by_people_review.text.split(" ")[0])
                    rest_data.append("UAE")
                    rd=rest_data
                    writer_object.writerow(rd)
        except:
            try:
                resturent_slug_url_page=requests.get(resturent_slug_url)
                if resturent_slug_url_page.status_code == 200:
                        find_resturent_rating=BeautifulSoup(resturent_slug_url_page.content, "html.parser")
                        resturent_rating=find_resturent_rating.find("div",class_="rating-number")
                        resturnet_rating_by_people=find_resturent_rating.find("div",class_="ratings-count")
                        resturnet_rating_by_people_review=find_resturent_rating.find("span",class_="f-500")
                        rest_data.append(resturent_rating.text)
                        rest_data.append(resturnet_rating_by_people.text.split(" ")[1])
                        rest_data.append(resturnet_rating_by_people_review.text.split(" ")[0])
                        rest_data.append("UAE")
                        rd=rest_data
                        writer_object.writerow(rd)
            except:       
                resturent_slug_url_page=requests.get(resturent_slug_url)
                if resturent_slug_url_page.status_code == 200:
                        find_resturent_rating=BeautifulSoup(resturent_slug_url_page.content, "html.parser")
                        resturent_rating=find_resturent_rating.find("div",class_="rating-number")
                        resturnet_rating_by_people=find_resturent_rating.find("div",class_="ratings-count")
                        resturnet_rating_by_people_review=find_resturent_rating.find("span",class_="f-500")
                        rest_data.append(resturent_rating.text)
                        rest_data.append(resturnet_rating_by_people.text.split(" ")[1])
                        rest_data.append(resturnet_rating_by_people_review.text.split(" ")[0])
                        rest_data.append("UAE")
                        rd=rest_data
                        writer_object.writerow(rd)
                        
                        
rest_file.close()