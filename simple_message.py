#!/usr/bin/env python3
import telebot
import appSettings as settings
import argparse

def main():
    parser = argparse.ArgumentParser(description='Send a telegram message')
    parser.add_argument('chat_id')
    parser.add_argument('message')

    args = parser.parse_args()

    bot = telebot.TeleBot(settings.botToken)

    try:
        chat_id = int(args.chat_id)
    except ValueError:
        chat_id = args.chat_id

    bot.send_message(chat_id=chat_id, text=args.message)



if __name__ == '__main__':
    main()

