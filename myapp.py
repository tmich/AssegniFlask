#from __future__ import print_function
import os, config, json, datetime, flask, sys
from functools import wraps
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, make_response, jsonify
from sqlalchemy import and_, or_, func, distinct
#from flask_mail import Mail, Message
#from flask.json import JSONEncoder, JSONDecoder
#from flask_babel import Babel, format_datetime, format_date
from decimal import Decimal
#from pdfs import create_pdf
from models import db  # , Anagrafica, Cliente, Prodotto, Fattura, VoceFattura, InvioFattura, User, FatturaSequence, ObjFatt, ObjVoce, EmailConfig, Messaggio, ListaDistribuzione, MembroListaDistribuzione, get_azienda
#from forms import FormNuovaFattura, FormAggiungiVoce, FormNuovaFattura, FormCliente, FormProdotto, FormProfilo, FormDate, FormDateFatture
#import jsonpickle
#from smtplib import SMTPException, SMTPAuthenticationError, SMTPRecipientsRefused
#from threading import Thread

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.DevelopmentConfig')
	app.static_folder = 'static'
	#mail_ext = Mail(app)
	#db = SQLAlchemy(app)
	db.init_app(app)
	##babel = Babel(app)
	#with app.app_context():
		#Extensions like Flask-SQLAlchemy now know what the "current" app
		#is while within this block. Therefore, you can now run........
		#db.create___all()

	return app

app = create_app()

def login_required(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if g.user is None:
			return redirect(url_for('login'))
		return f(*args, **kwargs)
	return decorated_function

## Views
'''
@app.before_request
def load_user():
  if "uid" in session:
	g.user = User.query.get(session['uid'])
  else:
	g.user = None #{'id' : 0, 'nome': 'Guest'}  # Make it better, use an anonymous User instead
'''
@app.route("/")
def main():
    return "Ciao!"
	#return render_template('index.html', n_fatture_da_inviare=n_fatture_da_inviare, n_fatture_da_stampare=n_fatture_da_stampare, current='home')

