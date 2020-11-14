import scrapy

#run as scrapy crawl asxdataextract -o output.csv in the terminal

class AsxDataExtract(scrapy.Spider):
    name='asxdataextract' #call by scrapy crawl asxdataextract -o output.csv 
    allowed_domains = ["listcorp.com",]
    start_urls = ["https://www.listcorp.com/asx/sectors/information-technology"]
    #category = 'information-technology'
    #links = {}
    print("Test")

    def parse(self, response):

        
        query = '/div[@class="elevation-1 SectorPageSubCategoryPage__companiesTable"]//*'
        #query= '//*[@class ="v-table__overflow"]//tbody/tr'
        #<div class="v-table__overflow">
        #<div class="elevation-1 SectorPageSubCategoryPage__companiesTable">
        
               
        urls = response.xpath(query).extract()
        print("URLS!!!!!  ",urls)
        print("Response  ",response.xpath('class="elevation-1 SectorPageSubCategoryPage__companiesTable"'))
