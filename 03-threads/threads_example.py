import threading


def start_threading(param):
    print('Executa algo....')
    print(f'Utiliza o parâmetro recebido: {param}')

    return print(f'Resultado final: {param * param}')

th = threading.Thread(target=start_threading, args=(5,))

th.start()
th.join()
