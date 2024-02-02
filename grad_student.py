from student import Student

class GradStudent(Student):
    def __init__(self, name, id):
        super().__init__(name, id)

        self.__published_papers = []

    def get_published_papers(self):
        return self.__published_papers
    
    def set_published_paper(self, published_papers):
        self.__published_papers = published_papers

    def publish_paper(self, published_paper):
        self.__published_papers.append(published_paper)

    def print_data(self):
        # print papers
        for paper_number, paper in enumerate(self.__published_papers):
            print(f'Publication #{paper_number+1}: {paper}')

        # print courses
        for course in self.get_courses():
            name, credits = course
            print(f'Course taken: {name} ({credits} credits)')

        print(f'\nCredits Completed {self.get_credits()}\nNumber of Publications: {len(self.__published_papers)}')