#insert update delete
#select
import mysql.connector

# insert_query = "INSERT INTO students (roll, name) VALUES (6, 'Hima');"
# update_query = "UPDATE students SET name = 'Neha Sharma' WHERE roll = 6;"
# delete_query = "DELETE FROM students WHERE roll = 6;"
#
#
# try:
#     con = mysql.connector.connect(host='localhost',port=3307,user='root',passwd='PASSWORD',database='school')
#     cur = con.cursor()
#     cur.execute(insert_query)
#     con.commit()
#     con.close()
#     print("finished......")
# except:
#     print("Connection Unsuccesful")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
select_query = "Select * from students"

try:
    con = mysql.connector.connect(host='localhost',port=3306,user='root',passwd='PASSWORD',database='school')
    cur = con.cursor()
    cur.execute(select_query)
    for row in cur:
        print(row[0],row[1])
except:
    print("Connection Unsuccesful")

