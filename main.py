import logging
import os
from pathlib import Path

import moviepy.editor as mp
from dotenv import load_dotenv
from telegram import Bot

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s, %(levelname)s, %(message)s')

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def choose_file():
    """Метод выбора файла"""
    while True:
        file_path = input("Введите имя файла: ")
        if not Path(file_path).exists():
            logging.error("Некорректное имя файла.")
            print("Файла с таким именем не существует. Убедитесь в корректности ввода.")
        else:
            return file_path


def convert_file(video_file_path):
    """Метод конвертации файла"""
    video_file = Path(video_file_path)
    if not video_file.exists():
        logging.error("Входной файл не найден.")
        return None
    try:
        video = mp.VideoFileClip(str(video_file))
        audio = video.audio
        audio_file_path = f'{video_file.stem}.mp3'
        audio.write_audiofile(audio_file_path)
        return audio_file_path
    except Exception as e:
        logging.error(f'Ошибка конвертации файла: {e}')
        return None


async def send_telegram(bot_token, chat_id, file_path):
    """Метод отправки файла"""
    try:
        bot = Bot(token=bot_token)
        with open(file_path, 'rb') as audio_file:
            await bot.send_audio(chat_id=chat_id, audio=audio_file)
        logging.debug('Сообщение отправлено успешно!')
    except Exception as e:
        logging.error(f'Сбой в работе программы: {e}')


async def main():
    """Основная функция"""
    # выбор файла
    video_file_path = choose_file()

    # Конвертация
    converted_file_path = convert_file(video_file_path)

    # Отправка
    if converted_file_path:
        await send_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, converted_file_path)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
