from bs4 import BeautifulSoup
import requests

# 1. Set up headers to avoid 403 errors
headers = {'user-agent': 'my-app/0.0.1'}

# 2. Fetch the Flatiron School homepage
html = requests.get("https://flatironschool.com/", headers=headers)   

# 3. Parse the HTML with BeautifulSoup
doc = BeautifulSoup(html.text, 'html.parser')

# 4. Select the element with the class 'heading-financier'
financier_elements = doc.select('.heading-financier')
print("Elements with class 'heading-financier':")
print(financier_elements)

# 5. Extract and clean the text from the first matching element       
if financier_elements:
    text = financier_elements[0].contents[0].strip()
    print("\nText content of first '.heading-financier':")
    print(text)

# 6. Fetch the Flatiron School courses page
courses_html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
courses_doc = BeautifulSoup(courses_html.text, 'html.parser')

# 7. Select all course title elements using all three classes
courses = courses_doc.select('.heading-60-black.color-black.mb-20')   
print("\nCourse titles found:")
for course in courses:
    # .contents[0] gets the text node, .strip() removes whitespace    
    print(course.contents[0].strip())

# 8. Show tag name and attributes for the first course element        
if courses:
    print("\nFirst course element tag name:", courses[0].name)        
    print("First course element attributes:", courses[0].attrs)
