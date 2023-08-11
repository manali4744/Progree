# import nltk
# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# import yaml

# # Set the NLTK data directory
# nltk.data.path.append('/home/pc/nltk_data')

# # Create a chatbot instance
# chatbot = ChatBot('MyBot')

# # Create a new instance of a ChatterBotCorpusTrainer
# trainer = ChatterBotCorpusTrainer(chatbot)

# # Train the chatbot on English language data
# trainer.train('chatterbot.corpus.english')

# # Main loop
# print("Chatbot: Hello! How can I assist you today?")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Chatbot: Goodbye!")
#         break
#     response = chatbot.get_response(user_input)
#     print("Chatbot:", response)

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

# Create a chatbot instance
chatbot = ChatBot("MyChatBot")

# Create a ListTrainer and train the chatbot
trainer = ListTrainer(chatbot)

# Set the path to the directory containing the custom data file
data_path = os.path.join(os.path.dirname(__file__), '')

# Read question-answer pairs from the text file
qa_pairs_path = os.path.join(data_path, 'input.txt')

with open(qa_pairs_path, "r") as file:
    lines = file.readlines()
    question_answer_pairs = [line.strip() for line in lines]

# Train the chatbot
trainer.train(question_answer_pairs)

# Test the trained chatbot
exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")




