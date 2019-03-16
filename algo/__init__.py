

def dropRateScore(drop_rate):
	return 0

def coreRequireScore(core_list, concentration_list, course):
	if course in core_list:
		return 2
	elif course in concentration_list:
		return 1
	return 0

def profPrefScore(prof_pref):
	return 0

def timeZoneScore(course, time_zone_pref):
	return 0

def totalScore(drop_rate_score, core_score, prof_pref_score, time_zone_score):
	drop_rate_coef = 1
	core_coef = 1
	prof_pref_coef = 1
	time_zone_coef = 1
	score = drop_rate_coef * drop_rate_score + core_coef * core_score + prof_pref_coef * prof_pref_score + time_zone_coef * time_zone_score
	return score