#!/usr/bin/env python2.7

import os
from sqlalchemy import *
from sqlalchemy.pool import NullPool
from flask import Flask, request, render_template, g, redirect, Response

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)


DATABASEURI = "postgresql://sv2525:6185@35.231.44.137/proj1part2"


#
# This line creates a database engine that knows how to connect to the URI above.
#
engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request 
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print "uh oh, problem connecting to database"
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass


@app.route('/')
def landing():
  return render_template("landing.html")

#Page for Donors and Recepients
@app.route('/Users')
def donorRecepient():
  return render_template("searchUser.html")

#Landing page for all administrators 
@app.route('/searchAdmin')
def searchAdmin():
  return render_template("searchAdmin.html")

#Page for Blood bank administrator
@app.route('/bbAdmin')
def bloodbankAdmin():
  return render_template("searchBB.html")    

#Page for Hospital Administrator
@app.route('/hospiAdmin')
def hospiAdmin():
  return render_template("searchHA.html")



@app.route('/index')
def index():
  print request.args

  cursor = g.conn.execute("SELECT name FROM test")
  names = []
  for result in cursor:
    names.append(result['name'])  # can also be accessed using result[0]
  cursor.close()

  context = dict(data = names)

  return render_template("index.html", **context)

@app.route('/another')
def another():
  return render_template("another.html")


# Example of adding new data to the database
@app.route('/add', methods=['POST'])
def add():
  name = request.form['name']
  g.conn.execute('INSERT INTO test(name) VALUES (%s)', (name))
  return redirect('/index')


@app.route('/searchUser', methods=['POST'])
def searchUser():
  id = request.form['name']
  cursor1 = g.conn.execute("SELECT * FROM donor WHERE donorID = %s;", id)
  # cursor2 = g.conn.execute("SELECT * FROM recipient WHERE recipientID = %s;", id)
  results1 = []
  results2 = []
  for result in cursor1:
    results1.append(result['name'])  # can also be accessed using result[0]
  cursor1.close()

  # for result in cursor2:
  #   results2.append(result['name'])  # can also be accessed using result[0]
  # cursor2.close()

  # if results1 == []:
  #   context = dict(data = results1)
  # else:
  #   context = dict(data = results2)
  context = dict(data=results1)

  return render_template("index.html", **context)



if __name__ == "__main__":
  import click

  @click.command()
  @click.option('--debug', is_flag=True)
  @click.option('--threaded', is_flag=True)
  @click.argument('HOST', default='0.0.0.0')
  @click.argument('PORT', default=8111, type=int)
  def run(debug, threaded, host, port):
    HOST, PORT = host, port
    print "running on %s:%d" % (HOST, PORT)
    app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)


  run()
