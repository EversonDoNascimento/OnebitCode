courses = []
with open("data/courses.csv", 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.strip().split(',')
        courses.append(f"{language} - {category}")

for course in sorted(courses, reverse=True):
    print(course)