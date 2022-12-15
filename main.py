from fastapi import FastAPI
import datetime
import mysql.connector

app = FastAPI()


query = ("SELECT * FROM user")
#
# insert = ("INSERT user(username, password, phone, email) VALUES('test21', 'Test123', '9778388383', 'tes@gmail.com')")
#
update = ("UPDATE `user` SET `password` = 'Test123', `phone` = '9128388383', `email` = 'tes@gmail.com' WHERE `username` ='saravananc'")



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/update/")
def read_update():
    cnx = mysql.connector.connect(user='root', password='root', database='testdb')
    cursor = cnx.cursor()    
    # cursor.execute(insert)
    cursor.execute(update)
    cnx.commit()
    
    cursor.execute(query)
    
    myresult = cursor.fetchall()
    
    for x in myresult:
        print(x)
    
    cursor.close()
    cnx.close()    
    return {"Hello": "Updated"}




