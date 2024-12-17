import random
print('1-poziom łatwy, 2-poziom trudny')
level = int(input('Jaki wybrać poziom trudnośći?: '))

punkty, ilosc_pytan = 0, 0
while True:
    if level == 1:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
    else:
        a = random.randint(1, 99)
        b = random.randint(1, 99)
        
    odp = int(input(f'Ile to {a} * {b}: '))
    if odp == a * b:
        print('Dobrze odpowiedziałeś!')
        punkty += 1
    else:
        print(f'Odpowiedź jest niepoprawna! Prawidłowa odpowiedź to {a * b}.')
    ilosc_pytan += 1
    if input() == '':
        continue
    else:
        break
print(f'Odpowiedziałeś poprawnie {punkty} razy, na {ilosc_pytan} pytania.')
print(f'To jest {punkty / ilosc_pytan * 100}% poprawnych odpowiedzi'.)
