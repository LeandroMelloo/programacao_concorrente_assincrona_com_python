import threading  # 1° Passo
import time


def main():
    th = threading.Thread(target=contar, args=('elefante', 10)) # 2° Passo - instânciando uma threading

    th.start() # 3° Passo - adiciona a nossa thread na pool de threads prontas para execução, a função start() não inicia o processo, ele fala pro processo python que tem uma thread pronta.

    print('Podemos fazer outras coisas no programa enquanto a thread vai executando...')
    print('Animal ' * 2)

    th.join() # 4° Passo - avisa para ficar aguardando aqui até a thread terminar a execução

    print('Pronto!')


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
