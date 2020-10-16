""" constructors and Destructors """
class employee:
    def __init__(self):
        print("constructor called")

    def __del__(self):
        print("destructor called")

emp = employee()

print ("calling Destructor")
del  emp

""" class variable and Instance Variables  """
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

"""inheritence"""
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

"""Method Overloading"""
def add(a.b):
    print(return a + b)
def add(a,b,c):
    print(return a+b+c)

add(1,2)
add(1,2,3)
