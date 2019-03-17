import algo.main

if __name__ == '__main__':
	popularity_coeff = 1
	core_coeff = 1
	prof_coeff = 1
	time_coeff = 1

	# popularity_coeff = 10  # coefficient of course popularity
	# core_coeff = 1         # coefficient of whether course is core requisite or not
	# prof_coeff = 1         # coefficient of overall and difficulty grade of professor
	# time_coeff = 1         # coefficient of time preference

	# Data of professors are scraped from RateMyProfessor
	# professor preferance:
	# difficulty from 1.0 to 5.0
	# overall_coeff + diff_coeff = 1
	difficulty = 3.0       # desired difficulty of professor
	overall_coeff = 0.65   # percentage of consideration of overall grade
	diff_coeff = 0.35      # percentage of consideration of difficulty
	num = 10               # max number of recommended courses

	fetch = False          # indicates whether to reload course data from RPI websites or not

	# call the main algorithm
	algo.main.recommendCourses(popularity_coeff, core_coeff, prof_coeff, time_coeff, difficulty, overall_coeff, diff_coeff, num, fetch)
