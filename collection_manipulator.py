s_id=()
s_name=[]
s_age=[]
s_grade=[]
s_birth=()
s_subjects=[]

student_information=[]

student_record={}


print("Welcome to the Student Data Organizer !")
print("")

while True:

    print("Select an option :")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects offered")
    print("6. Exit")
    print("")

    print("------------------------")
    num=int(input("Enter a number = "))
    print("------------------------")

    print("")
    
    if num==1:
        print("Enter student details : ")
        
        a=int(input("Student ID : "))

        if a in student_record:
            print("This id's student already exists please enter new student details !!")
        else:
            b=input("Name : ")
            c=int(input("Age : "))
            d=input("Grade : ")
            e=input("Date of Birth (YYYY-MM-DD) : ")
            f=input("Subjects (space-separated) : ").split()

            s_id=list(s_id)
            s_id.append(a)
            s_id=tuple(s_id)
        
            s_name.append(b)

            s_age.append(c)

            s_grade.append(d)

            s_birth=list(s_birth)
            s_birth.append(e)
            s_birth=tuple(s_birth)

            s_subjects.append(f)

            student_information.append([b,c,d,f])

            student_record.update({a:student_information[-1]})

            print("")
            print("Student added successfully !")
        
        print("")
        print("*********************************************************************************************")
        print("")

    elif num==2:
        print("----------------------------------- Display All Students -----------------------------------")

        for i in student_record:
            print("Student ID : ",i,end="  |  ")
            print("Name : ",student_record[i][0],end="  |  ")
            print("Age : ",student_record[i][1],end="  |  ")
            print("Grade : ",student_record[i][2],end="  |  ")
            print("Subjects : ",student_record[i][3],end="\n")
        
        print("")
        print("*********************************************************************************************")
        print("")

    elif num==3:
        g=int(input("Enter Student ID : "))
        print("")

        if g in student_record:
            print("Select an option :")
            print("1. Update Age")
            print("2. Update Subjects")
            print("")

            h=int(input("Enter a number for update information : "))

            if h==1:
                i=int(input("Enter new Age : "))

                student_record[g][1]=i

                print("Student Age Updated Successfully !!")

            elif h==2:
                j=input("Enter new Subjects (space-separated) : ").split()

                student_record[g][3]=j

                print("Student Subjects Updated Successfully !!")

            else:

                print("Please Select Valid Option !! ")

        else:

            print("Student record not found !!")
            print("Please Enter Correct Student ID !!")
        
        print("")
        print("*********************************************************************************************")
        print("")

    elif num==4:
        k=int(input("Enter Student ID :"))

        if k in student_record:
            del(student_record[k])
            print("Student Deleted Successfully !!")

        else:
            print("Student record not found !!")
            print("Please Enter Correct Student ID !!")
        
        print("")
        print("*********************************************************************************************")
        print("")

    elif num==5:
        l=[]
        
        for i in student_record:
            for j in student_record[i][3]:
                l.append(j)

        l=set(l)
        print("Subjects offered : ",l)
    
        
        print("")
        print("*********************************************************************************************")
        print("")

    elif num==6:
        print("Thank you for using student data analyzer",end="\n")
        print("Good Bye !!")
        break

    else:
        print("Please Select valid option !!")
        print("*********************************************************************************************")
        print("")