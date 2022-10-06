a="Hola Pythonista".upper()
b=set(a)
c=frozenset(a) #you cannot change a frozen set


setOne = {'a', 'b', 'c', 'd'}
setTwo = {'e', 'f', 'g', 'a', 'b', 'c', 'd'}

#print(setOne<setTwo) #& intersection, | Union, < is subset?

#Ejercicio asd
#intersection_update(), isdisjoint(), isupperset(), 
#pop(), remove(), symmetric_difference(), 
# symmetric_difference_update() union() update()


#________________________________________________________________________
#intersection_update(): removes the elements that arenot present in both sets
#it's different from the intersection() cuz this method remove the unwanted elements
#from the original set (intersection() creates a new set with this elements).

inup_a = {'e', 'f', 'g', 'a', 'b', 'c', 'd'}
inup_b = {'e', 'f', 'g', 'a', 'b', 'c', 'd', 'hola', 'sample'}
#print(inup_b)
inup_b.intersection_update(inup_a)
#print(inup_b)


#_______________________________________________________________________
#isdisjoint(): true or false depending if a set is disjoint with other
# can also be dictionaries, list or tuples


isdis_set1 = {1, 2, 3, 4}
isdis_set2 = {5, 6, 7, 2, 8}

#print(isdis_set1.isdisjoint(isdis_set2)) #-> false


#_____________________________________________________________________
#isupperset(): returns true if a set has every element of another set
#same as > or < 

isup_set1 = {1, 2, 3, 4, 5}
isup_set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#print(isup_set2.issuperset(isdis_set1)) -> true
#print(isup_set1<isup_set2) -> true


#_______________________________________________________________________________
#pop(): return and removes from the list, dictionary, set, the last element.

pop_set1 = {'first', 'second', 'lastone'}
#print(pop_set1.pop())
#print(pop_set1.pop())
#print(pop_set1.pop())

#___________________________________________________________________________________
#remove(): removes the given element

remove_set1 = {1, 3, 4, 56, 7}
#print(remove_set1)
remove_set1.remove(56)
#print(remove_set1)

#__________________________________________________________________________________
#symetric_difference(): returns a set with all the items excluding the identical ones from two sets

sydiff_set1 = {1, 2, 69, 4, 5, 6}
sydiff_set2 = {90, 2, 4, 5, 6, 15}

#print(sydiff_set1.symmetric_difference(sydiff_set2)) #-> {1, 69, 90, 15}

#______________________________________________________________________________
#symetric_difference_update(): updates the set that's calling the method leaving only the items 
#that arenot identical

sydiffup_set1 = {1, 2, 69, 4, 5, 6}
sydiffup_set2 = {1, 2, 69, 45, 51, 4, 5, 6}
sydiffup_set1.symmetric_difference_update(sydiffup_set2)
#print(sydiffup_set1) #-> {51, 45}

#______________________________________________________________________-
#update(): insert an item ot a dictionario or another key value iterable object

up_dic1 = {
    'si': 'si',
    'hola': 'no',
    'year': '1999'
}

up_dic1.update({'adios': 'si'})
#print(up_dic1) #-> update dictionary

#_________________________________________________________________________
#union():  Return a set that contains all items from both sets, duplicates are excluded

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y)

print(z)