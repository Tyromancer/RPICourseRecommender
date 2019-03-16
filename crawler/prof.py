from bs4 import BeautifulSoup
from selenium import webdriver
from urllib import request
from html.parser import HTMLParser

import time
import re


class Professor:
	def __init__(self, url, first_name='', last_name='', overall=0.0, difficulty=0.0, done=False):
		self.tid = url.split('tid=')[1]
		self.tid.replace('&showMyProfs=true', '')
		self.first_name = first_name
		self.last_name = last_name
		self.overall = overall
		self.difficulty = difficulty
		if not done:
			self.rmp()

	def rmp(self):
		html_file, headers = request.urlretrieve('https://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + self.tid)
		html = open(html_file, encoding='utf-8')
		soup = BeautifulSoup(html, 'html.parser')

		first_name_list = soup.find_all('span', attrs={'class': 'pfname'})
		for item in first_name_list:
			if len(item.get_text()) == 0:
				continue
			self.first_name += (' ' + item.get_text().lower().capitalize().strip())

		self.first_name.lstrip()
		last_name = soup.find('span', attrs={'class': 'plname'})
		# for item in last_name_list:
		# 	if len(item.get_text()) == 0:
		# 		continue
		# 	self.last_name += item.get_text()
		if not len(last_name.get_text()) == 0:
			self.last_name += last_name.get_text().strip().lower().capitalize()

		overall_quality_div = soup.find('div', class_='breakdown-container quality')
		quality_grade_div = overall_quality_div.find('div', class_='grade')
		if not quality_grade_div.get_text() == 'N/A':
			self.overall = float(quality_grade_div.get_text().strip())

		difficulty_div = soup.find('div', class_='breakdown-section difficulty')
		difficuty_grade_div = difficulty_div.find('div', class_='grade')
		if not difficuty_grade_div.get_text() == 'N/A':
			self.difficulty = float(difficuty_grade_div.get_text().strip())

		# time.sleep(1)

	def __str__(self):
		return self.last_name.strip() + ',' + self.first_name.strip() + ',' + str(self.overall) + ',' + str(self.difficulty) + ',' + self.tid


def make_prof_dict(filename):
	result = dict()
	with open(filename, 'r', encoding='utf-8') as file:
		prof_lines = file.readlines()
		for prof_line in prof_lines:
			pline = prof_line.split(',')
			prof = Professor('tid=' + pline[-1], pline[1], pline[0], float(pline[2]), float(pline[3]))
			if pline[0] in result.keys():
				result[pline[0]].append(prof)
			else:
				result[pline[0]] = [prof]

	return result


def make_cs_profs():
	with open('profs.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		with open('professors.txt', 'w', encoding='utf-8') as pf:
			for line in lines:
				p = Professor(line)
				pf.write(str(p).split('&')[0].lower().strip() + '\n')


if __name__ == '__main__':
	# make_cs_profs()
	# print(make_prof_dict('professors.txt'))
	pass

	# temp = list()
	# with open('professors.txt', 'r', encoding='utf-8') as f:
	# 	lines = f.readlines()
	# 	for line in lines:
	# 		if len(line.strip()) != 0:
	# 			tmp = line.split('&')[0].lower()
	# 			temp.append(tmp)
	#
	# with open('professors.txt', 'w', encoding='utf-8') as f:
	# 	i = 0
	# 	while i < len(temp):
	# 		f.write(temp[i].strip() + '\n')
	# 		i += 1
