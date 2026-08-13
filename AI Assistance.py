import customtkinter as ctk
from tkinter import END
import datetime
import webbrowser
import random
import string


# ============================================================
# SETTINGS
# ============================================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


# ============================================================
# DATA
# ============================================================

JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why don't skeletons fight each other? They don't have the guts!",
    "Programming is 10% coding and 90% debugging.",
    "Why was the computer cold? It forgot to close its Windows!",
    "Why do programmers prefer dark mode? Because light attracts bugs!"
]

QUOTES = [
    "Believe in yourself.",
    "Success comes from consistency.",
    "Never stop learning.",
    "Every expert was once a beginner.",
    "Dream big and work hard."
]

UNKNOWN_RESPONSES = [
    "Sorry, I didn't understand.",
    "Please try another command.",
    "Type 'help' to see available commands.",
    "I'm still learning that."
]


# ============================================================
# WINDOW
# ============================================================

root = ctk.CTk()

root.title("AI Assistant")
root.geometry("1000x650")
root.minsize(850, 550)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def add_message(sender, message):
    """
    Display a message in the chatbox.
    """

    chatbox.insert(
        END,
        f"{sender} : {message}\n\n"
    )

    chatbox.see(END)


def save_history():
    """
    Save the current conversation to history.txt.
    """

    data = chatbox.get("1.0", END)

    with open(
        "history.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(data)

    add_message(
        "AI",
        "Chat history saved successfully."
    )


def clear_chat():
    """
    Clear all messages from the chatbox.
    """

    chatbox.delete("1.0", END)

    add_message(
        "AI",
        "Chat cleared. How can I help you?"
    )


# ============================================================
# MAIN SEND FUNCTION
# ============================================================

def send():

    user = entry.get().strip()

    # Don't send empty messages
    if not user:
        return

    # Display user's message
    add_message("You", user)

    # Convert to lowercase for command checking
    text = user.lower()

    # --------------------------------------------------------
    # GREETING
    # --------------------------------------------------------

    if "hello" in text or "hi" in text:

        bot = "Hello Krishna! 👋"


    # --------------------------------------------------------
    # TIME
    # --------------------------------------------------------

    elif "time" in text:

        bot = datetime.datetime.now().strftime(
            "%H:%M:%S"
        )


    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    elif "date" in text:

        bot = str(
            datetime.date.today()
        )


    # --------------------------------------------------------
    # YOUTUBE
    # --------------------------------------------------------

    elif "youtube" in text:

        webbrowser.open(
            "https://youtube.com"
        )

        bot = "Opening YouTube..."


    # --------------------------------------------------------
    # GOOGLE
    # --------------------------------------------------------

    elif "google" in text:

        webbrowser.open(
            "https://google.com"
        )

        bot = "Opening Google..."


    # --------------------------------------------------------
    # GITHUB
    # --------------------------------------------------------

    elif "github" in text:

        webbrowser.open(
            "https://github.com"
        )

        bot = "Opening GitHub..."


    # --------------------------------------------------------
    # LINKEDIN
    # --------------------------------------------------------

    elif "linkedin" in text:

        webbrowser.open(
            "https://linkedin.com"
        )

        bot = "Opening LinkedIn..."


    # --------------------------------------------------------
    # GMAIL
    # --------------------------------------------------------

    elif "gmail" in text:

        webbrowser.open(
            "https://gmail.com"
        )

        bot = "Opening Gmail..."


    # --------------------------------------------------------
    # JOKE
    # --------------------------------------------------------

    elif "joke" in text:

        bot = random.choice(JOKES)


    # --------------------------------------------------------
    # MOTIVATION
    # --------------------------------------------------------

    elif "motivate" in text or "quote" in text:

        bot = random.choice(QUOTES)


    # --------------------------------------------------------
    # PASSWORD
    # --------------------------------------------------------

    elif "password" in text:

        characters = (
            string.ascii_letters
            + string.digits
            + "@#$%"
        )

        password = ""

        for _ in range(12):

            password += random.choice(
                characters
            )

        bot = (
            "Generated Password : "
            + password
        )


    # --------------------------------------------------------
    # CALCULATOR
    # --------------------------------------------------------

    elif text.startswith("calculate"):

        try:

            expression = text.replace(
                "calculate",
                "",
                1
            ).strip()

            if not expression:

                bot = "Please provide a calculation."

            else:

                answer = eval(expression)

                bot = (
                    "Answer = "
                    + str(answer)
                )

        except Exception:

            bot = "Invalid calculation."


    # --------------------------------------------------------
    # GOOGLE SEARCH
    # --------------------------------------------------------

    elif text.startswith("search"):

        query = text.replace(
            "search",
            "",
            1
        ).strip()

        if query:

            webbrowser.open(
                "https://www.google.com/search?q="
                + query
            )

            bot = (
                "Searching Google for: "
                + query
            )

        else:

            bot = "What would you like me to search for?"


    # --------------------------------------------------------
    # WHAT IS
    # --------------------------------------------------------

    elif text.startswith("what is"):

        query = text.replace(
            "what is",
            "",
            1
        ).strip()

        if query:

            webbrowser.open(
                "https://www.google.com/search?q="
                + query
            )

            bot = (
                "Searching Google for: "
                + query
            )

        else:

            bot = "Please tell me what you want to know."


    # --------------------------------------------------------
    # HELP
    # --------------------------------------------------------

    elif "help" in text:

        bot = """
Available Commands:

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
quote
password

calculate 25*4
search Python
what is artificial intelligence

help
"""


    # --------------------------------------------------------
    # UNKNOWN COMMAND
    # --------------------------------------------------------

    else:

        bot = random.choice(
            UNKNOWN_RESPONSES
        )


    # --------------------------------------------------------
    # DISPLAY AI RESPONSE
    # --------------------------------------------------------

    add_message(
        "AI",
        bot
    )

    # Clear input box
    entry.delete(
        0,
        END
    )


# ============================================================
# SIDEBAR
# ============================================================

sidebar = ctk.CTkFrame(
    root,
    width=200
)

sidebar.pack(
    side="left",
    fill="y"
)


title = ctk.CTkLabel(
    sidebar,
    text="AI Assistant",
    font=("Arial", 24, "bold")
)

title.pack(
    pady=30
)


save_button = ctk.CTkButton(
    sidebar,
    text="💾 Save Chat",
    command=save_history
)

save_button.pack(
    pady=15,
    padx=15
)


clear_button = ctk.CTkButton(
    sidebar,
    text="🗑 Clear Chat",
    command=clear_chat
)

clear_button.pack(
    pady=15,
    padx=15
)


# ============================================================
# MAIN FRAME
# ============================================================

main = ctk.CTkFrame(
    root
)

main.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ============================================================
# CHATBOX
# ============================================================

chatbox = ctk.CTkTextbox(
    main,
    font=("Consolas", 15)
)

chatbox.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)


# ============================================================
# INPUT AREA
# ============================================================

bottom = ctk.CTkFrame(
    main
)

bottom.pack(
    fill="x",
    padx=10,
    pady=10
)


entry = ctk.CTkEntry(
    bottom,
    placeholder_text="Type your message...",
    height=40,
    font=("Arial", 16)
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)


# Press Enter to send
entry.bind(
    "<Return>",
    lambda event: send()
)


send_button = ctk.CTkButton(
    bottom,
    text="Send",
    width=80,
    height=40,
    command=send
)

send_button.pack(
    side="right",
    padx=5
)


# ============================================================
# WELCOME MESSAGE
# ============================================================

add_message(
    "AI",
    "Hello Krishna! 👋 I am your AI Assistant."
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()
