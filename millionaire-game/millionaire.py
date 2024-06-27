"""This is a Who Wants To Be A Millionaire (Quiz Game).
It is built using the Tkinter module of Python.
In this game, the contestant's goal is to answer 15 multiple-choice
questions correctly in a row to win a cash prize.
To assist contestants in answering the questions correctly,
there are three lifelines available.
Date 30.05.2024
Author Lyudvig Asoyan
"""
# import libraries
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk
import json
import random
import pyttsx3

# The code part that opens user name window
root_name = Tk()
root_name.geometry("400x250+600+350")
root_name.title("User Name")
root_name.config(bg="black")
entry_name = Entry(
    root_name, width=30, background="white", fg="black", font=("arial", 13, "bold")
)
entry_name.pack(pady=40)


def name_window_destroy():
    """
    Retrieves the username entered by the user in the username entry field.
    Destroys the username window upon submission and returns the username.
    """
    global username
    username = entry_name.get()
    root_name.destroy()
    return username

def questions_answers_txt():
    """
    Parses the questions and answers stored in a JSON file and returns them as a dictionary.
    """
    with open("questions_answers.txt", "r") as file:
        content = json.loads(file.read())
        return content

def user_name():
    """
    Displays the username window and waits for the user to submit their name.
    """
    global root_name
    submit_button = Button(root_name, text="Enter", command=name_window_destroy)
    submit_button.pack()
    root_name.mainloop()
user_name()


def create_window():
    """
    Creates the main game window with specified dimensions and title.
    """
    global root
    root = Tk()
    root.geometry("1270x652")
    root.title("Who wants to be a Millionaire!")
    root.config(bg="black")
    return root


def create_positions(root):
    """
    Creates and returns frames for different sections of the game interface.
    """

    left_frame = Frame(root, bg="black", padx=90)
    left_frame.grid(row=0, column=0)
    top_frame = Frame(left_frame, bg="black", pady=-28)
    top_frame.grid(row=0, column=0)
    center_frame = Frame(left_frame, bg="black", pady=-30)
    center_frame.grid(row=1, column=0)
    bottom_frame = Frame(left_frame, bg="black")
    bottom_frame.grid(row=2, column=0)
    right_frame = Frame(root, pady=30, padx=30, bd=0, background="black")
    right_frame.grid(row=0, column=1)
    return top_frame, center_frame, right_frame, bottom_frame

