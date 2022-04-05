class Student:

    def __init__(self, na, id, crs):
        self.name = na
        self.idNum = id
        self.course = crs

    def get_name(self):
        return self.name


class Academic:

    def __init__(self, na, schl):
        self.name = na
        self.school = schl

    def get_name(self):
        return 'Dr ' + self.name

        