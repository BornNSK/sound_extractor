import os
import logging
import sys
from pathlib import Path
import moviepy.editor as mp
import telegram
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s, %(levelname)s, %(message)s',
                    )
logger = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')


def choose_file():
    while True:
        file_path = input("Введите имя файла: ")
        if not os.path.exists(file_path):
            print("Файла с таким именем не существует. Убедитесь в корректности ввода.")
        else:
            return file_path


def convert_file(video_file_path):
    video_file = Path(video_file_path)
    video = mp.VideoFileClip(str(video_file))
    audio = video.audio
    audio.write_audiofile(f'{video_file.stem}.mp3')
    return f'{video_file.stem}.mp3'


async def send_telegram(bot_token, chat_id, file_path):
    try:
        bot = telegram.Bot(token=bot_token)
        await bot.send_audio(chat_id=chat_id, audio=open(file_path, 'rb'))
        logging.debug('Сообщение отправлено успешно!')
    except Exception as error:
        error_message = f'Сбой в работе программы: {error}'
        logging.error(error_message)
    except FileNotFoundError:
        print("Файл не найден.")


async def main():
    # выбор файла
    video_file_path = choose_file()

    # Конвертация
    converted_file_path = convert_file(video_file_path)

    # Отправка
    await send_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, converted_file_path)


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
