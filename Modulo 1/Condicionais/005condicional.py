# crie um codigo python que verifique se a senha digitada pelo usuario
#  for "1234", exiba "acesso permitido"

#etapas para resolução
#criar uma variavel e a atribuir a ela uma senha
#atraves de um input solicitar a senha ao usuario
#atraves da condicional checar se a senha é igual a sennha armazenada
#liberar ou nao omacesso ao usuario

senha_usuario="1234"
senha= input("digite sua senha: ")
if senha == senha_usuario:
    print("acesso liberado bb")
else:
    print("acesso negado, tente novamente bb")