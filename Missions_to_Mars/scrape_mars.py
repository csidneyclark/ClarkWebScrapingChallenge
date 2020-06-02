from splinter import Browser
from bs4 import BeautifulSoup
import requests


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "./chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url ='https://mars.nasa.gov/news/'
    
    browser.visit(url)
    

    html = browser.html
    #html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    listings["title"] = soup.find('div', class_='content_title').get_text()

    
    url_two = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_two)
    browser.click_link_by_partial_text('FULL IMAGE')
    current_html = browser.html
    image_soup = BeautifulSoup(current_html, 'html.parser')
    featured_img_class = image_soup.find('img', class_='fancybox-image')["src"]
    featured_img_class

    listings["image"] = featured_img_class

    print(listings)

    browser.quit()
    
    return listings
