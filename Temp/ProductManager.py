#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def getHotProducts(url):
    if "adafruit" in url:
        r = requests.get(url)
        featuredProducts = []
        if r.status_code == 200:
            body = r.text
            bPage = BeautifulSoup(body, "html.parser", from_encoding="iso-8859-8")
            #products = bPage.select("#featured-products_block_center")
            products = bPage.find_all("div", {"class":"row product-listing"})

            for product in products:
                nameOfProduct = product.find_all("div", {"class": "product-listing-text-wrapper"})[0].find("h1").find("a").get("data-name")
                urlOfProduct = "https://www.adafruit.com" + product.find_all("div", {"class": "product-listing-text-wrapper"})[0].find("h1").find("a").get("href")
                descriptionOfProduct = product.find_all("div", {"class": "product-description clearfix hidden-sm hidden-xs hidden-lg"})[0].getText()[1:]
                priceOfProduct = product.find_all("div", {"class": "product-info clearfix row"})[0].\
                    find_all("div", {"class":"price-stock col-lg-8 col-md-6 col-sm-6 col-xs-12"})[0].\
                    find_all("span", {"class":"normal-price"})[0].getText()
                stockProduct = product.find_all("div", {"class": "product-info clearfix row"})[0]. \
                    find_all("div", {"class": "price-stock col-lg-8 col-md-6 col-sm-6 col-xs-12"})[0]. \
                    find_all("div", {"class": "stock"})[0].getText().replace("\n", "")

                featuredProducts.append([nameOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', ''), urlOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', ''), descriptionOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', ''), priceOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', ''), stockProduct.replace(u'\xa0', u' ').replace(u'\u200b', '')])


            return featuredProducts

        else:
            return None
    elif "sparkfun" in url:
        r = requests.get(url)
        featuredProducts = []
        if r.status_code == 200:
            body = r.text
            bPage = BeautifulSoup(body, "html.parser", from_encoding="iso-8859-8")
            products = bPage.find_all("div", {"class": "tile product-tile has_addl_actions  grid "})

            for product in products:
                main = product.find_all("div", {"class":"main"})[0]
                rawNameAndUrl = main.find_all("h3")[0].find("a")
                urlOfProduct = rawNameAndUrl.get("href").strip()
                nameOfProduct = rawNameAndUrl.find_all("span")[0].getText().strip()
                descriptionOfProduct = main.find_all("p", {"class": "description"})[0].getText().strip().replace(u'\n', u'').replace(u'\r', u'')
                stockProduct = main.find_all("span", {"class" : "bubbles"})[0].find("a").find_all("span")[0].find_all("span")[0].getText().strip()
                priceOfProduct = '$' + product.find_all("div", {"itemprop":"offers"})[0].find("div").find("span").find("span", {"itemprop": "price"}).getText().strip()

                if not nameOfProduct == "":
                    featuredProducts.append([nameOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', '').replace( u'\u2026', '').replace(u'\xae', '').replace(u'\u2013', '').replace(u'\u2019', '').replace(u'\ufffd', '').replace(u'\xb5', '').replace(u'\u201d', ''),
                                             urlOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', '').replace( u'\u2026', '').replace(u'\xae', '').replace(u'\u2013', '').replace(u'\u2019', '').replace(u'\ufffd', '').replace(u'\xb5', '').replace(u'\u201d', ''),
                                             descriptionOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', '').replace( u'\u2026', '').replace(u'\xae', '').replace(u'\u2013', '').replace(u'\u2019', '').replace(u'\ufffd', '').replace(u'\xb5', '').replace(u'\u201d', ''),
                                             priceOfProduct.replace(u'\xa0', u' ').replace(u'\u200b', '').replace( u'\u2026', '').replace(u'\xae', '').replace(u'\u2013', '').replace(u'\u2019', '').replace(u'\ufffd', '').replace(u'\xb5', '').replace(u'\u201d', ''),
                                             stockProduct.replace(u'\xa0', u' ').replace(u'\u200b', '').replace( u'\u2026', '').replace(u'\xae', '').replace(u'\u2013', '').replace(u'\u2019', '').replace(u'\ufffd', '').replace(u'\xb5', '').replace(u'\u201d', '')])
            return featuredProducts
        else:
            return None

def exportToCSV(data):
    import csv
    file = open("out.csv", 'w')
    outFile = csv.writer(file)
    for row in data:
        print list(row)
        outFile.writerow(list(row))


if __name__ == "__main__":
    products = getHotProducts("https://www.sparkfun.com/categories/top?per_page=400")
    exportToCSV(products)