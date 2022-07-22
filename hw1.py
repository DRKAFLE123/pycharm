print("Hello,World !")
#swapping two number without temp
a=2
b=4
print("a and b before swap",a,'and',b)
a=a+b
b=a-b
a=a-b
print("a and b after swap",a,'and',b)
#average no of given list
# def Average(l):
#     avg=sum(l)/len(l)
#     return avg
list=[1,2,3,4,5,6,7,8,9]
average=sum(list)/len(list)
print('Average list is :',average)
# #odd no from given list
# list_2=[1,2,3,4,5,6,7,8,9,0]
# if((list_2 % 2)!==0):
#     print('odd no are',)

#reverse the number
# n=123
# temp=n
# i=1
# while(temp>0):
# r=temp%10
# rev=rev*10+r
# temp=temp/10
# i=i+1
# print('Reverse=',rev)

# for-loop
# i=1;
# num=int(input("enter thr number:"));
# for i in range(0,10):
#     print("%d*%d=%d" %(num,i,num*i));

    #nested loop
# i=0;
# j=0;
# n=int(input("Enter the number"))
# for i in range(0,n):
#  print()
#  for j in range(0,i+1):
#   print("*",end=" ")

  # else loop

  # while loop
# i=1;
#  # n=0; starts and end rangee
#  # b=9;
# while(i<=10):
#   print("%d*%d=%d" %(num,i,num*i))
#   i=i+1
#list
Name=['Damodar','sandeep','bikash','subash'] #list of string

print(Name)
print(type(Name))
print(Name[3])
Name[3]='Roshan'
print(Name)
Name[3:4]=[11,12,23]
print(Name)
del Name[3:4]
print(Name)
#tuple
number=(1,2,3,4,5,6,7,8,9)
print(number)
count=0
for i in number:
  print("number(%d)=%d" %(count,i));
  count=count+1;
print(type(number))

#set
days={"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
print(days)
print(type(days))
for i in days:
  print(i);#set prints data in ordered way why ?beacause it is unordered collection

number={1,2,5,6,8,9,3,10,34,76}
print(number)
#use dir(number)
  #dictonary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#next example
# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# using dict()
my_dict = dict({1:'apple', 2:'ball'})

# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])


# Removing elements from a dictionary

# create a dictionary
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# remove a particular item, returns its value
# Output: 16
print(squares.pop(4))

# Output: {1: 1, 2: 4, 3: 9, 5: 25}
print(squares)

# remove an arbitrary item, return (key,value)
# Output: (5, 25)
print(squares.popitem())

# Output: {1: 1, 2: 4, 3: 9}
print(squares)

# remove all items
squares.clear()

# Output: {}
print(squares)

# delete the dictionary itself
del (squares)

# Throws Error
print(squares)
