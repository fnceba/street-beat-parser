import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
import re
import io

class ProductSpider(scrapy.Spider):
    name = "goods"
    #allowed_domains = ['street-beat.ru']
    start_urls = ['https://street-beat.ru/cat']
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--headless')
        self.driver = webdriver.Chrome('./chromedriver',options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (X11; Linux x86_64) '
                                                                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                                                  'Chrome/99.0.4844.51 Safari/537.36'})

    def parse(self, response):
        json_dict = self.get_json(response)
        for i in range(1,json_dict['catalog']['pagination']['lastPage']):
            yield scrapy.Request('https://street-beat.ru/cat/?page='+str(i), callback=self.parse_goods)

    def parse_goods(self, response):
        json_dict = self.get_json(response)
        for item in json_dict['catalog']['listing']['items']:
            yield item

    def get_json(self,response):
        self.driver.get(response.url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div')))
        raw_json = re.search(r'__INITIAL_STATE__ \= JSON\.parse\(\'(.+)\'\);\n', self.driver.page_source).group(1).replace('\\','')
        return json.loads(raw_json)
        
