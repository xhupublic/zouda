#!python

class Person:
    def __init__(self, name, addr, phone_num, date_of_birth, nationality):
        self.name = name
        self.addr = addr
        self.phone_num = phone_num
        self.date_of_birth = date_of_birth
        self.nationality = nationality

    def __str__(self):
        return "name : {}\naddr : {}\nphone : {}\nbirth : {}\nnationality : {}\n".format(self.name, self.addr, self.phone_num, self.date_of_birth, self.nationality)


class Worker(Person):
    def __init__(self, name, addr, phone_num, date_of_birth, nationality, company, company_addr, job_phone):
        super(Worker, self).__init__(name, addr, phone_num, date_of_birth, nationality)
        self.company = company
        self.company_addr = company_addr
        self.job_phone = job_phone

    def __str__(self):
        return "{}company : {}\ncompany addr : {}\njob phone : {}\n".format(super(Worker, self).__str__(), self.company, self.company_addr, self.job_phone)



class Scientist(Worker):
    def __init__(self, name, addr, phone_num, date_of_birth, nationality, company, company_addr, job_phone, discipline, types):
        super(Scientist, self).__init__(name, addr, phone_num, date_of_birth, nationality, company, company_addr, job_phone)
        self.discipline = discipline
        self.types = types

    def __str__(self):
        return "{}discipline : {}\ntypes : {}\n".format(super(Scientist, self).__str__(), self.discipline, self.types)

class Researcher(Scientist):
    pass

class Postdoc(Scientist):
    pass
    
class Professor(Scientist):
    pass


a = Person("Alpha", "NYC", "212-123-4567", "2001/01/02", "US")
print(a.__class__)
print(a)


b = Worker("Beta", "NYC", "212-123-4567", "2001/01/02", "US", "Facebook", "NYC", "212-987-6543")
print(b.__class__)
print(b)

c = Scientist("Charile", "NYC", "212-123-4567", "2001/01/02", "US", "Facebook", "NYC", "212-987-6543", "Physics", ["experimental", "computational"])
print(c.__class__)
print(c)

d = Researcher("Delta", "NYC", "212-123-4567", "2001/01/02", "US", "OSU", "OH", "212-987-6543", "Physics", ["experimental", "computational"])
print(d.__class__)
print(d)

e = Postdoc("Echo", "NYC", "212-123-4567", "2001/01/02", "US", "OSU", "OH", "212-987-6543", "Physics", ["experimental", "computational"])
print(e.__class__)
print(e)

f = Professor("Foxtrot", "NYC", "212-123-4567", "2001/01/02", "US", "OSU", "OH", "212-987-6543", "Physics", ["experimental", "computational"])
print(f.__class__)
print(f)