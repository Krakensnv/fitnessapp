#!/usr/bin/python
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

cnx = mysql.connector.connect(user="user", password="pass", host="server", port=3306,
                              database="database", ssl_ca="cert.pem", ssl_disabled=False)

cursor = cnx.cursor()

# Executing SQL Statements
cursor.execute("CREATE TABLE test3 (calc_id INT, calc_weight INT NOT NULL, calc_height INT NOT NULL, calc_gender INT "
               "NOT NULL, calc_age INT NOT NULL, calc_bmi FLOAT NOT NULL, calc_recommend VARCHAR(20), "
               "created_on DATETIME, client_id INT NOT NULL, PRIMARY KEY(`calc_id`), FOREIGN KEY (`client_id`))")

"""    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ca_weight = db.Column(db.Float, unique=True, nullable=False)
    ca_height = db.Column(db.Integer, unique=True, nullable=False)
    ca_gender = db.Column(db.Integer, unique=True, nullable=False)
    ca_age = db.Column(db.Integer, unique=True, nullable=False)
    ca_bmi = db.Column(db.Float, unique=True, nullable=False)
    ca_recommend = db.Column(db.String, unique=True, nullable=False)
    created_on = db.Column(db.DateTime, nullable=True)"""
# cursor.execute(''' INSERT INTO table_name VALUES(v1,v2...) ''')
# cursor.execute(''' DELETE FROM table_name WHERE condition ''')

# Saving the Actions performed on the DB
cnx.commit()

# Closing the cursor
print(cnx)
cursor.close()