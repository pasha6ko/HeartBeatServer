import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from validate_email import validate_email
import datetime

params = {
    "password_min": 8,
    "password_max": 128,
    "name_min": 2,
    "name_max": 60,
    "age_min": 16,
    "contact_data_min": 5,
    "contact_data_max": 60,
    "discription_max": 300
}


class Validator:
    def check_phone_number(number, contatins_region=False):
        number = str(number)
        if not contatins_region:
            number = "+" + number
        try:
            return carrier._is_mobile(number_type(phonenumbers.parse(number)))
        except:
            return False

    def check_email(email):
        return validate_email(email, verify=False)

    def has_chars(inputString):
        for i in inputString:
            if i.isalpha():
                return True
        return False

    def has_numbers(inputString):
        return any(char.isdigit() for char in inputString)

    def password_validation(password):
        password = str(password)
        if len(password) < params["password_min"] or len(password) > params["password_max"]:
            return False
        if not Validator.has_numbers(password):
            return False
        if not Validator.has_chars(password):
            return False
        return True

    def profile_name_validation(name):
        name = str(name)
        if len(name) < params["name_min"] or len(name) > params["name_max"]:
            return False
        if Validator.has_numbers(name):
            return False
        return True

    def age_validation(birth_date):
        birth_date = datetime.datetime.strptime(birth_date, '%Y-%m-%d')
        today = datetime.datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(age)
        return params["age_min"] <= age

    def contact_data_validation(contact_data):
        contact_data = str(contact_data)
        return len(contact_data) >= params["contact_data_min"] and len(contact_data) <= params["contact_data_max"]

    def discription_validation(discription):
        discription = str(discription)
        return len(discription) <= params["discription_max"]
