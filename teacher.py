import mysql.connector as sqltor
import matplotlib.pyplot as plt
import pandas as pd
import sys
import pyttsx3
import csv

def mainloop():
    mycon = sqltor.connect(host = "localhost", user = "root", passwd = "Tanish@0106", database = "stdbms")
    if mycon.is_connected():
        print("""
        +---------------------------------------------------------------------+
        |                  STUDENT REPORT GENERATOR SOFTWARE                  |
        |                       CREATED BY:TANISH PATEL                       |
        +---------------------------------------------------------------------+
        
        +---------------------------------------------------------------------+
        |                          FEATURES PROVIDED                          |
        +---------------------------------------------------------------------+
        | 1. | Enter a new record                                             |
        +---------------------------------------------------------------------+
        | 2. | Edit a pre-existing record                                     |
        +---------------------------------------------------------------------+
        | 3. | Extract a report of a student                                  |
        +---------------------------------------------------------------------+
        | 4. | Extract a report of a student to CSV file                      |
        +---------------------------------------------------------------------+
        | 5. | Calculate Average/Percentage                                   |
        +---------------------------------------------------------------------+
        | 6. | Show Complete Data                                             |
        +---------------------------------------------------------------------+
        | 7. | Export Full Data to CSV file                                   |
        +---------------------------------------------------------------------+
        | 8. | Data Analysis Tool to analyse marks of a student               |
        +---------------------------------------------------------------------+
        | 9. | Exit                                                           |
        +---------------------------------------------------------------------+
        |Note: Please enter the specified values within the limits within the |
        |      limits else the program won't accept the specified values and  |
        |      would encounter an error and would end the program abruptly    |
        |      causing dataloss                                               |
        +---------------------------------------------------------------------+
                """)
        choicemain = int(input("Please enter a choice: "))
        def prog1():
            if choicemain > 6:
                print("PLEASE ENTER A VALID CHOICE!!!")
                mainloop()
        if choicemain == 1:
            print("""
              1. Enter a new record
              2. Enter a new marks record
              3. Back to main menu
              """)
            choice1 = int(input("Enter your choice: "))   
            if choice1 == 1:
                def studentinfo():
                    mycon = sqltor.connect(host = "localhost", user = "root", passwd = "Tanish@0106", database = "stdbms")
                    FName = str(input("Enter the First Name: "))
                    LName = str(input("Enter the Last Name: "))
                    Student_ID = str(input("Enter the Student ID: "))
                    Class = int(input("Enter the Class: "))
                    Section = str(input("Enter the Section: "))
                    Student_PhoneNo = str(input("Enter the Student's Phone Number: "))
                    Age = int(input("Enter the Age: ")) 
                    DateOfJoining = str(input("Enter the date when student joined the School in (YYYY-MM-DD) form: "))
                    DateOfBirth = str(input("Enter the Date of Birth in (YYYY-MM-DD) form: "))
                    ResidenceCity = str(input("Enter the residence city: "))
                    Gender = str(input("Enter the Gender (M/F): "))
                    cur = mycon.cursor()
                    cur.execute('''
                                INSERT INTO studentinfo(Student_ID, First_Name, Last_Name, Class, Section, Student_PhoneNo, Age, DateOfJoining, DateOfBirth, ResidenceCity, Gender)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);''', (Student_ID, FName, LName, Class, Section, Student_PhoneNo, Age, DateOfJoining, DateOfBirth, ResidenceCity, Gender))
                    mycon.commit()
                    print("DATA INSERTED SUCESSFULLY")
                    engine = pyttsx3.init()
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data Entered Successfully for: {} {}, Student ID: {}". format(FName, LName, Student_ID))
                    engine.runAndWait()
                    stdin1 = str(input("Do you want to enter a new entry (Y/N) ????"))
                    if stdin1 == 'Y':
                        studentinfo()
                    else:
                        mainloop()
                studentinfo()
            elif choice1 == 2:
                print("""
                      1. Enter 1 for Periodic Test 1 Marks
                      2. Enter 2 for Periodic Test 2 Marks
                      3. Enter 3 for Half Yearly Marks
                      4. Enter 4 for Session Ending Marks
                      """)
                testchoice=int(input("Enter the value desired: "))
                if testchoice == 1:
                    def pt1marks():
                        print("Enter 0 For Null Values")
                        Student_ID = str(input("Enter the Student ID: "))
                        PhysicsMarks40 = int(input("Enter The Physics Marks out of 40: "))
                        ChemistryMarks40 = int(input("Enter The Chemistry Marks out of 40: "))
                        MathematicsMarks40 = int(input("Enter The Mathematics Marks out of 40: "))
                        BiologyMarks40 = int(input("Enter The Biology Marks out of 40: "))
                        EnglishMarks40 = int(input("Enter The English Marks out of 40: "))
                        FifthSubjectMarks40 = int(input("Enter The 5th Subject Marks out of 40: "))
                        NoOfSubjectsChosen = int(input("Enter the Number of Subjects Chosen: "))
                        cur = mycon.cursor()
                        cur.execute('''
                                    INSERT INTO pt1marks(Student_ID, Physics_40, Chemistry_40, Mathematics_40, Biology_40, English_40, 5thSubject_40, NoOfSubjectsChosen)
                                    VALUES
                                    (%s, %s, %s, %s, %s, %s, %s, %s)
                                    ''', (Student_ID, PhysicsMarks40, ChemistryMarks40, MathematicsMarks40, BiologyMarks40, EnglishMarks40, FifthSubjectMarks40, NoOfSubjectsChosen))
                        mycon.commit()
                        print("DATA INSERTED SUCESSFULLY")
                        engine = pyttsx3.init()
                        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                        engine.setProperty('voice', en_voice_id)
                        engine.say("Data Entered Successfully for Student ID {}". format(Student_ID))
                        engine.runAndWait()
                        print("---------------Graphical analysis of the student's Marks---------------")
                        Subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', '5th Subject']
                        Marks = [PhysicsMarks40, ChemistryMarks40, MathematicsMarks40, BiologyMarks40, EnglishMarks40, FifthSubjectMarks40]
                        plt.bar(Subjects, Marks)
                        plt.xlabel('Subjects')
                        plt.ylabel('Marks')
                        plt.show()
                        stdin1 = str(input("Do you want to enter a new entry (Y/N) ????"))
                        if stdin1 == 'Y':
                            pt1marks()
                        else:
                            mainloop()
                    pt1marks()
                elif testchoice == 2:
                    def pt2marks():
                        print("Enter 0 For Null Values")
                        Student_ID = str(input("Enter the Student ID: "))
                        PhysicsMarks40 = int(input("Enter The Physics Marks out of 40: "))
                        ChemistryMarks40 = int(input("Enter The Chemistry Marks out of 40: "))
                        MathematicsMarks40 = int(input("Enter The Mathematics Marks out of 40: "))
                        BiologyMarks40 = int(input("Enter The Biology Marks out of 40: "))
                        EnglishMarks40 = int(input("Enter The English Marks out of 40: "))
                        FifthSubjectMarks40 = int(input("Enter The 5th Subject Marks out of 40: "))
                        NoOfSubjectsChosen = int(input("Enter the Number of Subjects Chosen: "))
                        cur = mycon.cursor()
                        cur.execute('''
                                    INSERT INTO pt2marks(Student_ID, Physics_40, Chemistry_40, Mathematics_40, Biology_40, English_40, 5thSubject_40, NoOfSubjectsChosen)
                                    VALUES
                                    (%s, %s, %s, %s, %s, %s, %s, %s)
                                    ''', (Student_ID, PhysicsMarks40, ChemistryMarks40, MathematicsMarks40, BiologyMarks40, EnglishMarks40, FifthSubjectMarks40, NoOfSubjectsChosen))
                        mycon.commit()
                        engine = pyttsx3.init()
                        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                        engine.setProperty('voice', en_voice_id)
                        engine.say("Data Entered Successfully for Student ID {}". format(Student_ID))
                        engine.runAndWait()
                        Subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', '5th Subject']
                        Marks = [PhysicsMarks40, ChemistryMarks40, MathematicsMarks40, BiologyMarks40, EnglishMarks40, FifthSubjectMarks40]
                        plt.bar(Subjects, Marks)
                        plt.xlabel('Subjects')
                        plt.ylabel('Marks')
                        plt.show()
                        stdin2 = str(input("Do you want to enter a new entry (Y/N) ????"))
                        if stdin2 == 'Y':
                            pt2marks()
                    pt2marks()
                    stdin2 = str(input("Do you want to enter a new entry (Y/N) ????"))
                    if stdin2 == 'Y':
                        pt2marks()
                    else:
                        mainloop()
                elif testchoice == 3:
                    def hymarks():
                       print("Enter 0 For Null Values")
                       Student_ID = str(input("Enter the Student ID: "))
                       PhysicsMarks70 = int(input("Enter The Physics (Theory) Marks out of 70: "))
                       PhysicsMarks30 = int(input("Enter The Physics (Practical) Marks out of 30: "))
                       ChemistryMarks70 = int(input("Enter The Chemistry (Theory) Marks out of 70: "))
                       ChemistryMarks30 = int(input("Enter The Chemistry (Practical) Marks out of 30: "))
                       MathematicsMarks80 = int(input("Enter The Mathematics (Theory) Marks out of 80: "))
                       MathematicsMarks20 = int(input("Enter The Mathematics (Practical) Marks out of 20: "))
                       BiologyMarks70 = int(input("Enter The Biology (Theory) Marks out of 70: "))
                       BiologyMarks30 = int(input("Enter The Biology (Practical) Marks out of 30: "))
                       EnglishMarks80 = int(input("Enter The English (Theory) Marks out of 80: "))
                       EnglishMarks20 = int(input("Enter The English (Practical) Marks out of 20: "))
                       FifthSubjectMarks70 = int(input("Enter The 5th Subject (Theory) Marks out of 70: "))
                       FifthSubjectMarks30 = int(input("Enter The 5th Subject (Practical) Marks out of 30: "))
                       NoOfSubjectsChosen = int(input("Enter the Number of Subjects Chosen: "))
                       cur = mycon.cursor()
                       cur.execute('''
                                    INSERT INTO hymarks(Student_ID, Physics_70, Physics_30, Chemistry_70, Chemistry_30, Mathematics_80, Mathematics_20, Biology_70, Biology_30, English_80, English_20, 5thSubject_70, 5thSubject_30, NoOfSubjectsChosen)
                                    VALUES
                                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    ''', (Student_ID, PhysicsMarks70, PhysicsMarks30, ChemistryMarks70, ChemistryMarks30, MathematicsMarks80, MathematicsMarks20, BiologyMarks70, BiologyMarks30, EnglishMarks80, EnglishMarks20, FifthSubjectMarks70, FifthSubjectMarks30, NoOfSubjectsChosen))
                       mycon.commit()
                       engine = pyttsx3.init()
                       en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                       engine.setProperty('voice', en_voice_id)
                       engine.say("Data Entered Successfully for Student ID {}". format(Student_ID))
                       engine.runAndWait()
                       print("DATA INSERTED SUCESSFULLY")
                       Subjects = ['Physics(Theory)', 'Chemistry(Theory)', 'Mathematics(Theory)', 'Biology(Theory)', 'English(Theory)', '5thSubject(Theory)', 'Physics(Practical)', 'Chemistry(Pratical)', 'Mathematics(Practical)', 'Biology(Practical)', 'English(Practical)', '5thSubject(Practical)']
                       Marks = [PhysicsMarks70, PhysicsMarks30, ChemistryMarks70, ChemistryMarks30, MathematicsMarks80, MathematicsMarks20, BiologyMarks70, BiologyMarks30, EnglishMarks80, EnglishMarks20, FifthSubjectMarks70, FifthSubjectMarks30]
                       plt.bar(Subjects, Marks)
                       plt.xlabel('Subjects')
                       plt.ylabel('Marks')
                       plt.show()
                       stdin3 = str(input("Do you want to enter a new entry (Y/N) ????"))
                       if stdin3 == 'Y':
                           hymarks()
                       else:
                           mainloop()
                    hymarks()
                elif testchoice == 4:
                    def fymarks():
                       print("Enter 0 For Null Values")
                       Student_ID = str(input("Enter the Student ID: "))
                       PhysicsMarks70 = int(input("Enter The Physics (Theory) Marks out of 70: "))
                       PhysicsMarks30 = int(input("Enter The Physics (Practical) Marks out of 30: "))
                       ChemistryMarks70 = int(input("Enter The Chemistry (Theory) Marks out of 70: "))
                       ChemistryMarks30 = int(input("Enter The Chemistry (Practical) Marks out of 30: "))
                       MathematicsMarks80 = int(input("Enter The Mathematics (Theory) Marks out of 80: "))
                       MathematicsMarks20 = int(input("Enter The Mathematics (Practical) Marks out of 20: "))
                       BiologyMarks70 = int(input("Enter The Biology (Theory) Marks out of 70: "))
                       BiologyMarks30 = int(input("Enter The Biology (Practical) Marks out of 30: "))
                       EnglishMarks80 = int(input("Enter The English (Theory) Marks out of 80: "))
                       EnglishMarks20 = int(input("Enter The English (Practical) Marks out of 20: "))
                       FifthSubjectMarks70 = int(input("Enter The 5th Subject (Theory) Marks out of 70: "))
                       FifthSubjectMarks30 = int(input("Enter The 5th Subject (Practical) Marks out of 30: "))
                       NoOfSubjectsChosen = int(input("Enter the Number of Subjects Chosen: "))
                       cur = mycon.cursor()
                       cur.execute('''
                                    INSERT INTO fymarks(Student_ID, Physics_70, Physics_30, Chemistry_70, Chemistry_30, Mathematics_80, Mathematics_20, Biology_70, Biology_30, English_80, English_20, 5thSubject_70, 5thSubject_30, NoOfSubjectsChosen)
                                    VALUES
                                    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                    ''', (Student_ID, PhysicsMarks70, PhysicsMarks30, ChemistryMarks70, ChemistryMarks30, MathematicsMarks80, MathematicsMarks20, BiologyMarks70, BiologyMarks30, EnglishMarks80, EnglishMarks20, FifthSubjectMarks70, FifthSubjectMarks30, NoOfSubjectsChosen))
                       mycon.commit()
                       engine = pyttsx3.init()
                       en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                       engine.setProperty('voice', en_voice_id)
                       engine.say("Data Entered Successfully for Student ID {}". format(Student_ID))
                       engine.runAndWait()
                       print("DATA INSERTED SUCESSFULLY")
                       Subjects = ['Physics(Theory)', 'Chemistry(Theory)', 'Mathematics(Theory)', 'Biology(Theory)', 'English(Theory)', '5thSubject(Theory)', 'Physics(Practical)', 'Chemistry(Pratical)', 'Mathematics(Practical)', 'Biology(Practical)', 'English(Practical)', '5thSubject(Practical)']
                       Marks = [PhysicsMarks70, PhysicsMarks30, ChemistryMarks70, ChemistryMarks30, MathematicsMarks80, MathematicsMarks20, BiologyMarks70, BiologyMarks30, EnglishMarks80, EnglishMarks20, FifthSubjectMarks70, FifthSubjectMarks30]
                       plt.bar(Subjects, Marks)
                       plt.xlabel('Subjects')
                       plt.ylabel('Marks')
                       plt.show()
                       stdin3 = str(input("Do you want to enter a new entry (Y/N) ????"))
                       if stdin3 == 'Y':
                           fymarks()
                       else:
                           mainloop()
                    fymarks()
            elif choice1 == 3:
                mainloop()
            elif choice1 > 3:
                print("INVALID CHOICE!!! REDIRECTING TO MAIN MENU !!!")
                mainloop()
        elif choicemain == 2:
            print("""
              1. Edit the basic details of a pre-existing record
              2. Edit the marks of a pre-existing record
              """)
            def editing():
                choice2 = int(input("Enter the value desired: "))
                if choice2 == 1:
                    print("""
                    +----------------------------------+
                    |   Options offered for editing:   |
                    +----------------------------------+
                    | 1. | First Name                  |
                    +----------------------------------+
                    | 2. | Last Name                   |
                    +----------------------------------+
                    | 3. | Class                       |
                    +----------------------------------+
                    | 4. | Section                     |
                    +----------------------------------+
                    | 5. | Student Phone number        |
                    +----------------------------------+
                    | 6. | Age                         |
                    +----------------------------------+
                    | 7. | Date Of Joining             |
                    +----------------------------------+
                    | 8. | Residence city              |
                    +----------------------------------+
                    | 9. | Date Of Birth               |
                    +----------------------------------+
                    """)
                    def edit1():
                        editchoice1 = int(input("enter your choice: "))
                        def func1():
                            if editchoice1 == 1:
                                student1 = str(input("Enter the Student ID of the student: "))
                                edFname = str(input("Enter the New First Name: "))
                                sqlquery = "UPDATE studentinfo SET First_Name = '{}' WHERE (Student_ID = {});". format(edFname, student1)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, First_Name, Last_Name FROM studentinfo;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func1()
                        def func2():
                            if editchoice1 == 2:
                                student2 = str(input("Enter the Student ID of the student: "))
                                edLname = str(input("Enter the New Last Name: "))
                                sqlquery = "UPDATE studentinfo SET Last_Name = '{}' WHERE (Student_ID = {});". format(edLname, student2)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()                                
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry2 = pd.read_sql("SELECT Student_ID, First_Name, Last_Name FROM studentinfo;", mycon)
                                print(qry2)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func2()
                        def func3():
                            if editchoice1 == 3:
                                student3 = str(input("Enter the Student ID of the student: "))
                                edClass = str(input("Enter the New Class: "))
                                sqlquery = "UPDATE studentinfo SET Class = '{}' WHERE (Student_ID = {});". format(edClass, student3)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()                                
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry3 = pd.read_sql("SELECT Student_ID, First_Name, Last_Name, Class, Section FROM studentinfo;", mycon)
                                print(qry3)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func3()
                        def func4():
                            if editchoice1 == 4:
                                student4 = str(input("Enter the Student ID of the student: "))
                                edSection = str(input("Enter the New Section: "))
                                sqlquery = "UPDATE studentinfo SET Section = '{}' WHERE (Student_ID = {});". format(edSection, student4)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry4 = pd.read_sql("SELECT Student_ID, First_Name, Last_Name, Class, Section FROM studentinfo;", mycon)
                                print(qry4)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func4()
                        def func5():
                            if editchoice1 == 5:
                                student5 = str(input("Enter the Student ID of the student: "))
                                edPhone = str(input("Enter the New Student Phone Number: "))
                                sqlquery = "UPDATE studentinfo SET Student_PhoneNo = '{}' WHERE (Student_ID = {});". format(edPhone, student5)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry5 = pd.read_sql("SELECT Student_ID, Student_PhoneNo FROM studentinfo;", mycon)
                                print(qry5)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func5()
                        def func6():
                            if editchoice1 == 6:
                                student6 = str(input("Enter the Student ID of the student: "))
                                edAge = str(input("Enter the New Age: "))
                                sqlquery = "UPDATE studentinfo SET Age = '{}' WHERE (Student_ID = {});". format(edAge, student6)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry6 = pd.read_sql("SELECT Student_ID, Student_PhoneNo FROM studentinfo;", mycon)
                                print(qry6)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func6()
                        def func7():
                            if editchoice1 == 7:
                                student7 = str(input("Enter the Student ID of the student: "))
                                edYears = str(input("Enter the New Date Of Joining in (YYYY-MM-DD) Form: "))
                                sqlquery = "UPDATE studentinfo SET DateOfJoining = '{}' WHERE (Student_ID = {});". format(edYears, student7)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry7 = pd.read_sql("SELECT Student_ID, DateOfJoining FROM studentinfo;", mycon)
                                print(qry7)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func7()
                        def func8():
                            if editchoice1 == 8:
                                student8 = str(input("Enter the Student ID of the student: "))
                                edCity = str(input("Enter the New Residence City: "))
                                sqlquery = "UPDATE studentinfo SET ResidenceCity = '{}' WHERE (Student_ID = {});". format(edCity, student8)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry8 = pd.read_sql("SELECT Student_ID, ResidenceCity FROM studentinfo;", mycon)
                                print(qry8)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func8()
                        def func9():
                            if editchoice1 == 9:
                                student9 = str(input("Enter the Student ID of the student: "))
                                edDOB = str(input("Enter the new DOB in (YYYY-MM-DD) Format: "))
                                sqlquery = "UPDATE studentinfo SET DateOfBirth = '{}' WHERE (Student_ID = {});". format(edDOB, student9)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry9 = pd.read_sql("SELECT Student_ID, First_Name, DateOfBirth FROM studentinfo;", mycon)
                                print(qry9)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                mainloop()
                        func9()
                    edit1()
                elif choice2 > 2:
                    print("Invalid Choice !!!!")
                    editing()
                elif choice2 == 2:
                    print("""
                    +----------------------------------+
                    |   Options offered for editing:   |
                    +----------------------------------+
                    | 1. | Periodic Test 1             |
                    +----------------------------------+
                    | 2. | Periodic Test 2             |
                    +----------------------------------+
                    | 3. | Half Yearly                 |
                    +----------------------------------+
                    | 4. | Session Ending              |
                    +----------------------------------+
                    """)
                    def pt1marksedit():
                        print("""
                    +----------------------------------+
                    |   Options offered for editing:   |
                    +----------------------------------+
                    | 1. | Physics                     |
                    +----------------------------------+
                    | 2. | Chemistry                   |
                    +----------------------------------+
                    | 3. | Mathematics                 |
                    +----------------------------------+
                    | 4. | Biology                     |
                    +----------------------------------+
                    | 5. | English                     |
                    +----------------------------------+
                    | 6. | 5th Subject                 |
                    +----------------------------------+
                    """)
                        def internallooper1():
                            pt1choice = int(input("Enter your choice: "))
                            if pt1choice > 6:
                                print("INVALID CHOICE!!!")
                                print("Enter 0 to exit to main menu!!!")                                
                                internallooper1()
                            elif pt1choice == 1:
                                edstudentid1 = str(input("Enter the Student ID of the student: "))
                                edphypt1 = str(input("Enter the New Physics Marks: "))
                                sqlquery = "UPDATE pt1marks SET Physics_40 = '{}' WHERE (Student_ID = {});". format(edphypt1, edstudentid1)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Physics_40 FROM pt1marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper1()
                            elif pt1choice == 2:
                                edstudentid2 = str(input("Enter the Student ID of the student: "))
                                edchmpt1 = str(input("Enter the New Chemistry Marks: "))
                                sqlquery = "UPDATE pt1marks SET Chemistry_40 = '{}' WHERE (Student_ID = {});". format(edchmpt1, edstudentid2)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Chemistry_40 FROM pt1marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper1()
                            elif pt1choice == 3:
                                edstudentid3 = str(input("Enter the Student ID of the student: "))
                                edmatpt1 = str(input("Enter the New Mathematics Marks: "))
                                sqlquery = "UPDATE pt1marks SET Mathematics_40 = '{}' WHERE (Student_ID = {});". format(edmatpt1, edstudentid3)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Mathematics_40 FROM pt1marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper1()
                            elif pt1choice == 4:
                                edstudentid4 = str(input("Enter the Student ID of the student: "))
                                edbiopt1 = str(input("Enter the New Biology Marks: "))
                                sqlquery = "UPDATE pt1marks SET Biology_40 = '{}' WHERE (Student_ID = {});". format(edbiopt1, edstudentid4)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Biology_40 FROM pt1marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper1()
                            elif pt1choice == 5:
                                edstudentid5 = str(input("Enter the Student ID of the student: "))
                                edengpt1 = str(input("Enter the New English Marks: "))
                                sqlquery = "UPDATE pt1marks SET English_40 = '{}' WHERE (Student_ID = {});". format(edengpt1, edstudentid5)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, English_40 FROM pt1marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper1()
                            elif pt1choice == 6:
                                edstudentid6 = str(input("Enter the Student ID of the student: "))
                                ed5spt1 = str(input("Enter the New 5th Subject Marks: "))
                                sqlquery = "UPDATE pt1marks SET 5thSubject_40 = '{}' WHERE (Student_ID = {});". format(ed5spt1, edstudentid6)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, 5thSubject_40 FROM pt1marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper1()
                            elif pt1choice == 0:
                                mainloop()
                        internallooper1()
                    def pt2marksedit():
                        print("""
                    +----------------------------------+
                    |   Options offered for editing:   |
                    +----------------------------------+
                    | 1. | Physics                     |
                    +----------------------------------+
                    | 2. | Chemistry                   |
                    +----------------------------------+
                    | 3. | Mathematics                 |
                    +----------------------------------+
                    | 4. | Biology                     |
                    +----------------------------------+
                    | 5. | English                     |
                    +----------------------------------+
                    | 6. | 5th Subject                 |
                    +----------------------------------+
                    """)
                        def internallooper2():
                            pt2choice = int(input("Enter your choice: "))
                            if pt2choice > 6:
                                print("INVALID CHOICE!!!")
                                print("Enter 0 to exit to main menu!!!")                                
                                internallooper2()
                            elif pt2choice == 1:
                                edstudentid1 = str(input("Enter the Student ID of the student: "))
                                edphypt2 = str(input("Enter the New Physics Marks: "))
                                sqlquery = "UPDATE pt2marks SET Physics_40 = '{}' WHERE (Student_ID = {});". format(edphypt2, edstudentid1)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Physics_40 FROM pt2marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper2()
                            elif pt2choice == 2:
                                edstudentid2 = str(input("Enter the Student ID of the student: "))
                                edchmpt2 = str(input("Enter the New Chemistry Marks: "))
                                sqlquery = "UPDATE pt2marks SET Chemistry_40 = '{}' WHERE (Student_ID = {});". format(edchmpt2, edstudentid2)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Chemistry_40 FROM pt2marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper2()
                            elif pt2choice == 3:
                                edstudentid3 = str(input("Enter the Student ID of the student: "))
                                edmatpt2 = str(input("Enter the New Mathematics Marks: "))
                                sqlquery = "UPDATE pt2marks SET Mathematics_40 = '{}' WHERE (Student_ID = {});". format(edmatpt2, edstudentid3)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Mathematics_40 FROM pt2marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper2()
                            elif pt2choice == 4:
                                edstudentid4 = str(input("Enter the Student ID of the student: "))
                                edbiopt2 = str(input("Enter the New Biology Marks: "))
                                sqlquery = "UPDATE pt2marks SET Biology_40 = '{}' WHERE (Student_ID = {});". format(edbiopt2, edstudentid4)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, Biology_40 FROM pt2marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper2()
                            elif pt2choice == 5:
                                edstudentid5 = str(input("Enter the Student ID of the student: "))
                                edengpt2 = str(input("Enter the New English Marks: "))
                                sqlquery = "UPDATE pt2marks SET English_40 = '{}' WHERE (Student_ID = {});". format(edengpt2, edstudentid5)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, English_40 FROM pt2marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper2()
                            elif pt2choice == 6:
                                edstudentid6 = str(input("Enter the Student ID of the student: "))
                                ed5spt2 = str(input("Enter the New 5th Subject Marks: "))
                                sqlquery = "UPDATE pt2marks SET 5thSubject_40 = '{}' WHERE (Student_ID = {});". format(ed5spt2, edstudentid6)
                                cur = mycon.cursor()
                                cur.execute(sqlquery)
                                mycon.commit()
                                print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                                qry1 = pd.read_sql("SELECT Student_ID, 5thSubject_40 FROM pt2marks;", mycon)
                                print(qry1)
                                print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                                internallooper2()
                            elif pt2choice == 0:
                                mainloop()
                        internallooper2()
                    def hymarksedit():
                        print("""
                              +----------------------------------+
                              |   Options offered for editing:   |
                              +----------------------------------+
                              | 1.  | Physics (Theory)           |
                              | 2.  | Physics (Practical)        |
                              +----------------------------------+
                              | 3.  | Chemistry (Theory)         |
                              | 4.  | Chemistry (Practical)      |
                              +----------------------------------+
                              | 5.  | Mathematics (Theory)       |
                              | 6.  | Mathematics (Practical)    |
                              +----------------------------------+
                              | 7.  | Biology (Theory)           |
                              | 8.  | Biology (Practical)        |
                              +----------------------------------+
                              | 9.  | English (Theory)           |
                              | 10. | English (Practical)        |
                              +----------------------------------+
                              | 11. | 5th Subject (Theory)       |
                              | 12. | 5th Subject (Practical)    |
                              +----------------------------------+
                              """)
                    def internallooper3():
                        hychoice = int(input("Enter your choice: "))
                        if hychoice > 12:
                            print("INVALID CHOICE!!!")
                            print("Enter 0 to exit to main menu!!!")
                            internallooper3()
                        elif hychoice == 1:
                            edstudentid1 = str(input("Enter the Student ID of the student: "))
                            edphythhy = str(input("Enter the New Physics(Theory) Marks: "))
                            sqlquery1 = "UPDATE hymarks SET Physics_70 = '{}' WHERE (Student_ID = {});". format(edphythhy, edstudentid1)
                            cur = mycon.cursor()
                            cur.execute(sqlquery1)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Physics_70 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 3:
                            edstudentid2 = str(input("Enter the Student ID of the student: "))
                            edchmthhy = str(input("Enter the New Chemistry(Theory) Marks: "))
                            sqlquery2 = "UPDATE hymarks SET Chemistry_70 = '{}' WHERE (Student_ID = {});". format(edchmthhy, edstudentid2)
                            cur = mycon.cursor()
                            cur.execute(sqlquery2)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Chemistry_70 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 5:
                            edstudentid3 = str(input("Enter the Student ID of the student: "))
                            edmatthhy = str(input("Enter the New Mathematics(Theory) Marks: "))
                            sqlquery3 = "UPDATE hymarks SET Mathematics_80 = '{}' WHERE (Student_ID = {});". format(edmatthhy, edstudentid3)
                            cur = mycon.cursor()
                            cur.execute(sqlquery3)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Mathematics_80 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 7:
                            edstudentid4 = str(input("Enter the Student ID of the student: "))
                            edbiothhy = str(input("Enter the New Biology(Theory) Marks: "))
                            sqlquery4 = "UPDATE hymarks SET Biology_70 = '{}' WHERE (Student_ID = {});". format(edbiothhy, edstudentid4)
                            cur = mycon.cursor()
                            cur.execute(sqlquery4)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Biology_70 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 9:
                            edstudentid5 = str(input("Enter the Student ID of the student: "))
                            edengthhy = str(input("Enter the New English(Theory) Marks: "))
                            sqlquery5 = "UPDATE hymarks SET English_80 = '{}' WHERE (Student_ID = {});". format(edengthhy, edstudentid5)
                            cur = mycon.cursor()
                            cur.execute(sqlquery5)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, English_80 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 11:
                            edstudentid6 = str(input("Enter the Student ID of the student: "))
                            ed5sthhy = str(input("Enter the New 5th Subject(Theory) Marks: "))
                            sqlquery6 = "UPDATE hymarks SET 5thSubject_70 = '{}' WHERE (Student_ID = {});". format(ed5sthhy, edstudentid6)
                            cur = mycon.cursor()
                            cur.execute(sqlquery6)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, 5thSubject_70 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 2:
                            edstudentid7 = int(input("Enter the Student ID of the student: "))
                            edphypr = int(input("Enter the new Physics(Practical) Marks: "))
                            sqlquery7 = "UPDATE hymarks SET Physics_30 = '{}' WHERE (Student_ID = {});". format(edphypr, edstudentid7)
                            cur.execute(sqlquery7)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Physics_30 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 4:
                            edstudentid8 = int(input("Enter the Student ID of the student: "))
                            edchmpr = int(input("Enter the new Chemistry(Practical) Marks: "))
                            sqlquery8 = "UPDATE hymarks SET Chemistry_30 = '{}' WHERE (Student_ID = {});". format(edchmpr, edstudentid8)
                            cur.execute(sqlquery8)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Chemistry_30 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()       
                        elif hychoice == 6:
                            edstudentid9 = int(input("Enter the Student ID of the student: "))
                            edmatpr = int(input("Enter the new Mathematics(Practical) Marks: "))
                            sqlquery9 = "UPDATE hymarks SET Mathematics_20 = '{}' WHERE (Student_ID = {});". format(edmatpr, edstudentid9)
                            cur.execute(sqlquery9)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Mathematics_20 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 8:
                            edstudentid10 = int(input("Enter the Student ID of the student: "))
                            edbiopr = int(input("Enter the new Biology(Practical) Marks: "))
                            sqlquery10 = "UPDATE hymarks SET Biology_30 = '{}' WHERE (Student_ID = {});". format(edbiopr, edstudentid10)
                            cur.execute(sqlquery10)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Physics_30 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 10:
                            edstudentid11 = int(input("Enter the Student ID of the student: "))
                            edengpr = int(input("Enter the new English(Practical) Marks: "))
                            sqlquery11 = "UPDATE hymarks SET English_20 = '{}' WHERE (Student_ID = {});". format(edengpr, edstudentid11)
                            cur.execute(sqlquery11)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, English_20 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 12:
                            edstudentid12 = int(input("Enter the Student ID of the student: "))
                            ed5spr = int(input("Enter the new 5th Subject(Practical) Marks: "))
                            sqlquery12 = "UPDATE hymarks SET 5thSubject_30 = '{}' WHERE (Student_ID = {});". format(ed5spr, edstudentid12)
                            cur.execute(sqlquery12)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, 5thSubject_30 FROM hymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper3()
                        elif hychoice == 0:
                            mainloop()
                        internallooper3()
                    def fymarksedit():
                        print("""
                              +----------------------------------+
                              |   Options offered for editing:   |
                              +----------------------------------+
                              | 1.  | Physics (Theory)           |
                              | 2.  | Physics (Practical)        |
                              +----------------------------------+
                              | 3.  | Chemistry (Theory)         |
                              | 4.  | Chemistry (Practical)      |
                              +----------------------------------+
                              | 5.  | Mathematics (Theory)       |
                              | 6.  | Mathematics (Practical)    |
                              +----------------------------------+
                              | 7.  | Biology (Theory)           |
                              | 8.  | Biology (Practical)        |
                              +----------------------------------+
                              | 9.  | English (Theory)           |
                              | 10. | English (Practical)        |
                              +----------------------------------+
                              | 11. | 5th Subject (Theory)       |
                              | 12. | 5th Subject (Practical)    |
                              +----------------------------------+
                              """)
                    def internallooper4():
                        fychoice = int(input("Enter your choice: "))
                        if fychoice > 12:
                            print("INVALID CHOICE!!!")
                            print("Enter 0 to exit to main menu!!!")
                            internallooper4()
                        elif fychoice == 1:
                            edstudentid1 = str(input("Enter the Student ID of the student: "))
                            edphythhy = str(input("Enter the New Physics(Theory) Marks: "))
                            sqlquery1 = "UPDATE fymarks SET Physics_70 = '{}' WHERE (Student_ID = {});". format(edphythhy, edstudentid1)
                            cur = mycon.cursor()
                            cur.execute(sqlquery1)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Physics_70 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 3:
                            edstudentid2 = str(input("Enter the Student ID of the student: "))
                            edchmthhy = str(input("Enter the New Chemistry(Theory) Marks: "))
                            sqlquery2 = "UPDATE fymarks SET Chemistry_70 = '{}' WHERE (Student_ID = {});". format(edchmthhy, edstudentid2)
                            cur = mycon.cursor()
                            cur.execute(sqlquery2)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Chemistry_70 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 5:
                            edstudentid3 = str(input("Enter the Student ID of the student: "))
                            edmatthhy = str(input("Enter the New Mathematics(Theory) Marks: "))
                            sqlquery3 = "UPDATE fymarks SET Mathematics_80 = '{}' WHERE (Student_ID = {});". format(edmatthhy, edstudentid3)
                            cur = mycon.cursor()
                            cur.execute(sqlquery3)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Mathematics_80 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 7:
                            edstudentid4 = str(input("Enter the Student ID of the student: "))
                            edbiothhy = str(input("Enter the New Biology(Theory) Marks: "))
                            sqlquery4 = "UPDATE fymarks SET Biology_70 = '{}' WHERE (Student_ID = {});". format(edbiothhy, edstudentid4)
                            cur = mycon.cursor()
                            cur.execute(sqlquery4)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Biology_70 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 9:
                            edstudentid5 = str(input("Enter the Student ID of the student: "))
                            edengthhy = str(input("Enter the New English(Theory) Marks: "))
                            sqlquery5 = "UPDATE fymarks SET English_80 = '{}' WHERE (Student_ID = {});". format(edengthhy, edstudentid5)
                            cur = mycon.cursor()
                            cur.execute(sqlquery5)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, English_80 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 11:
                            edstudentid6 = str(input("Enter the Student ID of the student: "))
                            ed5sthhy = str(input("Enter the New 5th Subject(Theory) Marks: "))
                            sqlquery6 = "UPDATE fymarks SET 5thSubject_70 = '{}' WHERE (Student_ID = {});". format(ed5sthhy, edstudentid6)
                            cur = mycon.cursor()
                            cur.execute(sqlquery6)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, 5thSubject_70 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 2:
                            edstudentid7 = int(input("Enter the Student ID of the student: "))
                            edphypr = int(input("Enter the new Physics(Practical) Marks: "))
                            sqlquery7 = "UPDATE fymarks SET Physics_30 = '{}' WHERE (Student_ID = {});". format(edphypr, edstudentid7)
                            cur.execute(sqlquery7)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Physics_30 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 4:
                            edstudentid8 = int(input("Enter the Student ID of the student: "))
                            edchmpr = int(input("Enter the new Chemistry(Practical) Marks: "))
                            sqlquery8 = "UPDATE fymarks SET Chemistry_30 = '{}' WHERE (Student_ID = {});". format(edchmpr, edstudentid8)
                            cur.execute(sqlquery8)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Chemistry_30 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()       
                        elif fychoice == 6:
                            edstudentid9 = int(input("Enter the Student ID of the student: "))
                            edmatpr = int(input("Enter the new Mathematics(Practical) Marks: "))
                            sqlquery9 = "UPDATE fymarks SET Mathematics_20 = '{}' WHERE (Student_ID = {});". format(edmatpr, edstudentid9)
                            cur.execute(sqlquery9)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Mathematics_20 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 8:
                            edstudentid10 = int(input("Enter the Student ID of the student: "))
                            edbiopr = int(input("Enter the new Biology(Practical) Marks: "))
                            sqlquery10 = "UPDATE fymarks SET Biology_30 = '{}' WHERE (Student_ID = {});". format(edbiopr, edstudentid10)
                            cur.execute(sqlquery10)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, Physics_30 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 10:
                            edstudentid11 = int(input("Enter the Student ID of the student: "))
                            edengpr = int(input("Enter the new English(Practical) Marks: "))
                            sqlquery11 = "UPDATE fymarks SET English_20 = '{}' WHERE (Student_ID = {});". format(edengpr, edstudentid11)
                            cur.execute(sqlquery11)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, English_20 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 12:
                            edstudentid12 = int(input("Enter the Student ID of the student: "))
                            ed5spr = int(input("Enter the new 5th Subject(Practical) Marks: "))
                            sqlquery12 = "UPDATE fymarks SET 5thSubject_30 = '{}' WHERE (Student_ID = {});". format(ed5spr, edstudentid12)
                            cur.execute(sqlquery12)
                            mycon.commit()
                            print("DATA EDITED SUCCESSFULLY!!!, The Updated Data Stands as --> ")
                            qry1 = pd.read_sql("SELECT Student_ID, 5thSubject_30 FROM fymarks;", mycon)
                            print(qry1)
                            print("CONNECTION EXPIRED!!! GOING BACK TO MAIN MENU!!!")
                            internallooper4()
                        elif fychoice == 0:
                            mainloop()
                        internallooper4()                    
                    def markseditor():
                        edit1 = int(input("Enter your choice: "))
                        if edit1 > 5:
                            print("INVALID CHOICE!!!")
                            markseditor()
                        elif edit1 == 1:
                            pt1marksedit()
                        elif edit1 == 2:
                            pt2marksedit()
                        elif edit1 == 3:
                            hymarksedit()
                        elif edit1 == 4:
                            fymarksedit()
                    markseditor()
            editing()
        elif choicemain == 3:
            def reportstudent():
                print("""
                +----------------------------+
                |   Test Results Available   |
                +----------------------------+
                | 1. | Periodic Test 1       |
                +----------------------------+
                | 2. | Periodic Test 2       |
                +----------------------------+
                | 3. | Half Yearly           |
                +----------------------------+
                | 4. | Session Ending        |
                +----------------------------+
                """)
                repstudchoice = int(input("Enter your choice: "))
                if repstudchoice >4:
                    reportstudent()
                elif repstudchoice == 1:
                    def pt1marks():
                        student = int(input("Enter the Student ID of the student: "))
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, pt1marks.Physics_40, pt1marks.Chemistry_40, pt1marks.Mathematics_40, pt1marks.Biology_40, pt1marks.English_40, pt1marks.5thSubject_40, pt1marks.NoOfSubjectsChosen FROM studentinfo, pt1marks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {}".format(student, student)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        for row in rep:
                            avg = ((row[2]+row[3]+row[4]+row[5]+row[6]+row[7])/row[8])
                            per = (avg/40)*100
                            print()
                            print("Student_ID: ", row[0])
                            print("First_Name: ", row[1])
                            print()
                            print("Periodic Test 1 Results")
                            print()
                            print("+-------------------------+")
                            print("| Physics:         | ", row[2])
                            print("+-------------------------+")
                            print("| Chemistry:       | ", row[3])
                            print("+-------------------------+")
                            print("| Mathematics:     | ", row[4])
                            print("+-------------------------+")
                            print("| Biology:         | ", row[5])
                            print("+-------------------------+")
                            print("| English:         | ", row[6])
                            print("+-------------------------+")
                            print("| 5th Subject:     | ", row[7])
                            print("+-------------------------+")
                            print()
                            print("Average Marks: ", avg)
                            print("Percentage:    ", per)
                            Subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', '5th Subject']
                            Marks = [row[2], row[3], row[4], row[5], row[6], row[7]]
                            plt.bar(Subjects, Marks)
                            plt.xlabel('Subjects')
                            plt.ylabel('Marks')
                            plt.show()
                            print("CONNECTION CLOSED!!!! RETURNING TO MAIN MENU!!!!")
                        mainloop()
                    pt1marks()
                elif repstudchoice == 2:
                    def pt2marks():
                        student = int(input("Enter the Student ID of the student: "))
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, pt2marks.Physics_40, pt2marks.Chemistry_40, pt2marks.Mathematics_40, pt2marks.Biology_40, pt2marks.English_40, pt2marks.5thSubject_40, pt2marks.NoOfSubjectsChosen FROM studentinfo, pt2marks WHERE studentinfo.Student_ID = {} AND pt2marks.Student_ID = {}".format(student, student)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        for row in rep:
                            avg = ((row[2]+row[3]+row[4]+row[5]+row[6]+row[7])/row[8])
                            per = (avg/40)*100
                            print()
                            print("Student_ID: ", row[0])
                            print("First_Name: ", row[1])
                            print()
                            print("Periodic Test 2 Results")
                            print()
                            print("+-------------------------+")
                            print("| Physics:         | ", row[2])
                            print("+-------------------------+")
                            print("| Chemistry:       | ", row[3])
                            print("+-------------------------+")
                            print("| Mathematics:     | ", row[4])
                            print("+-------------------------+")
                            print("| Biology:         | ", row[5])
                            print("+-------------------------+")
                            print("| English:         | ", row[6])
                            print("+-------------------------+")
                            print("| 5th Subject:     | ", row[7])
                            print("+-------------------------+")
                            print()
                            print("Average Marks: ", avg)
                            print("Percentage:    ", per)
                            Subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', '5th Subject']
                            Marks = [row[2], row[3], row[4], row[5], row[6], row[7]]
                            plt.bar(Subjects, Marks)
                            plt.xlabel('Subjects')
                            plt.ylabel('Marks')
                            plt.show()
                        print("CONNECTION CLOSED!!!! RETURNING TO MAIN MENU!!!!")
                        mainloop()
                    pt2marks()
                elif repstudchoice == 3:
                    def hymarks():
                        student = int(input("Enter the Student ID of the student: "))
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, hymarks.Physics_70, hymarks.Physics_30, hymarks.Chemistry_70, hymarks.Chemistry_30, hymarks.Mathematics_80, hymarks.Mathematics_20, hymarks.Biology_70, hymarks.Biology_30, hymarks.English_80, hymarks.English_20, hymarks.5thSubject_70, hymarks.5thSubject_30, hymarks.NoOfSubjectsChosen FROM studentinfo, hymarks WHERE studentinfo.Student_ID = {} AND hymarks.Student_ID = {}".format(student, student)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        for row in rep:
                            phyavg = (row[2]+row[3])
                            chmavg = (row[4]+row[5])
                            matavg = (row[6]+row[7])
                            bioavg = (row[8]+row[9])
                            engavg = (row[10]+row[11])
                            addavg = (row[12]+row[13])
                            subjects = row[14]
                            totmarks = phyavg+chmavg+matavg+bioavg+engavg+addavg
                            ovravg = totmarks/subjects
                            print()
                            print("Student_ID: ", row[0])
                            print("First_Name: ", row[1])
                            print()
                            print("Half Yearly Results")
                            print()
                            print("Physics: ")
                            print("Theory:           |", row[2])
                            print("Practical:        |", row[3])
                            print("Overall:          |", phyavg)
                            print()
                            print("Chemistry: ")
                            print("Theory:           |", row[4])
                            print("Practical:        |", row[5])
                            print("Overall:          |", chmavg)
                            print()
                            print("Mathematics: ")
                            print("Theory:           |", row[6])
                            print("Practical:        |", row[7])
                            print("Overall:          |", matavg)
                            print()
                            print("Biology: ")
                            print("Theory:           |", row[8])
                            print("Practical:        |", row[9])
                            print("Overall:          |", bioavg)
                            print()
                            print("English: ")
                            print("Theory:           |", row[10])
                            print("Practical:        |", row[11])
                            print("Overall:          |", engavg)
                            print()
                            print("5th Subject: ")
                            print("Theory:           |", row[12])
                            print("Practical:        |", row[13])
                            print("Overall:          |", addavg)
                            print()
                            print("Overall Result:")
                            print("Average Marks:    |", ovravg)
                            print("Percentage:       |", ovravg, "%")
                            Subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', '5th Subject']
                            Marks = [phyavg, chmavg, matavg, bioavg, engavg, addavg]
                            plt.bar(Subjects, Marks)
                            plt.xlabel('Subjects')
                            plt.ylabel('Marks')
                            plt.show()
                        print("CONNECTION CLOSED!!!! RETURNING TO MAIN MENU!!!!")
                        mainloop()
                    hymarks()
                elif repstudchoice == 4:
                    def fymarks():
                        student = int(input("Enter the Student ID of the student: "))
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, fymarks.Physics_70, fymarks.Physics_30, fymarks.Chemistry_70, fymarks.Chemistry_30, fymarks.Mathematics_80, fymarks.Mathematics_20, fymarks.Biology_70, fymarks.Biology_30, fymarks.English_80, fymarks.English_20, fymarks.5thSubject_70, fymarks.5thSubject_30, fymarks.NoOfSubjectsChosen FROM studentinfo, fymarks WHERE studentinfo.Student_ID = {} AND fymarks.Student_ID = {}".format(student, student)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        for row in rep:
                            phyavg = (row[2]+row[3])
                            chmavg = (row[4]+row[5])
                            matavg = (row[6]+row[7])
                            bioavg = (row[8]+row[9])
                            engavg = (row[10]+row[11])
                            addavg = (row[12]+row[13])
                            subjects = row[14]
                            totmarks = phyavg+chmavg+matavg+bioavg+engavg+addavg
                            ovravg = totmarks/subjects
                            print()
                            print("Student_ID: ", row[0])
                            print("First_Name: ", row[1])
                            print()
                            print("Session Ending Examination Results")
                            print()
                            print("Physics: ")
                            print("Theory:           |", row[2])
                            print("Practical:        |", row[3])
                            print("Overall:          |", phyavg)
                            print()
                            print("Chemistry: ")
                            print("Theory:           |", row[4])
                            print("Practical:        |", row[5])
                            print("Overall:          |", chmavg)
                            print()
                            print("Mathematics: ")
                            print("Theory:           |", row[6])
                            print("Practical:        |", row[7])
                            print("Overall:          |", matavg)
                            print()
                            print("Biology: ")
                            print("Theory:           |", row[8])
                            print("Practical:        |", row[9])
                            print("Overall:          |", bioavg)
                            print()
                            print("English: ")
                            print("Theory:           |", row[10])
                            print("Practical:        |", row[11])
                            print("Overall:          |", engavg)
                            print()
                            print("5th Subject: ")
                            print("Theory:           |", row[12])
                            print("Practical:        |", row[13])
                            print("Overall:          |", addavg)
                            print()
                            print("Overall Result:")
                            print("Average Marks:    |", ovravg)
                            print("Percentage:       |", ovravg, "%")
                            Subjects = ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', '5th Subject']
                            Marks = [phyavg, chmavg, matavg, bioavg, engavg, addavg]
                            plt.bar(Subjects, Marks)
                            plt.xlabel('Subjects')
                            plt.ylabel('Marks')
                            plt.show()
                        print("CONNECTION CLOSED!!!! RETURNING TO MAIN MENU!!!!")
                        mainloop()
                    fymarks()
            reportstudent()
        elif choicemain == 4:
            def reportclass():
                print("""
                +----------------------------+
                |   Test Results Available   |
                +----------------------------+
                | 1. | Periodic Test 1       |
                +----------------------------+
                | 2. | Periodic Test 2       |
                +----------------------------+
                | 3. | Half Yearly           |
                +----------------------------+
                | 4. | Session Ending        |
                +----------------------------+
                """)
                def internallooper5():
                    chccls = int(input("Enter Your choice: "))
                    if chccls > 4:
                        print("INVALID!!!!")
                        internallooper5()
                    elif chccls == 1:
                        studentid1 = int(input("Enter the Student ID of the student: "))
                        print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, pt1marks.Physics_40, pt1marks.Chemistry_40, pt1marks.Mathematics_40, pt1marks.Biology_40, pt1marks.English_40, pt1marks.5thSubject_40, pt1marks.NoOfSubjectsChosen FROM studentinfo, pt1marks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {}".format(studentid1, studentid1)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        with open("randomname.csv","w") as outfile:
                            writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                            writer.writerow(col[0] for col in cur.description)
                            for row in rep:
                                writer.writerow(row)
                            engine = pyttsx3.init()
                            en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                            engine.setProperty('voice', en_voice_id)
                            engine.say("Data exported successfully to CSV File")
                            engine.runAndWait()    
                        mainloop()                            
                    elif chccls == 2:
                        studentid2 = int(input("Enter the Student ID of the student: "))
                        print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, pt2marks.Physics_40, pt2marks.Chemistry_40, pt2marks.Mathematics_40, pt2marks.Biology_40, pt2marks.English_40, pt2marks.5thSubject_40, pt2marks.NoOfSubjectsChosen FROM studentinfo, pt2marks WHERE studentinfo.Student_ID = {} AND pt2marks.Student_ID = {}".format(studentid2, studentid2)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        with open("randomname.csv","w") as outfile:
                            writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                            writer.writerow(col[0] for col in cur.description)
                            for row in rep:
                                writer.writerow(row)
                            engine = pyttsx3.init()
                            en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                            engine.setProperty('voice', en_voice_id)
                            engine.say("Data exported successfully to CSV File")
                            engine.runAndWait()
                        mainloop()
                    elif chccls == 3:
                        studentid3 = int(input("Enter the Student ID of the student: "))
                        print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED") 
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, hymarks.Physics_70, hymarks.Physics_30, hymarks.Chemistry_70, hymarks.Chemistry_30, hymarks.Mathematics_80, hymarks.Mathematics_20, hymarks.Biology_70, hymarks.Biology_30, hymarks.English_80, hymarks.English_20, hymarks.5thSubject_70, hymarks.5thSubject_30, hymarks.NoOfSubjectsChosen FROM studentinfo, hymarks WHERE studentinfo.Student_ID = {} AND hymarks.Student_ID = {}".format(studentid3, studentid3)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        with open("randomname.csv","w") as outfile:
                            writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                            writer.writerow(col[0] for col in cur.description)
                            for row in rep:
                                writer.writerow(row)
                            engine = pyttsx3.init()
                            en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                            engine.setProperty('voice', en_voice_id)
                            engine.say("Data exported successfully to CSV File")
                            engine.runAndWait()
                        mainloop()                                
                    elif chccls == 4:
                        studentid4 = int(input("Enter the Student ID of the student: "))
                        print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED") 
                        sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, fymarks.Physics_70, fymarks.Physics_30, fymarks.Chemistry_70, fymarks.Chemistry_30, fymarks.Mathematics_80, fymarks.Mathematics_20, fymarks.Biology_70, fymarks.Biology_30, fymarks.English_80, fymarks.English_20, fymarks.5thSubject_70, fymarks.5thSubject_30, fymarks.NoOfSubjectsChosen FROM studentinfo, fymarks WHERE studentinfo.Student_ID = {} AND fymarks.Student_ID = {}".format(studentid4, studentid4)
                        cur = mycon.cursor()
                        cur.execute(sqlquery)
                        rep = cur.fetchmany()
                        with open("randomname.csv","w") as outfile:
                            writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                            writer.writerow(col[0] for col in cur.description)
                            for row in rep:
                                writer.writerow(row)
                            engine = pyttsx3.init()
                            en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                            engine.setProperty('voice', en_voice_id)
                            engine.say("Data exported successfully to CSV File")
                            engine.runAndWait()
                        mainloop()
                internallooper5()
            reportclass()
        elif choicemain == 5:
            def internallooper6():
                print("""
                +----------------------------+
                |   Test Results Available   |
                +----------------------------+
                | 1. | Periodic Test 1       |
                +----------------------------+
                | 2. | Periodic Test 2       |
                +----------------------------+
                | 3. | Half Yearly           |
                +----------------------------+
                | 4. | Session Ending        |
                +----------------------------+
                """)
                chc1 = int(input("Enter Your choice: "))
                if chc1 > 4:
                    print("INVALID!!!")
                    internallooper6()
                elif chc1 == 1:
                    def looper1():
                        print("""
                        +----------------------------------+
                        |   Options offered for average:   |
                        +----------------------------------+
                        | 1. | Physics                     |
                        +----------------------------------+
                        | 2. | Chemistry                   |
                        +----------------------------------+
                        | 3. | Mathematics                 |
                        +----------------------------------+
                        | 4. | Biology                     |
                        +----------------------------------+
                        | 5. | English                     |
                        +----------------------------------+
                        | 6. | 5th Subject                 |
                        +----------------------------------+
                        """)
                        chccls1 = int(input("Enter Your Choice: "))
                        if chccls1 > 6:
                            print("INVALID !!!")
                            print("Enter 0 to exit to main menu!!!")                                
                            looper1()
                        elif chccls1 == 1:
                            cl5 = int(input("Enter The class: "))
                            sc5 = str(input("Enter The section: "))
                            qryavg1 = "SELECT AVG(pt1marks.Physics_40) FROM studentinfo, pt1marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl5, sc5)
                            cur = mycon.cursor()    
                            print("The Average marks of selected subject is: ")                                                        
                            cur.execute(qryavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls1 == 2:
                            cl6 = int(input("Enter The class: "))
                            sc6 = str(input("Enter The section: "))
                            qryavg2 = "SELECT AVG(pt1marks.Chemistry_40) FROM studentinfo, pt1marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl6, sc6)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                                                        
                            cur.execute(qryavg2)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls1 == 3:
                            cl7 = int(input("Enter The class: "))
                            sc7 = str(input("Enter The section: "))
                            qryavg3 = "SELECT AVG(pt1marks.Mathematics_40) FROM studentinfo, pt1marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl7, sc7)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                                                    
                            cur.execute(qryavg3)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls1 == 4:
                            cl8 = int(input("Enter The class: "))
                            sc8 = str(input("Enter The section: "))
                            qryavg4 = "SELECT AVG(pt1marks.Biology_40) FROM studentinfo, pt1marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl8, sc8)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                                                        
                            cur.execute(qryavg4)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls1 == 5:
                            cl9 = int(input("Enter The class: "))
                            sc9 = str(input("Enter The section: "))
                            qryavg5 = "SELECT AVG(pt1marks.English_40) FROM studentinfo, pt1marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl9, sc9)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                                                        
                            cur.execute(qryavg5)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls1 == 6:
                            cl10 = int(input("Enter The class: "))
                            sc10 = str(input("Enter The section: "))
                            qryavg6 = "SELECT AVG(pt1marks.5thSubject_40) FROM studentinfo, pt1marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl10, sc10)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                                                        
                            cur.execute(qryavg6)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls1 == 0:
                            mainloop()
                    looper1()
                    def looper2():
                        print("""
                        +----------------------------------+
                        |   Options offered for average:   |
                        +----------------------------------+
                        | 1. | Physics                     |
                        +----------------------------------+
                        | 2. | Chemistry                   |
                        +----------------------------------+
                        | 3. | Mathematics                 |
                        +----------------------------------+
                        | 4. | Biology                     |
                        +----------------------------------+
                        | 5. | English                     |
                        +----------------------------------+
                        | 6. | 5th Subject                 |
                        +----------------------------------+
                        """)
                        chccls2 = int(input("Enter Your Choice: "))
                        if chccls2 > 6:
                            print("INVALID !!!")
                            print("Enter 0 to exit to main menu!!!")                                
                            looper2()
                        elif chccls2 == 1:
                            cl5 = int(input("Enter The class: "))
                            sc5 = str(input("Enter The section: "))
                            qryavg1 = "SELECT AVG(pt2marks.Physics_40) FROM studentinfo, pt2marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl5, sc5)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls2 == 2:
                            cl6 = int(input("Enter The class: "))
                            sc6 = str(input("Enter The section: "))
                            qryavg2 = "SELECT AVG(pt2marks.Chemistry_40) FROM studentinfo, pt2marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl6, sc6)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryavg2)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls2 == 3:
                            cl7 = int(input("Enter The class: "))
                            sc7 = str(input("Enter The section: "))
                            qryavg3 = "SELECT AVG(pt2marks.Mathematics_40) FROM studentinfo, pt2marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl7, sc7)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryavg3)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls2 == 4:
                            cl8 = int(input("Enter The class: "))
                            sc8 = str(input("Enter The section: "))
                            qryavg4 = "SELECT AVG(pt2marks.Biology_40) FROM studentinfo, pt2marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl8, sc8)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryavg4)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls2 == 5:
                            cl9 = int(input("Enter The class: "))
                            sc9 = str(input("Enter The section: "))
                            qryavg5 = "SELECT AVG(pt2marks.English_40) FROM studentinfo, pt2marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl9, sc9)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryavg5)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls2 == 6:
                            cl10 = int(input("Enter The class: "))
                            sc10 = str(input("Enter The section: "))
                            qryavg6 = "SELECT AVG(pt2marks.5thSubject_40) FROM studentinfo, pt2marks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(cl10, sc10)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryavg6)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls2 == 0:
                            mainloop()
                    looper2()
                    def looper3():
                        print("""
                              +----------------------------------+
                              |   Options offered for average:   |
                              +----------------------------------+
                              | 1.  | Physics (Theory)           |
                              | 2.  | Physics (Practical)        |
                              +----------------------------------+
                              | 3.  | Chemistry (Theory)         |
                              | 4.  | Chemistry (Practical)      |
                              +----------------------------------+
                              | 5.  | Mathematics (Theory)       |
                              | 6.  | Mathematics (Practical)    |
                              +----------------------------------+
                              | 7.  | Biology (Theory)           |
                              | 8.  | Biology (Practical)        |
                              +----------------------------------+
                              | 9.  | English (Theory)           |
                              | 10. | English (Practical)        |
                              +----------------------------------+
                              | 11. | 5th Subject (Theory)       |
                              | 12. | 5th Subject (Practical)    |
                              +----------------------------------+
                              """)
                        chccls3 = int(input("Enter Your Choice: "))
                        if chccls3 > 12:
                            print("INVALID !!!")
                            print("Enter 0 to exit to main menu!!!")                                
                            looper3()
                        elif chccls3 == 0:
                            mainloop()
                        elif chccls3 == 1:
                            hycl1 = int(input("Enter The Class: "))
                            hysc1 = str(input("Enter The Section: "))
                            qryhyavg1 = "SELECT AVG(hymarks.Physics_70) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl1, hysc1)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 2:
                            hycl2 = int(input("Enter The Class: "))
                            hysc2 = str(input("Enter The Section: "))
                            qryhyavg2 = "SELECT AVG(hymarks.Physics_30) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl2, hysc2)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg2)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 3:
                            hycl3 = int(input("Enter The Class: "))
                            hysc3 = str(input("Enter The Section: "))
                            qryhyavg3 = "SELECT AVG(hymarks.Chemistry_70) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl3, hysc3)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg3)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 4:
                            hycl4 = int(input("Enter The Class: "))
                            hysc4 = str(input("Enter The Section: "))
                            qryhyavg4 = "SELECT AVG(hymarks.Chemistry_30) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl4, hysc4)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg4)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 5:
                            hycl5 = int(input("Enter The Class: "))
                            hysc5 = str(input("Enter The Section: "))
                            qryhyavg5 = "SELECT AVG(hymarks.Mathematics_80) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl5, hysc5)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")
                            cur.execute(qryhyavg5)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 6:
                            hycl6 = int(input("Enter The Class: "))
                            hysc6 = str(input("Enter The Section: "))
                            qryhyavg6 = "SELECT AVG(hymarks.Mathematics_20) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl6, hysc6)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg6)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 7:
                            hycl7 = int(input("Enter The Class: "))
                            hysc7 = str(input("Enter The Section: "))
                            qryhyavg7 = "SELECT AVG(hymarks.Biology_70) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl7, hysc7)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg7)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 8:
                            hycl8 = int(input("Enter The Class: "))
                            hysc8 = str(input("Enter The Section: "))
                            qryhyavg8 = "SELECT AVG(hymarks.Biology_30) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl8, hysc8)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg8)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 9:
                            hycl9 = int(input("Enter The Class: "))
                            hysc9 = str(input("Enter The Section: "))
                            qryhyavg9 = "SELECT AVG(hymarks.English_80) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl9, hysc9)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg9)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 10:
                            hycl10 = int(input("Enter The Class: "))
                            hysc10 = str(input("Enter The Section: "))
                            qryhyavg10 = "SELECT AVG(hymarks.English_20) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl10, hysc10)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg10)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 11:
                            hycl11 = int(input("Enter The Class: "))
                            hysc11 = str(input("Enter The Section: "))
                            qryhyavg1 = "SELECT AVG(hymarks.5thSubject_70) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl11, hysc11)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 12:
                            hycl12 = int(input("Enter The Class: "))
                            hysc12 = str(input("Enter The Section: "))
                            qryhyavg1 = "SELECT AVG(hymarks.5thSubject_30) FROM studentinfo, hymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl12, hysc12)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                    looper3()
                    def looper4():
                        print("""
                              +----------------------------------+
                              |   Options offered for average:   |
                              +----------------------------------+
                              | 1.  | Physics (Theory)           |
                              | 2.  | Physics (Practical)        |
                              +----------------------------------+
                              | 3.  | Chemistry (Theory)         |
                              | 4.  | Chemistry (Practical)      |
                              +----------------------------------+
                              | 5.  | Mathematics (Theory)       |
                              | 6.  | Mathematics (Practical)    |
                              +----------------------------------+
                              | 7.  | Biology (Theory)           |
                              | 8.  | Biology (Practical)        |
                              +----------------------------------+
                              | 9.  | English (Theory)           |
                              | 10. | English (Practical)        |
                              +----------------------------------+
                              | 11. | 5th Subject (Theory)       |
                              | 12. | 5th Subject (Practical)    |
                              +----------------------------------+
                              """)
                        chccls3 = int(input("Enter Your Choice: "))
                        if chccls3 > 12:
                            print("INVALID !!!")
                            print("Enter 0 to exit to main menu!!!")                                
                            looper3()
                        elif chccls3 == 0:
                            mainloop()
                        elif chccls3 == 1:
                            hycl1 = int(input("Enter The Class: "))
                            hysc1 = str(input("Enter The Section: "))
                            qryhyavg1 = "SELECT AVG(fymarks.Physics_70) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl1, hysc1)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")
                            cur.execute(qryhyavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 2:
                            hycl2 = int(input("Enter The Class: "))
                            hysc2 = str(input("Enter The Section: "))
                            qryhyavg2 = "SELECT AVG(fymarks.Physics_30) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl2, hysc2)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                          
                            cur.execute(qryhyavg2)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 3:
                            hycl3 = int(input("Enter The Class: "))
                            hysc3 = str(input("Enter The Section: "))
                            qryhyavg3 = "SELECT AVG(fymarks.Chemistry_70) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl3, hysc3)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg3)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 4:
                            hycl4 = int(input("Enter The Class: "))
                            hysc4 = str(input("Enter The Section: "))
                            qryhyavg4 = "SELECT AVG(fymarks.Chemistry_30) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl4, hysc4)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")
                            cur.execute(qryhyavg4)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 5:
                            hycl5 = int(input("Enter The Class: "))
                            hysc5 = str(input("Enter The Section: "))
                            qryhyavg5 = "SELECT AVG(fymarks.Mathematics_80) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl5, hysc5)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg5)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 6:
                            hycl6 = int(input("Enter The Class: "))
                            hysc6 = str(input("Enter The Section: "))
                            qryhyavg6 = "SELECT AVG(fymarks.Mathematics_20) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl6, hysc6)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                        
                            cur.execute(qryhyavg6)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 7:
                            hycl7 = int(input("Enter The Class: "))
                            hysc7 = str(input("Enter The Section: "))
                            qryhyavg7 = "SELECT AVG(fymarks.Biology_70) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl7, hysc7)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg7)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 8:
                            hycl8 = int(input("Enter The Class: "))
                            hysc8 = str(input("Enter The Section: "))
                            qryhyavg8 = "SELECT AVG(fymarks.Biology_30) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl8, hysc8)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg8)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 9:
                            hycl9 = int(input("Enter The Class: "))
                            hysc9 = str(input("Enter The Section: "))
                            qryhyavg9 = "SELECT AVG(fymarks.English_80) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl9, hysc9)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg9)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 10:
                            hycl10 = int(input("Enter The Class: "))
                            hysc10 = str(input("Enter The Section: "))
                            qryhyavg10 = "SELECT AVG(fymarks.English_20) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl10, hysc10)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg10)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 11:
                            hycl11 = int(input("Enter The Class: "))
                            hysc11 = str(input("Enter The Section: "))
                            qryhyavg1 = "SELECT AVG(fymarks.5thSubject_70) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl11, hysc11)
                            cur = mycon.cursor()
                            cur.execute(qryhyavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                        elif chccls3 == 12:
                            hycl12 = int(input("Enter The Class: "))
                            hysc12 = str(input("Enter The Section: "))
                            qryhyavg1 = "SELECT AVG(fymarks.5thSubject_30) FROM studentinfo, fymarks WHERE studentinfo.Class = {} AND studentinfo.section = '{}';". format(hycl12, hysc12)
                            cur = mycon.cursor()
                            print("The Average marks of selected subject is: ")                            
                            cur.execute(qryhyavg1)
                            rep = cur.fetchmany()
                            for row in rep:
                                print(rep)
                    looper4()                
            internallooper6()
        elif choicemain == 6:
            def fulldata():
                print("""
                +----------------------------+
                |     Database Available     |
                +----------------------------+
                | 1. | Student Data          |
                +----------------------------+
                | 2. | Periodic Test 1       |
                +----------------------------+
                | 3. | Periodic Test 2       |
                +----------------------------+
                | 4. | Half Yearly           |
                +----------------------------+
                | 5. | Session Ending        |
                +----------------------------+
                """)
                fdch = int(input("Enter your Choice: "))
                if fdch == 1:
                    qry1desc = pd.read_sql("DESC studentinfo;", mycon)
                    print("THE TABLE STRUCTURE IS: ")
                    print(qry1desc)
                    print()
                    print("THE TABLE IS: ")
                    qry1 = pd.read_sql("SELECT * FROM studentinfo;", mycon)
                    pd.set_option('display.expand_frame_repr', False)
                    print(qry1)
                    mainloop()
                if fdch == 2:
                    qry2desc = pd.read_sql("DESC pt1marks;", mycon)
                    print("THE TABLE STRUCTURE IS: ")
                    print(qry2desc)
                    print()
                    print("THE TABLE IS: ")
                    qry2 = pd.read_sql("SELECT * FROM pt1marks;", mycon)
                    pd.set_option('display.expand_frame_repr', False)
                    print(qry2)
                    mainloop()
                if fdch == 3:
                    qry3desc = pd.read_sql("DESC pt2marks;", mycon)
                    print("THE TABLE STRUCTURE IS: ")
                    print(qry3desc)
                    print()
                    print("THE TABLE IS: ")
                    qry3 = pd.read_sql("SELECT * FROM pt2marks;", mycon)
                    pd.set_option('display.expand_frame_repr', False)
                    print(qry3)
                    mainloop()
                if fdch == 4:
                    qry4desc = pd.read_sql("DESC hymarks;", mycon)
                    print("THE TABLE STRUCTURE IS: ")
                    print(qry4desc)
                    print()
                    print("THE TABLE IS: ")
                    qry4 = pd.read_sql("SELECT * FROM hymarks;", mycon)
                    pd.set_option('display.expand_frame_repr', False)
                    print(qry4)
                    mainloop()
                if fdch == 5:
                    qry5desc = pd.read_sql("DESC fymarks;", mycon)
                    print("THE TABLE STRUCTURE IS: ")
                    print(qry5desc)
                    print()
                    print("THE TABLE IS: ")
                    qry5 = pd.read_sql("SELECT * FROM fymarks;", mycon)
                    pd.set_option('display.expand_frame_repr', False)
                    print(qry5)
                    mainloop()
            fulldata()
        elif choicemain == 7:
            print("""
                              +----------------------------------+
                              |    Options offered for export:   |
                              +----------------------------------+
                              | 0.  | Return                     |
                              +----------------------------------+
                              | 1.  | Student Data               |
                              +----------------------------------+
                              | 2.  | Periodic Test 1            |
                              +----------------------------------+
                              | 3.  | Periodic Test 2            |
                              +----------------------------------+
                              | 4.  | Half Yearly                |
                              +----------------------------------+
                              | 5.  | Session Ending             |
                              +----------------------------------+
                              """)
            choicecsv = int(input("Enter your choice: (Enter 0 to return): "))
            if choicecsv == 0:
                mainloop()
            elif choicecsv == 1:
                sqlquery = "SELECT * FROM studentinfo"
                cur = mycon.cursor()
                cur.execute(sqlquery)
                rep = cur.fetchall()
                print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED") 
                with open("studentinfo.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    engine = pyttsx3.init()
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                mainloop()
            elif choicecsv == 2:
                sqlquery = "SELECT * FROM pt1marks"
                cur = mycon.cursor()
                cur.execute(sqlquery)
                rep = cur.fetchall()
                with open("pt1marks.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                mainloop()
            elif choicecsv == 3:
                sqlquery = "SELECT * FROM pt2marks"
                cur = mycon.cursor()
                cur.execute(sqlquery)
                rep = cur.fetchall()
                with open("pt2marks.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                mainloop()
            elif choicecsv == 4:
                sqlquery = "SELECT * FROM hymarks"
                cur = mycon.cursor()
                cur.execute(sqlquery)
                rep = cur.fetchall()
                with open("hymarks.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                mainloop()
            elif choicecsv == 5:
                sqlquery = "SELECT * FROM fymarks"
                cur = mycon.cursor()
                cur.execute(sqlquery)
                rep = cur.fetchall()
                with open("fymarks.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                mainloop()
        elif choicemain == 8:
            print("""
                        +----------------------------------+
                        |   Options offered for analysis:  |
                        +----------------------------------+
                        | 1. | Physics                     |
                        +----------------------------------+
                        | 2. | Chemistry                   |
                        +----------------------------------+
                        | 3. | Mathematics                 |
                        +----------------------------------+
                        | 4. | Biology                     |
                        +----------------------------------+
                        | 5. | English                     |
                        +----------------------------------+
                        | 6. | 5th Subject                 |
                        +----------------------------------+
                        """)
            choiceanal = int(input("Enter your Choice: (Enter 0 to exit) "))
            if choiceanal == 0:
                mainloop()
            elif choiceanal == 1:
                studentida1 = int(input("Enter the Student ID of the student: "))
                sqlquerya1 = "SELECT studentinfo.Student_ID, studentinfo.First_Name, pt1marks.Physics_40, pt2marks.Physics_40, hymarks.Physics_70, hymarks.Physics_30, fymarks.Physics_70, fymarks.Physics_30 FROM studentinfo, pt1marks, pt2marks, hymarks, fymarks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {} AND pt2marks.Student_ID = {} AND hymarks.Student_ID = {} AND fymarks.Student_ID = {};".format(studentida1, studentida1, studentida1, studentida1, studentida1)
                cur = mycon.cursor()
                cur.execute(sqlquerya1)
                rep = cur.fetchmany()
                for row in rep:
                    sidp = row[0]
                    fnamep = row[1]
                    phypt1 = row[2]*(100/40)
                    phypt2 = row[3]*(100/40)
                    phyhy = (row[4]+row[5])
                    phyfy = (row[6]+row[7])
                    marksphy = [phypt1, phypt2, phyhy, phyfy]
                    testsphy = ['Periodic 1', 'Periodic 2', 'Half Yearly', 'Final'] 
                    plt.bar(testsphy, marksphy)
                    plt.title("Physics Analysis")
                    plt.xlabel('Tests')
                    plt.ylabel('Marks')
                    plt.show()
                mainloop()
            elif choiceanal == 2:
                studentida2 = int(input("Enter the Student ID of the student: "))
                sqlquerya2 = "SELECT studentinfo.Student_ID, studentinfo.First_Name, pt1marks.Chemistry_40, pt2marks.Chemistry_40, hymarks.Chemistry_70, hymarks.Chemistry_30, fymarks.Chemistry_70, fymarks.Chemistry_30 FROM studentinfo, pt1marks, pt2marks, hymarks, fymarks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {} AND pt2marks.Student_ID = {} AND hymarks.Student_ID = {} AND fymarks.Student_ID = {};".format(studentida2, studentida2, studentida2, studentida2, studentida2)
                cur = mycon.cursor()
                cur.execute(sqlquerya2)
                rep = cur.fetchmany()
                for row in rep:
                    sidc = row[0]
                    fnamec = row[1]
                    chmpt1 = row[2]*(100/40)
                    chmpt2 = row[3]*(100/40)
                    chmhy = (row[4]+row[5])
                    chmfy = (row[6]+row[7])
                    markschm = [chmpt1, chmpt2, chmhy, chmfy]
                    testschm = ['Periodic 1', 'Periodic 2', 'Half Yearly', 'Final'] 
                    plt.bar(testschm, markschm)
                    plt.title("Chemistry Analysis")
                    plt.xlabel('Tests')
                    plt.ylabel('Marks')
                    plt.show()
                mainloop()
            elif choiceanal == 3:
                studentida3 = int(input("Enter the Student ID of the student: "))
                sqlquerya3 = "SELECT studentinfo.Student_ID, studentinfo.First_Name, pt1marks.Mathematics_40, pt2marks.Mathematics_40, hymarks.Mathematics_80, hymarks.Mathematics_20, fymarks.Mathematics_80, fymarks.Mathematics_20 FROM studentinfo, pt1marks, pt2marks, hymarks, fymarks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {} AND pt2marks.Student_ID = {} AND hymarks.Student_ID = {} AND fymarks.Student_ID = {};".format(studentida3, studentida3, studentida3, studentida3, studentida3)
                cur = mycon.cursor()
                cur.execute(sqlquerya3)
                rep = cur.fetchmany()
                for row in rep:
                    sidm = row[0]
                    fnamem = row[1]
                    matpt1 = row[2]*(100/40)
                    matpt2 = row[3]*(100/40)
                    mathy = (row[4]+row[5])
                    matfy = (row[6]+row[7])
                    marksmat = [matpt1, matpt2, mathy, matfy]
                    testsmat = ['Periodic 1', 'Periodic 2', 'Half Yearly', 'Final'] 
                    plt.bar(testsmat, marksmat)
                    plt.title("Mathematics Analysis")
                    plt.xlabel('Tests')
                    plt.ylabel('Marks')
                    plt.show()
                mainloop()
            elif choiceanal == 4:
                studentida4 = int(input("Enter the Student ID of the student: "))
                sqlquerya4 = "SELECT studentinfo.Student_ID, studentinfo.First_Name, pt1marks.Biology_40, pt2marks.Biology_40, hymarks.Biology_70, hymarks.Biology_30, fymarks.Biology_70, fymarks.Biology_30 FROM studentinfo, pt1marks, pt2marks, hymarks, fymarks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {} AND pt2marks.Student_ID = {} AND hymarks.Student_ID = {} AND fymarks.Student_ID = {};".format(studentida4, studentida4, studentida4, studentida4, studentida4)
                cur = mycon.cursor()
                cur.execute(sqlquerya4)
                rep = cur.fetchmany()
                for row in rep:
                    sidb = row[0]
                    fnameb = row[1]
                    biopt1 = row[2]*(100/40)
                    biopt2 = row[3]*(100/40)
                    biohy = (row[4]+row[5])
                    biofy = (row[6]+row[7])
                    marksbio = [biopt1, biopt2, biohy, biofy]
                    testsbio = ['Periodic 1', 'Periodic 2', 'Half Yearly', 'Final'] 
                    plt.bar(testsbio, marksbio)
                    plt.title("Biology Analysis")
                    plt.xlabel('Tests')
                    plt.ylabel('Marks')
                    plt.show()
                mainloop()
            elif choiceanal == 5:
                studentida5 = int(input("Enter the Student ID of the student: "))
                sqlquerya5 = "SELECT studentinfo.Student_ID, studentinfo.First_Name, pt1marks.English_40, pt2marks.English_40, hymarks.English_80, hymarks.English_20, fymarks.English_80, fymarks.English_20 FROM studentinfo, pt1marks, pt2marks, hymarks, fymarks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {} AND pt2marks.Student_ID = {} AND hymarks.Student_ID = {} AND fymarks.Student_ID = {};".format(studentida5, studentida5, studentida5, studentida5, studentida5)
                cur = mycon.cursor()
                cur.execute(sqlquerya5)
                rep = cur.fetchmany()
                for row in rep:
                    side = row[0]
                    fnamee = row[1]
                    engpt1 = row[2]*(100/40)
                    engpt2 = row[3]*(100/40)
                    enghy = (row[4]+row[5])
                    engfy = (row[6]+row[7])
                    markseng = [engpt1, engpt2, enghy, engfy]
                    testseng = ['Periodic 1', 'Periodic 2', 'Half Yearly', 'Final'] 
                    plt.bar(testseng, markseng)
                    plt.title("English Analysis")
                    plt.xlabel('Tests')
                    plt.ylabel('Marks')
                    plt.show()
                mainloop()
            elif choiceanal == 6:
                studentida6 = int(input("Enter the Student ID of the student: "))
                sqlquerya6 = "SELECT studentinfo.Student_ID, studentinfo.First_Name, pt1marks.5thSubject_40, pt2marks.5thSubject_40, hymarks.5thSubject_70, hymarks.5thSubject_30, fymarks.5thSubject_70, fymarks.5thSubject_30 FROM studentinfo, pt1marks, pt2marks, hymarks, fymarks WHERE studentinfo.Student_ID = {} AND pt1marks.Student_ID = {} AND pt2marks.Student_ID = {} AND hymarks.Student_ID = {} AND fymarks.Student_ID = {};".format(studentida6, studentida6, studentida6, studentida6, studentida6)
                cur = mycon.cursor()
                cur.execute(sqlquerya6)
                rep = cur.fetchmany()
                for row in rep:
                    sid5 = row[0]
                    fname5 = row[1]
                    fifpt1 = row[2]*(100/40)
                    fifpt2 = row[3]*(100/40)
                    fifhy = (row[4]+row[5])
                    fiffy = (row[6]+row[7])
                    marksfif = [fifpt1, fifpt2, fifhy, fiffy]
                    testsfif = ['Periodic 1', 'Periodic 2', 'Half Yearly', 'Final'] 
                    plt.bar(testsfif, marksfif)
                    plt.title("5th Subject Analysis")
                    plt.xlabel('Tests')
                    plt.ylabel('Marks')
                    plt.show()
                mainloop()
        elif choicemain == 9:
            print("""
              +----------------------------------------------------------------+
              |                 THANK YOU FOR USING OUR SYSTEM                 |
              +----------------------------------------------------------------+
              """)
            engine = pyttsx3.init()
            en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            engine.setProperty('voice', en_voice_id)
            engine.say("GOODBYE!!!")
            engine.runAndWait()
            sys.exit()
        else:
            print("INVALID CODE")
            prog1()
mainloop()