import random

absolute_truths = [
    "It will pass.",
    "It will be ok.",
    "One day it won't matter.",
    "Tomorrow is another day.",
    "Keep moving forward.",
    "This too shall pass.",
    "You are stronger than you think.",
    "You can only get stronger from this.",
    "You are not alone.",
]

thank_you_messages = [
    "Thanks for telling me.",
    "The weight is meant to be shared, every word makes you lighter.",
    "Let it out.",
    "I'm glad you said it out loud.",
    "Keeping everything inside is heavy.",
    "You don't have to carry every thought alone.",
    "Sometimes saying it helps.",
    "Thank you for trusting me with that.",
    "Every feeling passes through eventually.",
    "Some things hurt less once spoken.",
]

anything_else_questions = [
    "Anything else?",
    "Tell me more.",
    "I'm listening.",
    "What else is on your mind?",
    "You can keep going.",
    "Is there something more you want to say?",
    "What else has been weighing on you?",
    "Still carrying something?",
    "Do you want to talk about anything else?",
    "What else is troubling you?",
    "Go on.",
    "Take your time.",
    "And what happened then?",
    "What else have you been holding in?",
    "You don't have to stop there.",
    "If there's more, you can tell me.",
    "What else has been difficult lately?",
]

negative_answers = [
    "no",
    "não",
    "nah",
    "nope",
    "n",
    "nothing",
    "nothing else",
]

complaints = []

print("Tell me your problem:")
problem = input()

while True:

    complaints.append(problem)

    lower_problem = problem.lower()

    # Resposta especial para certas frases
    if (
        "eu sou" in lower_problem or
        "eu era" in lower_problem or
        "i am" in lower_problem or
        "i was" in lower_problem
    ):
        truth = "That was then."
    else:
        truth = random.choice(absolute_truths)

    thank_you = random.choice(thank_you_messages)

    print()
    print(thank_you)
    print(truth)
    print()

    question = random.choice(anything_else_questions)

    print(question)
    answer = input()

    # encerra o programa se for uma resposta negativa
    if answer.lower() in negative_answers:
        break

    # qualquer outra resposta vira uma nova complaint
    problem = answer

print()
print("See you space cowboy.")