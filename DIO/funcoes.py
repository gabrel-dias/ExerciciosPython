# a palavra reservada "def" serve como um identificador para o interpretador saber que aquela declaração se trata de
# uma função
def ola_funcao():
    print("olá, função!")


def ola_pessoa():
    nome = input("Digite o seu nome: ")
    # um método que receberá uma variável a ser atribuída no parâmetro
    print(f"Olá, {nome.capitalize()}, meu amigo(a)")


def ola_pessoa2(nome="Anônimo"):
    # se a variável do parâmetro for previamente atribuída, é opcional passar um parâmetro na chamada do método,
    # mas este sempre receberá o valor atribuído previamente
    print(f"Olá, {nome.capitalize()}, meu amigo(a)")


ola_funcao()
# ola_pessoa()
ola_pessoa2("teste".capitalize())


def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    # o retorno é uma tupla
    return antecessor, sucessor


print(antecessor_sucessor(10))  # como o método tem um "return" atribuído, ele precisa ser chamado dentro do print,


# do contrário, a saída será "none", já que não existe um valor atribuído"


def soma_numeros(numeros):
    return sum(numeros)  # sum() retorna 0 mais a soma dos elementos de um iterável, nesse caso é usado uma lista


print(soma_numeros([1, 2, 3, 4, 5]))


def func3():
    print("olá mudo!")  # quando uma função em Python não tem a instrução return, ela retorna None por padrão.


print(func3())


def salvar_carro(marca, modelo, ano, placa):
    print(f"carro inserido : {marca}, {modelo}, {ano}, {placa}")


# sintaxe porca que permite dados de qualquer tipo serem inseridos sem nenhuma restrição

# argumentos nomeados
salvar_carro("fiat", "palio", 1999, "ABC-1234")
salvar_carro(placa="abc-1234", marca="fiat", ano=1999, modelo="palio")
salvar_carro(**{"marca": "fiat", "modelo": "palio", "ano": 1999, "placa": "ABC-4321"})

# args e kwargs é possível combinar parâmetros obrigatórios com args e kwargs. quando esses são definidos (*args e
# **kwargs), o método recebe os valores como tupla e dicionário respectivamente (?????????)
