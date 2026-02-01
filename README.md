# 📰 News Scraper RSS

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-green.svg)](https://pandas.pydata.org/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.x-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)

## 📝 Sobre o Projeto
Este é um script de automação desenvolvido para extrair notícias de feeds RSS/XML de portais de tecnologia (configurado por padrão para o TechCrunch). O objetivo é coletar títulos, links e datas de publicação de forma estruturada para permitir análises de dados e monitoramento de tendências.

Este foi o meu primeiro projeto de Web Scraping, focado em entender o ciclo de vida de uma requisição HTTP até a persistência dos dados em formato tabular.


## 🚀 Funcionalidades
* Coleta automatizada via protocolo HTTP.
* Parsing de arquivos XML/RSS usando **BeautifulSoup**.
* Estruturação de dados com **Pandas**.
* Exportação de relatórios em **CSV** com codificação compatível com Excel (`utf-8-sig`).

