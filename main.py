import re
import longresponses as long

def message_probabity(user_message, recognised_words, single_response=False, required_words=[]):
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
        return int(percentage*100)
    else:
        return 0

def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words,single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probabity(message, list_of_words, single_response, required_words)

    #response ----------------------------------------------------------------------
    response("Hallo! Waarmee kan ik u helpen?",["hallo","hoi","he","hi","probleem"], single_response=True)
    response("De gemiddelde contributie voor een hockeyclub is 279 euro per jaar!",["geld","kosten","contributie"], required_words=["contributie"])
    response("Graaggedaan! Mocht u nog vragen hebben kunt u ze altijd stellen!",["bedankt","dank","klaar","thanks","tnx"], single_response=True)
    response("Dit is de club van Daan en Hidde! Welkom!", ["club", "daan", "hidde", "team"], single_response=True)
    response("De club is geheel rookvrij!", ["rookvrij", "roken"], single_response=True)
    response("Van welk team wil je deze informatie weten?", ["training", "hoelaat", "wedstrijd"], single_response=True)
    response("De jA1 traint van 19.00u-20.30u op maandag en hebben zaterdag een wedstrijd om 14.45u", ["a1", "ja1", "jongens a1"], single_response=True)
    response("De jB1 traint van 18.00u-19.30u op woensdag en hebben zaterdag een wedstrijd om 11.15u", ["b1", "jb1", "jongens b1"], single_response=True)
    response("De jC1 traint van 17.30u-19.00u op donderdag en hebben zaterdag een wedstrijd om 13.00u", ["c1", "jc1", "jongens c1"], single_response=True)
    response("De mA1 traint van 19.00u-20.30u op maandag en hebben zaterdag een wedstrijd om 16.00u", ["ma1", "meisjes a1"], single_response=True)
    response("De mB1 traint van 16.00u-18.00u op vrijdag en hebben zaterdag een wedstrijd om 9.00u", ["mb1", "meisjes b1"], single_response=True)
    response("De mC1 traint van 15.00u-17.00u op dinsdag en hebben zaterdag een wedstrijd om 11.00u", ["mc1", "meisjes c1"], single_response=True)
    response("Fijne training & wedstrijd! :-)", ["aanwezig", "ik ben er","erbij","Tot dan!"], single_response=True)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#testen antwoorden chatbot
while True:
    print('Bot: ' + get_response(input('You: ')))
