from gtts import gTTS
from model import InputData
import base64
from fastapi.responses import FileResponse

async def text2Speech(input_data: InputData,responses={200:{"description":"text to speech","content": {"audio/mpeg":{"example":"no audio available"}}}}):
    inputText = input_data.data
    tts = gTTS(text=inputText,lang='en',slow=False)
    tts.save("output.mp3")

    with open("output.mp3","rb") as file:
        myObj = base64.b64encode(file.read())

    return {"speech": FileResponse(path="E:\Fastapi\t2s\output.mp3",media_type="audio/mpeg",
                                   filename='speech.mp3'),
            "data":inputText
            }