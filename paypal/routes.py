from paypal import app
from flask import render_template, request




@app.route('/')
def smartbutton():
	try:
		return render_template("button/smartbutton.html")
	except Exception as e:
		return(str(e))
from .process import shippingParser

@app.route('/smart_button_ipn', methods=['POST'])
def smartbuttonipn():
    # from here i receive a response from paypal after the payment was done
    # also I need to store this data into db 
    data = request.get_json()
    shippingParser(data).put_it_in_db(True)

    return(data)






