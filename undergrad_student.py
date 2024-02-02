from student import Student

class UndergradStudent(Student):
    def __init__(self, name, id):
        super().__init__(name, id)

        self.__community_service = 0

    def get_community_service(self):
        return self.__community_service
    
    def set_community_service(self, community_service):
        self.__community_service = community_service

    def do_community_service(self, hours):
        self.__community_service += hours

    # print courses
    def print_data(self):
        for course in self.get_courses():
            name, credits = course
            print(f'Course taken: {name} ({credits} credits)')

        print(f'\nCredits Completed {self.get_credits()}\nHours of community sevice: {self.__community_service}')