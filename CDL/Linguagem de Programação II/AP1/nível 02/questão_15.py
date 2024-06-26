# Gabriel Magalhães Dias
# Questão 15 – (0,75 pontos)
# Desenvolva um gerador de tabuada, capaz de  gerar a tabuada de qualquer número inteiro
# entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve
# ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50.

multiplicando = 0
while (multiplicando <= 0) or (multiplicando > 10):  # forçando o laço a executar apenas com a entrada entre 1-10
    multiplicando = int(input("Digite um multiplicando entre 1 e 10 para ver a sua tabuada: "))
    multiplicador = 1

    if (multiplicando > 0) and (multiplicando <= 10):
        print(f"TABUADA DE {multiplicando}".center(20, "="))
        while multiplicador <= 10:
            produto = multiplicando * multiplicador
            print(f"{multiplicando} x {multiplicador} = {produto}")
            multiplicador += 1
    else:
        print("O multiplicando inserido é inválido! Por favor, escolha um número de 1 a 10.")
