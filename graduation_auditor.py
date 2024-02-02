class GraduationAuditor():

    # this receives a list of Students, graduate or undergrad
    def audit(self, students):
        for student in students:
            # if they are a grad student
            if getattr(student, 'publish_paper', False):
                # did they meet graduation requirements
                if student.get_credits() >= 30 and len(student.get_published_papers()) >= 2:
                    print(f'{student.get_name()} can graduate')
                else:
                    print(f'{student.get_name()} cannot graduate')
            # undergrad student
            else:
                # did they meet graduation requirements
                if student.get_credits() >= 30 and student.get_community_service() >= 20:
                    print(f'{student.get_name()} can graduate')
                else:
                    print(f'{student.get_name()} cannot graduate')