def put_images_and_buttons(top_frame, center_frame, right_frame, bottom_frame):
    """
    Places images and buttons for lifelines and game graphics on the game interface.
    """

    # The images should be global keep in memory
    global help50_50, hall_help, friend_call
    global game_logo, amount_image, questions_board, button_for50

    # The image for 50/50 help
    help50_50 = PhotoImage(file="public/images/50-50.png")
    button_for50 = Button(
        top_frame,
        image=help50_50,
        text=str("50-50"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",)
    button_for50.grid(row=0, column=0)
    button_for50.bind("<Button-1>", check_helps)

    # The image for audience help
    hall_help = PhotoImage(file=
    "public/images/audiencePole.png")
    button_for_audience = Button(
        top_frame,
        image=hall_help,
        text=str("hall_help"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",)
    button_for_audience.grid(row=0, column=1)
    button_for_audience.bind("<Button-1>", check_helps)

    # The image for friends call help
    friend_call = PhotoImage(file="public/images/phoneAFriend.png")
    button_call = Button(
        top_frame,
        image=friend_call,
        text=str("friend_call"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",)
    button_call.grid(row=0, column=2)
    button_call.bind("<Button-1>", check_helps)

    # The image for icon of millionaire game
    game_logo = PhotoImage(file="public/images/center.png")
    button_for_logo = Button(
        center_frame,
        image=game_logo,
        bg="black",
        bd=0,
        activebackground="black",
        width=360,
        height=250,
        highlightbackground="black",)
    button_for_logo.grid(row=0, column=0)

    # The image for amount of user
    amount_image = PhotoImage(file="public/images/Picture0.png")
    amount_lable = Label(right_frame, image=amount_image, bg="black")
    amount_lable.grid(row=0, column=0)

    # The image for questions board
    questions_board = PhotoImage(file="public/images/lay.png")
    questions_label = Label(bottom_frame, image=questions_board, background="black")
    questions_label.grid(row=0, column=0)

# The coordinates of the answers ans Variants A,B,C,D
answers_places = {
    "A": {"x": 60, "y": 105},
    "B": {"x": 330, "y": 105},
    "C": {"x": 60, "y": 185},
    "D": {"x": 330, "y": 185},
}

# congig for questions ans answers
configs = {"questionNumber": 0, "options": [], "questionsCount": 15}

def places_questions_and_answers(bottom_frame):
    """
    Places the question text and answer buttons on the game interface.
    """

    global quest_answ_right_ans, question_area, right_answer,answers

    question_area = Text(
        bottom_frame,
        font=("arial", 18, "bold"),
        width=34,
        height=2,
        wrap="word",
        bg="black",
        fg="white",
        bd=0,
        highlightbackground="black",)
    question_area.place(x=70, y=10)
    questions = questions_answers_txt()

    # The logic to put and delete questions and answers
    quest_answ_right_ans = questions[configs["questionNumber"]]
    answers = quest_answ_right_ans["answers"]
    question = quest_answ_right_ans["question"]

    right_answer = quest_answ_right_ans["rightAnswer"]

    configs["right_answer"] = right_answer
    question_area.insert(END, str(question))

    for key in answers:
        answer = answers[key]

        x = answers_places[key]["x"]
        y = answers_places[key]["y"]

        option_button = Button(
            bottom_frame,
            text=str(key + ": " + answer),
            font=("arial", 16, "bold"),
            bg="black",
            fg="white",
            bd=0,
            activebackground="black",
            highlightbackground="black",
            activeforeground="white",
            cursor="hand2",)
        option_button.place(x=x, y=y)
        option_button.bind("<Button-1>", check_right_and_wrong_answers)
        configs["options"].append(option_button)


correct_answer_count = 0
def check_right_and_wrong_answers(event):
    """
    Checks if the selected answer is correct or wrong and performs appropriate actions.
    """
    global is_continue, correct_answer_count
    global amount_image, is_correct
    value = event.widget["text"]
    answer = value.split(":")[0]
    is_correct = answer == configs["right_answer"]
    configs["questionNumber"] = configs["questionNumber"] + 1

    if is_correct:
        correct_answer_count += 1
        for i in configs["options"]:
            i.destroy()

        # function for destroy help bar
        if "help_audience" in configs:
            for bar in configs["help_audience"]:
                bar.destroy()
        if "help_audience" in configs:
            del configs["help_audience"]

        # function to show next amount picture
        amount_image = PhotoImage(
            file="public/images/Picture" + str(configs["questionNumber"]) + ".png")
        amount_lable = Label(right_frame, image=amount_image, bg="black")
        amount_lable.grid(row=0, column=0)

        # clear answers board for next answers
        configs["options"] = []

        # You win root window and winning count
        if configs["questionNumber"] == configs["questionsCount"]:
            root2 = Toplevel()
            root2.config(bg="black")
            root2.geometry("700x400")
            img_lable = Label(root2, image=game_logo, bd=0)
            img_lable.pack()
            top_users_and_amount_winning()
            win_label = Label(
                root2,
                text= f"Congratulations!!! \nThe winning amount is {winning}",
                font=("arial", 30, "bold"),
                bg="black",
                bd=0,
                fg="white",)
            win_label.pack()
            root2.mainloop()
        else:
            question_area.delete(1.0, END)

            places_questions_and_answers(bottom_frame)
    else:
        # create you lose window and winning count
        root1 = Toplevel()
        root1.config(bg="black")
        root1.geometry("700x400")
        img_lable = Label(root1, image=game_logo, bd=0)
        img_lable.pack()
        top_users_and_amount_winning()
        lose_label = Label(
            root1,
            text= f"Congratulations!! \nThe winning amount is {winning}",
            font=("arial", 30, "bold"),
            bg="black",
            bd=0,
            fg="white",)
        lose_label.pack()
        is_continue = False
        root1.mainloop()

def check_helps(event):
    """
    Determines which lifeline button was clicked and calls the corresponding lifeline function.
    """
    value = event.widget["text"]
    match value:
        case "50-50":
            help_50_50()
        case "hall_help":
            help_audience()
        case "friend_call":
            call_friend()

def help_50_50():
    """
    Implements the 50-50 lifeline by removing two incorrect answer options.
    """
    global button_for50x

    variants = {"A": 0, "B": 1, "C": 2, "D": 3}

    # Get the index of the correct answer from the configurations
    right_answer_index = variants[configs["right_answer"]]

    # Choose a random incorrect answer to remove
    random_wrong_answer1 = random.choice([i for i in range(4) if i != right_answer_index])

    # Calculate the indices of remaining options after removing the first incorrect answer
    remaining_indices = [
        i for i in range(4) if i != random_wrong_answer1 and i != right_answer_index
    ]

    # Choose a second random incorrect answer to remove from the remaining options
    random_wrong_answer2 = random.choice(remaining_indices)

    # Loop through the options and destroy the widgets corresponding to the two incorrect answers
    for k, v in enumerate(configs["options"]):
        if k != right_answer_index and k != random_wrong_answer2:
            v.destroy()

    # function for replace image 50/50X
    button_for50x = PhotoImage(file="public/images/50-50-X.png")

    button_50x = Button(
        top_frame,
        image=button_for50x,
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
        state=DISABLED,)
    button_50x.grid(row=0, column=0)


def help_audience():
    """
    Implements the 'Ask the Audience' lifeline by displaying audience opinion.
    """
    global hall_helpX, right_answer, help_bar, variants
    # coordinates for scales and variants
    help_bar_and_variants = {
        "A": {"scale": {"x": 580, "y": 240}, "letter": {"x": 580, "y": 190}},
        "B": {"scale": {"x": 620, "y": 240}, "letter": {"x": 620, "y": 190}},
        "C": {"scale": {"x": 660, "y": 240}, "letter": {"x": 660, "y": 190}},
        "D": {"scale": {"x": 700, "y": 240}, "letter": {"x": 700, "y": 190}},
    }

    # append help_bar and variants in configs, to destroy after answering
    configs["help_audience"] = []
    percentage = {}
    wrong_answer_sum = root

    # the loop for put help_bar and variants in click help_audience
    for key, value in help_bar_and_variants.items():

        # help_bar percents for right answer
        if key != right_answer:
            percent = random.randint(1, 25)
            percentage[key] = percent
            wrong_answer_sum += percent

    for key, value in help_bar_and_variants.items():

        if right_answer == key:
            percent = 100 - wrong_answer_sum
            percentage[key] = percent

        scale_x = value["scale"]["x"]
        scale_y = value["scale"]["y"]

        # function to make the the help scale tint green
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "green.Horizontal.TProgressbar", foreground="green", background="green")
        help_bar = Progressbar(
            root, orient=VERTICAL, length=120, style="green.Horizontal.TProgressbar")

        help_bar.place(x=scale_x, y=scale_y)
        help_bar.config(value=percentage[key])

        configs["help_audience"].append(help_bar)

        letter_x = value["letter"]["x"]
        letter_y = value["letter"]["y"]

        variants = Label(
            root, text=key, font=("arial", 20, "bold"), bg="black", fg="white"
        )
        variants.place(x=letter_x, y=letter_y)

        configs["help_audience"].append(variants)

    # replace image hall_help and unplug that button
    hall_helpX = PhotoImage(file="public/images/audiencePoleX.png")
    button_for_audience = Button(
        top_frame,
        image=hall_helpX,
        text=str("hall_help"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
        state=DISABLED,)
    button_for_audience.grid(row=0, column=1)

def call_friend():
    """
    Implements the 'Phone a Friend' lifeline by providing an audio hint about the correct answer.
    """
    global friend_call_helpX,right_answer

    #replace image call firend
    friend_call_helpX = PhotoImage(file="public/images/phoneAFriendX.png")
    firend_call = Button(
        top_frame,
        image=friend_call_helpX,
        text=str("friend_call"),
        bg="black",
        bd=0,
        activebackground="black",
        width=120,
        height=120,
        highlightbackground="black",
        state=DISABLED,)
    firend_call.grid(row=0, column=2)

    # library pyttxs3 text speach
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate',170)
    engine.setProperty('voices',voices[1].id)

    # speak right answer when click call firend icon
    engine.say(f"i think correct answer is {right_answer},{answers[right_answer]}")
    engine.runAndWait()

# function for show top users and their winnings
def top_users_and_amount_winning():
    """
    Displays the top users and their winnings in a separate window.
    """
    global winning

    list_of_amount_win = [0,1000,32000,1000000]
    if correct_answer_count < 5:
        winning = list_of_amount_win[0]

    elif correct_answer_count < 10:
        winning = list_of_amount_win[1]

    elif correct_answer_count < 15:
        winning = list_of_amount_win[2]
    else:
        winning = list_of_amount_win[3]

    # write and save users in txt file and save best result of user
    with open('top_users.txt','r+',encoding='utf-8') as users:
        element_lid = users.readlines()
        for i in element_lid:
            el = i.strip('\n').split(':')
            if el[0] == username:
                if int(el[2]) >= correct_answer_count:
                    break
                else:
                    users.write(f"{username}:{winning}:{correct_answer_count}\n")

    # read and sort users by their right answers count
    with open('top_users.txt','r+',encoding='utf-8') as users:
        final_leader_board = []
        lider_board = users.readlines()
        for i in lider_board:
            el = i.strip('\n').split(':')
            el[2] = int(el[2])
            final_leader_board.append(el)
        final_leader_board.sort(key=lambda x:x[2],reverse=True)

    # filter top 10 users for the final result
    with open('top_users.txt','w',encoding="utf-8") as users:
        for i in range(9):
            final_leader_board[i][2] = str(final_leader_board[i][2]) + '\n'
            el=":".join(final_leader_board[i])
            users.write(el)

    #window for the show top ten gamers
    top_users_window = Toplevel()
    top_users_window.config(bg='black')
    top_users_window.geometry('260x370+950+200')
    top_users_window.title('Top_Gamers')

    # loop for show User name, amount count and correct answers
    for i in final_leader_board:
        user_info = f"{i[0]} : {i[1]} : {i[2]}"
        label = Label(top_users_window, text=user_info,
        bg='black', fg='white',font=('arial',12,'bold'))
        label.pack()

root = create_window()
(
top_frame,
center_frame,
right_frame,
bottom_frame
) = create_positions(root)
put_images_and_buttons(top_frame, center_frame, right_frame, bottom_frame)
places_questions_and_answers(bottom_frame)
root.mainloop()
