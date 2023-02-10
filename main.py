import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import (GetHistoryRequest)
import string
from pymorphy3 import MorphAnalyzer
from collections import Counter

from config import *

EXCL_WORDS = ['этот', 'который', 'такой', 'быть', 'весь', 'есть', 'свой']


async def count_words(entity):
    async with TelegramClient(account, id, token) as client:

        my_channel = await client.get_entity(entity)

        offset_id = 0
        limit = 100
        all_messages = []
        total_count_limit = 0

        while True:
            history = await client(GetHistoryRequest(
                peer=my_channel,
                offset_id=offset_id,
                offset_date=None,
                add_offset=0,
                limit=limit,
                max_id=0,
                min_id=0,
                hash=0
            ))

            if not history.messages:
                break
            messages = history.messages

            for message in messages:
                all_messages.append(message.to_dict())

            offset_id = messages[len(messages) - 1].id
            total_messages = len(all_messages)

            if total_count_limit != 0 and total_messages >= total_count_limit or len(all_messages) >= 100:
                break

        message_str = ''
        morph = MorphAnalyzer()

        for i in range(limit):
            message_str += all_messages[i]['message']

        message_list = [i for i in message_str.replace('\n', ' ').split(' ')]
        message_list = [i.translate(str.maketrans('', '', string.punctuation)).lower() for i in message_list if
                        not i.startswith(('#', 'http', '@'))]
        message_list = [morph.parse(i)[0].normal_form for i in message_list if
                        morph.parse(i)[0].normal_form and morph.parse(i)[0].normal_form != ' ']
        message_list = [i for i in message_list if i.isalpha() and len(i) >= 4]

        for i in message_list:
            p = morph.parse(i)[0]

            if p.tag.POS == 'NUMR' or p.tag.POS == 'NPRO' or p.tag.POS == 'PREP' or p.tag.POS == 'CONJ' \
                    or p.tag.POS == 'PRCL' or p.tag.POS == 'INTJ':
                message_list.remove(i)
            elif i in EXCL_WORDS:
                message_list.remove(i)

        count = Counter(message_list).most_common(10)

        return [key for key, value in count]


if __name__ == "__main__":
    result = asyncio.run(count_words('https://t.me/bbcrussian'))
    print(result)