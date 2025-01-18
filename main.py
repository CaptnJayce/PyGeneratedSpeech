import asyncio
import edge_tts
import pygame
import speech_recognition as sr
import os

# Initialize recognizer
r = sr.Recognizer()

# Voice chosen for QT is en-IE-EmilyNeural
VOICES = ['en-AU-NatashaNeural', 'en-CA-ClaraNeural', 'en-GB-LibbyNeural', 'en-IN-NeerjaNeural', 'en-IE-EmilyNeural']
VOICE = VOICES[4]
OUTPUT_FILE = "output_audio.mp3"

async def generate_speech(text: str) -> None:
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.stop()
    pygame.mixer.quit()

def listen_for_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print("You said: " + said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        while True:
            user_input = listen_for_audio()
            if user_input:
                loop.run_until_complete(generate_speech(user_input))

                if os.path.exists(OUTPUT_FILE):
                    play_audio(OUTPUT_FILE)
                    os.remove(OUTPUT_FILE)
                    
    finally:
        loop.close()

if __name__ == "__main__":
    main()
