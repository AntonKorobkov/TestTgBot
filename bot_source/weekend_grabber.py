# Here we grab all the data from http://weekend.rambler.ru/ and parse it

import re
import requests
from bs4 import BeautifulSoup

__author__ = 'Anton Korobkov'


def update_data(method):
    """
    Each time client sends request
    we update url to get most recent data
    :param method:
    :return:
    """

    def reload(self, classname):
        page = requests.get(self.main_page).content
        self.soup = BeautifulSoup(page, 'html.parser')
        return method(self, classname)

    return reload


class WeekendMain:

    def __init__(self):
        self.main_page = 'http://weekend.rambler.ru/'

    @update_data
    def fetch_hot(self, classname):
        """
        Fetches news from main page
        :return:
        """

        newsdict = {self.restore_url(re.search('href=".*?"', str(element)).group(0)[6:-1]): element.text for
                    element in self.soup.find_all('h3', {'class': classname})}
        return newsdict

    def restore_url(self, url):
        return self.main_page + url
