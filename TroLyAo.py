import pyttsx3
import speech_recognition
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()

while True:
# lấy giọng nói của bạn
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
    print("Robot: ... ")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: "+you)

# truy vấn giọng nói của bạn
    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "hello Hai"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "bye" in you:
        robot_brain = "Bye Hai"
        print("Robot: "+robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"

# lấy dữ liệu từ truy vấn đưa vào giọng nói
    print("Robot: "+robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()