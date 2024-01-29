from aiogram import Bot, Dispatcher, executor, types #pip install --force-reinstall -v "aiogram==2.23.1"
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import random

# Берём токен для кода с телеграм бота https://t.me/BotFather
bot = Bot('6794140977:AAFJkp-9Ha3Ha_PD2Bd1lYu4bC8guNJYhH4')
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
h1 = KeyboardButton('/help')
kb.add(h1)

start_bot = """
------------------------------
🤩🤩🤩🤩                   -
Сәлем есімім <b>"Study"</b>   -
мен саған Python тілін тез   -
әрі оңай үйренуге            -
көмек тескім келеді😊        -
Ол үшін <b>"Help"</b>        -
командасын басып жбер        -
сол жерде саған керек барлық -
ақпарат бар❗                 -
------------------------------
"""

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text=start_bot, parse_mode='HTML', reply_markup=kb)

help_cmd = """
-------------<b>🤓[Study]</b>-----------------
<em>Pyhton нөлден бастап үйрену</em>

-------------<b>📚[ҰБТ]</b>-----------------
<em>ҰБТ дан келетін сұрақтарға дайындалу</em>

-------------<b>💾[Packages]</b>-----------------
<em>Бастапқы код</em>

-------------<b>🕹[Game-projeck]</b>-----------------
<em>Кішігірім ойын жасау</em>

-------------<b>📦[exe]</b>-----------------
<em>Python тапсырмалар</em>
"""
###############################################################################################################

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    ff = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/🤓Study')
    h3 = KeyboardButton('/📚ҰБТ')
    h4 = KeyboardButton('/💾Packages')
    h5 = KeyboardButton('/🕹Game-projeck')
    h6 = KeyboardButton('/📦exe')
    ff.add(h2).insert(h3).insert(h4).insert(h5).insert(h6).insert(h1)
    await bot.send_message(chat_id=message.chat.id, text=help_cmd, parse_mode='HTML', reply_markup=ff)

###############################################################################################################
@dp.message_handler(commands=['📚ҰБТ'])
async def command_help(message: types.Message):
    code = """
def hello():
    print("help me :( ")

hello()
"""
    formatted_message = f"```\n{code}\n```"
    gg = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/📑Теория')
    h3 = KeyboardButton('/💻code')
    # h4 = KeyboardButton('/Допалнително')
    gg.add(h3).insert(h2).insert(h1)#.insert(h4)
    text = """
-------------<b>📑[Теория]</b>-----------------
<em>Текстік сүрақтарға дайындалу</em>

-------------<b>💻[code]</b>-----------------
<em>ҰБТ да келетін кодтарға дайындалу</em>

"""
    await bot.send_message(chat_id=message.chat.id, text=text, parse_mode='HTML', reply_markup=gg)
    await bot.send_message(chat_id=message.chat.id, text=formatted_message, parse_mode='MarkdownV2')


