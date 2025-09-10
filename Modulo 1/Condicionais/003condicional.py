#criar um codigo python que indique se a temperatura esta agradavel ou nao
#condiçoes
#temperatura>=30 informar que esta muito quente
#temperatura>=20 informar que a temperatura esta agradavel
#temperatura>=10 informar que esta frio
#temperatura abaixo de 20 informar que esta muito frio

#etapas para resoluçao:
# 1) solicitar a temperatura para o usuario
#2) verificar a condicional
#3) inprimir a resposta segundo a temperatura

temperatura =float(input("digite a temperatura do dia:"))

# if condiçao:
#bloco de codigo a ser executado
# elif condiçao:
# bloco de codigo a  ser executado
#else
#bloco de codigo a ser executado

if temperatura>=30:
    print(f"a temperatura do dia e {temperatura} °C e o dia está muito quente")
elif temperatura >=20:
    print(f"a temperatura do dia e {temperatura} °C e o dia está muito agradavel.:")
if temperatura>=10:
    print(f"a temperatura do dia e {temperatura} °C e o dia está bem frio.:")