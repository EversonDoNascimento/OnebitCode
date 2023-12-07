'''
1 - The static method not uses the parameter referring to the class 
2 - The static method can access, but can't modify the state of class
3 - We use the decorator @staticmethod to create a new static method
'''

class Language:
    def __init__(self, name, trail):
        self.trail = trail
        self.name = name

    @staticmethod
    def courses_trail(trail):
        if trail == 'Introduction to Python':
            courses = ["Dominating the Python","Modules and PIP", "POO"]
        elif trail == "Automation with the Python":
            courses = ["Automation of tasks","WEB Scraping"]
        else:
            courses = ["To be defined"]
        return courses

print(Language.courses_trail("Introduction to Python"))

