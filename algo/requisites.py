import os


def getReqs(major):
	result = dict()
	with open(os.path.abspath(f'algo/doc/pre_req_{major}.txt'), 'r', encoding='utf-8') as f:
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
	result = set()
	with open(os.path.abspath(f'algo/doc/core_req_{major}.txt'), 'r', encoding='utf-8') as f:
		lines = f.readlines()
		for line in lines:
			line = line.strip()
			if len(line) > 0:
				result.add(line.strip())

	return result


def getCoursesTaken():
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