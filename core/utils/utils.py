import math
import random
import time
from datetime import date
from datetime import datetime
from string import ascii_uppercase


def generate_number_between(num1, num2):
    random_num = random.randrange(num1, num2)
    print("Random number: {}".format(random_num))
    return random_num


def generate_float_number_between(num1, num2):
    random_float_num = random.uniform(num1, num2)
    print("Random number: {}".format(random_float_num))
    return random_float_num


def floor_two_decimals(num):
    floored_value = math.floor(num * 100) / 100.0
    return floored_value


def generate_number_of_length_n(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    random_number = random.randint(range_start, range_end)
    print("Generated random number of length {}: {}".format(n, random_number))
    return random_number


def pick_random_list_item(my_list):
    random_index = random.randint(0, len(my_list) - 1)
    random_element = my_list[random_index]
    print("List element: {}".format(random_element))
    return random_element


def pick_random_dict_item(my_dict):
    random_element = random.choice(my_dict.keys())
    print("Dict element: {}".format(random_element))
    return random_element


def generate_random_string():
    random_string = ''.join(random.choice(ascii_uppercase))
    print("Generated random string: {}".format(random_string))
    return random_string


def generate_random_string_of_length_n(n):
    random_string = ''.join(random.choice(ascii_uppercase) for i in range(n))
    print("Generated random string of length {}: {}".format(n, random_string))
    return random_string


def generate_string_ending_with_number(string_starts_with):
    string = "{}{}".format(string_starts_with, random.randint(0, 100))
    print("Generated string {} starting with {}".format(string, string_starts_with))
    return string


def generate_now_timestamp_rc3339():
    return datetime.now().isoformat('T')


def get_current_date_and_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_today_date():
    return str(date.today())


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def get_utc_ms_time(value):
    try:
        date_obj = value
        if isinstance(value, str):
            date_obj = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return int(time.mktime(date_obj.timetuple())) * 1000
    except:
        return ''
