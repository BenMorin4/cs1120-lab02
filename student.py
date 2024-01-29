class Student:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
        self.__courses = []
        self.__credits = 0

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_courses(self):
        return self.__courses
    
    def get_credits(self):
        return self.__credits
    
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_courses(self, courses):
        self.__courses = courses

    def set_credits(self, credits):
        self.__credits = credits

    def take_course(self, name, credits):
        self.__courses.append({name, credits})
        self.__credits += credits

    def print_data(self):
        for name, credits in self.__courses.items():
            print(f'Course taken: {name} ({credits} credits)')

        print(f'Credits Completed {self.__credits}')
