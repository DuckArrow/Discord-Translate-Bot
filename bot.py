import os
import discord
from discord.ext import commands
from google.cloud import translate_v2 as translate
from google.cloud import texttospeech
from google.cloud import speech
import json
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!')

google_translate_client = translate.Client()
tts_client = texttospeech.TextToSpeechClient()
speech_client = speech.SpeechClient()

channel_languages = {}

language_flags = {
    'en': '🇺🇸',
    'ja': '🇯🇵',
    'fr': '🇫🇷',
    'de': '🇩🇪',
    'es': '🇪🇸',
}

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            await send_language_selection(channel)

async def send_language_selection(channel):
    message = "チャンネルの言語を選択してください。対応する国旗リアクションをクリックしてください：\n"
    for lang, flag in language_flags.items():
        message += f"{flag}: {lang}\n"
    sent_message = await channel.send(message)
    for flag in language_flags.values():
        await sent_message.add_reaction(flag)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    if str(reaction.emoji) in language_flags.values():
        channel_id = str(reaction.message.channel.id)
        selected_language = [lang for lang, flag in language_flags.items() if flag == str(reaction.emoji)][0]
        channel_languages[channel_id] = selected_language
        await reaction.message.channel.send(f"チャンネルの言語が {selected_language} に設定されました。")

@bot.command()
async def translate_voice(ctx):
    channel_id = str(ctx.channel.id)
    if channel_id not in channel_languages:
        await ctx.send("このチャンネルの言語が設定されていません。国旗リアクションで言語を選択してください。")
        return

    target_language = channel_languages[channel_id]
    
    # ここに音声録音のコードを追加
    # audio_data = record_audio()

    recognized_text = speech_to_text(audio_data, 'ja-JP')  # 仮に日本語を入力言語とする
    translated_text = translate_text(recognized_text, target_language)
    audio_content = text_to_speech(translated_text, target_language)
    
    await send_audio(ctx, audio_content)

def speech_to_text(audio_data, language_code):
    audio = speech.RecognitionAudio(content=audio_data)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code=language_code,
    )
    response = speech_client.recognize(config=config, audio=audio)
    return response.results[0].alternatives[0].transcript

def translate_text(text, target_language):
    result = google_translate_client.translate(text, target_language=target_language)
    return result['translatedText']

def text_to_speech(text, language):
    synthesis_input = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code=language, ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = tts_client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response.audio_content

async def send_audio(ctx, audio_content):
    with open("output.mp3", "wb") as out:
        out.write(audio_content)
    await ctx.send(file=discord.File("output.mp3"))

bot.run(os.getenv('DISCORD_TOKEN'))
