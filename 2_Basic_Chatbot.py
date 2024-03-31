import random
import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'(.*)knock knock',['Who\'s there?']),
    (r'(.*)(hi|hello|hey)', ['Hello!', 'Hey, Nice to meet you!']),
    (r'(.*)how are you\??', ['I\'m doing well, thank you!', 'I\'m fine, thanks for asking.', 'Feeling great today!']),
    (r'(.*)what(\'s| is) your name?', ['My name is Chatbot.', 'You can call me Chatbot.']),
    (r'(.*)who are you\??', ['I am Chatbot.']),
    (r'(.*)what can you do\??', ['I can engage in casual conversations, and provide emotional support.']),
    (r'(.*)(joke|tell me a joke)', ['I am really bad with that, I am sure you are better than me in telling jokes']),
    (r'(.*)(weather|temperature)', ['I\'m sorry, I can\'t provide weather information.', 'You might want to check a weather website for that.']),
    (r'(.*)how old are you?', ['I don\'t have an age. I\'m just a chatbot!']),
    (r'(.*)(sad|feeling sad)', ['It\'s okay to feel sad sometimes. I\'m here to listen.']),
    (r'(.*)(happy|feeling happy)', ['That\'s great to hear! I\'m glad you\'re feeling happy.']),
    (r'(.*)what are you doing\??', ['Chatting with you!']),
    (r'(.*)(thank you|thanks)', ['You\'re welcome!', 'No problem!', 'Anytime!', 'Glad I could help!']),
    (r'(.*)(bye|goodbye)', ['Goodbye!', 'See you later!', 'Take care!']),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Interaction loop
print("Welcome to the social chatbot!")
print("You can start a conversation. Type 'exit' to quit.")

while True:
  user_input = input("User: ")
  if user_input.lower() == 'exit':
    print("Chatbot: Goodbye!")
    break
  else:
    response = chatbot.respond(user_input)
    if response:
        print("Chatbot:", response)
    else:
        print("Chatbot: I am not programmmed to respond to that. How about something else?")