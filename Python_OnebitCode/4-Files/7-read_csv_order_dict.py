courses =[]

with open("data/courses.csv", "r", encoding="utf-8") as file:
    for line in file:
        language, category = line.strip().split(',')
        course = {}
        course['language'] = language
        course['category'] = category
        courses.append(course)
        #courses.append({'language': language, 'category': category})

def get_category(course):
    return course['category']

def get_language(course):
    return course['language']

for course in sorted(courses, key=get_language, reverse=True):
    print(f"{course['language']} - {course['category']}")