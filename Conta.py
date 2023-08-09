"""

#Iniciar um projeto de controle bancário!

#O objetivo do projeto é o desenvolvimento orientado a objetos para a execução de tarefas do cotidiano bancário, como saque, consulta de saldo e depósito.
#Durante esta aula, já desenvolvemos a classe Cliente e seus atributos. Agora, vamos desenvolver a classe Conta, que será definida recebendo o objeto Cliente, além dos atributos “número” e “saldo”.

class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 100000
        self.numero = numero
        self.titular = titular

#Para verificar o funcionamento do projeto até o momento, modifique a classe Main, trazendo os dois objetos criados:


#---------------

#Na prática, em Python (diferentemente da linguagem Java), o “_” (underline) antes do atributo não impede o acesso dele em outra classe, ou seja, ele não fica privado.
#Essa forma é somente um indicativo de que os métodos nos quais os nomes iniciam com “_” (underline) não devem (mas podem) ser acessados.
#Alterando a Classe Conta
#Para o atributo saldo não ser negativo, a utilização do método setter é justificável, ficando do seguinte modo:
class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

        def get_saldo(self):
            return self._saldo

        def set_saldo(self, saldo):
            if (saldo < 0):
                print("O saldo não pode ser negativo!")
            else:
                self._saldo = saldo

#---------------

"""
#@PROPERTY
#A linguagem Python traz uma outra solução para manter os atributos privados, conhecida como Property.
#A função Property é um Decorator e é utilizada para obter um valor de um atributo.
#Basicamente, a função Property permite que você declare uma função para obter o valor de um atributo.
#Na prática
#Podemos alterar a classe Conta utilizando Property da seguinte forma:
class Conta:
    def __init__(self, titular, numero, saldo):
        self._saldo = 0
        self._numero = numero
        self._titular = titular
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if (saldo < 0):
            print("O saldo não pode ser negativo!")
        else:
            self._saldo = saldo