@dp.message_handler(commands=['📑Теория'])
async def command_help(message: types.Message):
    ttt = """
<b>-------------------------------------------------</b>
<b>[1]Компьютер құрылғылары</b> 
<b>-------------------------------------------------</b>
<b>[2]Компьютерлік желілерді ұйымдастыру.</b>
<b>-------------------------------------------------</b>
<b>[3]Ақпаратты ұсыну және өлшеу.</b> 
<b>-------------------------------------------------</b>
<b>[4]Есептеу жүйелері.</b> 
<b>-------------------------------------------------</b>
<b>[5]Компьютердің логикалық негіздері.</b> 
<b>-------------------------------------------------</b>
<b>[6]Алгоритмдер </b>
<b>-------------------------------------------------</b>
<b>[7]Программалау.</b> 
<b>-------------------------------------------------</b>
<b>[8]Алгоритмдер және программалар.</b>
<b>-------------------------------------------------</b>
<b>[9]Ақпараттық қамтамасыз ету.</b> 
<b>-------------------------------------------------</b>
<b>[10]Реляциондық деректер қоры.</b>  
<b>-------------------------------------------------</b>
<b>[11]Мәліметтер қорын жасау.</b> 
<b>-------------------------------------------------</b>
<b>[12]Ақпараттық объектілерді құру және түрлендіру.</b> 
<b>-------------------------------------------------</b>
<b>[13]Web - жобалау.</b>"""
    ikb = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='(1)', url='https://drive.google.com/file/d/1ciSD0ybBBcIHhMwqrT28hWEqlS0tXY81/view?usp=sharing') #1(1)Компьютер құрылғылары
    button2 = InlineKeyboardButton(text='(2)', url='https://drive.google.com/file/d/1mg2RXHL_eeB7DeZ9TkDVvGY-hKjGn8dp/view?usp=sharing') #2(2)Компьютерлік желілерді ұйымдастыру
    button3 = InlineKeyboardButton(text='(3)', url='https://drive.google.com/file/d/19Iry7aank70MGFVgjlcu2THLarOBAPbF/view?usp=sharing') #3(3)Ақпаратты ұсыну және өлшеу
    button4 = InlineKeyboardButton(text='(4)', url='https://drive.google.com/file/d/11s_up77cj6sScG5RrNZGaOgnw0vn4DCS/view?usp=sharing')
    button5 = InlineKeyboardButton(text='(5)', url='https://drive.google.com/file/d/1wcUFbOl-43p8ZAe0KMDgR3Gml2_K5q6L/view?usp=sharing')
    button6 = InlineKeyboardButton(text='(6)', url='https://drive.google.com/file/d/1LWhmxZ_Qgseelu47JM5wSUJiqW3aH-GV/view?usp=sharing')
    button7 = InlineKeyboardButton(text='(7)', url='https://drive.google.com/file/d/1tmadPjVu1MO_fRFz-XwLU_QYFMicgefb/view?usp=sharing')
    button8 = InlineKeyboardButton(text='(8)', url='https://drive.google.com/file/d/16aOKvuH8FYsjCDGyIsCXCkXHX6wIo8Vr/view?usp=sharing')
    button9 = InlineKeyboardButton(text='(9)', url='https://drive.google.com/file/d/1N_40MqIzgEr9w-ZEts7rOf8vHS6ga1fT/view?usp=sharing')
    button10 = InlineKeyboardButton(text='(10)', url='https://drive.google.com/file/d/1FZ3eIWCY_4QISyZ6DoJ2SxOWwaK6BFdJ/view?usp=sharing')
    button11 = InlineKeyboardButton(text='(11)', url='https://drive.google.com/file/d/1AXJB45-82UMC_6uZX0mkoEgSsHbJ4Bkz/view?usp=sharing')
    button12 = InlineKeyboardButton(text='(12)', url='https://drive.google.com/file/d/1r0Bp3hO_qcSR5j2e-HUuWqoV8O3lS1J1/view?usp=sharing')
    button13 = InlineKeyboardButton(text='(13)', url='https://drive.google.com/file/d/1LGIevfPCxP6pq9g3Gg7Kkrmiuiimb4Fv/view?usp=sharing')
    ikb.insert(button1).insert(button2).insert(button3).insert(button4).insert(button5).insert(button6).insert(button7).insert(button8).insert(button9).insert(button10).insert(button11).insert(button12).add(button13)
    ffh = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/📚ҰБТ')
    ffh.add(h1)
    await bot.send_message(chat_id=message.chat.id, text=ttt, parse_mode='HTML', reply_markup=ikb)
    await bot.send_message(chat_id=message.chat.id, text='🤖 Бол жерде сізге керек кітаптан алынған үзінділер бар бол сұрақтар ҰБТ да келетініне сенімдімін !!', reply_markup=ffh)



questions_data = [
    {
        "question": "Что покажет этот код?"
        """
        for j in 'Hi! I\'m mister Robert':
	            if j == '\'':
	            print("Найдено")
	            break
            else:
	            print ("Готово")
        """,
        "options": ["A. Ошибку в коде", "B. Найдено и Готово", "C. Готово", "D. Найдено"],
        "correct_answer": "D",
        'explanation': "Найдено"
    },
    {
        'question': "Какая библиотека отвечает за время?",
        'options': ["A. time", "B. Time", "C. clock", "D. localtime"],
        'correct_answer': "A",
        'explanation': "библиотека time отвечает за время"
    },
    
    {
        'question': "Где правильно создана переменная?",
        'options': ["A. int num = 2", "B. var num = 2", "C. num = float(2)", "D. Нет подходящего варианта"],
        'correct_answer': "C",
        'explanation': "num = float(2)"
    },
    {
        'question': "Что такое Python?",
        'options': ["A. Животное", "B. Программирование", "C. Игрушка", "D. Отрасль математики"],
        'correct_answer': "B",
        'explanation': "Программирование"
        
    },
    {
        'question': "Какой язык программирования наиболее популярен?",
        'options': ["A. Python", "B. Java", "C. C++", "D. JavaScript"],
        'correct_answer': "A",
        'explanation': "Python"
        
    },
    {
        'question': "Сколько библиотек можно импортировать в один проект?",
        'options': ["A. Не более 3", "B. Не более 10", "C. Не более 23", "D. Неограниченное количество"],
        'correct_answer': "D",
        'explanation': "Неограниченное количество"
    },
    {
        'question': "Как получить данные от пользователя?",
        'options': ["A. Использовать метод input()", "B. Использовать метод get()", "C. Использовать метод readLine()", "D. Использовать метод read()"],
        'correct_answer': "A",
        'explanation': "Использовать метод input()"
    },
    {
        'question': "Сколько байт в одном килобайте?",
        'options': ["A. 1000", "B. 1024", "C. 500", "D. 2048"],
        'correct_answer': "B",
        'explanation': "1024"
    },
    {
        'question': "Что покажет этот код?"
        """
        for i in range(5):
          if i % 2 == 0:
            continue
          print(i)
        """,
        'options': ["A. Ошибку из-за неверного вывода", "B. Числа: 1, 3 и 5", "C. Числа: 1 и 3", "D. Числа: 0, 2 и 4"],
        'correct_answer': "C",
        'explanation': "Числа: 1 и 3"
    },
    {
        'question': "Какая функция выводит что-либо в консоль?",
        'options': ["A. write();", "B. log();", "C. out();", "D. print();"],
        'correct_answer': "D",
        'explanation': "print();"
    },
    {
        'question': "Что будет результатом этого кода?"
        """
        x = 23
        num = 0 if x > 10 else 11
        print(num)
        """,
        'options': ["A. 23", "B. 0", "C. Ошибка", "D. 11"],
        'correct_answer': "B",
        'explanation': "0"
    },
    {
        'question': "Какие ошибки допущены в коде ниже?"
        """
        def factorial(n):
          if n == 0:
            return 1
          else:
            return n * factorial(n - 1)
        print(factorial(5))
        """,
        'options': ["A. Функция не может вызывать сама себя", "B. Необходимо указать тип возвращаемого значения", "C. В коде нет никаких ошибок", "D. Функция всегда будет возвращать 1"],
        'correct_answer': "C",
        'explanation': "В коде нет никаких ошибок"
    },
    {
        'question': "Что будет показано в результате?"
        """
        name = "John"
        print('Hi, %s' % name)
        """,
        'options': ["A. Hi, John", "B. Ошибка", "C. Hi,", "D. Hi, name"],
        'correct_answer': "A",
        'explanation': "Hi, John"
    },
]

