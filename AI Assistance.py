from tkinter import *
import datetime
import webbrowser
import random

def reply():
    user_input = entry.get().lower()
    chat.insert(END, "You: " + user_input + "\n")

    if "hello" in user_input or "hi" in user_input:
        chat.insert(END, "AI: Hello! How can I help you?\n")

    elif "time" in user_input:
        import datetime
        t = datetime.datetime.now().strftime("%H:%M:%S")
        chat.insert(END, "AI: Current time is " + t + "\n")

    elif "date" in user_input:
        import datetime
        d = datetime.date.today()
        chat.insert(END, "AI: Today's date is " + str(d) + "\n")

    elif "youtube" in user_input:
        import webbrowser
        chat.insert(END, "AI: Opening YouTube...\n")
        webbrowser.open("https://youtube.com")

    elif "google" in user_input:
        import webbrowser
        chat.insert(END, "AI: Opening Google...\n")
        webbrowser.open("https://google.com")
    elif "joke" in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't skeletons fight each other? They don't have the guts!"
        ]
        chat.insert(END, "AI: Here's a joke for you: " + random.choice(jokes) + "\n")
    elif "How are you?" in user_input:
        chat.insert(END, "AI: I'm just a program, but I'm doing great! Thanks for asking.\n")
    else:
        chat.insert(END, "AI: I didn't understand.\n")

    entry.delete(0, END)

# GUI
root = Tk()
root.title("AI Assistant")
root.geometry("550x650")
root.config(bg="#6f8faf")

frame = LabelFrame(root, text="AI Assistant", padx=10, pady=10)
frame.pack(padx=10, pady=10)

chat = Text(frame, width=60, height=25)
chat.pack()

entry = Entry(root, width=40)
entry.pack(pady=10)

send = Button(root, text="Send", command=reply)
send.pack()

root.mainloop()