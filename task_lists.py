fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits)
print("the first fruit is:", fruits[0])
print("the last fruit is:", fruits[-1])

fruits[1]="mango"
print("the second fruit is now:", fruits[1])

fruits.insert(2,"watermelon")
print("after inserting watermelon, the fruits are:", fruits)

fruit = input("name a fruit : ")
print(fruits.count(fruit) != 0)

fruits.sort()
print(fruits)