user_progress = {}

random.shuffle(questions_data)

@dp.message_handler(commands=['💻code'])
async def command_help(message: types.Message):
    user_id = message.from_user.id

    # Initialize or reset user progress
    user_progress[user_id] = {
        'current_question_index': 0,
        'correct_answers': 0,
    }

    await bot.send_message(chat_id=message.chat.id, text='🤖')
    current_question_index = user_progress[user_id]['current_question_index']
    current_question = questions_data[current_question_index]
    await bot.send_message(chat_id=message.chat.id, text=current_question["question"] + "\n" + "\n".join(current_question["options"]))
    await bot.send_message(chat_id=message.chat.id, text="Введите букву вашего выбора:")

@dp.message_handler(lambda message: message.text.upper() in ['A', 'B', 'C', 'D'])
async def handle_user_answer(message: types.Message):
    user_id = message.from_user.id
    user_progress_data = user_progress.get(user_id)

    if user_progress_data:
        current_question_index = user_progress_data['current_question_index']
        correct_answers = user_progress_data['correct_answers']

        current_question = questions_data[current_question_index]
        correct_answer = current_question["correct_answer"]

        if message.text.upper() == correct_answer:
            await bot.send_message(chat_id=message.chat.id, text="Верно! " + current_question["explanation"])
            user_progress_data['correct_answers'] += 1
        else:
            await bot.send_message(chat_id=message.chat.id, text=f"Неверно. Правильный ответ: {correct_answer}.")

        # Move to the next question
        user_progress_data['current_question_index'] += 1

        if current_question_index + 1 < len(questions_data):
            next_question = questions_data[current_question_index + 1]
            await bot.send_message(chat_id=message.chat.id, text="Следующий вопрос:")
            await bot.send_message(chat_id=message.chat.id, text=next_question["question"] + "\n" + "\n".join(next_question["options"]))
            await bot.send_message(chat_id=message.chat.id, text="Введите букву вашего выбора:")
        else:
            await bot.send_message(chat_id=message.chat.id, text=f"Викторина завершена. Вы ответили правильно на {correct_answers} из {len(questions_data)} вопросов.")
            # Reset user progress after completing the quiz
            user_progress.pop(user_id)
    else:
        await bot.send_message(chat_id=message.chat.id, text="Что-то пошло не так. Попробуйте начать викторину снова.")











































@dp.message_handler(commands=['🤓Study'])
async def command_help(message: types.Message):
    ld = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/🎥video')
    h3 = KeyboardButton('/📘book')
    ld.insert(h2).insert(h3).insert(h1)
    study = """
------------------------------------------------

🎥[video] Ведио ролик арқылы курс өту

📘[book] Арнайы кітаптар арқылы үйрену

------------------------------------------------
"""
    await bot.send_message(chat_id=message.chat.id, text=study, reply_markup=ld)



