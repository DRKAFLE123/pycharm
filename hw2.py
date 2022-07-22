# reverse the number
# from goto import goto,label
# label.up
n=int(input("Enter the number"))
# n=123
temp=n


rev=0;
i=0;
while(temp>0):
 r=temp%10
 rev=rev*10+r
 temp=temp//10 #// is for quotient in python and / for float division
 i+=1
print('Reverse of given number is: ', rev) #this is the reverse
#check the palidrome
if(n==rev):
    print('Given input is a palidrome number')
else:
    print('Given input is not a palidrome number')
    # goto.up

#finding the sequence