"""

#Criando classes no projeto

#1 - Crie o arquivo .py

#2 - Classe:
#Sempre iniciar as classes com caracteres maiúsculos, inclusive as iniciais de nomes compostos:
#Exemplo: MinhaClasse()
class Cliente:
    pass
#Utilizamos a palavra reservada pass, quando nenhuma estrutura será definida no corpo dessa classe.


#-----------

#Inserindo o Método Construtor na Classe Cliente
class Cliente:
    def __init__(self):
        pass

#A palavra def é utilizada para a declaração de método.
#Para definir o construtor adicionamos: underline, underline, a palavra reservada init, underline, underline. O init() é um método especial que será chamado sempre que criarmos um objeto da classe.
#Incluímos o parâmetro obrigatório self, que está presente em todos os métodos. Resumidamente, podemos afirmar que o parâmetro self, neste momento, exporta as características do objeto.
#Para finalizar, adicionamos dois pontos (:)

#-----------

#atributos de uma classe representam as características que ela possui.
#Para adicionar atributos a uma classe, basta definir o nome do atributo acompanhado da palavra reservada self, no método especial denominado _ _init_ _ do Método Construtor.
#O Método Construtor tem a finalidade de estabelecer os valores obrigatórios para construção de um novo objeto.
#Primeiramente, remova a palavra reservada pass.
#Em seguida, insira o código correspondente aos atributos.
class Cliente:
    def __init__(self):

        self.nome
        self.telefone

#Com o parâmetro self são passados os parâmetros que serão utilizados para inicialização dos atributos.
#Inicializamos os atributos com os valores passados por parâmetro.

class Cliente:
    def __init__(self, n, fone):

        self.nome = n
        self.telefone = fone

#--------------
#Instanciando Objetos
#Na linguagem Python, as classes são utilizadas para definição dos objetos.
#Podemos afirmar que a classe é o nosso código e, para que esse código seja utilizado, precisamos criar os objetos, assim, criamos instâncias do objeto.
#Na orientação a objetos, instância e objetos são sinônimos.

#class Learning:
#    def __init__(self, name, age, gender):
#        self.title = learn
#        self.subtitle = python
#        self.paragraph = everyday

#Programmer = Learning("learn", "python", "everyday")
#print Sue
#__main__.Programmer instance at 0x32111320
#print Programmer.subtitle #= python

#-------------

#Na linguagem Python, todo objeto criado possui um código de identificação composto por um número inteiro não negativo, conhecido como ID.
#Assim, as instâncias de objetos são diferenciadas.
#Esse ID diferencia objeto e atributos deste objeto.

#--------------------------------


#ENCAPSULAMENTO DE DADOS

#O conceito de encapsulamento traz o isolamento do código, ou seja, variáveis e funções que são utilizadas internamente não devem estar disponíveis externamente.
#Para a implementação do encapsulamento é fundamental alterarmos a visibilidade dos atributos de uma classe. Para isso, utilizamos os modificadores de acesso.
#A linguagem Python utiliza o símbolo underscore ”_”.
#Dentro da orientação a objetos temos os modificadores Public, Protected e Private.
#Public: É o mais comum entre os modificadores. Ele permite acesso tanto de dentro, quanto de fora de uma classe. Sua implementação se dá por meio do uso do underline ”_” na frente do nome.
#Protected: Utilizando o modificador protegido, somente suas classes e subclasses terão acesso ao atributo ou método. Para sua implementação adicione um underline ”_” antes do nome.
#Private: É o modificador mais restrito do desenvolvimento orientado a objetos. Ele permite que somente a sua classe (onde foi definido) tenha acesso a um determinado atributo ou método. Para definir o método private adicionamos underline duplo ”__” na frente do nome.

#-
#Na prática - Modificando os Atributos
#Para iniciar o processo de encapsulamento, vamos modificar os atributos das classes já criadas de forma que fiquem privados. Vamos iniciar pela classe Cliente.
class Cliente:
    def __init__(self, n, fone):

        self._nome = n
        self._telefone = fone

#Observe que foi adicionado o símbolo underline (_) antes da definição do nome do atributo.

#-----

#Métodos de Acesso (Get e Set)
#Para permitir o acesso aos atributos de forma controlada, a prática mais comum é a utilização de dois métodos de acesso: um retornando valor e outro que muda valor.
#Get: Sempre retornam valores. O método Get é utilizado para ler os valores internos do objeto e enviá-los como valor de retorno da função.
#get_nome do atributo()
#Exemplo: 
get_idade(self):return self._idade

#Set: Recebem valores por parâmetros. Os métodos Set recebem argumentos que serão atribuídos a membros internos do objeto.
	#Exemplo:
#set_nome do atributo (valor por parâmetro)
##Exemplo: 
#def set_idade(self, valor):
#self.idade=valor


#-----

"""

#Dando continuidade ao processo de encapsulamento, vamos desenvolver os métodos de acesso nas classes já criadas. Assim, vamos acessar os atributos privados. Vamos iniciar pela classe Cliente.
class Cliente:
    def __init__(self, n, fone):

        self._nome = n
        self._telefone = fone

#método get
def get_nome(self):
    return self._nome

#método set
def set_nome(self, nome):
    self._nome = nome