@dp.message_handler(commands=['🎥video'])
async def command_help(message: types.Message):
    ggggg = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/🇷🇺RU')
    h3 = KeyboardButton('/🇺🇸US')
    h4 = KeyboardButton('/🇰🇿KZ')
    ggggg.insert(h2).insert(h3).insert(h4).insert(h1)
    study = """
------------------------------------------------
🤖 қай тілдегі видео ны көргіңіз келеді

        🇷🇺[RU]  🇺🇸[US]  🇰🇿[KZ]

------------------------------------------------
"""
    await bot.send_message(chat_id=message.chat.id, text=study, reply_markup=ggggg)


@dp.message_handler(commands=['🇷🇺RU'])
async def command_help(message: types.Message):
    text_vidru = """
---------------------------------------------------------------

🤖 Міне сізге Орыс тілінен керек 21 ведио \n осы арқылы сіз <b>"python"</b> тілін жақсы үйреніп шығасыз

<b>ютубер:</b> itProger
<b>Ссылка:</b> https://youtube.com/@itproger?si=SxngOF2MVHqRL48_ 

----------------------------------------------------------------
"""
    ikk = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='(1)video', url='https://youtu.be/34Rp6KVGIEM?si=vi9_Y_aM8CH7U3sH')
    button2 = InlineKeyboardButton(text='(2)video', url='https://youtu.be/CfqX2_xY8VQ?si=9ChObSHvFU7qFhQA') 
    button3 = InlineKeyboardButton(text='(3)video', url='https://youtu.be/ML5tP8m6SHw?si=-0n4OvXoZPJY322i') 
    button4 = InlineKeyboardButton(text='(4)video', url='https://youtu.be/DZvNZ9l9NT4?si=1GeM2IxfZxc_8SVF')
    button5 = InlineKeyboardButton(text='(5)video', url='https://youtu.be/SUDNfS_0X-Q?si=jZjwCD0oo0qef3EY')
    button6 = InlineKeyboardButton(text='(6)video', url='https://youtu.be/vMD6-jzgDvI?si=fi_iMX-QDUfwNJPA')
    button7 = InlineKeyboardButton(text='(7)video', url='https://youtu.be/-X2ubBdP2Ak?si=jAuGS7r7aG9qS71_')
    button8 = InlineKeyboardButton(text='(8)video', url='https://youtu.be/pqaBWcsBGyA?si=nMTaEnSTFU1RBjax')
    button9 = InlineKeyboardButton(text='(9)video', url='https://youtu.be/cQfu-hYo2o4?si=uvc2wmAY9Ms9WzHr')
    button10 = InlineKeyboardButton(text='(10)video', url='https://youtu.be/W2oO1Y-QDzo?si=2wz7FtNdLfHIEmri')
    button11 = InlineKeyboardButton(text='(11)video', url='https://youtu.be/6eNtZ8wY7qI?si=UpSCc1r6h2NCcL5E')
    button12 = InlineKeyboardButton(text='(12)video', url='https://youtu.be/6K5v4--G__U?si=G4VN1doaWDi1xJTX')
    button13 = InlineKeyboardButton(text='(13)video', url='https://youtu.be/t-xQAhLNYSs?si=l8ikmyg2--MCGfVx')
    button14 = InlineKeyboardButton(text='(14)video', url='https://youtu.be/3nveLco08Y0?si=3BvsZf18YLo7hRJk')
    button15 = InlineKeyboardButton(text='(15)video', url='https://youtu.be/uGsSTZjUoIc?si=CrMb23ALdMVLMXZX')
    button16 = InlineKeyboardButton(text='(16)video', url='https://youtu.be/dNg3l-wpRdY?si=DH9n-jcbfbjX412f')
    button17 = InlineKeyboardButton(text='(17)video', url='https://youtu.be/gFRa6qVN980?si=vKOH0A3DW6ayKspX')
    button18 = InlineKeyboardButton(text='(18)video', url='https://youtu.be/Y6N-na2WOx8?si=PR3VxibqK9VkrsCY')
    button19 = InlineKeyboardButton(text='(19)video', url='https://youtu.be/4N4GSzLF7JM?si=JBkvN9g9Un5W3hNQ')
    button20 = InlineKeyboardButton(text='(20)video', url='https://youtu.be/tuFuDKE7DF8?si=MDCOdPjk-SRbG3D0')
    button21 = InlineKeyboardButton(text='(21)video', url='https://youtu.be/-viVz4cwDU4?si=i7i1oeMC39JYmBv8')
    ikk.insert(button1).insert(button2).insert(button3).insert(button4).insert(button5).insert(button6).insert(button7).insert(button8).insert(button9).insert(button10).insert(button11).insert(button12).add(button13).insert(button14).insert(button15).insert(button16).insert(button17).insert(button18).insert(button19).insert(button20).insert(button21)
    await bot.send_message(chat_id=message.chat.id, text=text_vidru, reply_markup=ikk, parse_mode='HTML')


