def modifyList(lst):
    lst.append(10)
    print("inside funtion:",lst)
    
numbers=[1,2,3,4]
modifyList(numbers)
print("outside funtion:",numbers)
