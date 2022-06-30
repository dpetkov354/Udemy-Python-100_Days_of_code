from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
WORD_GROUP = {}
# ---------------------------- Data base SETUP ------------------------------- #
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    word_from_csv = original_data.to_dict(orient="records")
else:
    word_from_csv = data.to_dict(orient="records")
# ---------------------------- Button Function SETUP ------------------------------- #


def get_card():
    global WORD_GROUP, timer
    window.after_cancel(timer)
    WORD_GROUP = random.choice(word_from_csv)
    canvas.itemconfig(word_label, text=WORD_GROUP["French"], fill="black")
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(image, image=french_img)
    timer = window.after(3000, func=card_swap)


def known():
    global WORD_GROUP, word_from_csv
    word_from_csv.remove(WORD_GROUP)
    data_learned = pandas.DataFrame(word_from_csv)
    data_learned.to_csv("data/words_to_learn.csv", index=False)
    get_card()


# ---------------------------- Delay Function SETUP ------------------------------- #


def card_swap():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=WORD_GROUP["English"], fill="white")
    canvas.itemconfig(image, image=english_img)


# ---------------------------- UI SETUP ------------------------------- #
# ----Window---- #
window = Tk()
window.title("Flashcard exercise FR-EN")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, func=card_swap)

canvas = Canvas(height=526, width=800, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)

# ----Main image---- #
french_img = PhotoImage(file="images/card_front.png")
english_img = PhotoImage(file="images/card_back.png")
current_img = french_img
image = canvas.create_image(400, 263, image=current_img)
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)

# ----Ok button---- #
ok_button_image = PhotoImage(file="images/right.png")
ok_button = Button(image=ok_button_image, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR, highlightthickness=0,
                   bd=0, command=known)
ok_button.grid(row=2, column=1)

# ----NOk button---- #
nok_button_image = PhotoImage(file="images/wrong.png")
nok_button = Button(image=nok_button_image, bg=BACKGROUND_COLOR, activebackground=BACKGROUND_COLOR,
                    highlightthickness=0, bd=0, command=get_card)
nok_button.grid(row=2, column=0)

# ----Language text---- #
language_label = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

# ----Word text---- #
word_label = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# ---------------------------- Default beginning words ------------------------------- #
get_card()

# ---------------------------- Program loop ------------------------------- #
window.mainloop()
