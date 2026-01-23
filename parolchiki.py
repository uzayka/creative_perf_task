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



