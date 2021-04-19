# Linguagens de programação
#
# Terceiro Trabalho
#
# Luan B. J. Freire - 218060074

from lib.classe_pilha import Pilha

##### h) #####
def main():
    objeto = Pilha()
    objeto.Push('10')
    objeto.Push(20)
    objeto.Push(30)
    objeto.Pop_var(2)
    objeto.Top()
    objeto.Empty()
