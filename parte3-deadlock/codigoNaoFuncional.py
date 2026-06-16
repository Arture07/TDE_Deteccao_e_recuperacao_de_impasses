#Pseudocódigo de referência (versão que trava)

""""

LOCK_A, LOCK_B = locks distintos

Thread 1:
    adquirir(LOCK_A)
        dormir(50ms) // aumenta a chance do deadlock
        adquirir(LOCK_B)
            imprimir "T1 concluiu"
        liberar(LOCK_B)
    liberar(LOCK_A)


Thread 2:
    adquirir(LOCK_B)
        dormir(50ms)
        adquirir(LOCK_A)
            imprimir "T2 concluiu"
        liberar(LOCK_A)
    liberar(LOCK_B) 

"""
import threading
import time

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()

def thread_1():
    print("Thread 1:")
    print()

    LOCK_A.acquire()
    print("Adquirindo lock A")
    time.sleep(0.5)

    LOCK_B.acquire()
    print("Adquirindo lock B")
    

    print("T1 concluiu")

    LOCK_B.release()
    LOCK_A.release()
    print("liberando locks")


def thread_2():
    print("Thread 2:")
    print()

    LOCK_B.acquire()
    print("Adquirindo lock B")
    time.sleep(0.5)

    LOCK_A.acquire()
    print("Adquirindo lock A")
    

    print("T2 concluiu")

    LOCK_A.release()
    LOCK_B.release()
    print("liberando locks")

thread_1 = threading.Thread(target=thread_1)
thread_2 = threading.Thread(target=thread_2)

thread_1.start()
thread_2.start()


thread_1.join()
thread_2.join()
print("Chegou aqui?")