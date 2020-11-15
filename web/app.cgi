#!/usr/bin/python3

from wsgiref.handlers import CGIHandler
from flask import Flask
from flask import render_template, request, redirect, url_for

## Libs postgres
import psycopg2
import psycopg2.extras

app = Flask(__name__)

## SGBD configs
DB_HOST="db.tecnico.ulisboa.pt"
DB_USER="ist425999" 
DB_DATABASE=DB_USER
DB_PASSWORD="gss97"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)


## Runs the function once the root page is requested.
## The request comes with the folder structure setting ~/web as the root
@app.route('/instituicao')
def list_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM instituicao;"
    cursor.execute(query)
    return render_template("instituicao.html", cursor=cursor)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

@app.route('/editar_instituicao')
def alter_instituicao():
  try:
    return render_template("editar_instituicao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/update', methods=["POST"])
def update_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE instituicao SET tipo='{request.form["novo_tipo"]}', num_regiao='{request.form["novo_num_regiao"]}', num_concelho='{request.form["novo_num_concelho"]}' WHERE nome = '{request.form["nome"]}' and tipo = '{request.form["tipo"]}' and num_regiao = '{request.form["num_regiao"]}' and num_concelho = '{request.form["num_concelho"]}';'''
    cursor.execute(query)
    return redirect(url_for('list_instituicao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/remove', methods=["DELETE", "GET"])
def remove_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM instituicao WHERE nome = '{request.args.get('nome')}' and tipo = '{request.args.get('tipo')}' and num_regiao = '{request.args.get('num_regiao')}' and num_concelho = '{request.args.get('num_concelho')}';'''
    cursor.execute(query)
    return redirect(url_for('list_instituicao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/medico')
def list_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM medico;"
    cursor.execute(query)
    return render_template("medico.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

@app.route('/editar_medico')
def alter_medico():
  try:
    return render_template("editar_medico.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/update', methods=["POST"])
def update_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE medico SET nome='{request.form["novo_nome"]}', especialidade='{request.form["nova_especialidade"]}' WHERE num_cedula = '{request.form["num_cedula"]}' and nome = '{request.form["nome"]}' and especialidade = '{request.form["especialidade"]}';'''
    cursor.execute(query)
    return redirect(url_for('list_medico'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/remove', methods=["DELETE", "GET"])
def remove_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM medico WHERE num_cedula = '{request.args.get('num_cedula')}' and nome = '{request.args.get('nome')}' and especialidade = '{request.args.get('especialidade')}';'''
    cursor.execute(query)
    return redirect(url_for('list_medico'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/lista_substancia')
def alter_listasubs():
  try:
    return render_template("lista_substancia.html", params=request.args)
  except Exception as e:
    return str(e)


@app.route('/printsubstancias', methods=["GET"])
def list_substancias():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''SELECT substancia FROM prescricao_venda WHERE date_part('month', data) = '{request.args.get('novo_mes')}' and date_part('year', data) = '{request.args.get('novo_ano')}' and num_cedula = '{request.form["num_cedula"]}';'''
    cursor.execute(query)
    return render_template("printsubstancias.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

CGIHandler().run(app)

