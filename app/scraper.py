import requests
from bs4 import BeautifulSoup

def scrape_courses():
    url = "https://brainlox.com/courses/category/technical"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    courses = []
    for course in soup.find_all('div', class_='course-details'):
        title = course.find('h2').text.strip()
        description = course.find('p').text.strip()
        courses.append({'title': title, 'description': description})

    return courses
