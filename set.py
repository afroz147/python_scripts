print ("empty set")
set1=set()
print (set1)
print("set with elememts")
set2= set([1,"afroz"])
print (set2)
print("adding elements")
set3=set([1,2])
set3.add((3,4))
print (set3)
print("updating elements")
set3.update([5,6])
print (set3)

print("removing  elements")
set3.remove(5)
print (set3)
print("discarding elements")
set3.discard(1)
print (set3)
print("key error")
set3.discard(1)
print (set3)
print("pop Action")
set3.pop()
print (set3)

