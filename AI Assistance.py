import customtkinter as ctk
from tkinter import END
import datetime
import webbrowser

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

    if user=="":

        return

    chatbox.insert(END,"You : "+user+"\n\n")

    text=user.lower()

    if "hello" in text or "hi" in text:

        bot="Hello Krishna! 👋"

    elif "time" in text:

        bot=datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in text:

        bot=str(datetime.date.today())

    elif "youtube" in text:

        webbrowser.open("https://youtube.com")

        bot="Opening YouTube..."

    elif "google" in text:

        webbrowser.open("https://google.com")

        bot="Opening Google..."

    else:

        bot="Sorry, I don't understand."

    chatbox.insert(END,"AI : "+bot+"\n\n")

    entry.delete(0,END)

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
