#Assertion
def greater(num):
    if (num<0):
        raise Exception("sorry 0 and Negative number not allowed")
    
    assert (num>0),"number is less than 0"
greater(4)
print("terminating the Program")

#Exception handling
try:
    fp=open("text.txt","r")
    fp.write("i am doing well now")
except Exception as e:
    print("Error: cant find the file ",e)
finally:
    fp.close()
    print("file is closed succesfully")
print("finally Terminating the Program")

