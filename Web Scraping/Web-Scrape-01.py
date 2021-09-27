# SCRAPING MY LOCAL HTMLs

from bs4 import BeautifulSoup
import requests
# 'lxml' as parser


# Opening simple html file using BeautifulSoup:
with open('LAN-Table.html','r') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

# print(soup)
 

# Format to a more readable output using
# prettify method:
with open('LAN-Table.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

# print(soup.prettify())


# Grab information from a 'tag':
with open('LAN-Table.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

scrape_h1 = soup.body.h1
# print(scrape_h1)

 
# Only grab the text inside a tag:
with open('LAN-Table.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

scrape_title = soup.title.text
# print(scrape_title)


# Using the 'find' method to grab information from tags:
with open('LAN-Table.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

find_h1 = soup.find('h1').text
# print(find_h1)

find_hr = soup.find('table').th.text
# print(find_hr)

with open('multi-level nav.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

find_inner = soup.find('div',class_='inner').h2.text
# print(find_inner)

find_footer = soup.find('div',{'id':'footer'}).p.text
# print(find_footer)


# Grabbing a div with a class of 'Third':
with open('multi-level nav.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

find_third = soup.find('div',class_='Third').text
# print(find_third)


# Walking-through or digging to a specific tag:
with open('multi-level nav.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

dig_header = soup.find('div',{'id':'header'}).nav.ul.li.a.text
# print(dig_header)

dig_links = soup.find('div',{'id':'header'}).find_all('li')[1].text
# print(dig_links)


# Loop over the lists using the 'find_all' method:
with open('multi-level nav.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

for digs in soup.find_all('div',{'id':'body'}):
	first_parag = digs.p.text
	# print(first_parag)

	second_parag = digs('p')[1]
	# print(second_parag)

	# print()

for digs in soup.find_all('div',{'id':'header'}):
	first_link = digs.nav.ul.li.a.text
	# print(first_link)

	second_link = digs('li')[1].text
	# print(second_link)

	some_link = digs('ul')[3].text
	# print(some_link)

with open('LAN-Table.html') as html_file:
	soup = BeautifulSoup(html_file,'lxml')

for th in soup.find_all('th'):
	th_txt = th.text 
	# print(th_txt)


