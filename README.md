# Anonymous Chat Bot on Telegram

A completely free anonymous chat bot on Telegram, built using the `pyTelegramBotAPI` library.

## How to Run on Linux?

1. Install the Python package manager:

```bash
sudo apt install pip
```

2. Clone the repository:

```bash
git clone https://github.com/nepoloboyshawty/anon-chat-tg-no-db.git
cd anon-chat-tg-no-db
```

3. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install pyTelegramBotAPI dotenv
```

5. In the `anon-chat-tg-no-db` folder, create a file named `.env` and add the following line:

```bash
API_TOKEN=YOUR_TOKEN # Replace YOUR_TOKEN with your Telegram bot token
```

6. Launch the bot:

```bash
python3 main.py
```

## Interface Example

![Interface Example](https://i.postimg.cc/yNYzJgMV/photo-2025-08-12-11-32-55.jpg)
