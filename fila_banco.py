#gerenciamento de fila de banco
import array as ar
import time
# fila = ar.array('u')


class cliente():
    def __init__(self):
        # self.fila = ar.array('s') fazer com array
        self.fila = []

    def adicionar_cliente_fila(self):
        nome = input("Nome Cliente: ")
        prioritario = input("Cliente Prioritario? 'S' / 'N': ").lower()
        if prioritario == 's':
            self.fila.insert(0, nome)
        else:
            self.fila.append(nome)

    def atender_cliente(self):
        try:
            atendido = self.fila.pop(0)

        except IndexError:
            print(f"Não a cliente em fila para ser atendido! ")
        else:
            print(f"\nCliente {atendido.upper()} atendido! \n")
            self.visualizar_fila()

    def visualizar_fila(self):
        if not self.fila:
            print("Fila Vazia! ")
        else:
            print("Clientes para serem atendidos! ")
            position = 1
            for cliente in self.fila:
                print(f"\t {position}. {cliente}")
                position += 1
        time.sleep(1)

    def remover_da_fila_cliente(self):
        self.visualizar_fila()
        if self.fila:
            remover = int(
                input("Qual deseja remover da fila? Digite numeração: "))
            removido = self.fila.pop(remover-1)
            print(f"\nCliente {removido}  foi removido da fila! \n")


Banco = cliente()

while True:
    print("\n" +
          "1. Adicionar cliente à fila: \n" +
          "2. Atender próximo cliente: \n" +
          "3. Visualizar fila: \n" +
          "4. Remover Cliente da fila: \n" +
          "5. Sair do programa: \n"
          )

    opcao = input("\t Digite o numero correspondente: ")
    if opcao == '1':
        Banco.adicionar_cliente_fila()

    elif opcao == '2':
        Banco.atender_cliente()

    elif opcao == '3':
        Banco.visualizar_fila()
    elif opcao == '4':
        Banco.remover_da_fila_cliente()
    elif opcao == '5':
        break
    else:
        print("\n\tOpção Invalida!\n")
