# Grid_rowContainer__RAVMO
import requests
from bs4 import BeautifulSoup
import os

# url = 'https://supercell.com/en/games/brawlstars/blog/page/1'
class_name = 'Grid_full-3__Q8P5A Grid_full-offset-3__K8Ci5 Grid_large-2__YHaSM Grid_large-offset-1__lqxqe Grid_medium-2__omk8d Grid_medium-offset-1__291rr Grid_small-2__LP1Ll Grid_small-offset-1__zh611 Grid_mobile-6__Cl_i4 archivedArticles_imageContainer__L_34L'

def ScrapeBSBlog(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
            res = []
            base = 'https://supercell.com'
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('div', class_=class_name)
            for article in articles:
                # headline = article.find('h2').text
                link = article.find('a')
                link_href = link['href']
                link_img = article.find('picture').find('source')['srcset']
                
                # summary = article.find('p').text
                
                # print(f'Headline: {headline}')
                res.append((base + link_href, link_img))
            return res
        return 'I am not feeling well and unable to fetch Brawl Stars news at the moment'
    except Exception as e:
        print(f"An error occurred: {e}")
        return 'I am not feeling well and unable to fetch Brawl Stars news at the moment'




