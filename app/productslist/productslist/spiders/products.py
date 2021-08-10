import scrapy
import mysql.connector


class ProductsSpider(scrapy.Spider):
	name = 'products'
	start_urls = ['https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops']
	def parse(self, response, **kwargs):
		dados = []

		banco = mysql.connector.connect(
			host = 'localhost',
			user = 'root',
			passwd = 'Nubia-2008',
			database = 'visionBD',
			auth_plugin='mysql_native_password'
		)
		cursor = banco.cursor()
			
		comando_sql = "INSERT INTO products (title, price, description) VALUES(%s, %s, %s)"
			
			
		for i in response.xpath('//div[@class="col-sm-4 col-lg-4 col-md-4"]'):
			notebookPrice = i.xpath('.//h4[@class="pull-right price"]//text()').getall()
			notebookTitle = i.xpath('.//a[@title]').get()
			notebookDescription = i.xpath('.//p[@class="description"]/text()').get()

			if(notebookTitle.split('\"')[5].find('Lenovo') == 0):
				dados = ('"' + notebookTitle.split('\"')[5] + '"', '"' + notebookPrice[0] + '"', '"' + notebookDescription + '"')
				cursor.execute(comando_sql, dados)
				banco.commit()
				