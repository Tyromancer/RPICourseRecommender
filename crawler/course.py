from bs4 import BeautifulSoup
from urllib import request


class Course(object):
	'''
	class for an RPI course
	'''
	def __init__(self, data):
		'''
		Constructor of Course
		:param data: a string that holds all information of this course
		'''
		src = data.split('^')

		self.CRN = src[0]                        # CRN of course
		temp_val = src[1].split('-')
		if len(temp_val) == 3:
			self.major = temp_val[0].upper()     # Field of course e.g: CSCI
			self.course_id = temp_val[1]         # id of course    e.g: 1010
			self.section = temp_val[2]           # section of course e.g: 01
		else:                                    # in case of invalid entry, set all to empty string
			self.major = ''
			self.course_id = ''
			self.section = ''

		self.name = src[2]                       # name (title) of course
		self.type = src[3]                       # type of course (should be LEC)
		self.credit = src[4]                     # num of credits for course
		self.grtp = src[5]                       # I don't know what this is
		self.week_day = src[6]                   # when the classes are
		self.start_time = src[7]                 # when it starts
		self.end_time = src[8]                   # when it ends
		self.instructor = src[9]                 # name of instructors (might be multiple)
		self.location = src[10]                  # room the course is held

		if src[11] == '':
			self.max_enroll = 0
		else:
			self.max_enroll = int(src[11])       # maximum enroll seats

		if src[12] == '':
			self.current_enroll = 0
		else:
			self.current_enroll = int(src[12])   # current enrolled

		self.remaining_seats = src[13]           # remaining seats (can be negative)
		self.raw_string = data                   # string repr

	def __str__(self):
		return self.raw_string

	def getName(self):
		name = self.major + "-" + self.course_id + "-" + self.section
		return name

	def getTitle(self):
		title = self.major.strip().upper() + "-" + self.course_id.strip()
		return title

	def getPopularity(self):
		if self.max_enroll == 0:
			return -1

		popularity = ((self.max_enroll - self.current_enroll) / 2 + self.current_enroll) / self.max_enroll
		return popularity

	def getProfessors(self):
		return self.instructor.split("/")


class Session:
	'''
	ADT that represents a connect session, used for scraping data from RPI website
	'''
	def __init__(self, url):
		self.url = url

	def fetch(self, filename):
		'''

		:param filename: filename of the txt file to be written
		:return: None
		'''
		html, header = request.urlretrieve(self.url)
		html_file = open(html, encoding='utf-8')
		soup = BeautifulSoup(html_file, 'html.parser')

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


def get_all_courses(fetch):
	'''
	Get all course data and return in dictionary
	:param fetch: boolean that indicates whether to fetch data from website again
	:return: dirctionary that conatains all course data
	'''

	# if we are fetching from the website
	if fetch:
		URL = 'https://sis.rpi.edu/reg/zs201901.htm'
		session = Session(URL)
		session.fetch('courses.txt')

	all_courses = dict()

	# read from txt file and pack into a dictionary, namely result
	with open('courses.txt', 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			temp = line.split('^')  # use a symbol that does not appear in course names
			if len(temp) >= 2:
				field = temp[1].split('-')
				if len(field) >= 2:
					course_id = field[0] + field[1]
				else:
					continue
			else:
				continue

			# check if course has been added or not
			if course_id in all_courses.keys():
				all_courses[course_id].append(Course(line))  # add a different section of course
			else:
				all_courses[course_id] = [Course(line)]      # create a new entry

	return all_courses


if __name__ == '__main__':
	# URL = 'https://sis.rpi.edu/reg/zs201901.htm'
	# session = Session(URL)
	# session.fetch('courses.txt')
	# all_courses = dict()
	#
	# with open('courses.txt', 'r', encoding='utf-8') as f:
	# 	lines = f.readlines()
	# 	for line in lines:
	# 		temp = line.split('^')
	# 		if len(temp) >= 2:
	# 			field = temp[1].split('-')
	# 			if len(field) >= 2:
	# 				course_id = field[0] + field[1]
	# 			else:
	# 				continue
	# 		else:
	# 			continue
	#
	# 		if course_id in all_courses.keys():
	# 			all_courses[course_id].append(Course(line))
	# 		else:
	# 			all_courses[course_id] = [Course(line)]

	# for item in all_courses.keys():
	# 	for course in all_courses[item]:
	# 		print(course)
	#
	# print(len(all_courses))
	pass
