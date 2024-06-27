# Voice Assistant

## Overview
This Python program is a voice assistant that executes specific commands using speech recognition. It listens for voice commands, recognizes them, and performs various actions such as opening web browsers, searching Google, creating directories, and listing files in the current directory.

## Author
- Lyudvig Asoyan

## Date
- 08, June 2024

## Prerequisites
- Python 3.x
- `speech_recognition` library (install via `pip install SpeechRecognition`)
- Firefox browser (for `open_firefox()` function)
- Xterm terminal emulator (for `open_terminal()` function)

## Usage
1. Clone or download the repository.
3. Ensure Firefox browser and Xterm terminal emulator are installed and accessible.
4. The assistant will start listening for voice commands. Speak clearly and wait for the assistant to recognize your command.
5. Commands you can use:
   - "Open Firefox": Opens the Firefox browser.
   - "Open Google": Prompts you to speak a query and opens Google search results in the default web browser.
   - "Search music": Opens a YouTube search for music.
   - "Open terminal": Opens a new terminal window.
   - "Create directory [directory_name]": Creates a directory with the specified name.
   - "List files": Lists files in the current directory.

