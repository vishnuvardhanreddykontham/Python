##
##
####1.  Add a list of elements to a given set
##
##set1={"python","java",12,21.32}
##lst1=[1,2,4,5]
##set1.update(lst1)
##    
##print(set1)
##
##output:
##{1, 2, 4, 5, 'python', 12, 'java', 21.32}
##  
##
####2. Return a set of identical items from a given two Python
##
##set1={"python","java",1,3}
##set2={1,5,"java"}
##
##set3=set1.intersection(set2)
##print(set3)
##
##output:
##
##{1, 'java'}
##
####3.Returns a new set with all items from both sets by removing duplicates
##
##set1={"python","java",1,3}
##set2={1,5,"java"}
##
##set3=set1.union(set2)
##        
##        
##print("set3:",set3)
##
##output:
##
##set3: {1, 3, 'java', 5, 'python'}
##
####4.Given two Python sets, update first set with items that exist only in the first set and not in the second set.
##
##set1={"python","java",1,3}
##
##set2={1,5,"java"}
##
##set3=set1-set2
##print(set3)
##
##
##output:
##
##{3, 'python'}
##
##
####5.Remove 10, 20, 30 elements from a following set at once
##
##set1={10,20,30,40,5,60}
##set2={10,20,30}
##set3=set1.symmetric_difference(set2)
##print(set3)
##
##
##output:
##{5, 40, 60}
##
####6.Return a set of all elements in either A or B, but not both
##
##set1={10,20,30,40,50}
##set2={20,30,40,70,80}
##
##print(set1.symmetric_difference(set2))
##
##output:
##{80, 50, 70, 10}
##
##
####7.Determines whether or not the following two sets have any elements in common. If yes display the common elements
##
##set1 = {10, 20, 30, 40, 50}
##set2 = {60, 70, 80, 90, 10,30}
##set3 = set()
##set1.isdisjoint(set2)
##set3=set1.intersection(set2)
##print(set3)
##
####output:
####
####{10, 30}
##
####8. Update set1 by adding items from set2, except common items
##
##set1 = {10, 20, 30, 40, 50}
##set2 = {30, 40, 50, 60, 70}
##set1.symmetric_difference_update(set2)
##
##print(set1)
##
##output:
##{20, 70, 10, 60}
##
##
##
####9. Remove items from set1 that are not common to both set1 and set2
##
##set1 = {10, 20, 30, 40, 50}
##set2 = {30, 40, 50, 60, 70}
##
##set1.intersection_update(set2)
##print(set1)
##
##output:
##{40, 50, 30}
##
##
####10.Write a Python program to check if a given set is superset of itself and superset of another given set
##
##set1={"python","java",1,2}
##set2={"python",1,2}
##if set1.issuperset(set2):
##    print("True",set2)
##else:
##    print("False",set2)
##
##    
##output:
##True {1, 2, 'python'}
##
####11.Write a Python program to check a given set has no elements in common with other given set
##set1={"python",1,2}
##set2={"python","java",1,2}
##set3={"maruti"}
##print(set1.isdisjoint(set2))
##print(set1.isdisjoint(set3))
##
##
##output:
##
##False
##True
##
####12.Write a Python program to remove the intersection of a 2nd set from the 1st set.
##
##set1={"HYD","MUMBAI","CHENNAI","LUCKNOW","DELHI"}
##set2={"HYD","DELHI"}
##result=set1-set2
##
##print(result)
##set1.difference_update(set2)
##print(set1)
##
##output:
##{'LUCKNOW', 'CHENNAI', 'MUMBAI'}
##{'LUCKNOW', 'MUMBAI', 'CHENNAI'}
##
####13. Perform all sets methods by taking an example of your own.
##
####Create a Set:
##thisset={"apple","banana","orange","mango"}
##print(thisset)
##
##output:
##{'orange', 'banana', 'mango', 'apple'}
##
####Get the Length of a Set:
##
##thisset={"apple","banana","orange","mango"}
##print(len(thisset))
##
##output:
##4
##type():
##
##thisset={"apple","banana","orange","mango"}
##print(type(thisset))
##
##output:
##
##<class 'set'>
##
####The set() Constructor:
##thisset=set(("apple","banana","orange","mango"))
##print(thisset)
##output:
##
##{'apple', 'orange', 'mango', 'banana'}
##
####Access Items:
##
##thisset={"apple","banana","orange","mango"}
##for i in thisset:
##    print(i)
##output:
##orange
##banana
##apple
##mango
##
##
####Add Items:
##    
##thisset={"apple","banana","orange","mango"}
##
##thisset.add("watermelon")
##print(thisset)
##
##output:
##{'banana', 'watermelon', 'mango', 'apple', 'orange'}
##
##
####Add Sets:
##
##thisset={"apple","banana","orange","mango"}
##thisset2={"rose","lotus"}
##thisset.update(thisset2)
##print(thisset)
##
##output:
##
##{'mango', 'lotus', 'banana', 'orange', 'rose', 'apple'}
##
####Add Any Iterable:
##
##thisset={"apple","banana","orange","mango"}
##
##list=["rose","lotus"]
##thisset.update(list)
##print(thisset)
##
##output:
##{'rose', 'apple', 'lotus', 'banana', 'orange', 'mango'}
##
####Python - Remove Set Items:
##
##thisset={"apple","banana","orange","mango"}
##thisset.remove("mango")
##print(thisset)
####output:
####{'banana', 'orange', 'apple'}
##
####thisset={"apple","banana","orange","mango"}
####thisset.discard("banana")
####print(thisset)
##
####output:
##
####{'apple', 'orange', 'mango'}
####
##
##thisset={"apple","banana","orange","mango"}
##x=thisset.pop()
##print(x)
##print(thisset)
##
##output:
##apple
##{'orange', 'mango', 'banana'}
##
##thisset={"apple","banana","orange","mango"}
##thisset.clear()
##print(thisset)
##
##output:
##
##set()
##
##thisset={"apple","banana","orange","mango"}
##del thisset
##print(thisset)
##
##output:
##
##Traceback (most recent call last):
##  File "C:\Users\vk22213\Desktop\pyhton\08-08-2022\sets.py", line 268, in <module>
##    print(thisset)
##NameError: name 'thisset' is not defined
##

"""
thisset={"apple","banana","orange","mango"}
thisset2={"rose","lotus"}
set2=thisset.union(thisset2)
print(set2)

output:

{'orange', 'banana', 'mango', 'apple', 'lotus', 'rose'}

##Keep ONLY the Duplicates:
thisset={"pyhton","java","c++"}
thisset1={"python","c++"}

thisset.intersection_update(thisset1)
print(thisset)

output:
{'c++'}

thisset={"pyhton","java","c++"}
thisset1={"python","c++"}
result=thisset.intersection(thisset1)
print(result)

output:
{'c++'}

##Keep All, But NOT the Duplicates:

thisset = {"apple", "banana", "cherry"}
thisset1 = {"google", "microsoft", "apple"}

thisset.symmetric_difference_update(thisset1)

print(thisset)

output:
{'google', 'microsoft', 'cherry', 'banana'}
"""
thisset = {"apple", "banana", "cherry"}
thisset1 = {"google", "microsoft", "apple"}
result=thisset.symmetric_difference(thisset1)
print(result)

output:
{'cherry', 'google', 'banana', 'microsoft'}
























  











