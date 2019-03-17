import crawler.prof
import algo.requisites
import crawler.course

PROF_FILENAME = crawler.prof.get_abs_prof_path()


def popularityScore(course):
	'''
	:param course: course instance
	:return: popularity of that course
	'''
	return course.getPopularity()


def coreRequireScore(course, core_courses):
	'''
	:param course: instance of Course
	:param core_courses: core requisite courses
	:return: core score
	'''
	score = 1
	if course in core_courses:
		score = 2
	return score/2


def profPrefScore(professor_dict, course, difficulty, overall_coeff, diff_coeff):
	professors = course.getProfessors()
	score = 0
	for name in professors:
		name = name.lower()
		if name not in professor_dict.keys():
			return -1
		professor = professor_dict[name]
		score += professor.getScore(difficulty, overall_coeff, diff_coeff)

	if score == 0:
		return -1

	score = score / len(professors)
	return score


def timeScore():
	'''
	This function is currently not used and is left here for future usages, if we remember to do that
	:return:
	'''
	return -1


def getScore(popularity_coef, core_coef, prof_pref_coef, time_coef, course, difficulty, overall_coeff, diff_coeff, prof_dict, core_courses):
	popularity_score = popularityScore(course)
	core_score = coreRequireScore(course, core_courses)
	prof_pref_score = profPrefScore(prof_dict, course, difficulty, overall_coeff, diff_coeff)
	time_score = timeScore()

	NA_count = 0
	if popularity_score == -1:
		popularity_score = 0
		NA_count += popularity_coef
	if core_score == -1:
		core_score = 0
		NA_count += core_coef
	if prof_pref_score == -1:
		prof_pref_score = 0
		NA_count += prof_pref_coef
	if time_score == -1:
		time_score = 0
		NA_count += time_coef

	if NA_count == 1:
		return (-1, "")

	popularity_comp = popularity_coef * popularity_score / 4 * 100
	core_comp = core_coef * core_score / 4 * 100
	prof_comp = prof_pref_coef * prof_pref_score / 4 * 100
	time_comp = time_coef * time_score / 4 * 100
	score = popularity_comp + core_comp + prof_comp + time_comp
	adjust_coeff = 1 / (1 - NA_count)
	score = score * adjust_coeff
	# print("score details:",popularity_score,core_score,prof_pref_score,time_score,adjust_coeff,score)

	if popularity_comp == 0:
		popularity_comp = "N.A"
	else:
		popularity_comp = str(round(popularity_comp, 1))

	if core_comp == 0:
		core_comp = "N.A"
	else:
		core_comp = str(round(core_comp, 1))

	if prof_comp == 0:
		prof_comp = "N.A"
	else:
		prof_comp = str(round(prof_comp, 1))

	if time_comp == 0:
		time_comp = "N.A"
	else:
		time_comp = str(round(time_comp, 1))

	return (score, popularity_comp + "\t" + core_comp + " \t" + prof_comp + " \t" + time_comp)


def getBestCourse(unavailable, popularity_coeff, core_coeff, prof_coeff, time_coeff, courses, difficulty, overall_coeff, diff_coeff, prof_dict, core_courses):
	score_best = (-1, "")
	course_best = None
	for course in courses:
		score = getScore(popularity_coeff, core_coeff, prof_coeff, time_coeff, course, difficulty, overall_coeff, diff_coeff, prof_dict, core_courses)
		if score[0] == -1:
			unavailable.append((course, "-- Insufficient Data"))
		if score[0] > score_best[0]:
			score_best = score
			course_best = course

	if course_best == None:
		return ((-1, ""), None)
	return (score_best, course_best)


def satisfyPre(course, pre_reqs, courses_taken, unavailable):
	title = course.getTitle()
	if title not in pre_reqs.keys():
		unavailable.append((course, "-- Course Not Found"))
		return False
	courses_req = pre_reqs[title]
	for course_req in courses_req:
		if course_req.strip().upper() not in courses_taken:
			return False
	return True


def recommendCourses(popularity_coeff, core_coeff, prof_coeff, time_coeff, difficulty, overall_coeff, diff_coeff, n = 5, fetch=False):
	total_coeff = popularity_coeff + core_coeff + prof_coeff + time_coeff
	popularity_coeff = popularity_coeff / total_coeff
	core_coeff = core_coeff / total_coeff
	prof_coeff = prof_coeff / total_coeff
	time_coeff = time_coeff / total_coeff

	professor_dict = crawler.prof.make_prof_dict(PROF_FILENAME)
	courses_dict = crawler.course.get_all_courses(fetch)
	core_courses = algo.requisites.getCores("csci")
	pre_reqs = algo.requisites.getReqs("csci")
	courses_taken = algo.requisites.getCoursesTaken()
	best_score_courses = []
	unavailable = []
	for name, courses in courses_dict.items():
		if "CSCI" not in name:
			continue
		if len(courses) == 0:
			raise RuntimeError
		if courses[0].getTitle() in courses_taken:
			continue
		if not satisfyPre(courses[0], pre_reqs, courses_taken, unavailable):
			continue
		best_score_course = getBestCourse(unavailable, popularity_coeff, core_coeff, prof_coeff, time_coeff, courses, difficulty, overall_coeff, diff_coeff, professor_dict, core_courses)
		if best_score_course[1] == None:
			continue
		# print(best_score_course[1].getName(),"with score:", best_score_course[0][0])
		best_score_courses.append(best_score_course)

	n = min(n, len(best_score_courses))
	print("\nRecommended", n, "Courses:\t\t\t pop\tcore\tprof\ttime")
	best_score_courses.sort(reverse=True, key=lambda x: x[0][0])
	for score, course in best_score_courses[:n]:
		print(course.getName(), "with score", round(score[0], 1), "\t("+ score[1], ")\t", course.name)

	print("\nUnavailable Courses:")
	for course, reason in unavailable:
		print(course.getName(), reason)