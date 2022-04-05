class School:

    def __init__(self, na, bldg):
        self.name = na
        self.building = bldg

    class Academic:

        def __init__(self, na, schl):
            self.name = na
            self.school = schl

            def et_name(self):
                return self.name + 'PHD'

from people import Academic

ncs = School('NCS', 'Meston')
staff = Academic('Julie Kow', ncs)
print(staff.get_name())