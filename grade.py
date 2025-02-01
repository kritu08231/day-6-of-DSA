""""Write a Python program to calculate a student's total marks, percentage, and grade. The user will input
the marks obtained in each of the three subjects. Assign grades according to the following criteria:
Grade A: Percentage >= 80
Grade B: Percentage >= 70 and < 80
Grade C: Percentage >= 60 and < 70
Grade D: Percentage >= 40 and < 60
Grade E: Percentage < 40"""
S1=int(input ('Enter the marks of 1st subject '))
S2=int(input ('Enter the marks of 2st subject '))
S3=int(input ('Enter the marks of 3st subject '))
S4=int(input ('Enter the marks of 4st subject '))
S5=int(input ('Enter the marks of 5st subject '))
Total_Marks=S1+S2+S3+S4+S5
print("Total Marks:",Total_Marks)
Percentage=Total_Marks/500*100
print('Percentage:',Percentage)
if(Percentage>=80):
    print("Grade A")
elif(Percentage >=70 and Percentage< 80):
    print("Grade B")
elif(Percentage >= 60 and Percentage< 70):
    print("Grade C")
elif( Percentage >= 40 and Percentage< 60):
    print("Grade D")
else:
    print("Grade E")


