import requests
import lxml.html #you have to explicitly import html as it is hidden package and is not imported by default with lxml
"""
Request Library Demo to post simple Post call and receiving output in JSON
"""
#Simple Get request using requests library 
payload = {"q": "chetan"}
r = requests.get('https://github.com/search', params=payload)
print("Requested URL = ",r.url)

#Simple Post request using requests library 
payload = {"key": "value1"}
r = requests.post("http://httpbin.org/post", data=payload)
print("Response text :", r.json())

#Simple lxml library example for fetching the price 
page = requests.get('https://github.com/pricing/') #Receiving whole page in variable page
tree = lxml.html.fromstring(page.content) #formatting the whole page from string format to html 
print("Page Object:", tree) 
plans = tree.xpath('//h3[@class="h3-mktg pt-2"]/text()') #using xpath to look into default class for plans on github
pricing = tree.xpath('//h3[@class="h000-mktg lh-condensed-ultra my-2"]/text()') #Using xpath to fetch default pricing from github
print(f"Plans offered by github : {plans} \nPricing according to plan : {pricing}")

