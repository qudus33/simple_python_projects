# This script identifies what network provider a phone number belongs to in Nigeria.
import sys

MTN = ["0803", "0703", "0806", "0706", "0813", "0810", "0814", "0816", "0903", "0906"]
GLO = ["0805", "0705", "0905", "0807", "0815", "0811"]
AIRTEL = ["0907", "0708", "0802", "0902", "0812", "0808", "0701"]
NINE_MOBILE = ["0909", "0908", "0818", "0809", "0817"]

def check_number(number):
    if number[:4] == "+234":
        number_code = "0" + number[4:]
        if number_code[:4] in MTN:
            print("{} is MTN Number.".format(number))
        if number_code[:4] in GLO:
            print("{} is GLO Number.".format(number))
        if number_code[:4] in AIRTEL:
            print("{} is Airtel Number.".format(number))
        if number_code[:4] in NINE_MOBILE:
            print("{} is 9mobile Number.".format(number))
    else:
        if number[:4] in MTN:
            print("{} is MTN Number.".format(number))
        if number[:4] in GLO:
            print("{} is GLO Number.".format(number))
        if number[:4] in AIRTEL:
            print("{} is Airtel Number.".format(number))
        if number[:4] in NINE_MOBILE:
            print("{} is 9mobile Number.".format(number))


# Usage = checK_network_provider.py <number> e.g checK_network_provider.py 080234*****
number = sys.argv[1]
check_number(number)