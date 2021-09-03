rno = int(input("Enter Roll Number : "))
name = input("Enter Name : ")
standerd = input("Enter Class : ")
eng = int(input("Enter Marks of English : "))
math = int(input("Enter Marks of Maths : "))
phy = int(input("Enter Marks of Physics : "))
chem = int(input("Enter Marks of Chemistry: "))

obt_marks = eng+math+phy+chem
per = obt_marks/4

#MarkSheet
print("-------------STUDENT'S MARKSHEET-------------")
print("Your Roll Number is : " + str(rno))
print("Your Name is : " + name)
print("Your Class is : " + standerd)
print("Obtained Marks are : " + str(obt_marks))
print("Your Percentage is : " + str(per))

#Grade
if per >=80:
    print("Grade : A+\nRemarks : Excellent")
elif per>=70:
    print("Grade : A\nRemarks : Very Good")
elif per>=60:
    print("Grade : B\nRemarks : Good")
elif per>=50:
    print("Grade : C\nRemarks : Fair")
elif per>=40:
    print("Grade : D\nRemarks : Poor")
elif per>=33:
    print("Grade : E\nRemarks : Need Improvement")
else:
    print("FAIL!!!!\nRemarks : Failure")

#Fail Subjects Name & Counts
i = 0
fail_sub = ""
if eng<33:
    i=i+1
    fail_sub+="English"
if math<33:
    i=i+1
    fail_sub+="Maths"
if phy<33:
    i=i+1
    fail_sub+="Physics"
if chem<33:
    i=i+1
    fail_sub+="Chemistry"
print("Failed Subjects Count : " + str(i))
print("Failed Subjects Name : " + str(fail_sub))