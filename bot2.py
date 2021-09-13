import random

responses_hello = ['sup', 'yo', '...']
responses_bye = ['bye', 'bye-bye', 'goodbye']
questions_hello = ['hello','heya', 'morning']
questions_bye = ['bye', 'chao', 'tschuss']
failure_phrases = ['idk', ':(','i\'m a sad bot']

def filter_text(text):
    text = text.lower()
    deletechars = '.,:;*?!@<>\|/'
    for c in deletechars:
        text = text.replace (c, '')
    return text

def get_intent (question):
    question = filter_text(question)
    if question in questions_hello:
        intent = 'hello'
    elif question in questions_bye:
        intent = 'bye'
    else:
        intent = None
    return intent

def get_answer_by_intent (intent):
    if intent == 'hello':
        answer = random.choice(responses_hello)
    elif intent == 'bye':
        answer = random.choice(responses_bye)
    else:
        answer = random.choice(failure_phrases)
    return answer

def bot (question):
    #NLU
    intent = get_intent(question)

    #getting answer
    answer = get_answer_by_intent(intent)

    return answer

print ('Bot is ready')

while True:
    question = input()
    if question == 'stop':
        break
    answer = bot (question)
    print (answer)


