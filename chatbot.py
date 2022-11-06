
from signal import pause


def chatbot():
    while True:
        print("-=" * 10)
        print("""
        OPÇÕES ESCOLHA UMA!
        [1] - VER QUARTOS
        [2] - VER PREÇOS
        [3] - RESERVAR QUARTO
        [4] - SAIR DO CHAT
        """)
        quartos = ["Quarto de solteiro", "Quarto de casal",  "Suíte Master"]
        preco = ["Quarto de solteiro ------ R$50", "Quarto de casal ------ R$100", "Suíte Master ------- R$200"]

        escolha = str(input("Digite sua escolha "))

        if escolha == "1":
            print("-=" * 10)
            for item in quartos:
                print(item)
            print("-=" * 10)
        elif escolha == "2":
            print("-=" * 10)
            for item in preco:
                print(item)
            print("-=" * 10)
        elif escolha == "3":
            print("-=" * 10)
            clienteReserva = str(input("Digite S para sim e N para não sua escolha").lower().strip())
            if clienteReserva == "s":
                print("OK, Reserva realizada")
                break
            else:
                print("OK, nenhuma reserva feita")
        elif escolha == "4":
            break
        else:
            print("-=" * 10)
            print("Digite uma opção válida")
            print("-=" * 10)

chatbot()
print("-=" * 10)
print("Obrigado pro utilizar nosso serviço")
print("-=" * 10)




