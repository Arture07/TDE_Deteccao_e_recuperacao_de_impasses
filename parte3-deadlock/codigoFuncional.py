#Pseudocódigo de referência (versão corrigida — hierarquia  
""""

Regra global: sempre adquirir LOCK_A antes de LOCK_B, em TODAS as threads.

Thread 1 e Thread 2:
    adquirir(LOCK_A)
        adquirir(LOCK_B)
            // secao critica
        liberar(LOCK_B)
    liberar(LOCK_A)

"""

import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread_1():
    print("Thread 1:")
    print()
    time.sleep(0.5)
    
    LOCK_A.acquire()
    print("Adquirindo lock A - 1")
    time.sleep(0.5)
    
    LOCK_B.acquire()
    print("Adquirindo lock B - 1")
    time.sleep(0.5)

    print("Executando código critico - 1")
    time.sleep(0.5)
    
    LOCK_B.release()
    print("liberando lock B - 1")
    time.sleep(0.5)

    LOCK_A.release()
    print("liberando lock A - 1")
    time.sleep(0.5)

def thread_2():
    print("Thread 2:")
    print()
    time.sleep(0.5)

    LOCK_A.acquire()
    print("Adquirindo lock A - 2")
    time.sleep(0.5)

    LOCK_B.acquire()
    print("Adquirindo lock B - 2")
    time.sleep(0.5)

    print("Executando código critico - 2")
    time.sleep(0.5)
    
    LOCK_B.release()
    print("liberando lock B - 2")
    time.sleep(0.5)

    LOCK_A.release()
    print("liberando lock A - 2")
    time.sleep(0.5)


thread_1 = threading.Thread(target=thread_1)
thread_2 = threading.Thread(target=thread_2)

thread_1.start()
thread_2.start()


thread_1.join()
thread_2.join()
print("Chegou aqui?")