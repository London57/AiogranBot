


with open('bad.txt', 'r', encoding='utf-8') as file:
    a = file.readlines()
    
s = []

for i in a:
    if i not in ['\n']:

        i = i.replace("\n", '')
        s.append(i)

BAD_PHRASES = s

import pymorphy2

morth = pymorphy2.MorphAnalyzer()

import asyncio

async def task_cr(sl):
    p = morth.parse(sl)[0]

    return [x.word.encode() for x in p.lexeme]
    
task_list = []



async def main():
    for i in BAD_PHRASES:
        task = asyncio.create_task(task_cr(i))
        task_list.append(task)
    a = []
    for task in task_list:
        a += await task
    with open('task.txt', 'w') as file:
        file.writelines(str(a))

asyncio.run(main())

# при запуске ошибка т.к. BAD_PHRASES=[]