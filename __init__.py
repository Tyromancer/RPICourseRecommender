from crawler import *
from algo import *


popularity_coeff = 1
core_coeff = 1
prof_coeff = 1
time_coeff = 1

#professor preferance:
#difficulty from 1.0 to 5.0
#overall_coeff + diff_coeff = 1
difficulty = 3.0
overall_coeff = 0.65
diff_coeff = 0.35

recommandCourses(popularity_coeff, core_coeff, prof_coeff, time_coeff, difficulty, overall_coeff, diff_coeff)