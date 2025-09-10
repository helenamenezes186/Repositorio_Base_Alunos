# cri um codigo receba 3 notas, calcule a média e informe se o aluno está aprovado, em recuperação ou reprovado

# OBS: aprovado media>= 7
# recuperaçao media> 4

#ETAPAS
#1) solicitar as notas ao usuario
n1= float(input("digite a primeira nota: "))
n2= float(input("digite a segunda nota: "))
n3= float(input("digite a terceira nota: "))
#2) calcular a media
media = (n1 + n2 + n3) / 3
# 3) checar a condiçao do aluno
if media >= 7:
     print(f"o aluno tem media {media} e esta aprovado.")
elif media > 4:
    print("o aluno teve media {media:.2f} e esta reprovado")
else:
    print(f"o aluno teve media {media:.2f} e esta reprovado")
