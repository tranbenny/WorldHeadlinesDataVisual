'''

'''
import re
import time

import requests
from bs4 import BeautifulSoup

from Config.MonthMapping import MONTHS
from DatabaseAccess.service.CountriesService import CountriesService
from HeadlineData.HeadlineSourcesURLs import HEADLINE_URLS


class GetHeadlineService:

    def __init__(self):
        self.date = time.strftime('%Y-%m-%d')
        self.countryService = CountriesService()


    def __formatRSSDate__(self, date):
        '''
        :param date:
        :return:
        '''
        tokens = date.split(" ")
        result = '{}-{}-{}'.format(str(tokens[3]), str(MONTHS[tokens[2]]), str(tokens[1]))
        return result

    def __getRSSData__(self, source, url):
        '''
        :param source:
        :param url:
        :return:
        '''
        data = []
        text = requests.get(url).text
        soup = BeautifulSoup(text, 'html.parser')
        container = soup.find_all('item')
        # attributes: <title>, <pubdate>, <description>
        for result in container:
            article = {}
            title = result.find('title').text
            try:
                description = result.find('description').text
            except:
                description = ''

            try:
                title = self.__removeTags__(str(title)).replace("'", "")
                description = self.__removeTags__(str(description))
            except:
                title = self.__removeTags__(str(title.encode('utf8')))
                description = self.__removeTags__(str(description.encode('utf8')))

            description = re.sub('<[^>]*>', '', description)
            article['title'] = title.replace("'", "")
            article['description'] = description.replace("'", "")

            try:
                article['published_date'] = str(result.find('pubdate').text)
                article['published_date'] = self.__formatRSSDate__(article['published_date'])
            except:
                article['published_date'] = self.date

            article['countries'] = []
            article['source'] = source
            article['headline_date'] = self.date
            data.append(article)
        return data


    def getData(self):
        '''
        :return: dictionary of url and list of headline objects
        '''
        result = {}
        for url in HEADLINE_URLS.keys():
            print('STARTING ' + url)
            result[url] = self.__getRSSData__(url, HEADLINE_URLS[url])
            print('FINISHED ' + url)
        return result

    def __removeTags__(self, text):
        '''
        :param text:
        :return:
        '''
        result = re.sub('<(br|a|img|p|span|time)([^>]*)>', '', text)
        result = re.sub('(</a>|</p>|<ul>|</ul>|<li>|</li>|</span>|</time>|<em>|</em>|<strong>|</strong>)', '',
                          result)
        return result