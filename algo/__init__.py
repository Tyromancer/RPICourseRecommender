import crawler

def popularityScore():
	return 0

def coreRequireScore(course, core_courses = [], concentration_courses = []):
	if course in core_courses:
		return 2
	elif course in concentration_courses:
		return 1
	return 0

def profPrefScore():
	return 0

def timeScore():
	return 0

def getScore(popularity_coef, core_coef, prof_pref_coef, time_coef, course):
	popularity_score = popularityScore()
	core_score = coreRequireScore(course)
	prof_pref_score = profPrefScore()
	time_score = timeScore()
	score = popularity_coef * popularity_score + core_coef * core_score + prof_pref_coef * prof_pref_score + time_coef * time_score
	return score

def getBestCourse(popularity_coeff, core_coeff, prof_coeff, time_coeff, courses):
	score_best = -1
	course_best = None
	for course in courses:
		score = getScore(popularity_coeff, core_coeff, prof_coeff, time_coeff, course)
		if score > score_best:
			score_best = score
			course_best = course

	if course_best == None:
		raise RuntimeError
	return (score_best, course_best.getName())

def satisfyPre(course):
	return True

def recommandCourses(popularity_coeff, core_coeff, prof_coeff, time_coeff):
	total_coeff = popularity_coeff + core_coeff + prof_coeff + time_coeff
	popularity_coeff = total_coeff / popularity_coeff
	core_coeff = total_coeff / core_coeff
	prof_coeff = total_coeff / prof_coeff
	time_coeff = total_coeff / time_coeff

	courses_dict = crawler.get_all_courses()
	for name, courses in courses_dict.items():
		if "CSCI" not in name:
			continue
		if len(courses) == 0:
			raise RuntimeError
		if not satisfyPre(courses[0]):
			continue
		print(getBestCourse(popularity_coeff, core_coeff, prof_coeff, time_coeff, courses)[1])