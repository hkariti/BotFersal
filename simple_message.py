#!/usr/bin/env python3
import sys
import argparse

import telebot
import appSettings as settings

def main():
    parser = argparse.ArgumentParser(description='Send a telegram message')
    parser.add_argument('chat_id')
    parser.add_argument('message', nargs="?")

    args = parser.parse_args()

    bot = telebot.TeleBot(settings.botToken)

    try:
        chat_id = int(args.chat_id)
    except ValueError:
        chat_id = args.chat_id

    if args.message is None:
        message = sys.stdin.read()
    else:
        message = args.message

    bot.send_message(chat_id=chat_id, text=message)



if __name__ == '__main__':
    main()

