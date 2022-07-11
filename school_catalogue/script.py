# Create Parent Class
class School():
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    def set_numberOfStudents(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents

    def __repr__(self):
        return f'A {self.level} school named {self.name} with {self.numberOfStudents} students'

class Primary():
    pass

class Middle():
    pass

class High():
    pass

class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy, level='primary'):
        super().__init__(name, "primary", numberOfStudents)
        self.pickupPolicy = pickupPolicy
        
        def get_pickup_policy(self):
            return self.pickupPolicy
        
        def __repr__(self):
            parentRepr = super().__repr__()
            return parentRepr + "The pickup polity is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
    def __init__init(self, name, numberOfStudents, sportsTeams):
        super().__init__(self.name, "high", numberOfStudents)
        self.sportsTeams = sportsTeams
        
    def get_sports_teams(self):
        return self.sportsTeams

    def __repr__(self):
        return self.sportsTeams
        
c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sports_teams())
print(c)
