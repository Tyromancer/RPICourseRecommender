# RPICourseRecommender -- A course recommender python script for RPI students

## Developers:
- Bogong Yang
- Yutao Sun

## Inspiration
When we were deciding what courses to take for the next semesters, it was a slow and painful process.
So we wanted to build something that gives us some suggestions for course selection

## How we built it
### Dependencies:
- Python 3.6+
- urllib.request
- bs4 (BeautifulSoup)

### Test run:
- For the hackathon submission zip file, just run RPICourseRecommender/__init__.py

### Usage:
This is for HackRPI 2019 (it's a hackathon). Did not have much time for arranging and refactoring, so....
- Open RPICourseRecommender/__init__.py
- Change the variable fetch to True for first time running
- Run crawler/profs.py manually for first time running (It should create some txt file)
- Change the rest variables to your preferences
- Create a txt file under /algo/doc named courses_taken.txt, it should include all classes the user has taken (One course per line, in form of 'XXXX-XXXX')
- Run RPICourseRecommender/__init__.py

## Challenges we ran into
- Scraping from RPI website was hard. Used a ton of time to find where the information was located
- The project structure is a huge mess...

## Accomplishments that we are proud of
- Well at least it works, kind of

## What we learned
- How to scrape data from websites
- How to use txt file as database XD

## What's next for RPICourseRecommender
- Add templates for other majors than CSCI
- Use database instead of txt file. Reading from txt is sooooo slow
- Refactor code

## Notes:
- This thing currently only works for the major CSCI. For other majors, add the templates in /algo/doc, and modify the scripts accordingly (hmmmm)
- If you modifies this script and use it for a larger set of data, REMEMBER TO PAUSE EACH REQUEST FOR AT LEAST ONE SECOND SO THAT YOU DO NOT DDOS STUFF