@dp.message_handler(commands=['🇰🇿KZ'])
async def command_help(message: types.Message):
    text_vidkz = """
---------------------------------------------------------------

🤖 Міне сізге Қазақ тілінен керек 19 ведио \n осы арқылы сіз <b>"python"</b> тілін жақсы үйреніп шығасыз!!

<b>ютубер:</b> ҚАЗАҚША САБАҚТАР
<b>Ссылка:</b> https://youtube.com/@Roboforce?si=OC1W7C_qDftyd5N2

❗❗ егер орыс тілін білсеңіз сол тілдегі практика видеоларын көруді ұсынамын :)

----------------------------------------------------------------
"""
    ikkk = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='(1)video', url='https://youtu.be/zvhIzR9E9Dg?si=A63EvUGtbSBKWme-')
    button2 = InlineKeyboardButton(text='(2)video', url='https://youtu.be/gLtvohHj1MA?si=-38PJY8_huob7KPW') 
    button3 = InlineKeyboardButton(text='(3)video', url='https://youtu.be/5yEDf2B9nBo?si=nTexemFhGkngdqPU') 
    button4 = InlineKeyboardButton(text='(4)video', url='https://youtu.be/xtsqdHTabWY?si=lErrPzBCJO7ZirlU')
    button5 = InlineKeyboardButton(text='(5)video', url='https://youtu.be/m9kz1eJy98k?si=9AbenCi7-C_ifatb')
    button6 = InlineKeyboardButton(text='(6)video', url='https://youtu.be/1WBXTHM6YY4?si=nbeCyMVGitnYv-o2')
    button7 = InlineKeyboardButton(text='(7)video', url='https://youtu.be/ItEYBd7Ra34?si=cbFJdKI-DkwRNa1U')
    button8 = InlineKeyboardButton(text='(8)video', url='https://youtu.be/pMkhuiBN1HA?si=K8Ye8-lwuiJG7ofH')
    button9 = InlineKeyboardButton(text='(9)video', url='https://youtu.be/k7oAhAx2EJU?si=pCAuh7_pqs2pUkFj')
    button10 = InlineKeyboardButton(text='(10)video', url='https://youtu.be/YtkQVGfGKWU?si=hv95bmIWf-1dTzpf')
    button11 = InlineKeyboardButton(text='(11)video', url='https://youtu.be/sQ9y7tBRBSQ?si=9bOoPDQ2SFJImOnT')
    button12 = InlineKeyboardButton(text='(12)video', url='https://youtu.be/jBpZI7MOD0c?si=IXzx4SoHvRxF5XhW')
    button13 = InlineKeyboardButton(text='(13)video', url='https://youtu.be/SV8sVnkhEZc?si=1fY7uOssDDgA13WD')
    button14 = InlineKeyboardButton(text='(14)video', url='https://youtu.be/SViuYhSyBzA?si=zgAJwlq0-6wRuQoe')
    button15 = InlineKeyboardButton(text='(15)video', url='https://youtu.be/LYSljxML7Co?si=rTkr5_0D7w44Poiu')
    button16 = InlineKeyboardButton(text='(16)video', url='https://youtu.be/mfju8K3wZrE?si=x8WSkahjhx9GIFjO')
    button17 = InlineKeyboardButton(text='(17)video', url='https://youtu.be/63aUbuBZ_Rg?si=nTopWjkUrHcOh80P')
    button18 = InlineKeyboardButton(text='(18)video', url='https://youtu.be/7Bba4pCvymc?si=FRa0TXQhtsqdcKNI')
    button19 = InlineKeyboardButton(text='(19)video', url='https://youtu.be/05kINCxYCFc?si=YsxZU-Pn6UWryyNj')
    ikkk.insert(button1).insert(button2).insert(button3).insert(button4).insert(button5).insert(button6).insert(button7).insert(button8).insert(button9).insert(button10).insert(button11).insert(button12).add(button13).insert(button14).insert(button15).insert(button16).insert(button17).insert(button18).insert(button19)
    await bot.send_message(chat_id=message.chat.id, text=text_vidkz, reply_markup=ikkk, parse_mode='HTML')


