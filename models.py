# models.py
# from __future__ import print_function
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
# import sys
# import datetime
# from decimal import Decimal
# from flask.json import jsonify

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    nome = db.Column(db.String(80))
    profilo = db.Column(db.String(1))
    attivo = db.Column(db.Integer)

    def __init__(self, username, password, email, nome, profilo='U', attivo=1):
        self.username = username
        self.password = password
        self.email = email
        self.nome = nome
        self.profilo = profilo
        self.attivo = attivo

    def is_admin(self):
        return self.profilo == 'A'

    def __repr__(self):
        return '<User %r>' % self.username


class Assegno(db.Model):
    __tablename__ = 'assegno'
    id = Column(Integer, primary_key=True)
    id_libretto = Column(Integer, ForeignKey('libretto_assegni.id'))
    numero = Column(String(50))
    data_emissione = Column(DateTime)
    data_scadenza = Column(DateTime)
    beneficiario = Column(String(50))
    importo = Column(Float)
    data_incasso = Column(DateTime)
    note = Column(String(50))
    libretto = relationship("Libretto", back_populates="assegni")

    def __repr__(self):
        return "<Assegno(id={0}, beneficiario={1})>".format(
            self.id, self.beneficiario)


class Azienda(db.Model):
    __tablename__ = 'azienda'
    id = Column(Integer, primary_key=True)
    ragione_sociale = Column(String(100))
    indirizzo = Column(String(100))
    partita_iva = Column(String(20))
    conti = relationship("ContoCorrente", back_populates="azienda")

    def __repr__(self):
        return "<Azienda {0}>".format(self.ragione_sociale)


class ContoCorrente(db.Model):
    __tablename__ = 'conto_corrente'
    id = Column(Integer, primary_key=True)
    id_azienda = Column(Integer, ForeignKey("azienda.id"))
    numero = Column(String(50))
    banca = Column(String(100))
    sede = Column(String(50))
    agenzia = Column(String(50))
    note = Column(String(200))
    azienda = relationship("Azienda", back_populates="conti")


class Fornitore(db.Model):
    __tablename__ = 'fornitori'
    id = Column(Integer, primary_key=True)
    denominazione = Column(String(100))
    indirizzo = Column(String(100))
    telefono = Column(String(100))
    partita_iva = Column(String(100))


class Libretto(db.Model):
    __tablename__ = 'libretto_assegni'
    id = Column(Integer, primary_key=True)
    id_conto_corrente = Column(Integer, ForeignKey("conto_corrente.id"))
    numero = Column(String(50))
    codice = Column(String(100))
    qta = Column(Integer)
    conto = relationship("ContoCorrente")
    assegni = relationship("Assegno", back_populates="libretto")
