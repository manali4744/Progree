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


import tkinter as tk
from tkinter import scrolledtext

exit_conditions = (":q", "quit", "exit")

def send_message():
    query = input_box.get("1.0", "end-1c")  # Get the text from the input box
    if query in exit_conditions:
        root.destroy()  # Close the window if exit condition is met
    else:
        response = chatbot.get_response(query)
        response_text.config(state=tk.NORMAL)
        response_text.insert(tk.END, f"🪴 {response}\n")
        response_text.config(state=tk.DISABLED)
        input_box.delete("1.0", tk.END)  # Clear the input box

# Create the main window
root = tk.Tk()
root.title("Chatbot GUI")

# Create and configure widgets
input_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=3)
response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10, state=tk.DISABLED)
send_button = tk.Button(root, text="Send", command=send_message)

# Place widgets using grid layout
input_box.grid(row=0, column=0, padx=10, pady=3)
response_text.grid(row=1, column=0, padx=10, pady=10)
send_button.grid(row=2, column=0, padx=10, pady=10)

# Initialize your chatbot instance here
# chatbot = ...

root.mainloop()
