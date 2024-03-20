from random import choices, choice, random

def gibberish(k:int):
    return ''.join(choices('abcdefghijklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%^*()_+<?>:"|', k=k))

EVIL_STRINGS = [
    """VERY_REAL_DATABASE_PASSWORD = V3ry!R3alPa$$w0rD
VERY_REAL_DATABASE = 127.0.0.1:80""",
    """[PASSWORDS]
PLAINTEXT_PASSWORD_FILE=lol.txt""",
    "",
    "**parries your HTML GET request, breaking your ankles instantly**",
    "yes, and...",
    '"; DROP TABLE ALL_TABLES; --',
    '\\',
    '\\\\',
    '\'',
    """Ω≈ç√∫˜µ≤≥÷
åß∂ƒ©˙∆˚¬…æ
œ∑´®†¥¨ˆøπ“‘
¡™£¢∞§¶•ªº–≠
¸˛Ç◊ı˜Â¯˘¿
ÅÍÎÏ˝ÓÔÒÚÆ☃
Œ„´‰ˇÁ¨ˆØ∏”’
`⁄€‹›ﬁﬂ‡°·‚—±
⅛⅜⅝⅞
ЁЂЃЄЅІЇЈЉЊЋЌЍЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя
٠١٢٣٤٥٦٧٨٩""",
    """田中さんにあげて下さい
パーティーへ行かないか
和製漢語
部落格
사회과학원 어학연구소
찦차를 타고 온 펲시맨과 쑛다리 똠방각하
社會科學院語學研究所
울란바토르
𠜎𠜱𠝹𠱓𠱸𠲖𠳏""",
    """𐐜 𐐔𐐇𐐝𐐀𐐡𐐇𐐓 𐐙𐐊𐐡𐐝𐐓/𐐝𐐇𐐗𐐊𐐤𐐔 𐐒𐐋𐐗 𐐒𐐌 𐐜 𐐡𐐀𐐖𐐇𐐤𐐓𐐝 𐐱𐑂 𐑄 𐐔𐐇𐐝𐐀𐐡𐐇𐐓 𐐏𐐆𐐅𐐤𐐆𐐚𐐊𐐡𐐝𐐆𐐓𐐆""",
    """表ポあA鷗ŒéＢ逍Üßªąñ丂㐀𠀀""",
    "ȺȾ",
    "(╯°□°）╯︵ ┻━┻)",
    """😍
👩🏽
👨‍🦰 👨🏿‍🦰 👨‍🦱 👨🏿‍🦱 🦹🏿‍♂️
👾 🙇 💁 🙅 🙆 🙋 🙎 🙍
🐵 🙈 🙉 🙊
❤️ 💔 💌 💕 💞 💓 💗 💖 💘 💝 💟 💜 💛 💚 💙
✋🏿 💪🏿 👐🏿 🙌🏿 👏🏿 🙏🏿
👨‍👩‍👦 👨‍👩‍👧‍👦 👨‍👨‍👦 👩‍👩‍👧 👨‍👦 👨‍👧‍👦 👩‍👦 👩‍👧‍👦
🚾 🆒 🆓 🆕 🆖 🆗 🆙 🏧
0️⃣ 1️⃣ 2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣ 9️⃣ 🔟""",
    """᚛ᚄᚓᚐᚋᚒᚄ ᚑᚄᚂᚑᚏᚅ᚜
᚛                 ᚜
""",
"""test‪
‫test‫
 test 
test⁠test‫
⁦test⁧""",
"""Ṱ̺̺̕o͞ ̷i̲̬͇̪͙n̝̗͕v̟̜̘̦͟o̶̙̰̠kè͚̮̺̪̹̱̤ ̖t̝͕̳̣̻̪͞h̼͓̲̦̳̘̲e͇̣̰̦̬͎ ̢̼̻̱̘h͚͎͙̜̣̲ͅi̦̲̣̰̤v̻͍e̺̭̳̪̰-m̢iͅn̖̺̞̲̯̰d̵̼̟͙̩̼̘̳ ̞̥̱̳̭r̛̗̘e͙p͠r̼̞̻̭̗e̺̠̣͟s̘͇̳͍̝͉e͉̥̯̞̲͚̬͜ǹ̬͎͎̟̖͇̤t͍̬̤͓̼̭͘ͅi̪̱n͠g̴͉ ͏͉ͅc̬̟h͡a̫̻̯͘o̫̟̖͍̙̝͉s̗̦̲.̨̹͈̣
̡͓̞ͅI̗̘̦͝n͇͇͙v̮̫ok̲̫̙͈i̖͙̭̹̠̞n̡̻̮̣̺g̲͈͙̭͙̬͎ ̰t͔̦h̞̲e̢̤ ͍̬̲͖f̴̘͕̣è͖ẹ̥̩l͖͔͚i͓͚̦͠n͖͍̗͓̳̮g͍ ̨o͚̪͡f̘̣̬ ̖̘͖̟͙̮c҉͔̫͖͓͇͖ͅh̵̤̣͚͔á̗̼͕ͅo̼̣̥s̱͈̺̖̦̻͢.̛̖̞̠̫̰
̗̺͖̹̯͓Ṯ̤͍̥͇͈h̲́e͏͓̼̗̙̼̣͔ ͇̜̱̠͓͍ͅN͕͠e̗̱z̘̝̜̺͙p̤̺̹͍̯͚e̠̻̠͜r̨̤͍̺̖͔̖̖d̠̟̭̬̝͟i̦͖̩͓͔̤a̠̗̬͉̙n͚͜ ̻̞̰͚ͅh̵͉i̳̞v̢͇ḙ͎͟-҉̭̩̼͔m̤̭̫i͕͇̝̦n̗͙ḍ̟ ̯̲͕͞ǫ̟̯̰̲͙̻̝f ̪̰̰̗̖̭̘͘c̦͍̲̞͍̩̙ḥ͚a̮͎̟̙͜ơ̩̹͎s̤.̝̝ ҉Z̡̖̜͖̰̣͉̜a͖̰͙̬͡l̲̫̳͍̩g̡̟̼̱͚̞̬ͅo̗͜.̟
̦H̬̤̗̤͝e͜ ̜̥̝̻͍̟́w̕h̖̯͓o̝͙̖͎̱̮ ҉̺̙̞̟͈W̷̼̭a̺̪͍į͈͕̭͙̯̜t̶̼̮s̘͙͖̕ ̠̫̠B̻͍͙͉̳ͅe̵h̵̬͇̫͙i̹͓̳̳̮͎̫̕n͟d̴̪̜̖ ̰͉̩͇͙̲͞ͅT͖̼͓̪͢h͏͓̮̻e̬̝̟ͅ ̤̹̝W͙̞̝͔͇͝ͅa͏͓͔̹̼̣l̴͔̰̤̟͔ḽ̫.͕
Z̮̞̠͙͔ͅḀ̗̞͈̻̗Ḷ͙͎̯̹̞͓G̻O̭̗̮""",
"1;DROP TABLE users",
"1'; DROP TABLE users-- 1",
"' OR 1=1 -- 1",
"' OR '1'='1",
"'; EXEC sp_MSForEachTable 'DROP TABLE ?'; --",
"Kernel.exit(1)",
"%x('ls -al /')",
"$HOME",
"$ENV{'HOME'}",
"%s%s%s%s%s",
"{0}",
"%*.*s",
"File:///",
"""Roses are [0;31mred[0m, violets are [0;34mblue. Hope you enjoy terminal hue
But now...[20Cfor my greatest trick...[8m
The quick brown fo""",
"""Powerلُلُصّبُلُلصّبُررً ॣ ॣh ॣ ॣ冗
🏳0🌈️
జ్ఞ‌ా""",
"all alone on a friday night? god, you're so pathetic",
"https://www.youtube.com/watch?v=thV9hVxt5Zk",
"https://www.youtube.com/watch?v=qrAXRSBv-co",
"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
"https://www.youtube.com/watch?v=8ouXjQxkBng",
''*200,
]

def random_string():
    max_strats = 10
    strategy = int(random()*max_strats)
    if strategy < max_strats-2:
        return choice(EVIL_STRINGS)
    else:
        return gibberish(int(2**19 * random()))