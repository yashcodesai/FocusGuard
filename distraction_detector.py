# Inside the loop or detection condition
if distraction_detected:
    print("Distraction detected!")
    playsound(os.path.join(os.path.dirname(__file__), 'alert.mp3'))