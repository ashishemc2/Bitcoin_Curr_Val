import robobrowser, json
from bs4 import BeautifulSoup
import pandas as pd
from requests import sessions
class Getdata:
    def __init__(self,url):
        self.url=url

    def getdatafromurl(self):
        session = sessions.Session()
        #session.proxies = {'https': '135.245.115.123:8000'}
        self.browser = robobrowser.RoboBrowser(history=True,session=session)
        self.browser.open(self.url)
        #print(self.browser.parsed)


    def convertdatafromurl(self):
        jsontext=self.browser.parsed.getText()
        self.jsondata = json.loads(jsontext)
        return self.jsondata
'''
def main():
    url1=Getdata("https://koinex.in/api/ticker")
    url1.getdatafromurl()
    print(url1.convertdatafromurl())


if __name__ == '__main__':
    main()
'''