#input python list for fruits

fruits=["Apple", "Peach", "Pear"]
for fruits in fruits:
    print(fruits)
    print(fruits+"Pie")
    print(fruits)
       
#input python list for student heights
student_heights=input().split()
for n in range (0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
    
total_height=0
for height in student_heights:
    total_height+=height    #total+height=total_height+height
    print(f"total_height= {total_height}")  
    
number_of_students=0
for student in student_heights:
    number_of_students+=1
    print(f"number of students= {number_of_students}")   
    
average_height=round(total_height / number_of_students)
print(f"average_height={average_height}")