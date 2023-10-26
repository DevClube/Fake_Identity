from datetime import datetime

from faker import Faker
from faker.providers.phone_number import Provider
from flask import Flask, render_template

from Backend.FakeObject import Person, AdditionalInfo

app = Flask(__name__)



@app.route('/')
def index():
    # Example data

    faker = Faker(locale='en-US')

    # Set the start and end dates for the date_of_birth method
    start_date = datetime.strptime('1970-01-01', '%Y-%m-%d')
    end_date = datetime.strptime('2000-12-31', '%Y-%m-%d')
    # Create an instance of the Person class
    fake_profile = faker.profile()
    fake_birthdate = faker.date_between_dates(date_start=start_date, date_end=end_date)
    fake_profile['birthdate'] = fake_birthdate

    person_object = Person(fake_profile)
    additional_info_data = {
        'phone_number': faker.phone_number(),
        'city': faker.city(),
        'postcode': faker.postcode(),
        'country': faker.country(),
        'credit_card_number': faker.credit_card_number(),
        'credit_card_expire': faker.credit_card_expire(),
        'credit_card_security_code': faker.credit_card_security_code(),
    }

    phone_provider = Provider(generator=faker)
    formatted_phone_number = phone_provider.msisdn()
    fake_profile['phone_number'] = formatted_phone_number
    additional_object = AdditionalInfo(additional_info_data)



    # Render the HTML template and pass the person object to it
    return render_template('index.html', person=person_object, additional_info=additional_object)

if __name__ == '__main__':
    app.run(debug=True)
