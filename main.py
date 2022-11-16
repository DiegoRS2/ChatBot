import re
import long_responses as long


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognised_words))

    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    response('Olá em que posso ajudar', ['olá', 'oi', 'ei', 'opa'], single_response=False)
    response('Bom dia, como posso te ajudar', ['Bom', 'dia',], single_response=True)
    response('Bom Tarde, como posso te ajudar', ['Boa', 'tarde',], single_response=True)
    response('Bom noite, como posso te ajudar', ['Boa', 'noite',], single_response=True)
    response('Vou bem', ['como', 'vai', 'você'])
    response('Os valores das nossas acomodações são: \n Quato de solteiro: R$ 50,00 \n Quarto de casal: R$ 100,00\n Suíte: R$ 150,00 \n Suíte premium com hidro: R$ 200,00', ['Gostaria', 'de', 'saber', 'os', 'valores', 'dos', 'quartos', 'acomodações', 'preço'], single_response=True)
    response('Foi um prazer ajudar', ['ok', 'já é', 'obrigado', 'só', 'isso'])
    response('Verificando se já vagas ... Quarto agendado com sucesso!', ['queria', 'agendar', 'reservar', 'um', 'quarto', 'acomodação', 'suíte', 'suíte premium', 'gostaria'])

    response(long.R_ADVICE, ['qualque', 'coisa', 'escolhe', 'pra', 'eu'])
    
    best_match = max(highest_prob_list, key=highest_prob_list.get)
 

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

while True:
    print('Connie: ' + get_response(input('Você: ')))
