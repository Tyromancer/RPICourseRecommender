import os


def getReqs(major):
	'''
	:param major: string of Field of study. e.g: csci
	:return: dictionary of courses and their pre_reqs
	'''
	result = dict()
	with open(os.path.abspath(f'algo/doc/pre_req_{major.lower()}.txt'), 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			line = line.split(',')
			if len(line) > 0:
				if line[1].strip() == 'NONE':
					result[line[0].strip()] = list()
				else:
					result[line[0].strip()] = line[1:]

	return result


def getCores(major):
	'''

	:param major: string of Field of study. e.g: csci
	:return: set of core requisites of the major
	'''
	result = set()
	with open(os.path.abspath(f'algo/doc/core_req_{major.lower()}.txt'), 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			if len(line) > 0:
				result.add(line.strip())

	return result


def getCoursesTaken():
	'''

	:return: set of courses the user has already taken
	'''
	result = set()
	with open(os.path.abspath(f'algo/doc/courses_taken.txt'), 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			if len(line) > 0:
				result.add(line.strip())

	return result


if __name__ == '__main__':
	pass
