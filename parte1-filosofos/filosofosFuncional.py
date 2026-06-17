
from random import uniform
from time import sleep
from threading import Thread, Lock
pratos = [0, 0, 0, 0, 0]

class Filosofo(Thread):
    exe = True # variavel de execucao
    
    def __init__ (self, nome, garfoE, garfoD ):
        Thread.__init__(self)
        self.nome = nome
        self.garfoE= garfoE
        self.garfoD = garfoD
        
    def run(self):
        while self.exe:
            print(f"\n {self.nome} está pensando")
            sleep(uniform(5, 15))
            self.comer()
            
    def comer(self):
        garfo1, garfo2 = self.garfoE , self.garfoD
        
        while self.exe:
            garfo1.acquire(True) #tenta pegar o primeiro garfo, da esquerda
            locked = garfo2.acquire(False) # verifica se o segundo garfo ta livre
            if locked:
                break
            garfo1.release() #larga o garfo
        else:
            print(f"\n {self.nome} ta com fome")
            return
        print(f"\n {self.nome} ta comendo")
        sleep(uniform(5, 10))
        print(f"\n {self.nome} parou de comer e ta pensando")
        pratos[nomes.index(self.nome)] += 1 
        print(pratos)
        #larga os garfos
        garfo1.release()
        garfo2.release()
        
        
nomes = ['Maquiavel', 'Kant','Sartre','Nietzsche','Dostoiévski']
garfos = [Lock() for _ in range(5)]
        
mesa =[Filosofo(nomes[i], garfos[i % 5], garfos[(i + 1) % 5]) for i in range(5)]

for _ in range(50):
    Filosofo.exe = True #inicia a execucao
    for filosofo in mesa:
        try:
            filosofo.start()
            sleep(2)
        except RuntimeError:
            pass
    sleep(uniform(5, 15))
    Filosofo.exe = False