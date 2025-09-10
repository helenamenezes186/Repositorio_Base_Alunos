# cri um codigo python que peça o valor da conta. Se for maior que RS 100,00
# adicione uma gorjeta de 10% e exiba o total a pagar
#caso contrario adicioneuma gorjeta de 5%

#etapas para resoluçao
#1) solicitar o valor da conta para o usuario
#2) seva conta for maior que100 adicionar 10% de gorjeta e apresentar o total a pagar
#3) se a conta for menor que100 adicionar 5% de gorjeta e apresentar  total a pagar

conta= float(input("digite o valor da conta RS: "))
if conta>= 100:
    conta_final= conta*1.1
    print(f'obrigadapor su visita, sua conta é RS {conta_final:.2f}. ')