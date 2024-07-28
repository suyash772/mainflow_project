

print()
print()
print("*"*200)
print("TASK 1 = create a list ,dictonary, and a set and perform basic operation like adding, deleting & modifing elements ")
print("*"*200)
print()
print("********* creating list*******")
print()

list_1= ["hello",10,20,30,40.1,"world"]
print("list elements are:",list_1)
print()

print("********* adding element in list *******")
print("***   1. Append   ***")
list_1.append(500)
print(list_1)

print("***  2.Extend   ***")
list_1.extend(["mainflow",100,45])
print(list_1)
print()
print()

print("********* Remove element from list *******")
print("***    1.remove    *** ")
list_1.remove(100)
print(list_1)
print("***    2.pop    ***")
list_1.pop(2)
print(list_1)
print()
print()
print("********* Modifying element from list *******")
list_1[3]=("suyash")
print(list_1)
print()
print("*"*200)
print()

print("********** creating Dictionary ***********")
print()

dict_1= {'name':'suyash','age':23,'department':'computer application'}
print("dictionary elements are",dict_1)
print()

print("******** adding new key value pair *******")
dict_1['address']= "khalghat,mp"
print(dict_1)
print()

print("********* remove key value pair *******")
del dict_1['address']
print(dict_1)
print()

print("********* Modifying key value pair *******")
dict_1['mobile_number']= 87977977655
print(dict_1)
print()
print("*"*200)
print()

print("*************** creating set ***************")
print()
set_1={"apple",20,30,40,"mainflow","internship"}
print("set elements are:",set_1)
print()
print("********** adding element in set *******")
set_1.add(500)
print(set_1)
print()

print("********** remove element from set *******")
set_1.remove("mainflow")
print(set_1)
print()

print("********** modify element from set *******")
set_1.add('ram')
set_1.discard('1')
print(set_1)
print()
print("*"*200)
print()

print("****************************************************** 1ST TASK COMPLETED  THANK YOU ******************************************************************")
print()
print("*"*200)