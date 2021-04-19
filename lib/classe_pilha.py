# Linguagens de programação
#
# Terceiro Trabalho
#
# Luan B. J. Freire - 218060074

class Pilha:
    ##### a) | b) #####
    def __init__(self):
        self.__TAM_MAX = 1000
        self.__valores = []
        self.__topo = -1

    ##### c) #####
    def Empty(self):
        if self.__topo == -1:
            return 'A pilha está vazia!'
        else:
            return 'A pilha não está vazia!'

    ##### d) | i) #####
    def Push(self, valor):
        self.__valores.append(int(valor))
        self.__topo+=1

    ##### e) #####
    def Pop(self):
        del(self.__valores[self.__topo])
        self.__topo-=1

    ##### f) | i) #####
    def Pop_var(self, numero):
        if int(numero) > self.__topo:
            self.__valores.clear()
            self.__topo = -1
        else:
            for i in range(int(numero)):
                del(self.__valores[self.__topo])
                self.__topo-=1

    ##### g) #####
    def Top(self):
        return self.__valores[self.__topo]