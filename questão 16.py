a = float(input('Insira, em metros quadrados, a �rea a ser pintada:'))
vol = round(a/3,2)
l = round(vol/18,0)
if ((vol//18) > 0):
    l = l+1
c = round(l*80,2)
print('A quantidade de latas a serem compradas � de {} e o pre�o total � de R$: {}.'.format(l, c))
