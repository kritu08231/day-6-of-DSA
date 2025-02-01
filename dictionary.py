""""Write a program to create a dictionary with student names and their marks, and apply the following
operations:
 Add a new student with marks.
 Update the marks of an existing student.
 Remove a student
 Print student names with their marks."""
student={'name':['Kritika'],'marks':[90]}
print('Dictionary:',student)
#Add a new student with marks.
student['name'].append('astha')
student['marks'].append(70)
print(student)
#Update the marks of an existing student.
student['marks']=[85,56]
print(student)
#Remove a student
student['name'].remove('astha')
student['marks'].remove(56)
#Print student names with their marks.
print(student)
print(type(student))
