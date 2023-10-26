


class Person:
    def __init__(self, data):
        self.job = data['job']
        self.company = data['company']
        self.ssn = data['ssn']
        self.residence = data['residence']
        self.phone_number = data.get('phone_number')
        self.current_location = data['current_location']
        self.blood_group = data['blood_group']
        self.website = data['website']
        self.username = data['username']
        self.name = data['name']
        self.sex = data['sex']
        self.address = data['address']
        self.mail = data['mail']
        self.birthdate = data['birthdate']
        self.city = data.get('city')
        self.postcode = data.get('postcode')
        self.country = data.get('country')

class AdditionalInfo:
    def __init__(self, data):
        self.phone_number = data.get('phone_number')
        self.city = data.get('city')
        self.postcode = data.get('postcode')
        self.country = data.get('country')
        self.credit_card_number = data.get('credit_card_number')
        self.credit_card_expire = data.get('credit_card_expire')
        self.credit_card_security_code = data.get('credit_card_security_code')



