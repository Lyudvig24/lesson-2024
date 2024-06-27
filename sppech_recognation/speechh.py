"""
Author: Lyudvig Asoyan
Date: 08,06.2024

this program is a voice assistant,
that execute specific commands using speech

"""

import os # Used for operating system operations.
import webbrowser # Used for opening web browsers.
import subprocess # Used for executing system commands.
import speech_recognition as sr # Used for recognizing speech from the microphone

recognizer = sr.Recognizer()

def open_firefox():
    """
    Opens the Firefox web browser.
    """
    os.system("firefox")

def search_music():
    """
    Opens YouTube and searches for music.
    """
    webbrowser.open("https://www.youtube.com/results?search_query=music")

def open_terminal():
    """
    Opens a terminal window.
    """

    subprocess.Popen(['xterm'])

def create_directory(test_directory):
    """
    Creates a new directory.

    Parameters:
        test_directory (str): The name of the directory to be created.
    """
    os.mkdir(test_directory)

def google_search():
    """
    Performs a Google search based on speech input.
    """
    print("What do you want to search on Google?")
    with sr.Microphone(device_index=5) as source:
        audio = recognizer.listen(source)
        query = recognizer.recognize_google(audio)
        webbrowser.open(f"https://www.google.com/search?q={query}")

def list_files():
    """
    Lists files in the current directory.
    """
    files = os.listdir()
    print("Files in current Directory:")
    for file in files:
        print(file)

def execute_command(command):
    """
    Executes a command based on speech input.

    Parameters:
        command (str): The command to be executed.
    """
    command = command.lower()
    if 'open firefox' in command:
        open_firefox()

    elif "open google" in command:
        google_search()

    elif 'search music' in command:
        search_music()

    elif 'open terminal' in command:
        open_terminal()

    elif 'create directory' in command:
        directory_name = command.replace("create directory","test_directory")
        create_directory(directory_name)

    elif 'list files' in command:
        list_files()

    else:
        print("Unknown Command")

def listen():
    """
    Listens for speech input and executes commands accordingly.
    """
    print('Listening...')
    with sr.Microphone(device_index=5) as source:
        audio = recognizer.listen(source)

    print("Recognizing...")
    command = recognizer.recognize_google(audio)
    print("You said:",command)
    execute_command(command)

listen()
