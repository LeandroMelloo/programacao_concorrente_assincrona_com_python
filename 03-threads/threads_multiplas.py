import threading  # 1° Passo
import time
from concurrent.futures import thread


def main():
    threads = [
        # 2° Passo - instânciando varias threadings
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('moeda', 23)),
        threading.Thread(target=contar, args=('pato', 12))
    ] 

    [th.start() for th in threads] # 3° Passo - adiciona a nossa thread na pool de threads prontas para execução, a função start() não inicia o processo, ele fala pro processo python que tem uma thread pronta.

    print('Podemos fazer outras coisas no programa enquanto a thread vai executando...')
    print('Animal ' * 2)

    [th.join() for th in threads] # 4° Passo - avisa para ficar aguardando aqui até a thread terminar a execução

    print('Pronto!')


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
