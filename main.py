import asyncio
import edge_tts

# voice chosen for QT is en-IE-EmilyNeural
VOICES = ['en-AU-NatashaNeural', 'en-CA-ClaraNeural', 'en-GB-LibbyNeural', 'en-IN-NeerjaNeural', 'en-IE-EmilyNeural']
TEXT = "Hello! My name is Quartermaster, your assistive AI"
VOICE = VOICES[4]
OUTPUT_FILE = "test.mp3"

# asynchronous as to prevent problems with saving to file
# also important as it will be running alongside llm agents
async def main() -> None:
    communicate = edge_tts.Communicate(TEXT, VOICE)
    await communicate.save(OUTPUT_FILE)

loop = asyncio.get_event_loop_policy().get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()