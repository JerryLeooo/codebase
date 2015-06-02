# -*- coding: utf-8 -*-

from main.core import db, SurrogatePK, Model

class Partner(SurrogatePK, Model):

    __tablename__ = 'partner'

    name = db.Column(db.String(128), unique=True)

class Activity(SurrogatePK, Model):

    __tablename = 'activity'

    name = db.Column(db.String(128), unique=True)
    partner_id = db.Column(db.Integer, db.ForeignKey('partner.id'))
    partner = db.relationship('Partner',
        backref=db.backref('activities'), lazy='dynamic')

class User(SurrogatePK, Model):

    __tablename__ = 'user'

    douban_id = db.Column(db.String(10))
    role = db.Column(db.String(8))

class Coupon(SurrogatePK, Model):

    __tablename__ = 'coupon'

    token = db.Column(db.String(128))
