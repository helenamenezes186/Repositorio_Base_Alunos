#solicite ao usuario 4 notas.
#calcule a media
#informe se o aluno esta aprovado (media>=7), recuperação(5<media<7) ou reprovado.
#apresente as notas que o aluno tirou, a media e o status de sua situação

#lista
#for
#if/elif/else

notas=[]
for i in range(4):
    nota=float(input(f'informe a nota da prova {i+1}: '))
    if nota>0:
        notas.append(nota)
    else:
        print('valor invalido.')
print(f'suas notas são>:{notas}')
media= sum(notas)/len(notas)

if media >7:
    print(f'suas notas foram {notas}, sua {media:.2f} e voce esta aprovado')
elif 5<= media<7:
    print(f'suas notas foram {notas}, sua {media:.2f} e voce esta de recuperaçao')
else:
    print(f'suas notas foram {notas}, sua {media:.2f} e voce esta de reprovado')
