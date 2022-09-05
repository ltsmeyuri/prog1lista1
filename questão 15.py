s = float(input('Insira o quanto você ganha por hora: '))
h = int(input('Insira o número de horas trabalhadas no mês: '))
b = s*h
ir = b*(11/100)
inss = b *(8/100)
sind = b *(5/100)
l = b - ir - inss - sind
print ('Seu salário bruto é de R$: {}'.format(b))
print ('Você pagou R$:{} de INSS. '.format(inss))
print ('Você pagou R$: {} ao sindicato'.format(sind))
print ('Seu salário líquido é de R$: {}'.format(l))