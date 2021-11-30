
from paypal import db
from datetime import datetime

class OderProcessing(db.Model):
    id                 = db.Column(db.Integer, primary_key=True)
    # order
    order_id           = db.Column(db.String(50), unique=False, nullable=False)#   5N575537KH865605U  ==> use it in url for more detail on paypal
    order_intent       = db.Column(db.String(50), unique=False, nullable=False)#   CAPTURE
    order_status       = db.Column(db.String(50), unique=False, nullable=False)#   COMPLETED
    # shipping info 
    street             = db.Column(db.String(50), unique=False, nullable=False)#   Av. de la Pelouse
    city_1             = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  Paris
    city_2             = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  Alsace
    postal_code        = db.Column(db.Integer(), unique=False, nullable=False)#    75002
    country_code       = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  FR
    # product detail
    unit_reference_id  = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  default
    unit_currency_code = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  EUR
    unit_amount        = db.Column(db.Float(6, 2), unique=False, nullable=False)#  35.00
    # customer data
    full_name          = db.Column(db.String(50), unique=False, nullable=False)#   John Doe
    payer_first_name   = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  John
    payer_name         = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  Doe
    payer_email        = db.Column(db.String(50), unique=False, nullable=False)#   sb-s60z28668822@personal.example.com
    payer_id           = db.Column(db.String(50), unique=False, nullable=False)#   HPG6DCCZLRKW8
    # some other info 
    merchand_id        = db.Column(db.String(50), unique=False, nullable=False)#   E7VZ3S7TB4HUA
    links              = db.Column(db.String(100), unique=False, nullable=False)#  https://api.sandbox.paypal.com/v2/checkout/orders/5N575537KH865605U
    rel                = db.Column(db.String(50), unique=False, nullable=False)#   E7VZ3S7TB4HUA
    method             = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  GET
    # amount detail
    tva_amount         = db.Column(db.Float(6, 2), unique=False, nullable=False)#  30
    for_paypal         = db.Column(db.Float(6, 2), unique=False, nullable=False)#  paypal ==> 5.22 + 0.33 = 5.55
    for_me             = db.Column(db.Float(6, 2), unique=False, nullable=False)#  me ==> 180 - 30 - 5.55 = 144.5
    # date
    create_time        = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  2021-11-28T04:06:42Z
    update_time        = db.Column(db.VARCHAR(50), unique=False, nullable=False)#  2021-11-28T04:07:13Z
    date_db_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)



db.create_all()