"""

#Criando Referência de Classes
#Para instanciar o objeto de uma classe para outra, devemos criar a referência da classe que será instanciada.

class Main:
    pass 	#A classe Main não possui atributos. Utilizamos apenas a palavra reservada pass.

#print("Testando o projeto")

from Cliente import Cliente
#Adicionamos a linha de código correspondente à importação da classe.
#A palavra reservada from é utilizada para indicar qual classe será importada...
#e a palavra reservada import é a referência de qual classe será utilizada para a criação de objetos em um arquivo à parte.


#Após criarmos a referência da classe, adicionamos, na linha seguinte, o novo objeto, passando por parâmetro os valores para inicialização dos atributos.
class Main:
    pass

#print("Testando o projeto")

from Cliente import Cliente

c1 = Cliente("João", "114444-2222")
#c1 = A declaração de um novo objeto funciona como declarar uma nova variável.
#Cliente =  Passamos o nome da classe que será instanciada.
#Passamos todos os atributos criados no Método Construtor da classe Cliente. 'self.nome' e 'self.telefone'

#----------

#Testando o Projeto
#Para verificarmos a prática de instanciar objetos, vamos acrescentar os comandos para impressão e, em seguida, compilar o nosso código.
class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

c1 = Cliente("João", "114444-2222")
print(c1)
print(c1.nome, " e ", c1.telefone)
#A primeira linha imprime a referência do objeto (id). Já a segunda linha imprime o conteúdo adicionado.

#Será apresentado o ID do objeto = <Cliente.Cliente object at 0x0000013677682FD0>
#E será exibido o conteúdo do objeto = João  e  114444-2222

#---------------------

"""

#Importando dados da classe/arquivo Conta
class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente
from Conta import Conta #importando da classe/arquivo Conta

c1 = Cliente("João", "114444-2222")
conta = Conta(c1.nome, 6565, 0)

print(conta.titular, "Numero: ", conta.numero, "Seu Saldo: ", conta.saldo)

#Observe que, ao compilar o projeto (por meio da classe Main), as informações são impressas e a informação relacionada ao titular é trazida do objeto Cliente:
#Testando o projeto
#"Joao Numero: 6565 Seu Saldo: 0
