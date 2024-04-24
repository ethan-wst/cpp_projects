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

def getClassArray(year, term):
    try:
        sql = "SELECT class_num, class_name, grade FROM classes WHERE year=%s AND term=%s ORDER BY class_num"
        val = (year, term)
        input = sql, val
        mycursor.execute(sql, val)
        result = mycursor.fetchall()
        return result
    except:
        print("Failed to collect array of classes")