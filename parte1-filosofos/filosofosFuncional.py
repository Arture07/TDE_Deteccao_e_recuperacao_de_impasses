
# N = 5 filósofos
# Garfos 0..N-1 (garfo i fica entre filósofos i e (i+1) mod N)
# Para cada filósofo p:
#   left  = min(garfo_esquerda(p), garfo_direita(p))   <- compara pelo indc do garfo
#   right = max(garfo_esquerda(p), garfo_direita(p))
# Loop:
#   pensar()
#   estado[p] <- "com fome"
#   adquirir(left)   // bloqueia até o garfo estar livre
#   adquirir(right)  // bloqueia até o garfo estar livre
#   estado[p] <- "comendo"
#   comer()
#   liberar(right)
#   liberar(left)
#   estado[p] <- "pensando"
#


from random import uniform
from time import sleep
from threading import Thread, Lock

nomes = ['Maquiavel', 'Kant', 'Sartre', 'Nietzsche', 'Dostoiévski']
N = len(nomes)
pratos = [0] * N
estado = ["pensando"] * N  # estado[p]: pensando  com fome  comendo


class Filosofo(Thread):
    exe = True  # variavel de execucao 

    def __init__(self, indc, nome, indcE, garfoE, indcD, garfoD):
        Thread.__init__(self)
        self.indc = indc
        self.nome = nome
        self.indcE = indcE
        self.garfoE = garfoE
        self.indcD = indcD
        self.garfoD = garfoD

    def run(self):
        while self.exe:
            estado[self.indc] = "pensando"
            print(f"\n {self.nome} está pensando")
            sleep(uniform(5, 15))
            self.comer()

    def comer(self):
        if self.indcE < self.indcD:
            indc_left, garfo_left = self.indcE, self.garfoE
            indc_right, garfo_right = self.indcD, self.garfoD
        else:
            indc_left, garfo_left = self.indcD, self.garfoD
            indc_right, garfo_right = self.indcE, self.garfoE

        estado[self.indc] = "com fome"
        print(f"\n {self.nome} ta com fome (vai pedir garfo {indc_left} antes do {indc_right})")

        garfo_left.acquire()   # sempre o de menor índice primeiro
        garfo_right.acquire()  # depois o de maior índice

        estado[self.indc] = "comendo"
        print(f"\n {self.nome} ta comendo")
        sleep(uniform(5, 10))
        print(f"\n {self.nome} parou de comer e ta pensando")
        pratos[self.indc] += 1
        print(pratos)
        
        garfo_right.release()
        garfo_left.release()


if __name__ == "__main__":
    garfos = [Lock() for _ in range(N)]

    for janta in range(50):
        Filosofo.exe = True
        mesa = [
            Filosofo(i, nomes[i], i, garfos[i], (i + 1) % N, garfos[(i + 1) % N])
            for i in range(N)
        ]

        for filosofo in mesa:
            filosofo.start()
            sleep(2)

        sleep(uniform(5, 15))
        Filosofo.exe = False
        print(f"\n--- fim da janta {janta + 1} ---")
