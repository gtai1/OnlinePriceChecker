import requests
from bs4 import BeautifulSoup
import re
import json

urls = ["https://www.homedepot.ca/product/samsung-33-inch-24-5-cu-ft-3-door-french-door-smart-refrigerator-beverage-center-autofill-water-pitcher-in-stainless-steel/1001795000",
"https://www.homedepot.ca/product/samsung-33-inch-24-5-cu-ft-3-door-french-door-smart-refrigerator-with-dual-auto-ice-maker-in-stainless-steel/1001794999?rrec=true",
"https://www.homedepot.ca/product/lg-electronics-33-inch-w-24-5-cu-ft-french-door-refrigerator-with-water-ice-dispenser-in-smudge-resistant-stainless-steel-energy-star-/1001431617?rrec=true"]

stores = ["Home Depot",
"Best Buy",
"Ronas"]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

thisdict = {}

for x in range(3):

    r = requests.get(urls[x], headers=headers, timeout=5)

    soup = BeautifulSoup(r.text, "html.parser")
    result = soup.find("span", itemprop="price")
    

    thisdict[stores[x]] = "$" + result.text

print("\n".join("{}\t{}".format(k, v) for k, v in thisdict.items()))