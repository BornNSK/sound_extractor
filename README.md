# sound_extractor :radio:
.mp4 to .mp3 converter with telegram send option

It's a simple script that convert your video file (for example downloaded from youtube) to the .mp3 file and send it to your telegram.

## How to install:
1. Coppy the project:
```sh
git clone https://github.com/BornNSK/sound_extractor.git
```
2. Create virtual envarment:
```sh
python3 -m venv venv
. venv/bin/activate
```
3. Install requirements:
```sh
pip install -m requirements.txt
```
4. Add Telegram settings:

create file with name: .env and add
```sh
TELEGRAM_TOKEN='telegram_bot_token'
TELEGRAM_CHAT_ID='your_chat_id'
```

## How to use:
1. Coppy files that you want to convert into the folder with script
2. Run script
3. Write file name
4. Enjoy 
