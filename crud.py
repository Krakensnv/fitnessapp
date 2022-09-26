#!/usr/bin/python
import mysql.connector

cnx = mysql.connector.connect(user="user", password="pass", host="host", port=3306,
                              database="database", ssl_ca="cert", ssl_disabled=False)


cursor = cnx.cursor()

"""cursor.execute("CREATE TABLE users (id INT, email VARCHAR(50) NOT NULL UNIQUE, "
               "hashed_password	BLOB NOT NULL, authenticated BOOLEAN, registered_on	DATETIME, role VARCHAR(50), "
               "PRIMARY KEY(`id`))")"""
# cursor.execute("DROP TABLE users")

"""cursor.execute("INSERT INTO `users` VALUES (1,'admin@admin',"
               "'$2b$15$tkugR2xyCofzCjcNzfoW2.2p63zXmxOy0BLxVPn9IRTF0D2GzPmau',1,'2022-03-07 20:33:20.763559','user')")
cursor.execute("INSERT INTO `users` VALUES (2,'user1@user',"
               "'$2b$15$80/aGfymjMdQI.4oWEWDJOcQ.kh07Vm9dyTMPu0VGLLNwzbBsH8.S',0,'2022-03-08 00:52:52.872602','user')")
cursor.execute("INSERT INTO `users` VALUES (3,'kk@admin',"
               "'$2b$15$TYWvZ/8lZeSF2Npv0sbLZOn/eNdv.OchYzySNsTrtt9Ymrz2XC3UK',0,'2022-03-08 13:01:22.802225','user')")
cursor.execute("INSERT INTO `users` VALUES (4,'pedro@gmail.com',"
               "'$2b$15$8BucOrRRWg9quse6Q2pkSedfIUl93tW4vln1cBhi0NY/2KiJuEhzC',1,'2022-09-23 07:29:40.043051','user')")
cnx.commit()"""

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()

# print(cnx)
cnx.close()
