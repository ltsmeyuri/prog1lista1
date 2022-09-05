p = float(input('Insira, em quilogramas, o "peso" do peixe: '))
if p>50:
    print('O pescador deve pagar R$ {} de multa por ter excedido o limite legal de Kg de peixe.'.format(round(p-50,2)))
else:
    print('O pescador não pagará multa.')