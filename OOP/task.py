class User:

    def __init__(self,name,birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_name(self):
       self.name =  self.name.upper()
       print(self.name)

    def age(self,current_year):
        return current_year - self.birthyear

me =User("Chris",1975)
print(me.age(current_year=2026))

john = User("John",1999)
print(john.age(current_year=2023))

john.get_name()