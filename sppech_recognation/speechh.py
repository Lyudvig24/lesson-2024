import speech_recognition
import webbrowser
sr  = speech_recognition.Recognizer()

sr.pause_threshold = 0.3

def greeting():
    return 'hello '

def create_tasks():
    print('what add to notebook')
    
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source=mic,duration=1)
        audio = sr.listen(source=mic)
        query  = sr.recognize_google(audio_data=audio)
        
    with open("today_tasks.txt",'a') as file:
        file.write(f"{query}\n")
        
    return f"today {query} add to today_tasks"
    
    
with speech_recognition.Microphone() as mic:
    sr.adjust_for_ambient_noise(source=mic,duration=2)
    audio = sr.listen(source=mic)
    query  = sr.recognize_google(audio_data=audio)

if query == "hello friend":
    print(greeting())
elif query == "create notebook":
    print(create_tasks())
else:
    print("Unknown command")
        
