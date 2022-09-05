h = float(input('Insira sua altura: '))
g = str(input('Insira um dos dois gêneros a seguir: homem ou mulher: '))
if g == 'homem':
    print('Seu peso ideal é de: {}'.format((72.7*h)-58))
else:
    print('Seu peso ideal é de: {}'.format((62.1*h)-44.7))