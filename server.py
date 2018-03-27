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

#Page for Hospital Administrator
@app.route('/searchHA')
def hospiAdmin():
  id = request.args['eid']
  cursor = g.conn.execute("SELECT * FROM hospitaldept where employeeid = %s;", id)
  results = []
  results.append("Hospital ID, Department ID, Admin ID, Admin since:")
  for result in cursor:
    hID = result[0]
    dID = result[1]
    results.append(result)
  cursor.close()

  context = dict(data=results)
  return render_template("searchHA.html", **context)

@app.route('/searchHA2')
def findDetails():
  hid = request.args['hid']
  rid = request.args['rid']
  option = request.args['avail']

  results = []

  if option == 'check':
    cursor = g.conn.execute("SELECT * FROM bloodcapacity WHERE hospitalID = %s;", hid)
    results.append("Hospital ID, Blood type, Units of Blood:")
  elif option == 'history':
    cursor = g.conn.execute("SELECT * FROM transfusions WHERE hospitalID = %s AND recipientID = %s;", (hid, rid))
    results.append("Transfusion ID, Request ID, Recipient ID, Hospital ID, Units of Blood, Date:")
  elif option == 'available':
    cursor = g.conn.execute("SELECT * FROM bloodcapacity WHERE hospitalID = %s AND bloodtype = (SELECT bloodType FROM recipients WHERE recipientID = %s)", (hid, rid))
    results.append("Units of Blood:")
  elif option == 'internal':
    cursor = g.conn.execute("SELECT * FROM internalrequest WHERE hospitalID = %s", hid)
    results.append("Request ID, Blood type, Units of Blood, Department ID, Hospital ID")
  else:
    cursor1 = g.conn.execute("SELECT * FROM transfers WHERE fromID = %s", hid)
    results.append("Transfer ID, From ID, To ID, Blood Type, Units")
    results.append("Transferred To: ")
    for result in cursor1:
        results.append(result)
    cursor1.close()
    cursor = g.conn.execute("SELECT * FROM transfers WHERE toID = %s", hid)
    results.append("Received From: ")

  for result in cursor:
    results.append(result)
  cursor.close()

  context = dict(data=results)
  return render_template("searchHA2.html", **context)

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
@app.route('/addDonor', methods=['POST'])
def add():
  name = request.form['name']
  id = request.form['did']
  bloodtype = request.form['bloodtype']
  address = request.form['address']
  phone = request.form['phone']
  userType = request.form['usertype']
  if userType == 'donor':
    g.conn.execute('INSERT INTO donor(name, donorID, bloodType, address, phone) VALUES (%s, %s, %s, %s, %s)', (name, id, bloodtype, address, phone))
  else:
    g.conn.execute('INSERT INTO recipients(name, recipientID, bloodType, address, phone) VALUES (%s, %s, %s, %s, %s)',
                   (name, id, bloodtype, address, phone))

  return render_template("searchAdmin.html")


@app.route('/Users')
def user():
  return render_template("searchUser.html")

@app.route('/searchUser')
def searchUser():
  userType = request.args['usertype']
  id = request.args['name']
  if userType == 'donor':
    cursor1 = g.conn.execute("SELECT * FROM donor WHERE donorID = %s;", id)
    cursor2 = g.conn.execute("SELECT donationID, unitsDonated, institutionID, date FROM donor d1, donations d2 WHERE d1.donorID = d2.donorID AND d1.donorID = %s;", id)
  else:
    cursor1 = g.conn.execute("SELECT * FROM recipients WHERE recipientID = %s;", id)
    cursor2 = g.conn.execute("SELECT transfusionID, unitsTransfused, hospitalID, date FROM recipients R, transfusions T WHERE R.recipientID = T.recipientID AND R.recipientID = %s;", id)
  results = []
  results.append("ID, Blood Type, Name, Address, Phone: ")
  for result in cursor1:
    newRow = []
    for item in result:
      newRow.append(item)
    results.append(newRow) # can also be accessed using result[0]
  cursor1.close()
  results.append("Transaction ID, Units of Blood, Institution ID, Date: ")
  for result in cursor2:
    newRow = []
    for item in result:
      newRow.append(item)
    results.append(newRow)  # can also be accessed using result[0]
  cursor2.close()

  context = dict(data=results)

  return render_template("searchUser.html", **context)

#Landing page for all administrators
@app.route('/searchAdmin')
def searchAdmin():
  return render_template("searchAdmin.html")

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
