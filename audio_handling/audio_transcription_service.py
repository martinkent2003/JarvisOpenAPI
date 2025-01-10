import os
import asyncio
from openai import AsyncOpenAI
from project_config import setup_app_config

setup_app_config()

client = AsyncOpenAI()

async def convert_audio_to_text(local_input_file_path: str):
    with open(local_input_file_path, 'rb') as audio_file:
        response =  await client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"  # Ensure the output is JSON
        )
    print(response)
    return response

if __name__== '__main__':
    asyncio.run(convert_audio_to_text("hello.mp3"))