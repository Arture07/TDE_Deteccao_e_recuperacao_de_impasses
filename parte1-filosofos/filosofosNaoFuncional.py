# Dados:
# N = 5 filósofos
# Garfos 0..N-1 (garfo i fica entre filósofos i e (i+1) mod N)
# Para cada filósofo p:
# left = min(garfo_esquerda(p), garfo_direita(p))
# right = max(garfo_esquerda(p), garfo_direita(p))
# Loop:
# pensar()
# estado[p] <- "com fome"
# adquirir(left) // bloqueia até o garfo estar livre
# adquirir(right) // bloqueia até o garfo estar livre
# estado[p] <- "comendo"
# comer()
# liberar(right)
# liberar(left)
# estado[p] <- "pensando"

#logica de exemplo


from random import uniform
from time import sleep
from threading import Thread, Lock

pratos = [0, 0, 0, 0, 0]

class Filosofo(Thread):
    exe = True  # variavel de execucao

    def __init__(self, nome, garfoE, garfoD):
        Thread.__init__(self)
        self.nome = nome
        self.garfoE = garfoE
        self.garfoD = garfoD

    def run(self):
        while self.exe:
            print(f"\n {self.nome} está pensando")
            sleep(uniform(5, 15))
            self.comer()

    def comer(self):
        garfo1, garfo2 = self.garfoE, self.garfoD

        print(f"\n {self.nome} ta com fome")
        garfo1.acquire()  # bloqueia até conseguir o garfo da esquerda
        garfo2.acquire()  # bloqueia até conseguir o garfo da direita

        print(f"\n {self.nome} ta comendo")
        sleep(uniform(5, 10))
        print(f"\n {self.nome} parou de comer e ta pensando")
        pratos[nomes.index(self.nome)] += 1
        print(pratos)

        # larga os garfos
        garfo1.release()
        garfo2.release()


nomes = ['Maquiavel', 'Kant', 'Sartre', 'Nietzsche', 'Dostoiévski']
garfos = [Lock() for _ in range(5)]

mesa = [Filosofo(nomes[i], garfos[i % 5], garfos[(i + 1) % 5]) for i in range(5)]
for _ in range(50):
    Filosofo.exe = True
    for filosofo in mesa:
        try:
            filosofo.start()
            sleep(2)
        except RuntimeError:
            pass
    sleep(uniform(5, 15))
    Filosofo.exe = False