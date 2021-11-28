

class shippingParser():
    def __init__(self, data):
        self.data = data

        # data send by js origin from smartbutton page
        # here I will filter the dict reponse for put the important data into database

        self.order_id = data['id']#5N575537KH865605U  ==> use it in url for more detail on paypal
        self.order_intent = data['intent']#CAPTURE
        self.order_status = data['status']#COMPLETED
        self.create_time = data['create_time']#2021-11-28T04:06:42Z
        self.update_time = data['update_time']#2021-11-28T04:07:13Z
        self.merchand_id = data['purchase_units'][0]['payee']['merchant_id']#E7VZ3S7TB4HUA
        self.unit_reference_id = data['purchase_units'][0]['reference_id']#default
        
        self.street = data['purchase_units'][0]['shipping']['address']['address_line_1']#Av. de la Pelouse
        self.city_1 = data['purchase_units'][0]['shipping']['address']['admin_area_2']#Paris
        self.city_2 = data['purchase_units'][0]['shipping']['address']['admin_area_1']#Alsace
        self.postal_code =data['purchase_units'][0]['shipping']['address']['postal_code']#75002
        self.country_code = data['purchase_units'][0]['shipping']['address']['country_code']#FR
        self.full_name =data['purchase_units'][0]['shipping']['name']['full_name']#John Doe
        self.unit_currency_code = data['purchase_units'][0]['amount']['currency_code']#EUR
        self.unit_amount = data['purchase_units'][0]['amount']['value']#35.00

        self.payer_first_name = data['payer']['name']['given_name']#John
        self.payer_name = data['payer']['name']['surname']#Doe
        self.payer_mail = data['payer']['email_address']#sb-s60z28668822@personal.example.com
        self.payer_id = data['payer']['payer_id']#HPG6DCCZLRKW8
        
        self.link = data['links'][0]['href']#https://api.sandbox.paypal.com/v2/checkout/orders/5N575537KH865605U
        self.rel = data['links'][0]['rel']#self
        self.method = data['links'][0]['method']#GET

        # calculate paypal fee
        # (2.9*150/100)  ==> tax x price / 100
        total = float(self.unit_amount)
        payal_fee = 2.9# 2.9%
        min_fee = 0.33# 0.33 --> EUR
        formula = payal_fee * total / 100
        self.fee = formula + min_fee#to paypal
        self.net = total - self.fee#to me

        

    def put_it_in_db(self, debug=False):
        if debug:
            print('\n\n\t\t DEBUG MODE:\n\n')
            # customer data
            print(f'NAME:\t{self.payer_name}\t FIRSTNAME:\t{self.payer_first_name }\n FULLNAME:\t{self.full_name}\nPAYER_ID:\t{self.payer_id } \tMAIL:\t{self.payer_mail } ')
            print(f'\nORDER_ID:\t{self.order_id}\t ORDER_INTENT:\t{self.order_intent }\n ORDER_STATUS:\t{self.order_status}\n CREATE_TIME:\t{self.create_time } \tLAST_UPDATE:\t{self.update_time } ')
            
            print(f'MERCHANT_ID:\t{self.merchand_id}\t UNIT_CUR:\t{self.unit_currency_code }\nUNIT_AMOUNT:\t{self.unit_amount}\n')
            print(f'\nSTREET:\t{self.street}\nCITY_1:\t{self.city_1 }\nCITY_2:\t{self.city_2}\nPOSTAL:\t{self.postal_code } \tCOUNTRY:\t{self.country_code } ')
            
            print('LINK:\t', self.link)
            print('REL:\t', self.rel)
            print('METHOD:\t', self.method)

        print('here the function for put my data into DB')


'''if __name__ == '__main__':
    response = {'id': '5N575537KH865605U', 'intent': 'CAPTURE', 'status': 'COMPLETED', 'purchase_units': [{'reference_id': 'default', 'amount': {'currency_code': 'EUR', 'value': '35.00'}, 'payee': {'email_address': 'sb-qrq0i8668082@business.example.com', 'merchant_id': 'E7VZ3S7TB4HUA'}, 'shipping': {'name': {'full_name': 'John Doe'}, 'address': {'address_line_1': 'Av. de la Pelouse', 'admin_area_2': 'Paris', 'admin_area_1': 'Alsace', 'postal_code': '75002', 'country_code': 'FR'}}, 'payments': {'captures': [{'id': '0RU30241TS283821M', 'status': 'COMPLETED', 'amount': {'currency_code': 'EUR', 'value': '35.00'}, 'final_capture': True, 'seller_protection': {'status': 'ELIGIBLE', 'dispute_categories': ['ITEM_NOT_RECEIVED', 'UNAUTHORIZED_TRANSACTION']}, 'create_time': '2021-11-28T04:07:13Z', 'update_time': '2021-11-28T04:07:13Z'}]}}], 'payer': {'name': {'given_name': 'John', 'surname': 'Doe'}, 'email_address': 'sb-s60z28668822@personal.example.com', 'payer_id': 'HPG6DCCZLRKW8', 'address': {'country_code': 'FR'}}, 'create_time': '2021-11-28T04:06:42Z', 'update_time': '2021-11-28T04:07:13Z', 'links': [{'href': 'https://api.sandbox.paypal.com/v2/checkout/orders/5N575537KH865605U', 'rel': 'self', 'method': 'GET'}]}
    shippingParser(response).put_it_in_db(True)'''



'''
response items


('id', '5N575537KH865605U')
('intent', 'CAPTURE')      
('status', 'COMPLETED')


('purchase_units', [{
        'reference_id': 'default', 

        'amount': {'currency_code': 'EUR',
                   'value': '35.00'
                   },

        'payee': {
                   'email_address': 'sb-qrq0i8668082@business.example.com', 
                   'merchant_id': 'E7VZ3S7TB4HUA'
                 }, 

        'shipping': {'name': {'full_name': 'John Doe'}, 
                    'address': {
                                'address_line_1': 'Av. de la Pelouse', 
                                'admin_area_2': 'Paris', 
                                'admin_area_1': 'Alsace', 
                                'postal_code': '75002', 
                                'country_code': 'FR'
                                }
                    },
        'payments': {
                    'captures': [{
                        'id': '0RU30241TS283821M',
                        'status': 'COMPLETED',
                        'amount': {'currency_code': 'EUR', 'value': '35.00'}, 
                        'final_capture': True, 
                        'seller_protection': {
                            'status': 'ELIGIBLE', 
                            'dispute_categories': ['ITEM_NOT_RECEIVED', 'UNAUTHORIZED_TRANSACTION']}, 
                            'create_time': '2021-11-28T04:07:13Z', 
                            'update_time': '2021-11-28T04:07:13Z'}]}}])

('payer', 
    {'name': {
                'given_name': 'John', 
                'surname': 'Doe'
            }, 
    'email_address': 'sb-s60z28668822@personal.example.com', 
    'payer_id': 'HPG6DCCZLRKW8', 
    'address': {'country_code': 'FR'}})


('create_time', '2021-11-28T04:06:42Z')
('update_time', '2021-11-28T04:07:13Z')
('links', [{'href': 'https://api.sandbox.paypal.com/v2/checkout/orders/5N575537KH865605U', 'rel': 'self', 'method': 'GET'}])



purchase info
dict_keys(['reference_id', 'amount', 'payee', 'shipping', 'payments'])



'''