@dp.message_handler(commands=['🇺🇸US'])
async def command_help(message: types.Message):
    text_vidus = """
---------------------------------------------------------------

🤖 Here are 19 vedios you need from English \n with this you will learn <b>"python"</b> well!!

<b>YouTuber:</b> NetworkChuck
<b>link:</b> https://www.youtube.com/@NetworkChuck

❗❗ if you know English, I recommend watching practice videos in the same language :)

----------------------------------------------------------------
"""
    ik = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text='(1)video', url='https://www.youtube.com/watch?v=mRMmlo_Uqcs&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp')
    button2 = InlineKeyboardButton(text='(2)video', url='https://www.youtube.com/watch?v=IXr0-J5XXMA&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=2') 
    button3 = InlineKeyboardButton(text='(3)video', url='https://www.youtube.com/watch?v=T6OLDHAWjjA&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=3') 
    button4 = InlineKeyboardButton(text='(4)video', url='https://www.youtube.com/watch?v=5-5Mf_L0UKw&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=4')
    button5 = InlineKeyboardButton(text='(5)video', url='https://www.youtube.com/watch?v=Ec9WQGw4lW0&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=5')
    button6 = InlineKeyboardButton(text='(6)video', url='https://www.youtube.com/watch?v=nD1REhS6e3Y&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=6')
    button7 = InlineKeyboardButton(text='(7)video', url='https://www.youtube.com/watch?v=1KLgcBcWCsE&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=7')
    button8 = InlineKeyboardButton(text='(8)video', url='https://www.youtube.com/watch?v=rW5sCgSSpI8&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=8')
    button9 = InlineKeyboardButton(text='(9)video', url='https://www.youtube.com/watch?v=jdTwCSxNINA&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=9')
    button10 = InlineKeyboardButton(text='(10)video', url='https://www.youtube.com/watch?v=fR_D_KIAYrE&list=PLIhvC56v63ILPDA2DQBv0IKzqsWTZxCkp&index=10')
    ik.insert(button1).insert(button2).insert(button3).insert(button4).insert(button5).insert(button6).insert(button7).insert(button8).insert(button9).insert(button10)
    await bot.send_message(chat_id=message.chat.id, text=text_vidus, reply_markup=ik, parse_mode='HTML')



@dp.message_handler(commands=['📘book'])
async def command_help(message: types.Message):
    gggf = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/🏫shcool')
    h3 = KeyboardButton('/🔍dop')
    gggf.insert(h2).insert(h3).insert(h1)
    texttext = """
-------------------------------------------

🏫[shcool] Мектеп бағдарламасының кітаптарын алу

🔍[dop] қосымша көмекші кітаптар

-------------------------------------------
"""
    await bot.send_message(chat_id=message.chat.id, text=texttext, reply_markup=gggf, parse_mode='HTML')


@dp.message_handler(commands=['🏫shcool'])
async def command_help(message: types.Message):
    boock = """
-------------------------------------------------------

|Информатика 11 сынып ЖМБ| https://drive.google.com/file/d/1RKuAtLb12r2oOpGuoZlnvfQeZih1-PuM/view?usp=share_link
|Информатика 11 сынып ҚГБ| https://drive.google.com/file/d/1kyrFuqzKMNns6r2WQdMqigkW5E50PpP-/view?usp=share_link

-------------------------------------------------------

|Информатика 10 сынып ЖМБ| https://drive.google.com/file/d/1nrIlejgmuGdtcC9k_n2d6ajMWoS9ZODD/view?usp=share_link
|Информатика 10 сынып ҚГБ| https://drive.google.com/file/d/1Qrh4D1x1GwR3huJ8QLTzp1bKnDL0UamA/view?usp=share_link

-------------------------------------------------------

|Информатика 9 сынып| https://drive.google.com/file/d/1Y9TDgjR0L9MFO2g5YI2nwPPsv3kHi834/view?usp=share_link
|Информатика 8 сынып| https://drive.google.com/file/d/1uYPQyhorYjK2NTljrwmkJ08EU7BY_3O1/view?usp=share_link
|Информатика 7 сынып| https://drive.google.com/file/d/1m2IpFlfdkW5ppKsLwviuAlcA22Vz4Yjb/view?usp=share_link
|Информатика 6 сынып| https://drive.google.com/file/d/1Arof57Dz5fQsWHITd9FKGclefnTfKVzb/view?usp=share_link
|Информатика 5 сынып| https://drive.google.com/file/d/1Uk8CfY99KGD2ce5vIoZcRP7Egi4YHSRJ/view?usp=share_link
|Цифрлық сауаттылық 4 сынып| https://drive.google.com/file/d/1fUt1x2iG0Chde8qB78RFAPXYn34VJ2mH/view?usp=share_link
|Цифрлық сауаттылық 3 сынып| https://drive.google.com/file/d/13lVlGdJjlA8ku6K6Ej2gKoV5mauOLIIv/view?usp=share_link
|Цифрлық сауаттылық 2 сынып| https://drive.google.com/file/d/1RMfyNvea53FPMWOmWRJeiI42n68jbQec/view?usp=share_link
|Цифрлық сауаттылық 1 сынып| https://drive.google.com/file/d/1ZuTqnHSCyO_u1ZOLRdO0GCpbdALakfVQ/view?usp=share_link

-------------------------------------------------------
"""
    await bot.send_message(chat_id=message.chat.id, text=boock)


@dp.message_handler(commands=['🔍dop'])
async def command_help(message: types.Message):
    dop = """
-----------------------------------------------------

🤖 <b>бол қосымша кітаптар саған көмек теседі</b>

[Чистый Python] https://drive.google.com/file/d/1Cb5MejPIL6HSZ7P5UEXAwdVzJichwia1/view?usp=sharing

[Математика на Python] https://drive.google.com/file/d/1FUrSlbuuwcQ5_bnqioSt7qldD9C0GpPG/view?usp=sharing

-----------------------------------------------------
"""
    await bot.send_message(chat_id=message.chat.id, text=dop, parse_mode='HTML')


