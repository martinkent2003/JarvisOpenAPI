import boto3


polly_client = boto3.client('polly')


def convert_text_to_audio(text_content:str):
    response = polly_client.synthezise_speech(
        Engine = 'standard',
        LanguageCode = 'en-US',
        OutputFormat = 'mp3',
        Text = text_content,
        VoiceID = 'Brian'
    )
    return response