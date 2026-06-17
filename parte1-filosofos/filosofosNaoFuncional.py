# Cada filósofo pega sempre o garfo da "esquerda" e depois o
# da "direita", na ordem da mesa.

# Como essa ordem depende da posição na mesa (e não de um índice),
# é possível que todos peguem seu primeiro garfo ao mesmo tempo e fiquem
# bloqueados esperando o segundo, que está nas mãos do vizinho.
# Isso forma a espera circular (deadlock).
#
# As 4 condições de Coffman estão aqui:
#   - exclusão mútua (Lock)
#   - posse-e-espera (segura garfoE enquanto espera garfoD)
#   - sem preempção (acquire nunca tira o lock de outra thread)
#   - espera circular (possível dado o arranjo em anel dos garfos)

from random import uniform
from time import sleep
from threading import Thread, Lock

nomes = ['Maquiavel', 'Kant', 'Sartre', 'Nietzsche', 'Dostoiévski']
N = len(nomes)
pratos = [0] * N
estado = ["pensando"] * N  # estado[p]: pensando  com fome e comendo


class Filosofo(Thread):
    exe = True  # variavel de execucao

    def __init__(self, indc, nome, garfoE, garfoD):
        Thread.__init__(self)
        self.indc = indc
        self.nome = nome
        self.garfoE = garfoE
        self.garfoD = garfoD

    def run(self):
        while self.exe:
            estado[self.indc] = "pensando"
            print(f"\n {self.nome} está pensando")
            sleep(uniform(5, 15))
            self.comer()

    def comer(self):
        estado[self.indc] = "com fome"
        print(f"\n {self.nome} ta com fome")

        self.garfoE.acquire()  # bloqueia até conseguir o garfo da esquerda
        self.garfoD.acquire()  # bloqueia até conseguir o garfo da direita

        estado[self.indc] = "comendo"
        print(f"\n {self.nome} ta comendo")
        sleep(uniform(5, 10))
        print(f"\n {self.nome} parou de comer e ta pensando")
        pratos[self.indc] += 1
        print(pratos)

        self.garfoD.release()
        self.garfoE.release()


if __name__ == "__main__":
    garfos = [Lock() for _ in range(N)]

    for rodada in range(50):
        Filosofo.exe = True
        mesa = [Filosofo(i, nomes[i], garfos[i], garfos[(i + 1) % N]) for i in range(N)]

        for filosofo in mesa:
            filosofo.start()
            sleep(2)

        sleep(uniform(5, 15))
        Filosofo.exe = False
        print(f"\n--- fim da rodada {rodada + 1} (se travar aqui, é deadlock :( )) ---")
