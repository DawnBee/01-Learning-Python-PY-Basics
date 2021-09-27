# DECODE A WEBPAGE
'''
Use the BeautifulSoup and requests Python packages to print out a 
list of all the article titles on the New York Times homepage.
'''

from bs4 import BeautifulSoup
import requests


source = requests.get("https://www.nytimes.com").text
soup = BeautifulSoup(source,'lxml')

incr_indx = 0
title_list = []

while incr_indx <= 10:
	updt_indx = 3 #We can increment or decrement index here.
	find_titles = soup.find_all('h3')[incr_indx]
	incr_indx += 1
	if incr_indx > updt_indx:
		break

	for title in find_titles:
		title_list.append(title.text)

print(title_list)

# Because the website is constantly updating its headlines and articles I  
# couldn't come up with a solid approach on scraping the entire website's 
# article titles, also noticed that a lot of people struggles in scraping the 
# website, probably because we aren't using its public API. And just a reminder previous
# class names from 2014 like; story-header and story-heading have been updated 
# on the site's html, but even if we used the current classname 'balancedHeadline'
# or 'ghost' it still dispalys "None" or even worst wouldn't display a thing.



	
	
	