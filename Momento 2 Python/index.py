from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="medicalcare"
)
app = Flask(__name__)

""" Create and Read """

@app.route('/')
def index():
  sql = "SELECT * FROM register"
  cur = mydb.cursor()
  cur.execute(sql) 
  result = cur.fetchall()
  return render_template('/home.html', medi = result)

@app.route('/createtask')
def createtask():
    return render_template('create-task.html')

""" app route BD """

@app.route('/addmed', methods=['POST'])
def addmed():
    if request.method == 'POST':
        Nombre = request.form['name']
        Apellido = request.form['surname']
        Cedula = request.form['cc']
        Fecha = request.form['date']
        Ciudad = request.form['city']
        Barrio = request.form['residence']
        Celular = request.form['phone']
        cur = mydb.cursor()
        sql = f"INSERT INTO register (Nombre,Apellido,Cedula,Fecha,Ciudad,Barrio,Celular) VALUES ('{Nombre}','{Apellido}',{Cedula},{Fecha},'{Ciudad}','{Barrio}',{Celular})"
        cur.execute(sql)
        mydb.commit()
        # return redirect (url_for['index'])
        return render_template('/home.html')


if __name__ == "__main__":
    app.run(debug=True)