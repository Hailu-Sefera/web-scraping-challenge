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

def scrape():
    # In[75]:


    # Site Navigation
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # ## NASA Mars News (Splinter)

    # In[76]:


    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)


    # In[77]:


    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    mars_news_soup = BeautifulSoup(html, 'html.parser')


    # In[78]:



    # Scrape the first article title
    first_title = mars_news_soup.find('div', class_='content_title').text
    first_title


    # In[79]:


    # Scrape the first article teaser paragraph text
    first_paragraph = mars_news_soup.find('div', class_='article_teaser_body').text
    first_paragraph


    # ## JPL Mars Space Featured Image (Splinter)

    # In[80]:


    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    # In[81]:


    # Go to 'FULL IMAGE'
    browser.click_link_by_partial_text('FULL IMAGE')


    # In[82]:


    # Go to 'more info'
    browser.click_link_by_partial_text('more info')


    # In[83]:


    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    image_soup = BeautifulSoup(html, 'html.parser')


    # In[84]:


    # Scrape the URL
    feat_img_url = image_soup.find('figure', class_='lede').a['href']
    feat_img_full_url = f'https://www.jpl.nasa.gov{feat_img_url}'
    feat_img_full_url


    # ## Mars Weather Tweet (Splinter)

    # In[85]:


    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)


    # In[86]:


    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    tweet_soup = BeautifulSoup(html, 'html.parser')


    # In[87]:


    # Scrape the tweet info
    first_tweet = tweet_soup.find('p', class_='TweetTextSize').text
    first_tweet


    # ## Mars Facts (Pandas)

    # In[88]:


    # Scrape the table of Mars facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    df = tables[0]
    #df.columns = ['Property', 'Value']
    df


    # In[89]:


    # Convert to HTML table string
    df.to_html()


    # ## Mars Hemispheres (Splinter)

    # In[90]:


    # URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)


    # In[91]:


    # Create BeautifulSoup object; parse with 'html.parser'
    html = browser.html
    hemi_soup = BeautifulSoup(html, 'html.parser')


    # In[92]:


    # Populate a list with links for the hemispheres
    hemi_strings = []
    links = hemi_soup.find_all('h3')

    for hemi in links:
        hemi_strings.append(hemi.text)
        
    hemi_strings


    # In[93]:


    import time 
    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
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
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})


    # In[94]:


    mars_hemisphere


    # In[95]:


    # close the browser
    browser.quit()

    return mars_hemisphere

    # In[ ]:




