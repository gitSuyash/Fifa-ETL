import requests
import json

class Extract:

	def __init__(self):
		self.data_source = json.load(open(r'E:\Fifa Data Pipeline\DataSource\data_config.json'))
		self.api_names = self.data_source['api']
		self.header = self.data_source['headers']
		# print(self.api_names)
		# print(self.header)

	def getAPISData(self,api_name):
		url = self.api_names[api_name]
		response = requests.request("GET",url,headers=self.header)
		# file = open(api_name+'.txt','w+',encoding="utf-8")
		# file.write(response.text)
		# file.close()
		return response.text
#test runs
# Extract().getAPISData('Teams')
# Extract().getAPISData('Goals')
# Extract().getAPISData('Players')
# Extract().getAPISData('Games')
# Extract().getAPISData('Rounds')
# print('Successfully loaded')	

