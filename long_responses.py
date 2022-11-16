import random

R_ADVICE = "Não posso escolher por você"


def unknown():
    response = ["Não entendi, ainda não consigo responder está pergunta ",
                "Por favor, reformule a pergunta",
                "Qual é, não entendi"][
        random.randrange(3)]
    return response
