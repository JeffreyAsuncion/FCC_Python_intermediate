# Lists: ordered, mutable, allows duplicate elemetns

mylist = ["banana", "cherry", "apple"]
print(mylist)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("Found it!")
else:
    print("No not Found :'(")

# number of elements in your list
print("length of list")
print(len(mylist))

# append "lemon" to mylist
mylist.append("lemons")

print(mylist)

# insert into list
mylist.insert(1, "mangos")

print(mylist)

# remove items use pop()
mango = mylist.pop(1)

print(mango + " was popped")
print(mylist)

# remove method if not found ValueError raised
mylist.remove("cherry")

print(mylist)

# clear makes an []
mylist.clear()

print(mylist)


mylist = ["banana", "cherry", "apple"]

# reverse method
mylist.reverse()

print(mylist)

# sort method sorts inplace
mylist.sort()

print(mylist)

# sorted sorts a new list
mylist.reverse()
print(mylist)
newList = sorted(mylist)
print(newList)

mylist = [0] * 5 
print(mylist)

mylist2 = [1,2,3,4,5]

new_list = mylist + mylist2
print(new_list)


# 10:35 slicing