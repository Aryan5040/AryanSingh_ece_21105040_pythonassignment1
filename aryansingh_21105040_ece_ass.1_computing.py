#Assignment 1


#Question1

numb1=int(input("enter first number: "))
numb2=int(input("enter second number:"))
numb3=int(input("enter third number:"))

avg=(numb1+numb2+numb3)/3  #finding average of numbers
print(avg,'\n')


#Question 2

Income=int(input("Enter your income:"))
Members=int(input("No. of family members:"))#no of dependents

Taxableincome=Income-10000-(3000*Members)
tax=Taxableincome*20/100
print(tax,'\n')

#Question 3

print("Student=[SID, Name, Gender, Branch, CGPA]") #data needed
Info=[40, 'aryan', 'M', 'ECE', 9.9] #information
print('Info',Info,'\n')

#Question 4

print('Marks of five student')
Marks=[69, 96, 100, 2, 52]
print('list before sorting:',Marks)
Marks.sort()  #sorting a list
print('list after sorting:',Marks,'\n')

#Question 5(a)

Color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(Color)
Color.pop(3)
print('output color: ',Color,'\n')

#Question 5(b)

Color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(Color)
Color.pop(3)
print(Color)
Color.pop(3)
Color.insert(3,"purple")
print(Color,"\n")




                
