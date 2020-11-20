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
DB_USER="ist426057" 
DB_DATABASE=DB_USER
DB_PASSWORD="1q2w3e"
DB_CONNECTION_STRING = "host=%s dbname=%s user=%s password=%s" % (DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD)


## Runs the function once the root page is requested.
## The request comes with the folder structure setting ~/web as the root

#FUNCOES INDEX--------------------------------------------------------------------------------------------

@app.route('/')
def choose_options():
  try:
    return render_template("index.html", params=request.args)
  except Exception as e:
    return str(e)

#FUNCOES INSTITUICAO--------------------------------------------------------------------------------------

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
    query = '''insert into instituicao values(%s, %s, %s, %s);'''
    cursor.execute(query, (f'''{request.form["novo_nome"]}''', f'''{request.form["novo_tipo"]}''', f'''{request.form["novo_num_regiao"]}''', f'''{request.form["novo_num_concelho"]}'''))
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

#--------------------------------------------------------------------------------------------------------
#FUNCOES MEDICO------------------------------------------------------------------------------------------

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
    query = '''insert into medico values(%s, %s, %s);'''
    cursor.execute(query, (f'''{request.form["novo_num_cedula"]}''', f'''{request.form["novo_nome"]}''', f'''{request.form["nova_especialidade"]}'''))
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

