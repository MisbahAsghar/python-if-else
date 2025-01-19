#1st student
student_name = input("Enter 1st student name: ")
math = int(input("Enter maths marks: "))
english = int(input("Enter english marks: "))
urdu = int(input("Enter urdu marks: "))
islamiat = int(input("Enter islamiat marks: "))
computer = int(input("Enter computer marks: "))

Total = math + english + urdu + islamiat + computer
print("Total marks:", Total)

percentage = (Total / 500) * 100
print("Percentage:", percentage)

# Determine grade
if percentage >= 90:
    print("Your Grade is A+")
elif percentage >= 80:
    print("Your Grade is A")
elif percentage >= 70:
    print("Your Grade is B")
elif percentage >= 60:
    print("Your Grade is C")
elif percentage >= 50:
    print("Your Grade is D")
else:
    print("You Are Fail")
    print("Work Herd,Next Time")

# 2nd student
student_name = input("Enter 2nd student name: ")
math = int(input("Enter math marks: "))
english =int(input("Enter english marks: "))
urdu =int(input("Enter urdu marks: "))
islamiat =int(input("Enter islamiat marks: "))
computer =int(input("Enter computer marks: "))

Total = math + english + urdu + islamiat + computer
print("Total marks:", Total)

percentage = (Total / 500) * 100
print("Percentage:", percentage)

if percentage >= 90:
    print("Your Grade is A+")
elif percentage >= 80:
    print("Your Grade is A")
elif percentage >= 70:
    print("Your Grade is B")
elif percentage >= 60:
    print("Your Grade is C")
elif percentage >= 50:
    print("Your Grade is D")
else:
    print("You Are Fail")
    print("Work Hard,Next Time ")                      

    