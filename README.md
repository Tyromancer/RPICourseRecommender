# RPICourseRecommender -- A course recommend python script for RPI students

## Developers:
-[x] Bogong Yang
-[x] Yutao Sun

## Dependencies:
- urllib.request
- bs4 (BeautifulSoup)

## Usage:
This is for HackRPI 2019 (it's a hackathon). Did not have much time for arranging and refactoring, so....
- Open RPICourseRecommender/__init__.py
- Change the variable fetch to True for first time running
- Change the rest variables to your preferences
- Create a txt file under /algo/doc named courses_taken.txt, it should include all classes the user has taken (One course per line, in form of 'XXXX-XXXX')
- Run Open RPICourseRecommender/__init__.py

##Notes:
- This thing currently only works for the major CSCI. For other majors, add the templates in /algo/doc, and modify the scripts accordingly (hmmmm)
