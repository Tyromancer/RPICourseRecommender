from bs4 import BeautifulSoup
from selenium import webdriver
import selenium


# https://github.com/phantomlei3/RPICourseTrends/blob/master/sample/version1/getDatarequest.py
class Course(object):
	def __init__(self, data):
		src = data.split('^')

		self.CRN = src[0]
		temp_val = src[1].split('-')
		if len(temp_val) == 3:
			self.major = temp_val[0].upper()
			self.course_id = temp_val[1]
			self.section = temp_val[2]
		else:
			self.major = ''
			self.course_id = ''
			self.section = ''

		self.name = src[2]
		self.type = src[3]
		self.credit = src[4]
		self.grtp = src[5]
		self.week_day = src[6]
		self.start_time = src[7]
		self.end_time = src[8]
		self.instructor = src[9]
		self.location = src[10]

		if src[11] == '':
			self.max_enroll = 0
		else:
			self.max_enroll = int(src[11])

		if src[12] == '':
			self.current_enroll = 0
		else:
			self.current_enroll = int(src[12])

		if self.max_enroll == 0:
			self.popularity = -1
		else:
			self.popularity = float(self.current_enroll) / float(self.max_enroll)
		self.remaining_seats = src[13]
		self.raw_string = data

	def __str__(self):
		return self.raw_string + ' | ' + str(self.popularity)


class Session:
	def __init__(self, url):
		self.driver = webdriver.Chrome()

		self.url = url

	def fetch(self, filename):
		self.driver.get(self.url)
		html = self.driver.page_source
		soup = BeautifulSoup(html, 'html.parser')

		courses = soup.find_all('tr')
		with open(filename, 'w', encoding='utf-8') as f:
			for course in courses:
				valid = True
				line = list()
				items = course.find_all('td')

				for item in items:
					temp = item.get_text()
					if temp.lower().find('lab') != -1 or temp.lower().find('tes') != -1 or temp.lower().find('note') != -1:
						valid = False
						break
					elif temp.lower().find('view textbook') != -1:
						break

					line.append(temp.strip())
				if valid:
					#f.write('|'.join('|'.join(line).split()).replace('|||', '|'))
					if len(line) >= 2:
						f.write('^'.join(line[0].split()) + '^' + '^'.join(line[1:]))
						f.write('\n')


def course_equiv(course_obj, target):
	return course_obj.major + ' ' + course_obj.course_id == target


if __name__ == '__main__':
	URL = 'https://sis.rpi.edu/reg/zs201901.htm'
	session = Session(URL)
	session.fetch('courses.txt')
	all_courses = dict()

	with open('courses.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			temp = line.split('^')
			if len(temp) >= 2:
				field = temp[1].split('-')
				if len(field) >= 2:
					course_id = field[0] + field[1]
				else:
					continue
			else:
				continue

			if course_id in all_courses.keys():
				all_courses[course_id].append(Course(line))
			else:
				all_courses[course_id] = [Course(line)]

	for item in all_courses.keys():
		for course in all_courses[item]:
			print(course)

	print(len(all_courses))
