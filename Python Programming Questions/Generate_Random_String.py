# There are multiple ways to generate random string
# 1. Using random & string modules
import random
import string
import secrets


def gen_random_str(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


random_str = gen_random_str(5)
print("Random String is:" + random_str)


# 2.By Specifying chars manually
def generate_ran_str(len_str):
    let = "abcd1346kly"
    res_str = ''.join(random.choice(let) for j in range(len_str))
    return res_str


ran_str = generate_ran_str(6)
print("Random String is:" + ran_str)  # Here it will generate random string by combination of string declared in method


# 3.By Using secrets module
# It is designed for cryptographic purposes and is considered more secure for generating random data.


def generate_random_string(length_of_string):
    letter_and_digits = string.ascii_letters + string.digits
    exp_string = ''.join(secrets.choice(letter_and_digits) for k in range(length_of_string))
    return exp_string


crypto_random_string = generate_random_string(16)
print("Random String is:" + crypto_random_string)
