import random
def create_password(words,number,symbol):
    password = []
    password.extend(words)
    password.extend(number)
    password.extend(symbol)

    random.shuffle(password)
    combined = ''.join(password)
    return combined
