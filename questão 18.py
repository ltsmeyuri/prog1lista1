t = float(input('Insira, em MB, o tamanho do arquivo para download: '))
v = float(input('Insira a velocidade de internet, em Mbps: '))
ta= t/(v/60)
print ('O tempo de download � de, aproximadamente, {} Mbpm'.format(ta))
