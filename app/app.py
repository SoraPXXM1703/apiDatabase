from re import escape
from flask import Flask, jsonify, render_template, request
import mysql.connector
import os
from flask import Flask
from flask import Flask, jsonify
import mysql.connector
from collections import OrderedDict, defaultdict

app = Flask(__name__)

# เชื่อมต่อฐานข้อมูล MySQL โดยใช้ค่าคงที่
mydb = mysql.connector.connect(
  host="db",
  user="root",
  password="12345",
  database="sora_data",
)

mycursor = mydb.cursor()


@app.route('/data')
def get_company_names():
    mycursor.execute("SELECT DISTINCT company_name FROM companies LIMIT 5")
    results = mycursor.fetchall()
    company_names = [row[0] for row in results] 
    return jsonify(company_names)


#test 
@app.route('/hello')
def name():
    return "YORNNAME....>>"


@app.route('/')
def hello():
    return f"WELLOME > "


@app.route('/index')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    # Flask จะรันที่ 0.0.0.0 และพอร์ต 5000
    app.run(host='0.0.0.0', port=5000 ,debug=True)

