"""
This is my first webscraping! :)
PROJETO: Web Scraper de Notícias RSS
AUTOR: Daniel Andrade
DESCRIÇÃO: 
    Este script automatiza a extração de notícias de feeds RSS/XML. 
    Ele acessa o feed do TechCrunch, extrai os títulos, links e datas das 
    postagens recentes e organiza tudo em um arquivo CSV para análise posterior.

DEPENDÊNCIAS:
    - beautifulsoup4: Para processar o conteúdo XML.
    - lxml: Parser auxiliar para leitura de XML (recomendado).
    - pandas: Para estruturação de dados e exportação para CSV.
    - urllib: (Nativa) Para realizar as requisições HTTP.
"""

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd 

class NewsScraper:
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def fetch_news(self):
        try:
            req = urllib.request.Request(self.url, headers=self.headers)
            with urllib.request.urlopen(req) as response:
                soup = BeautifulSoup(response.read(), "xml")
                
            news_list = []
            for item in soup.find_all("item"):
                news_list.append({
                    "titulo": item.title.text,
                    "link": item.link.text,
                    "data": item.pubDate.text
                })
            return news_list
        except Exception as e:
            print(f"Erro na captura: {e}")
            return []


scraper = NewsScraper("https://techcrunch.com/feed/")
dados = scraper.fetch_news()


df = pd.DataFrame(dados)
df.to_csv("noticias_google.csv", index=False, encoding='utf-8-sig')
print("Arquivo noticias_google.csv gerado com sucesso!")