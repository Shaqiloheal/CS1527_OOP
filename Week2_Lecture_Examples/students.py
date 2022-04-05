class Student:
    """A class representing a student."""
    
    def __init__(self, na, ag):
        self.full_name = na
        self.age = ag

    def get_name(self):
        return self.full_name
    
    def get_age(self):
        return self.age

    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) > 1   

# Driver code
if __name__ == '__main__':

    student_1 = Student('James Smith', 32)
    student_2 = Student('Ada Wong', 25)
    student_3 = Student('William Wallace',45)
    student_4 = Student('Gergana Paskova', 20)


    #print(student_1.get_name(), 'is', student_1.get_age(), 'years old.')
    #print(student_2.get_name(), 'is', student_2.get_age(), 'years old.')
    #print(student_3.get_name(), 'is', student_3.get_age(), 'years old.')
    #print(student_4.get_name(), 'is', student_4.get_age(), 'years old.')

    # Uses staticmethod to check if full name has a space greater than 1
    print(Student.is_full_name('Bob'))          # False
    print(Student.is_full_name('James Smith'))  # True