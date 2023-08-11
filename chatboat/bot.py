from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus
import json
import logging


logger = logging.getLogger()
logger.setLevel(logging.ERROR)


# CORPUS_JSON_FILE = "ambignq_light/dev_light.json"
# with open(CORPUS_JSON_FILE, "r") as json_file:
#     conversations = json.load(json_file)


chatbot = ChatBot("Chatpot")

def extract_messages(conversations):
    messages = []
    for conv in conversations:
        for message in conv:
            if "text" in message:
                messages.append(message["text"])
    return messages

CORPUS_FILE = "chat.txt"
trainer = ListTrainer(chatbot)
# cleaned_corpus = extract_messages(conversations)
cleaned_corpus = clean_corpus(CORPUS_FILE)
with open('data.txt', 'w+') as f:
    f.write(str(cleaned_corpus))
trainer.train(cleaned_corpus)

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🪴 {chatbot.get_response(query)}")
