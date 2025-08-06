import cv2
from focus_detector import detect_focus
import threading

# Load face cascade only once
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Avoid overlapping sounds
alert_playing = False

def play_alert():
    global alert_playing
    alert_playing = True
    try:
        from pygame import mixer
        mixer.init()
        mixer.music.load("alert.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            continue
    except Exception as e:
        print(f"Error playing sound: {e}")
    alert_playing = False

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    # Face detection + drawing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Detect focus
    is_focused = detect_focus(frame)

    # Display focus status
    status_text = "FOCUSED" if is_focused else "DISTRACTED"
    color = (0, 255, 0) if is_focused else (0, 0, 255)
    cv2.putText(frame, status_text, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Sound alert
    if not is_focused and not alert_playing:
        threading.Thread(target=play_alert).start()

    # Show window (only one window)
    cv2.imshow("FocusGuard - Press 'q' to quit", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()