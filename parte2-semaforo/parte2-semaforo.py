import threading
import time

num_threads = 8
repeticoes = 200000
total = 0

def rodar_teste(com_semaforo):
    global total
    total = 0
    semaforo = threading.Semaphore(1)

    def contar():
        global total
        for i in range(repeticoes):
            if com_semaforo:
                semaforo.acquire()
                try:
                    total += 1
                finally:
                    semaforo.release()
            else:
                valor_atual = total
                time.sleep(0) # força preferência por conta de processadores mais rapidos e por causa do GIL
                total = valor_atual + 1

    threads = []
    inicio = time.time()

    for i in range(num_threads):
        t = threading.Thread(target=contar)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    fim = time.time()
    return total, (fim - inicio)

total_esperado = num_threads * repeticoes

print(f"Configuração: {num_threads} threads, {repeticoes} repetições.")
print(f"Resultado esperado: {total_esperado}\n")

print("--- Teste SEM Semáforo ---")
for i in range(3):
    resultado, duracao = rodar_teste(False)
    perdas = total_esperado - resultado
    print(f"Rodada {i+1} -> Obtido: {resultado} | Perdas: {perdas} | Tempo: {duracao:.4f}s")

print("\n--- Teste COM Semáforo ---")
for i in range(3):
    resultado, duracao = rodar_teste(True)
    perdas = total_esperado - resultado
    print(f"Rodada {i+1} -> Obtido: {resultado} | Perdas: {perdas} | Tempo: {duracao:.4f}s")