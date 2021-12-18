import mysql.connector as sqltor
import matplotlib.pyplot as plt
import sys
import pyttsx3
import csv

mycon = sqltor.connect(host = "localhost", user = "root", passwd = "Tanish@0106", database = "stdbms", auth_plugin='mysql_native_password')

def result():
    print("""
    +-------------------------------------------------------------------------+
    |                         RESULT ACCESSING PORTAL                         |
    +-------------------------------------------------------------------------+
    """)
    chc1 = int(input("Enter 1 to enter the portal, 2 to exit the portal: "))
    if chc1 == 1:
        std_id = int(input("Enter Your Student ID: "))
        std_dob = str(input("Enter Your DOB (YYYY-MM-DD) Form: ")) 
        print("""
          WHAT RESULT YOU WANT TO ACCESS??
          +-----------------------------+
          |       Tests Available       |
          +-----------------------------+
          | 1. | Periodic Test 1        |
          +-----------------------------+
          | 2. | Periodic Test 2        |
          +-----------------------------+
          | 3. | Half Yearly            |
          +-----------------------------+
          | 4. | Session Ending         |
          +-----------------------------+
          | 5. | Exit                   |
          +-----------------------------+
        """)
        std_choice = int(input("Enter Your Choice: "))
        if std_choice == 1:
            sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, pt1marks.Physics_40, pt1marks.Chemistry_40, pt1marks.Mathematics_40, pt1marks.Biology_40, pt1marks.English_40, pt1marks.5thSubject_40, pt1marks.NoOfSubjectsChosen FROM studentinfo, pt1marks WHERE studentinfo.Student_ID = {} AND studentinfo.DateOFBirth = '{}' AND pt1marks.Student_ID = {}".format(std_id, std_dob, std_id)
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
                print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine.runAndWait()
                with open("pt1marks_student.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    engine = pyttsx3.init()
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("Showing result for '{}' student id {} ". format(row[1], row[0]))
                engine.say("CONNECTION EXPIRED, RETURNING TO MAIN MENU!!!")
                engine.runAndWait()
                for i in [0,10]:
                    result()
        elif std_choice == 2:
            sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, pt2marks.Physics_40, pt2marks.Chemistry_40, pt2marks.Mathematics_40, pt2marks.Biology_40, pt2marks.English_40, pt2marks.5thSubject_40, pt2marks.NoOfSubjectsChosen FROM studentinfo, pt2marks WHERE studentinfo.Student_ID = {} AND studentinfo.DateOFBirth = '{}' AND pt2marks.Student_ID = {}".format(std_id, std_dob, std_id)
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
                print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED") 
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine.runAndWait()
                with open("pt2marks_student.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    engine = pyttsx3.init()
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("Showing result for '{}' student id {} ". format(row[1], row[0]))
                engine.say("CONNECTION EXPIRED, RETURNING TO MAIN MENU!!!")
                engine.runAndWait()
                for i in [0,10]:
                    result()
        elif std_choice == 3:
            sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, hymarks.Physics_70, hymarks.Physics_30, hymarks.Chemistry_70, hymarks.Chemistry_30, hymarks.Mathematics_80, hymarks.Mathematics_20, hymarks.Biology_70, hymarks.Biology_30, hymarks.English_80, hymarks.English_20, hymarks.5thSubject_70, hymarks.5thSubject_30, hymarks.NoOfSubjectsChosen FROM studentinfo, hymarks WHERE studentinfo.Student_ID = '{}' AND studentinfo.DateOFBirth = {} AND hymarks.Student_ID = {}".format(std_id, std_dob, std_id)
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
                print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine.runAndWait()
                with open("hymarks_student.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    engine = pyttsx3.init()
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("Showing result for '{}' student id {} ". format(row[1], row[0]))
                engine.say("CONNECTION EXPIRED, RETURNING TO MAIN MENU!!!")
                engine.runAndWait()
                for i in [0,10]:
                    result()
        elif std_choice == 4:
            sqlquery = "SELECT studentinfo.Student_ID, studentinfo.First_name, fymarks.Physics_70, fymarks.Physics_30, fymarks.Chemistry_70, fymarks.Chemistry_30, fymarks.Mathematics_80, fymarks.Mathematics_20, fymarks.Biology_70, fymarks.Biology_30, fymarks.English_80, fymarks.English_20, fymarks.5thSubject_70, fymarks.5thSubject_30, fymarks.NoOfSubjectsChosen FROM studentinfo, fymarks WHERE studentinfo.Student_ID = '{}' AND studentinfo.DateOFBirth = {} AND fymarks.Student_ID = {}".format(std_id, std_dob, std_id)
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
                print("Session Ending Results")
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
                print("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("PLEASE MAKE SURE TO CHANGE THE NAME OF THE FILE AFTER IT IS EXECUTED")
                engine.runAndWait()
                with open("fymarks_student.csv","w") as outfile:
                    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(col[0] for col in cur.description)
                    for row in rep:
                        writer.writerow(row)
                    engine = pyttsx3.init()
                    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                    engine.setProperty('voice', en_voice_id)
                    engine.say("Data exported successfully to CSV File")
                    engine.runAndWait()
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("Showing result for '{}' student id {} ". format(row[1], row[0]))
                engine.say("CONNECTION EXPIRED, RETURNING TO MAIN MENU!!!")
                engine.runAndWait()
                for i in [0,10]:
                    result()
        elif std_choice > 5:
            print("INVALID CHOICE!!! PLEASE RE-ENTER THE CORRECT CHOICE!!!, Enter 5 for Logging out and exiting the portal")
            for i in [0,10]:
                result()
        elif std_choice == 5:
            print("Successfully logged out of the portal!!!")
            print("Exiting the portal")
            engine = pyttsx3.init()
            en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
            engine.setProperty('voice', en_voice_id)
            engine.say("Successfully logged out of the portal")
            engine.runAndWait()
            sys.exit()
    elif chc1 == 2:
        print("Successfully logged out of the portal!!!")
        print("Exiting the portal")
        engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', en_voice_id)
        engine.say("GOODBYE!!!")
        engine.runAndWait()
        sys.exit()
    else:
        print("INVALID CHOICE!!!")
        result()
result()