#--------------------------------------------------------------------------------------------------------
#FUNCOES VENDA_FARMACIA----------------------------------------------------------------------------------

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
    query = '''INSERT INTO venda_farmacia VALUES (%s, %s, %s, %s, %s, %s);'''
    cursor.execute(query, (f'''{request.form["num_venda"]}''', f'''{request.form["data_registo"]}''', f'''{request.form["substancia"]}''', f'''{request.form["quant"]}''', f'''{request.form["preco"]}''', f'''{request.form["inst"]}'''))
    query = f'''INSERT INTO prescricao_venda (num_cedula, num_doente, data, substancia, num_venda) SELECT num_cedula, num_doente, data, substancia, '{request.form["num_venda"]}' FROM prescricao WHERE (data='{request.form["data_registo"]}' AND substancia='{request.form["substancia"]}' AND quant = '{request.form["quant"]}');'''
    cursor.execute(query)
    return redirect(url_for('list_venda_farmacia'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

#--------------------------------------------------------------------------------------------------------
#FUNCOES SUBSTANCIA--------------------------------------------------------------------------------------

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
    query = f'''SELECT substancia FROM prescricao_venda WHERE num_cedula='{request.args.get('num_cedula')}' and date_part('month', data)='{request.args.get('novo_mes')}' and date_part('year', data)='{request.args.get('novo_ano')}';'''
    cursor.execute(query)
    return render_template("printsubstancias.html",cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

#--------------------------------------------------------------------------------------------------------
#FUNCOES PRESCRICAO--------------------------------------------------------------------------------------

@app.route('/prescricao')
def list_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM prescricao;"
    cursor.execute(query)
    return render_template("prescricao.html", cursor=cursor)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

@app.route('/editar_prescricao')
def alter_prescricao():
  try:
    return render_template("editar_prescricao.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/inserir_prescricao')
def new_prescricao():
  try:
    return render_template("inserir_prescricao.html")
  except Exception as e:
    return str(e)

@app.route('/update_presc', methods=["POST"])
def update_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE prescricao SET num_cedula='{request.form["novo_num_cedula"]}', num_doente='{request.form["novo_num_doente"]}', data='{request.form["nova_data"]}', substancia='{request.form["nova_substancia"]}', quant='{request.form["nova_quant"]}' WHERE num_cedula='{request.form["num_cedula"]}' and num_doente='{request.form["num_doente"]}' and data='{request.form["data"]}' and substancia='{request.form["substancia"]}' and quant='{request.form["quant"]}';'''
    cursor.execute(query)
    return redirect(url_for('list_prescricao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/insert_presc', methods=["POST"])
def insert_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = '''insert into prescricao values(%s, %s, %s, %s, %s);'''
    cursor.execute(query, (f'''{request.form["novo_num_cedula"]}''', f'''{request.form["novo_num_doente"]}''', f'''{request.form["nova_data"]}''', f'''{request.form["nova_substancia"]}''', f'''{request.form["nova_quant"]}'''))
    return redirect(url_for('list_prescricao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/remove_presc', methods=["DELETE", "GET"])
def remove_prescricao():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM prescricao WHERE num_cedula='{request.args.get('num_cedula')}' and num_doente='{request.args.get('num_doente')}' and data='{request.args.get('data')}' and substancia='{request.args.get('substancia')}' and quant='{request.args.get('quant')}';'''
    cursor.execute(query)
    return redirect(url_for('list_prescricao'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

#-------------------------------------------------------------------------------------------------------
#FUNCOES analise---------------------------------------------------------------------------------------

@app.route('/analise')
def list_analise():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM analise;"
    cursor.execute(query)
    return render_template("analise.html", cursor=cursor)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()

@app.route('/editar_analise')
def alter_analise():
  try:
    return render_template("editar_analise.html", params=request.args)
  except Exception as e:
    return str(e)

@app.route('/inserir_analise')
def new_analise():
  try:
    return render_template("inserir_analise.html")
  except Exception as e:
    return str(e)

@app.route('/update_analis', methods=["POST"])
def update_analise():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''UPDATE analise SET num_analise='{request.form["novo_num_analise"]}', especialidade='{request.form["nova_especialidade"]}', num_cedula='{request.form["novo_num_cedula"]}', num_doente='{request.form["novo_num_doente"]}', data='{request.form["nova_data"]}', data_registo='{request.form["nova_data_registo"]}', nome='{request.form["novo_nome"]}', quant='{request.form["nova_quant"]}', inst='{request.form["nova_inst"]}' WHERE num_analise='{request.form["num_analise"]}' and especialidade='{request.form["especialidade"]}' and num_cedula='{request.form["num_cedula"]}' and num_doente='{request.form["num_doente"]}' and data='{request.form["data"]}' and data_registo='{request.form["data_registo"]}' and nome='{request.form["nome"]}' and quant='{request.form["quant"]}' and inst='{request.form["inst"]}';'''
    cursor.execute(query)
    return redirect(url_for('list_analise'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/insert_analis', methods=["POST"])
def insert_analise():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = '''insert into analise values(%s, %s, %s, %s, %s, %s, %s, %s, %s);'''
    cursor.execute(query, (f'''{request.form["novo_num_analise"]}''', f'''{request.form["nova_especialidade"]}''', f'''{request.form["novo_num_cedula"]}''', f'''{request.form["novo_num_doente"]}''', f'''{request.form["nova_data"]}''', f'''{request.form["nova_data_registo"]}''', f'''{request.form["novo_nome"]}''', f'''{request.form["nova_quant"]}''', f'''{request.form["nova_inst"]}'''))
    return redirect(url_for('list_analise'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

@app.route('/remove_analis', methods=["DELETE", "GET"])
def remove_analise():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = f'''DELETE FROM analise WHERE num_analise='{request.args.get('num_analise')}' and especialidade='{request.args.get('especialidade')}' and num_cedula='{request.args.get('num_cedula')}' and num_doente='{request.args.get('num_doente')}' and data='{request.args.get('data')}' and data_registo='{request.args.get('data_registo')}' and nome='{request.args.get('nome')}' and quant='{request.args.get('quant')}' and inst='{request.args.get('inst')}';'''
    cursor.execute(query)
    return redirect(url_for('list_analise'))
  except Exception as e:
    return str(e) 
  finally:
    dbConn.commit()
    cursor.close()
    dbConn.close()

#--------------------------------------------------------------------------------------------------------
#FUNCOES PRESCRICAO_VENDA----------------------------------------------------------------------------------

@app.route('/prescricao_venda')
def list_prescricao_venda():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT * FROM prescricao_venda;"
    cursor.execute(query)
    return render_template("prescricao_venda.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()


@app.route('/lista_glicemia')
def list_glicemia():
  dbConn=None
  cursor=None
  try:
    dbConn = psycopg2.connect(DB_CONNECTION_STRING)
    cursor = dbConn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    query = "SELECT concelho.nome as concelho, num_doente, quant\
             FROM concelho\
             JOIN\
             (SELECT t.*\
             FROM (SELECT num_doente, quant, num_regiao, num_concelho,\
                          ROW_NUMBER() OVER (PARTITION BY num_regiao ORDER BY quant DESC) as seqnum\
                   FROM (SELECT * FROM analise WHERE nome = 'Glicemia') t1 JOIN\
                         instituicao t2\
                         ON t1.inst = t2.nome\
                   ) AS t\
             WHERE seqnum = 1) AS max_num\
             ON concelho.num_concelho = max_num.num_concelho AND concelho.num_regiao = max_num.num_regiao\
             UNION \
             SELECT concelho.nome as concelho, num_doente, quant\
             FROM concelho\
             JOIN\
             (SELECT t.*\
             FROM (SELECT num_doente, quant, num_regiao, num_concelho,\
                          ROW_NUMBER() OVER (PARTITION BY num_regiao ORDER BY quant ASC) as seqnum\
                   FROM (SELECT * FROM analise WHERE nome = 'Glicemia') t1 JOIN\
                         instituicao t2\
                         ON t1.inst = t2.nome\
                   ) AS t\
             WHERE seqnum = 1) AS max_num\
             ON concelho.num_concelho = max_num.num_concelho AND concelho.num_regiao = max_num.num_regiao;"
    cursor.execute(query)
    return render_template("lista_glicemia.html", cursor=cursor, params=request.args)
  except Exception as e:
    return str(e) #Renders a page with the error.
  finally:
    cursor.close()
    dbConn.close()


CGIHandler().run(app)

