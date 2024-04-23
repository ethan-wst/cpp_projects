import mysql.connector
import os

try: 
    print("Connecting to MySQL Server")
    gradeData = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "RitaRose",
        database="grades"
    )
    print("Server connection established!")
except: 
    print ("Failed to connect to server. \nAttempting to start MySQL server.")
    try: 
        os.system("sudo systemctl start mysql")
    except:
        print ("Failed to start server")

    gradeData = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "RitaRose",
        database="grades"
    )
    print("Server connection established!")

mycursor = gradeData.cursor()
def addClass(class_num, class_name, year, term):
    try:
        sql = "INSERT INTO classes (class_num, class_name, year, term) VALUES (%s, %s, %s, %s)"
        val = (class_num, class_name, year, term)
        mycursor.execute(sql, val)
        gradeData.commit()  
        print(mycursor.rowcount, "record inserted.")
    except:
        print("Insertion Failed. Insure the class number is unique.")

##addClass(3368, 'Data Structures and Algorithms', 2024, 'Spring')