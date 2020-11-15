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

@app.route('/inserir_instituicao')
def new_instituicao():
  try:
    return render_template("inserir_instituicao.html")
  except Exception as e:
    return str(e)

@app.route('/update_inst', methods=["POST"])
def update_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE instituicao SET nome='{request.form["novo_nome"]}', tipo='{request.form["novo_tipo"]}', num_regiao='{request.form["novo_num_regiao"]}', num_concelho='{request.form["novo_num_concelho"]}' WHERE nome = '{request.form["nome"]}' and tipo = '{request.form["tipo"]}' and num_regiao = '{request.form["num_regiao"]}' and num_concelho = '{request.form["num_concelho"]}';'''
    cursor.execute(query)
    return redirect(url_for('list_instituicao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/insert_inst', methods=["POST"])
def insert_instituicao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''insert into instituicao values('{request.form["novo_nome"]}', '{request.form["novo_tipo"]}', '{request.form["novo_num_regiao"]}', '{request.form["novo_num_concelho"]}');'''
    cursor.execute(query)
    return redirect(url_for('list_instituicao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/remove_inst', methods=["DELETE", "GET"])
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

@app.route('/inserir_medico')
def new_medico():
  try:
    return render_template("inserir_medico.html")
  except Exception as e:
    return str(e)

@app.route('/update_med', methods=["POST"])
def update_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE medico SET num_cedula='{request.form["novo_num_cedula"]}', nome='{request.form["novo_nome"]}', especialidade='{request.form["nova_especialidade"]}' WHERE num_cedula = '{request.form["num_cedula"]}' and nome = '{request.form["nome"]}' and especialidade = '{request.form["especialidade"]}';'''
    cursor.execute(query)
    return redirect(url_for('list_medico'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()
    
@app.route('/insert_med', methods=["POST"])
def insert_medico():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''insert into medico values('{request.form["novo_num_cedula"]}', '{request.form["novo_nome"]}', '{request.form["nova_especialidade"]}');'''
    cursor.execute(query)
    return redirect(url_for('list_medico'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()


@app.route('/remove_med', methods=["DELETE", "GET"])
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

@app.route('/venda_farmacia')
def list_venda_farmacia():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM venda_farmacia;"
    cursor.execute(query)
    return render_template("venda_farmacia.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

@app.route('/registo_venda')
def alter_venda_farmacia():
  try:
    return render_template("registo_venda.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/registo', methods=["POST"])
def update_venda_farmacia():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''INSERT INTO venda_farmacia VALUES ('{request.form["num_venda"]}', '{request.form["data_registo"]}', '{request.form["substancia"]}', '{request.form["quant"]}', '{request.form["preco"]}', '{request.form["inst"]}');'''
    cursor.execute(query)
    return redirect(url_for('list_venda_farmacia'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

CGIHandler().run(app)

