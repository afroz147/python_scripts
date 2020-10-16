# constructors and Destructors
class employee:
    def __init__(self):
        print("constructor called")

    def __del__(self):
        print("destructor called")

emps = employee()

print ("calling Destructor")
del  emps


# class variable and Instance Variables 
class emp:
    count =0
    def __init__(self,name,eid):
        print("Adding Employee")
        self.name= name
        self.eid= eid
        emp.count = emp.count+1
    def employee_disp(self):
        print("Displaying Employee Details")
        print("employee name is %s" %self.name)
        print("employee eid is %s" %self.eid)
        print ("employee count is %d" %emp.count)
emp1=emp("afroz",726772)
emp1.employee_disp()
print("%d employee is added successfully" %emp.count)


#inheritence
class Parent:
    attr=0
    def __init__(self):
        print("Parent Constructor called")
    
    def parent_method(self):
        print("parent method called")
        print("attribute value is %d" %Parent.attr)

class child(Parent):
    def __init__(self):
        print("child constructor called")
    
    def child_method(self):
        print("child method called")
        self.value = Parent.attr + 59
        print("attribute value is %d" %self.value)
c=child()
c.child_method()
c.parent_method()

# Method Overloading

"""def add(a,b):
    return a+b"""

def add(a,b,c):
    return a+b+c

#func1=add(1,2)
func2= add(1,2,3)
#print(func1)
print(func2)

#Method Overiding
class animal:

    def eat(self):
        print("Animal eat method called")
        

class dog(animal):
    def eat(self):
        print("Dog eat method called")

    def bark(self):
        print("Dog bark method called")
    

a=animal()   
c=dog()
c.eat()
a.eat()

## Data Hiding
class attr:
    count=2
    __count=3
    def display(self,a):
        self.a=a
        print(self.a)

attribute=attr()
print(attr.count)
attribute.display(4)
print(attribute._attr__count)

