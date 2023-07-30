import customtkinter as cstk
import tkinter as tk
from tkinter import filedialog, PhotoImage

questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "When was the Eiffel Tower built?",
        "answer": "1889"
    },
    {
        "question": "What is the formula for calculating the area of a circle?",
        "answer": "3.14*r^2"
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "answer": "100 degree celcius"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet?",
        "answer": "William Shakespeare"
    }
]

def check_answer(user_answer, correct_answer):
    return user_answer.lower() == correct_answer.lower()

print("Chatbot: Welcome to the quiz! Type 'exit' to end the quiz.")

correct_answers = 0

for question_data in questions:
    question_text = question_data["question"]
    print("Chatbot: " + question_text)

    user_input = input("User: ")
    if user_input.lower() == "exit":
        print("Chatbot: Thank you for playing!")
        break

    if check_answer(user_input, question_data["answer"]):
        print("Chatbot: Congratulations, your answer is correct!")
        correct_answers += 1
    else:
        print("Chatbot: Sorry, your answer is incorrect.")

    print()

print("Chatbot: Quiz completed!")
print(f"Chatbot: You answered {correct_answers} questions correctly out of {len(questions)}.")
