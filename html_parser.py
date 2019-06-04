from unidecode import unidecode
import re
from bs4 import BeautifulSoup
from annotations import *
#-*- coding: windows-1250 -*-

class HtmlParser:
    def __init__(self):
        self.patient = {}
        self.separator = ':'

    @safe_run
    def set_name(self, soup):
        element = soup.find(lambda tag:tag.name=="td" and "Pacjent:" in tag.text)
        self.patient['Pacjent'] = element.get_text().split(self.separator)[1].strip()

    @safe_run
    def set_birthdate(self, soup):
        element = soup.find(lambda tag:tag.name=="td" and "Data urodzenia:" in tag.text)
        self.patient['Data urodzenia'] = element.get_text().split(self.separator)[1].strip()

    @safe_run
    def set_gender(self, soup):
        td = soup.find_all("td", {"valign" : "top"})[1]
        self.patient['Płeć'] = td.text.strip()

    @safe_run
    def set_main_book_number(self, soup):
        element = soup(text=re.compile(r'Nr księgi głównej:'))[0].find_next('td')
        self.patient['Nr księgi głównej'] = element.text.strip()

    @safe_run
    def set_pesel(self, soup):
        element = soup(text=re.compile(r'PESEL:'))[0].find_next('td')
        self.patient['PESEL'] = element.text.strip()

    @safe_run
    def set_research(self, soup):
        element = soup(text=re.compile(r'Badanie:'))[0].find_next('td')
        self.patient['Badanie'] = element.text.strip()

    @safe_run
    def set_researcher(self, soup):
        element = soup(text=re.compile(r'Badający:'))[0].find_next('td')
        self.patient['Badający'] = element.text.strip()

    @safe_run
    def parse(self, html_content):
        print('--- Parsing HTML ---')
        soup = BeautifulSoup(html_content, 'lxml')

        self.set_name(soup)
        self.set_birthdate(soup)
        self.set_gender(soup)
        self.set_main_book_number(soup)
        self.set_pesel(soup)
        self.set_research(soup)
        self.set_researcher(soup)

        print('\nResult:')
        # s1 = str(self.patient).decode('utf-8')
        # s2 = unicodedata.normalize('NFD', s1).encode('ascii', 'ignore')     
        # print(s1)
        print(unidecode(str(self.patient)))
        print('--- End --- \n')

        return self.patient
