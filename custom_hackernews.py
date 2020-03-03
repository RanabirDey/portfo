# search all Hacker News pages(website link will be fed while running the program) and choose news having votes > 300

import requests
from bs4 import BeautifulSoup
import pprint
import sys

def scrape_web(weblink):
	all_page_links = []
	all_page_subtexts = []
	res = requests.get(weblink)
	if res.status_code == 200:
		soup = BeautifulSoup(res.text, 'html.parser')
		all_page_links.append(soup.select('.storylink'))     # this will store all links in a page as a 2 dimentional resultset - [page][links]
		all_page_subtexts.append(soup.select('.subtext'))    # this will store all subtexts in a page as a 2 dimentional resultset - [page][subtexts]
		page_cnt = 1                                    # in both above cases (links and subtexts) the set will be 
		page_cnt_str = str(page_cnt)                    # to understand with data, uncomment pprint.pprint in inspect_votes func
		next_weblink = weblink + '?p=' + page_cnt_str
		res = requests.get(next_weblink)
		while res.status_code == 200 and page_cnt < 10:
			soup = BeautifulSoup(res.text, 'html.parser')
			all_page_links.append(soup.select('.storylink'))
			all_page_subtexts.append(soup.select('.subtext'))
			page_cnt += 1
			page_cnt_str = str(page_cnt)
			next_weblink = weblink + '?p=' + page_cnt_str
			res = requests.get(next_weblink)
	else:
		return f'improper response : {res}'
	
	return all_page_links, all_page_subtexts

def inspect_votes(all_page_links, all_page_subtexts):
	#pprint.pprint(all_page_links)
	#pprint.pprint(all_page_subtexts)
	linklist = []
	votelist = []
	for page_indx, page in enumerate(all_page_links):    # first iterate the page set (all_page_links & all_subtext is a 2D result set)
		for link_indx, link in enumerate(page):     # then iterate links in each page
			linklist.append({"link":link, "page_count": page_indx})
			vote_class = all_page_subtexts[page_indx][link_indx].select('.score')
			for text in vote_class:
				vote = text.getText()
			if len(vote):
			#	print('if voted : ', indx)
				votelist.append(vote)
			else:
			#	print('Not voted: ', indx)
				votelist.append(' ')			

	return linklist, votelist

def ceate_custhm(links, votes, vote_points):
	hm = []
	for indx, item in enumerate(links):
		title = item["link"].getText()
		href = item["link"].get('href', None)
		points = int(votes[indx].replace(' points',''))
		if points > int(vote_points):
			hm.append({"title": title, "link": href, "votes": points, "page_number": item["page_count"]})

	hm = sorted(hm, key = lambda k:k['votes'], reverse=True)
	return hm
#	return pprint.pprint(hm)

def cust_hackernews(vote_points):
	website = 'https://news.ycombinator.com/'
	links, subtexts = scrape_web(website)
	links, votes = inspect_votes(links, subtexts)
	return ceate_custhm(links, votes, vote_points)

