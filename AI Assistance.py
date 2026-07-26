from random import random
import customtkinter as ctk
from tkinter import END
import datetime
import webbrowser
import string
# ------------------ SETTINGS ------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# ------------------ WINDOW ------------------

root = ctk.CTk()

root.geometry("1000x650")
root.title("AI Assistant")

# ------------------ FUNCTIONS ------------------

def save_history():

    data = chatbox.get("1.0", END)

    with open("history.txt","w",encoding="utf-8") as file:
        file.write(data)


def clear_chat():

    chatbox.delete("1.0",END)


def send():

    user = entry.get()

    if user == "":
        return

    chatbox.insert(END, "You : " + user + "\n\n")

    text = user.lower()

    # Greeting
    if "hello" in text or "hi" in text:

        bot = "Hello Krishna! 👋"

    # Time
    elif "time" in text:

        bot = datetime.datetime.now().strftime("%H:%M:%S")

    # Date
    elif "date" in text:

        bot = str(datetime.date.today())

    # Open YouTube
    elif "youtube" in text:

        webbrowser.open("https://youtube.com")
        bot = "Opening YouTube..."

    # Open Google
    elif "google" in text:

        webbrowser.open("https://google.com")
        bot = "Opening Google..."

    # Open GitHub
    elif "github" in text:

        webbrowser.open("https://github.com")
        bot = "Opening GitHub..."

    # Open LinkedIn
    elif "linkedin" in text:

        webbrowser.open("https://linkedin.com")
        bot = "Opening LinkedIn..."

    # Open Gmail
    elif "gmail" in text:

        webbrowser.open("https://gmail.com")
        bot = "Opening Gmail..."

    # Joke
    elif "joke" in text:

        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why don't skeletons fight each other? They don't have the guts!",
            "Programming is 10% coding and 90% debugging.",
            "Why was the computer cold? It forgot to close its Windows!"
        ]

        bot = random.choice(jokes)

    # Motivation
    elif "motivate" in text or "quote" in text:

        quotes = [
            "Believe in yourself.",
            "Success comes from consistency.",
            "Never stop learning.",
            "Every expert was once a beginner.",
            "Dream big and work hard."
        ]

        bot = random.choice(quotes)

    # Password Generator
    elif "password" in text:

        import string

        characters = string.ascii_letters + string.digits + "@#$%"

        password = ""

        for i in range(12):
            password += random.choice(characters)

        bot = "Generated Password : " + password

    # Calculator
    elif text.startswith("calculate"):

        try:

            expression = text.replace("calculate", "")

            answer = eval(expression)

            bot = "Answer = " + str(answer)

        except:

            bot = "Invalid Expression."

    # Google Search
    elif text.startswith("search"):

        query = text.replace("search", "")

        webbrowser.open(
            "https://www.google.com/search?q=" + query
        )

        bot = "Searching Google..."

    # Help
    elif "help" in text:

        bot = """
Available Commands

hello
time
date
youtube
google
github
linkedin
gmail
joke
motivate
password
calculate 5*10
search python tkinter
help
"""

    # Unknown command
    else:

        replies = [
            "Sorry, I didn't understand.",
            "Please try another command.",
            "Type 'help' to see available commands.",
            "I don't know that command yet."
        ]

        bot = random.choice(replies)

    chatbox.insert(END, "AI : " + bot + "\n\n")

    entry.delete(0, END)

    chatbox.see(END)
# ------------------ SIDEBAR ------------------

sidebar=ctk.CTkFrame(root,width=200)

sidebar.pack(side="left",fill="y")

title=ctk.CTkLabel(
sidebar,
text="AI Assistant",
font=("Arial",24,"bold")
)

title.pack(pady=30)

saveButton=ctk.CTkButton(
sidebar,
text="Save Chat",
command=save_history
)

saveButton.pack(pady=15)

clearButton=ctk.CTkButton(
sidebar,
text="Clear Chat",
command=clear_chat
)

clearButton.pack(pady=15)

# ------------------ MAIN FRAME ------------------

main=ctk.CTkFrame(root)

main.pack(fill="both",expand=True,padx=10,pady=10)

chatbox=ctk.CTkTextbox(
main,
width=700,
height=500,
font=("Consolas",15)
)

chatbox.pack(pady=15,padx=10)

entry=ctk.CTkEntry(
main,
placeholder_text="Type your message...",
height=40,
font=("Arial",16)
)

entry.pack(fill="x",padx=10,pady=10)

entry.bind("<Return>",lambda event:send())

sendButton=ctk.CTkButton(
main,
text="Send",
height=40,
command=send
)

sendButton.pack(pady=10)

chatbox.insert(
END,
"AI : Hello! I am your AI Assistant.\n\n"
)

root.mainloop()
