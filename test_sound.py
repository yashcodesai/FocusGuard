from pygame import mixer
import time

mixer.init()  # Initialize the mixer
mixer.music.load("alert.mp3")  # Load the sound file
mixer.music.play()  # Play the sound

print("Playing sound...")

# Wait while sound is playing
while mixer.music.get_busy():
    time.sleep(0.1)

print("Sound finished.")