@dp.message_handler(commands=['💾Packages'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='🤖[https://github.com/aespi808/tg_bot]', parse_mode='HTML')


@dp.message_handler(commands=['🕹Game-projeck'])
async def command_help(message: types.Message):
    aaa = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/🔍Угадай-чесло')
    h3 = KeyboardButton('/🏓Pinc_ponc')
    aaa.insert(h2).insert(h3).insert(h1)
    listtt = """
---------------------------------------------------------
🤖 қалаған ойыныңызды таңдаңыз және оның қалай жасалғанын талдаңыз

<b>🔍[Угадай-чесло]</b> <em>ползовотель должен угадать чесло от 1 до 10</em>

<b>🏓[Pinc_ponc]</b> игра для 2 человек

---------------------------------------------------------
"""
    await bot.send_message(chat_id=message.chat.id, text=listtt, parse_mode='HTML', reply_markup=aaa)


@dp.message_handler(commands=['🔍Угадай-чесло'])
async def command_help(message: types.Message):
    mm = """
---------------------------------------------------------
🤖 Вам не надо скачивать модуль <b>"random"</b> \n так как он встроен на пайтон

Скапируйте код и тестируйте...

---------------------------------------------------------
"""

    code = """
    # Импортируем модуль для генерации случайных чисел
    import random

    # Функция для запуска игры
    def guess_the_number():
        # Генерируем случайное число от 1 до 10
        secret_number = random.randint(1, 10)
        
        # Выводим приветствие и объяснение правил игры
        print("Добро пожаловать в игру 'Угадай число до 10'!")
        print("Я загадал число от 1 до 10. Попробуй угадать.")
        
        # Начинаем бесконечный цикл - игра продолжается, пока число не угадано
        while True:
            # Получаем ввод от пользователя
            guess = int(input("Введи свой вариант: "))
            
            # Проверяем, угадал ли пользователь число
            if guess == secret_number:
                print("Поздравляю! Ты угадал число!")
                break  # Выходим из цикла, так как число угадано
            else:
                print("Не угадал. Попробуй еще раз.")  # Выводим подсказку

    # Запускаем игру
    guess_the_number()
"""

    formatted_message = f"```\n{code}\n```"
    await bot.send_message(chat_id=message.chat.id, text=mm, parse_mode='HTML')
    await bot.send_message(chat_id=message.chat.id, text=formatted_message, parse_mode='MarkdownV2')


@dp.message_handler(commands=['🏓Pinc_ponc'])
async def command_help(message: types.Message):
    mmv = """
---------------------------------------------------------
🤖 Вам надо установить модуль "pygame" \n вот установчик "pip install pygame"

👱🏼‍♂️управление 1 го играка
[w] Верх   [s] Вниз

👩🏻управление 2 го играка
[🔼] Верх   [🔽 ]Вниз

Скапируйте код и тестируйте...
Код был разделён иза того что в телеграме есть ограничение

---------------------------------------------------------
"""

    code = """
# Импортируем модуль Pygame для создания игр
import pygame
import random
import time

# Инициализация Pygame
pygame.init()

# Создаем окно игры
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption('My game')

# Инициализация часов для управления FPS
clock = pygame.time.Clock()

# Инициализация игровых объектов: два игрока (player и player2), мяч (ball),
# а также преграды npsshar1-6
player = pygame.rect.Rect(10, 200, 20, 100)
player2 = pygame.rect.Rect(885, 200, 20, 100)
ball = pygame.rect.Rect(445, 245, 20, 20)
npsshar = pygame.rect.Rect(400, 200, 70, 70)
npsshar2 = pygame.rect.Rect(430, 1, 10, 600)
npsshar3 = pygame.rect.Rect(40, 1, 10, 1000)
npsshar4 = pygame.rect.Rect(850, 1, 10, 1000)
npsshar5 = pygame.rect.Rect(1, 1, 910, 10)
npsshar6 = pygame.rect.Rect(1, 490, 910, 10)

# Инициализация скорости мяча и стартовых значений для игры
ball_speed_x = -6
ball_speed_y = 6
running = True
player_speed_y = 0
player2_speed_y = 0

# Инициализация счетчиков голов для каждого игрока
score_player1 = 0
score_player2 = 0

# Инициализация шрифта для отображения текста
font = pygame.font.Font(None, 36)

# Установка времени игры на 5 минут (300 секунд)
game_duration = 300
start_time = time.time()

# Функция для обновления положения мяча
def update_ball():
    global ball_speed_x, ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.colliderect(player) or ball.colliderect(player2):
        ball_speed_x = -ball_speed_x
    if ball.y <= 0 or ball.y >= 490:
        ball_speed_y = -ball_speed_y

# Функция для сброса положения мяча
def reset_ball():
    global ball
    ball.x = random.randint(0, 890)
    ball.y = random.randint(0, 490)

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed_y = -6
            if event.key == pygame.K_s:
                player_speed_y = 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player_speed_y = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_speed_y = -6
            if event.key == pygame.K_DOWN:
                player2_speed_y = 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_speed_y = 0
# Обработка событий голов (гол для player1 и player2) част кода 🔽
"""
    code1 = """
# Обработка событий голов (гол для player1 и player2) част кода 🔼
    if ball.x <= 0:
        score_player2 += 1
        reset_ball()

    if ball.x >= 880:
        score_player1 += 1
        reset_ball()

    # Обновление положения игроков и мяча
    player2.y += player2_speed_y
    player.y += player_speed_y
    update_ball()

    # Отрисовка объектов на экране
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (20, 200, 20), player)
    pygame.draw.rect(screen, (200, 20, 20), player2)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    pygame.draw.ellipse(screen, (100, 100, 100), npsshar)
    pygame.draw.rect(screen, (100, 100, 100), npsshar2)
    pygame.draw.rect(screen, (20, 200, 20), npsshar3)
    pygame.draw.rect(screen, (200, 20, 20), npsshar4)
    pygame.draw.rect(screen, (200, 200, 200), npsshar5)
    pygame.draw.rect(screen, (200, 200, 200), npsshar6)

    # Отображение счета на экране
    text = font.render(f"        {score_player1}    {score_player2}", True, (255, 255, 255))
    screen.blit(text, (350, 10))

    # Рассчитываем оставшееся время
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, game_duration - elapsed_time)

    # Отображаем оставшееся время на экране
    timer_text = font.render(f"Time: {remaining_time} seconds", True, (255, 255, 255))
    screen.blit(timer_text, (350, 50))

    # Проверяем, не истекло ли время
    if remaining_time <= 0:
        running = False

    # Обновление экрана и управление FPS
    pygame.display.flip()
    clock.tick(60)

# Вывод сообщения о завершении игры
if score_player1 > score_player2:
    winner_text = font.render("Player 1 wins!", True, (255, 255, 255))
elif score_player2 > score_player1:
    winner_text = font.render("Player 2 wins!", True, (255, 255, 255))
else:
    winner_text = font.render("It's a draw!", True, (255, 255, 255))

screen.blit(winner_text, (350, 200))
pygame.display.flip()

# Ожидание закрытия окна
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

"""

    formatted_message = f"```\n{code}\n```"
    formatted_message1 = f"```\n{code1}\n```"
    await bot.send_message(chat_id=message.chat.id, text=formatted_message, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=message.chat.id, text=formatted_message1, parse_mode='MarkdownV2')
    await bot.send_message(chat_id=message.chat.id, text=mmv, parse_mode='HTML')




@dp.message_handler(commands=['📦exe'])
async def command_help(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text='🤖 [https://code.mu/ru/python/tasker/stager/]', parse_mode='HTML')



@dp.message_handler(commands=['menu'])
async def command_help(message: types.Message):
    ff = ReplyKeyboardMarkup(resize_keyboard=True)
    h1 = KeyboardButton('/menu')
    h2 = KeyboardButton('/🤓Study')
    h3 = KeyboardButton('/📚ҰБТ')
    h4 = KeyboardButton('/💾Packages')
    h5 = KeyboardButton('/🕹Game-projeck')
    h6 = KeyboardButton('/📦exe')
    ff.add(h2).insert(h3).insert(h4).insert(h5).insert(h6).insert(h1)
    await bot.send_message(chat_id=message.chat.id, text=help_cmd, parse_mode='HTML', reply_markup=ff)

@dp.message_handler(commands=['send_code'])
async def send_code(message: types.Message):
    code = """
def hello():
    print("Hello, World!")

hello()
"""

    # Переносим код в блок кода Markdown
    formatted_message = f"```\n{code}\n```"

    await bot.send_message(chat_id=message.chat.id, text=formatted_message, parse_mode='MarkdownV2')

# Добавим новую команду, которая будет ожидать интернет-соединение
@dp.message_handler(commands=['wait_for_internet'])
async def command_wait_for_internet(message: types.Message):
    await bot.send_message(message.chat.id, 'Ожидание подключения к интернету...')
    
    while True:
        try:
            # Попробуем выполнить запрос к какому-то ресурсу (например, google.com)
            response = bot.get_me()
            
            # Если успешно, выходим из цикла
            break
        except Exception as e:
            print(f"Error: {e}")
            # Если возникает ошибка, подождем 10 секунд перед следующей попыткой
            time.sleep(5)
    
    await bot.send_message(message.chat.id, 'Подключение к интернету восстановлено!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
