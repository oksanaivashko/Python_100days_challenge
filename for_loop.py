### Print the list of fruits from the list
#Fruits list
fruits=["Apple", "Peach", "Pear"]
#does the command to print each fruit from the list
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
    print(fruits)


### For Loop
    ### Calculate the average of height of students
    student_heights = input("Input a list of student ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = sum(student_heights)
number_height = len(student_heights)
average_height = round(total_height / number_height)
print(average_height)