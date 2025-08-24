class Student:
    def __init__(self, full_name, section, spanish_grade, english_grade, socials_grade, science_grade):
        self.full_name = full_name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.socials_grade = socials_grade
        self.science_grade = science_grade
        self.average_grade = self.calculate_average()
    
    def calculate_average(self):
        return (self.spanish_grade + self.english_grade
                + self.socials_grade + self.science_grade) / 4
    
    def to_dict(self):
        return {
            'full name' : self.full_name,
            'Section' : self.section,
            'Spanish grade' : self.spanish_grade,
            'English_grade' : self.english_grade,
            'Socials grade' : self.socials_grade,
            'Science grade' : self.science_grade,
            'Average grade' : self.average_grade
        }