from bs4 import BeautifulSoup
import requests

# SCRAPING Mr. Corey Schafer's Personal Website ('coreyms.com')

'''
To prevent any performance issues on the website comment out each code one-by-one.
All credits belong to: Mr. Corey Schafer
'''


# Grabbing information from an actual website:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())


# Parsing specific information from the site:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# print(article.prettify())


# Grabbing the page's headline:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# headline = article.h2.a.text
# print(headline)


# Grabbing the page's summary:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# summary = article.find('div',class_='entry-content').p.text
# print(summary)


# Grabbing the correct video link by parsing 
# the embedded version of the video:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# vid_src = article.find('iframe',class_='youtube-player')
# print(vid_src)


# Access 'vid_src' like a dictionary:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# vid_src = article.find('iframe',class_='youtube-player')['src'] #creates a list starting from 'src' string.
# print(vid_src)


# Parsing the url string to grab the video ID:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# vid_src = article.find('iframe',class_='youtube-player')['src']
# vid_id = vid_src.split('/')[4] #splits the string by forward slashes and selects the index '4' in 'src' list.
# print(vid_id)


# Parsing the url string to grab the video ID:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# vid_src = article.find('iframe',class_='youtube-player')['src']

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]
# print(vid_id)


# Construct a youtube link using the video ID we parse from the string:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# article = soup.find('article')
# vid_src = article.find('iframe',class_='youtube-player')['src']

# vid_id = vid_src.split('/')[4]
# vid_id = vid_id.split('?')[0]

# yt_link = f"https://youtube.com/watch?v={vid_id}"
# print(yt_link)


# Loop over all the information inside 'article' section:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# for article in soup.find_all('article'):
# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.find('div',class_='entry-content').p.text
# 	print(summary)

# 	vid_src = article.find('iframe',class_='youtube-player')['src']
# 	vid_id = vid_src.split('/')[4]
# 	vid_id = vid_id.split('?')[0]
# 	yt_link = f"https://youtube.com/watch?v={vid_id}"
# 	print(yt_link)

# 	print()


# Skip by any missing information within the page:
# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# for article in soup.find_all('article'):
# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.find('div',class_='entry-content').p.text
# 	print(summary)

# 	try:
# 		vid_src = article.find('iframe',class_='youtube-player')['src']
# 		vid_id = vid_src.split('/')[4]
# 		vid_id = vid_id.split('?')[0]
# 		yt_link = f"https://youtube.com/watch?v={vid_id}"
# 	except Exception as e:
# 		yt_link = None
# 	print(yt_link)

# 	print()


# Saving the scraped information to a CSV file:
# import csv

# source = requests.get('https://coreyms.com').text
# soup = BeautifulSoup(source,'lxml')

# csv_file = open('cms_scrape.csv','w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['headline','summary','video_link'])

# for article in soup.find_all('article'):
# 	headline = article.h2.a.text
# 	print(headline)

# 	summary = article.find('div',class_='entry-content')
# 	print(summary)

# 	try:
# 		vid_src = article.find('iframe',class_='youtube-player')['src']
# 		vid_id = vid_src.split('/')[4]
# 		vid_id = vid_id.split('?')[0]
# 		yt_link = "https://youtube.com/watch?v={}".format(vid_id)
# 	except Exception as e:
# 		yt_link = None

# 	print(yt_link)

# 	print()

# 	csv_writer.writerow([headline,summary,yt_link])

# csv_file.close()
	

