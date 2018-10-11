class Telephone:
    '''
    creates an object that stores a telephone number and its type/location and returns it as one string
    '''
    def __init__(self, tele):
        self.loc = tele.split(' ')[0]
        self.number = tele.split(' ')[1]
    def __repr__(self):
        return '<'+ self.loc + ': ' + self.number + '>'
            
class Student:
    '''
    creates an object that stores different properies of a student and lets you add phone numbers
    '''
    def __init__(self,first_name, last_name,tele,email,grade):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = []
        self.phone.append(Telephone(tele))
        self.email = email
        self.grade = grade
    
    def name(self):
        return self.first_name + self.last_name
    
    def add_phone(self,tele):
        self.phone.append(Telephone(tele))
            
    def __str__(self):
        output = []
        for element in vars(self).items():
            output.append(element[0]+': '+ str(element[1]))
        str_all_items = '\n'.join(output)
        return str_all_items

erik = Student('Erik','Lehmann','office 555','erik.lehmann@gmail.com','pending')
erik.add_phone('mobile 444') 
erik.add_phone('home 777') 

print(erik)