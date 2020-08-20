class Employee:

    noOfLeaves = 8

    def __init__(self,name,role,salary):
           self.name = name
           self.role = role
           self.salary = salary

    def printDetails(self):
        return f'Hey your name is {self.name} and your role  is {self.role} and your salary is {self.salary}'

    @classmethod
    def changeOfleaves(cls,newleaves):
           cls.noOfLeaves = newleaves 

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        #print(params)
        return cls(params[0],params[1],params[2])
    
    @staticmethod
    def printgood(string):
        print('This is good'+string)  
        return 'Hii' 

    #Dunder Methods
    def __add__(self,other):
            return self.salary+other.salary

    def __truediv__(self,other):
        return 756    

    def __repr__(self):
        return self.printDetails() 
    

    def __str__(self):
        return f'Hey your name is {self.name} and your role  is {self.role} and your salary is {self.salary}'
    
        



    



emp1 = Employee('Harry','Instructor',400000)
#emp2 = Employee('Rohan','Engineer',50000)
#print(emp1+emp2)
#print(emp1/emp2)
print(str(emp1))
