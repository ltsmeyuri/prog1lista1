s = float(input('Insira o quanto voc� ganha por hora: '))
h = int(input('Insira o n�mero de horas trabalhadas no m�s: '))
b = s*h
ir = b*(11/100)
inss = b *(8/100)
sind = b *(5/100)
l = b - ir - inss - sind
print ('Seu sal�rio bruto � de R$: {}'.format(b))
print ('Voc� pagou R$:{} de INSS. '.format(inss))
print ('Voc� pagou R$: {} ao sindicato'.format(sind))
print ('Seu sal�rio l�quido � de R$: {}'.format(l))