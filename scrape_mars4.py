#!/usr/bin/env python
# coding: utf-8

# ## Setup

# In[74]:



# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from pprint import pprint
#import time
#from selenium import webdriver
import time

def scrape():
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    # Run the function below:
    first_title, first_paragraph = mars_news(browser)
    
    # Run the functions below and store into a dictionary
    results = {
        "title": first_title,
        "paragraph": first_paragraph,
        "image_URL": jpl_image(browser),
        "weather": mars_weather_tweet(browser),
        "facts": mars_facts(),
        "hemispheres": mars_hemis(browser),
    }
# Quit the browser and return the scraped results
    browser.quit()
    return results
   

def mars_news(browser):

    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')
    first_title = mars_news_soup.find('div', class_='content_title').text
    first_paragraph = mars_news_soup.find('div', class_='article_teaser_body').text
    return first_title, first_paragraph

def jpl_image(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(2)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(2)
    browser.click_link_by_partial_text('more info')
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')
    feat_img_url = image_soup.find('figure', class_='lede').a['href']
    feat_img_full_url = f'https://www.jpl.nasa.gov{feat_img_url}'
    feat_img_full_url
    return feat_img_full_url

def mars_weather_tweet(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')
    first_tweet = tweet_soup.find('p', class_='TweetTextSize').text
    return first_tweet

def mars_facts():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    df.to_html()
    # Convert to HTML table string and return
    return df.to_html()
    
def mars_hemis(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    hemi_soup = BeautifulSoup(html, 'html.parser')
    hemi_strings = []
    links = hemi_soup.find_all('h3')

    for hemi in links:
        hemi_strings.append(hemi.text)
        
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        time.sleep(2)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})

    mars_hemisphere

    
    return hemispheres_url
    
    

    # browser.quit()

    # return {"meh":mars_hemisphere}
    