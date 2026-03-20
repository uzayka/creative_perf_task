from random import choice, shuffle

def generate_password(lowercase, numbers, uppercase, signs, num_1, num_2, num_3, num_4):
    password = []
    strk = 'qwertyuiopasdfghjklzxcvbnm'
    num = '1234567890'
    krts = 'QWERTYUIOPASDFGHJKLZXCVBNM'
    sig = '!@#$%^&*()'
    if lowercase:
        for i in range(num_1):
            bukva = choice(strk)
            password.append(bukva)
    if numbers:
        for i in range(num_2):
            tsifra = choice(num)
            password.append(tsifra)
    if uppercase:
        for i in range(num_3):
            buk = choice(krts)
            password.append(buk)
    if signs:
        for i in range(num_4):
            s = choice(sig)
            password.append(s)
    shuffle(password)
    return ''.join(password)


def check_safety(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_spec = any(c in '!@#$%^&*()' for c in password)

    types_count = sum([has_lower, has_upper, has_digit, has_spec])

    if length >= 12 and types_count >= 3:
        return "This password is safe ^^", "green"
    elif length >= 8 and types_count >= 2:
        return "This is not the best option. Try to generate again", "orange"
    else:
        return "It is not a safe option:(", "red"

