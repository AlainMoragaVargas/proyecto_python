#NOMBRE: ALAIN MORAGA VARGAS

import requests
import json
from flask import Flask, render_template, jsonify, request, url_for, redirect
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors
from datetime import date

app = Flask(__name__)

app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_DB"]  = "vacunatorio"
app.config["MYSQL_DATABASE_PASSWORD"]  = "1234"

mysql = MySQL(app) 

mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor 

@app.route('/listado_pacientes')
def listado_pacientes():
    cursor = mysql.get_db().cursor()
    sql= "SELECT *FROM paciente"
    cursor.execute(sql)
    pacientes = cursor.fetchall()
    return render_template("vacunatorio.html",pacientes=pacientes)


@app.route('/listado_pacientes/nuevo_paciente',  methods=["GET","POST"])
def nuevo_paciente():
    cursor = mysql.get_db().cursor()
    
    if request.method == "POST":
        nombre_paciente= request.form["nombrePaciente"]
        rut_paciente= request.form["rutPaciente"]
        fecha_nacimiento= request.form["fechaNacimiento"]
    
        sql="INSERT INTO paciente (nombre_paciente, rut_paciente, fecha_nacimiento) VALUES (%s,%s,%s)"
        cursor.execute(sql,(nombre_paciente.upper(),rut_paciente,fecha_nacimiento))
        return render_template('registrar_paciente.html')
    else:
        return render_template('registrar_paciente.html')

@app.route('/listado_pacientes/listado_vacunas')
def listado_vacunas():
    cursor = mysql.get_db().cursor()
    sql= "SELECT *FROM vacuna"
    cursor.execute(sql)
    vacunas = cursor.fetchall()
    return render_template("listado_vacunas.html",vacunas=vacunas)


@app.route('/listado_vacunas/nueva_vacuna',methods=["GET","POST"])
def nueva_vacuna():
    cursor = mysql.get_db().cursor()
    fecha_registro= date.today()

    if request.method == "POST":
        nombre_enfermedad= request.form["nombreEnfermedad"]
        sql="INSERT INTO vacuna (nombre_enfermedad,fecha_registro) VALUES (%s,%s)"
        cursor.execute(sql,(nombre_enfermedad.upper(),fecha_registro))
        return render_template('registrar_vacuna.html')
    else:
        return render_template('registrar_vacuna.html')

    
@app.route('/listado_pacientes/vacunar_paciente/<int:id_paciente>',methods=["GET","POST"])
def vacunar_paciente(id_paciente):
    cursor = mysql.get_db().cursor()

    if request.method == "POST":
        id_paciente= request.form["idPaciente"]
        id_vacuna= request.form["vacunaPaciente"]
        fecha_registro= date.today()
        sql="INSERT INTO recibe (fecha_vacuna, id_paciente, id_vacuna) VALUES (%s,%s,%s) "
        cursor.execute(sql,(fecha_registro,id_paciente,id_vacuna))
        return redirect(url_for('listado_pacientes'))

    else:
        sql="SELECT *FROM paciente WHERE id_paciente= %s "
        cursor.execute(sql,(id_paciente))
        paciente = cursor.fetchall()

        sql2="SELECT *FROM vacuna"
        cursor.execute(sql2)
        vacuna= cursor.fetchall()
        return render_template('vacunar_paciente.html',paciente=paciente,vacuna=vacuna)

@app.route('/listado_pacientes/vacunas_paciente/<int:id_paciente>')
def vacunas_paciente(id_paciente):
    cursor = mysql.get_db().cursor()
    sql="SELECT nombre_paciente, nombre_enfermedad, fecha_vacuna"
    sql+=" FROM paciente P, recibe R, vacuna V"
    sql+=" WHERE P.id_paciente=R.id_paciente AND R.id_vacuna=V.id_vacuna AND R.id_paciente=%s "
    cursor.execute(sql,(id_paciente))
    vacunas_paciente = cursor.fetchall()

    if vacunas_paciente:
        mensaje=""
    else:
        mensaje="NO EXISTEN VACUNAS PARA ESTE PACIENTE."
    
    sql2="SELECT nombre_paciente FROM paciente WHERE id_paciente=%s"
    cursor.execute(sql2,(id_paciente))
    nombre_p = cursor.fetchall()
    for iterador in nombre_p:
        nombre_paciente=iterador['nombre_paciente']

    return render_template('vacunas_paciente.html',vacunas_paciente=vacunas_paciente,nombre_paciente=nombre_paciente, mensaje=mensaje)


@app.route('/listado_vacunas/vacunas_administradas/<int:id_vacuna>')
def vacunas_administradas(id_vacuna):
    cursor = mysql.get_db().cursor()
    sql="SELECT nombre_paciente, rut_paciente,fecha_vacuna"
    sql+=" FROM paciente P, recibe R, vacuna V"
    sql+=" WHERE P.id_paciente=R.id_paciente AND R.id_vacuna=V.id_vacuna AND R.id_vacuna= %s"
    cursor.execute(sql,(id_vacuna))
    vacunas_administradas = cursor.fetchall()

    if vacunas_administradas:
        mensaje=""
    else:
        mensaje="NO EXISTEN PACIENTES ASOCIADOS A ESTA VACUNA."

    
    sql2="SELECT nombre_enfermedad FROM vacuna WHERE id_vacuna=%s"
    cursor.execute(sql2,(id_vacuna))
    nombre_enf = cursor.fetchall()
    for iterador in nombre_enf:
        nombre_enfermedad=iterador['nombre_enfermedad']

    return render_template('vacunas_administradas.html',vacunas_administradas=vacunas_administradas,nombre_enfermedad=nombre_enfermedad,mensaje=mensaje)


if __name__ == "__main__":
	app.run(debug=True)