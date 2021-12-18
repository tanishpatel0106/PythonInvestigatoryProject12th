import mysql.connector as sqltor
import sys
import pyttsx3
mycon = sqltor.connect(host = "localhost", user = "root", passwd = 'Tanish@0106', database = "stdbms")

def funclooper1():
    print("""
    +-------------------------------------------------------------------+
    |         Welcome to the student database management system         |
    +-------------------------------------------------------------------+
    |   Enter 1 to enter the student database                           |
    |   Enter 2 to enter the teacher database                           |
    |   Enter 3 to exit the app                                         |
    +-------------------------------------------------------------------+
    """)
    a = int(input("Enter Your Choice: "))
    if a == 1:
        print("CONNECTION SUCCESSFUL!!! REDIRECTING TO STUDENT DATABASE!!!")
        engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', en_voice_id)
        engine.say("CONNECTION SUCCESSFUL!!! REDIRECTING TO STUDENT DATABASE!!!")
        engine.runAndWait()
        import student
        student.result()
    elif a == 2:
        def internallooper1():
            password = str(input("Enter the password to enter: "))
            if password == "password":
                print("CONNECTION SUCCESSFUL!!! REDIRECTING TO TEACHER DATABASE!!!")
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("CONNECTION SUCCESSFUL!!! REDIRECTING TO TEACHER DATABASE!!!")
                engine.runAndWait()
                import teacher
                teacher.mainloop()
            elif password == 1:
                funclooper1()
            else:
                print("INCORRECT PASSWORD!!! PLEASE RE-ENTER YOUR PASSWORD OR ENTER 1 TO EXIT!!!")
                engine = pyttsx3.init()
                en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                engine.setProperty('voice', en_voice_id)
                engine.say("INCORRECT PASSWORD!!! PLEASE RE-ENTER YOUR PASSWORD OR ENTER 1 TO EXIT!!!")
                engine.runAndWait()
                internallooper1()
        internallooper1()
    elif a == 3:
        print("GOODBYE!!!")
        engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', en_voice_id)
        engine.say("GOODBYE")
        engine.runAndWait()
        sys.exit()
    else:
        print("INVALID VALUE!!!")
        engine = pyttsx3.init()
        en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
        engine.setProperty('voice', en_voice_id)
        engine.say("INVALID VALUE!!!")
        engine.runAndWait()
        funclooper1()
funclooper1()