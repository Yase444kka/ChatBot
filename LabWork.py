import os
import random
import math
from math import pi
import datetime
import sys


topic_history = []
topics_dictionary = {
    'математика': {'квадратні рівняння', 'скалярний добуток', 'довжина відрізка між двома точками на площині', 'площа кола'},
    'фізика': {'формула ампера' , 'закон збереження енергії'},
    'географія': {'найбільше озеро у світі', 'де знаходиться сахара', 'найбільше місто за населенням', 'знайти координати точки'},
    'філологія': {'різниця між present simple та present continuous', 'passive voice у present simple', 'роди іменників в українській мові', 'часи в англійській мові'},
    'астрономія': {'космічне випромінювання', 'найменші та найбільші орбіти планет сонячної системи', 'сонячні процеси та як вони впливають на землю'},
    'загальні питання': {'який зараз рік', 'камінь-ножиці-папір', 'зачитати вірш', 'виписати цитату'},
    'програмування': {'семафори', 'парсінг', 'змінна', 'функція'}
}

poems = {
    1: {
        'text': 'Назва: Встала весна\nАвтор: Тарас Шевченко (Уривок із поеми «Гайдамаки»)\nВстала весна, чорну землю\n'
                                                                                            'Сонну розбудила,\n'
                                                                                            'Уквітчала її рястом,\n'
                                                                                            'Барвінком укрила;\n'
                                                                                            'І на полі жайворонок,\n'
                                                                                            'Соловейко в гаї\n'
                                                                                            'Землю, убрану весною,\n'
                                                                                            'Вранці зустрічають...'
    },
    2: {'text': 'Назва: *****\nАвтор: Ліна Костенко\nНе знаю, чи побачу Вас, чи ні.\n'
                                                    'А може, власне, і не в тому справа.\n'
                                                    'А головне, що десь вдалечині\n'
                                                    'є хтось такий, як невтоленна спрага.\n'
                                                    
                                                    'Я не покличу щастя не моє.\n'
                                                    'Луна луни туди не долітає.\n'
                                                    'Я думаю про Вас. Я знаю, що Ви є.\n'
                                                    'Моя душа й від цього вже світає.\n'},

    3: {'text': 'Назва: *****\nАвтор: Олександр Олесь\nОдну я любив за веселість,\n'
                                                        'Другу я за вроду кохав,\n'
                                                        'А третій за соняшний усміх\n'
                                                        'Квітками дорогу встилав.\n'
                                                        
                                                        'Ти зовсім була не вродлива\n'
                                                        'І завжди, як вечір, смутна…\n'
                                                        'Чого ж ти з усіх моїх милих\n'
                                                        'У серці осталась одна?!.\n'},
    4: {'text': 'Назва: *****\nАвтор: Василь Симоненко\nВсе було. Дорога закричала,\n'
                                                        'Блиснули байдужі ліхтарі.\n'
                                                        'Ти пішла від мене до причалу\n'
                                                        'І згоріла в полум’ї зорі.\n'
                                                        
                                                        'Вибухали дні незрозуміло\n'
                                                        'І життя котилося моє…\n'
                                                        'Але там, де ти тоді згоріла,\n'
                                                        'Кожен ранок сонце устає.\n'},
    5: {'text': 'Назва: *****\nАвтор: Денис Нарбут \nСвобода йде, прискорюючи хід,\n'
                                                    'І квітне сила у зів\'ялих травах,\n'
                                                    'гілля́ підносять Лондон і Варшава,\n'
                                                    'Свобода йде із заходу на схід.\n'
                                                    'Усе палає навкруги ущент:\n'
                                                    'блакитне небо у багряній лаві\n'
                                                    'і Україна в боротьбі та славі\n'
                                                    'за вільний європейський континент,\n'
                                                    'аби життя продовжувалось в нім.\n'
                                                    'Незламний дух будує нові стіни,\n'
                                                    'Соборність – новий дах для України,\n'
                                                    'Свобода йде у свій майбутній дім!\n'}
}


quotes = {
    1: {'text': 'Ніколи не рано запитати себе: «Справою я займаюся чи дрібницями?»'},
    2: {'text': 'Щастя – це коли ти знаєш, що ти є, і ти цим задоволений.'},
    3: {'text': 'Любити – це бути сильним. Любити – це допомагати іншим бути сильними.'},
    4: {'text': 'Часом найкращий спосіб допомогти людині – це не заважати їй.'},
    5: {'text': 'Кохати когось – це бачити його таким, яким він є, і не бачити його недоліків.'},
}




log_file_name = f'dialog-{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.txt'
back_flag = False
help_flag = False
exit_flag = False


def find_point_b(x1, y1, d, theta):
    global back_flag
    # Convert azimuth from degrees to radians
    theta_rad = math.radians(theta)

    # Calculate x and y components of displacement vector
    dx = d * math.cos(theta_rad)
    dy = d * math.sin(theta_rad)

    # Calculate x and y coordinates of point B
    x2 = x1 + dx
    y2 = y1 + dy
    print_response('Координати точки B: ({:.2f}, {:.2f})'.format(x2, y2))
    back_flag = True

def set_flag(text):
    global back_flag
    global help_flag
    global exit_flag
    if text == 'назад':
        back_flag = True
    elif text == 'допомога':
        help_flag = True
    elif text == 'вихід':
        exit_flag = True
    else:
         return



def ampere(a, b):
    global back_flag
    u_0 = 4 * pi * 10**-7
    I = a
    r = b
    B = (u_0 * I) / (2 * pi * r)
    print_response(f'Індукція магнітного поля B = {B}')
    back_flag = True

def area(a):
    global back_flag
    x = 3.14 * a ** 2
    print_response(f'Площа кола = {x}')
    back_flag = True




def length(a,b,c,d):
    global back_flag
    x = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
    print_response(f'Довжина відрізка = {x}')
    back_flag = True



def scalar_product(koef, koef2):
    global back_flag
    dot_product = sum(a * b for a, b in zip(koef, koef2))
    length_koef = math.sqrt(sum(a ** 2 for a in koef))
    length_koef2 = math.sqrt(sum(b ** 2 for b in koef2))
    angle = math.acos(dot_product / (length_koef * length_koef2))
    scalar_product = length_koef * length_koef2 * math.cos(angle)
    print_response(f'Скалярний добуток = {scalar_product}')
    back_flag = True


def check_argument(x):
    if len(str(x)) != 1:
        return False
    try:
        float_x = float(x)
        return True
    except ValueError:
        return False


def quadratic_equation(a, b, c):
    global back_flag
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print_response(f'Ваші корені: x1 = {x1}, x2 = {x2}')
        back_flag = True
    elif d == 0:
        x = -b / (2 * a)
        print_response(f'Ваш корінь: x = {x}')
        back_flag = True
    else:
        print_response('Немає розв\'язків')
        back_flag = True



def print_greeting():
    global topics_dictionary
    greeting = f"""Бот: Вітаю, мене звати Ярополк. Ви можете
поставити мені запитання з таких тем: {', '.join(topics_dictionary.keys())}."""
    print_response(greeting)


def get_file_name():
    now = datetime.datetime.now()
    file_name = f'dialog-{now.strftime("%Y-%m-%d_%H-%M")}.txt'
    return file_name

def print_response(text, color='cyan'):
    colors = {
        'blue': '\033[34m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    color_code = colors.get(color.lower(), colors['white'])
    bot_tag = f'{colors["blue"]}[Bot]: {color_code}'
    print(f'{colors["reset"]}{bot_tag} {color_code}{text}{colors["reset"]}')
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'[Bot]: {text}\n')

def get_user_input():
    colors = {
        'yellow': '\033[33m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    user_tag = f'{colors["yellow"]}[User]: {colors["reset"]}'
    user_text = input(f'{user_tag}')
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'[User]: {user_text}\n')
    return user_text

file_name = get_file_name()



def print_help():
    help_message = ""
    if len(topic_history) == 0:
        help_message += "Введіть назву операції"
    else:
        help_message += f"""Ви обрали операцію «{get_current_topic()}»"""

    help_message += f"""\nДля виходу, напишіть «вихід».\nДля повернення до останньої теми напишіть «назад»."""
    print_response(help_message)


def get_main_topic():
    global topic_history
    if len(topic_history) == 0:
        return None
    return topic_history[0]



def get_current_topic():
    global topic_history
    if len(topic_history) == 0:
        return None
    return topic_history[-1]


print_greeting()

while True:
    try:
        if help_flag == True:
            help_flag = False
            print_help()
            continue
        elif back_flag == True:
            back_flag = False
            input_text = 'назад'
        elif exit_flag == True:
            exit_flag = False
            input_text = 'вихід'
        else:
            input_text = get_user_input()
    except KeyboardInterrupt:
        break

    if input_text.lower() == 'вихід':
        break

    if input_text.lower() == 'допомога':
        print_help()
        continue


    if input_text.lower() == 'назад':
        if len(topic_history) > 0:
            topic_history.pop()
        else:
            print_greeting()
            continue

        if len(topic_history) == 0:
            print_greeting()
            continue
    else:
        if input_text.lower() in topics_dictionary:
            topic_history.append(input_text)
        elif get_main_topic() is not None:
                if input_text.lower() in topics_dictionary[get_main_topic()]:
                    topic_history.append(input_text.lower())
                elif topic_history[-1] in topics_dictionary[get_main_topic()]:
                    pass
                else:
                    if get_main_topic() == 'математика':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'квадратні рівняння\n'
                                       'скалярний добуток\n'
                                       'довжина відрізка між двома точками на площині\n'
                                       'площа кола')
                        continue
                    elif get_main_topic() == 'фізика':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'формула ампера\n'
                                       'Підказка: Введіть «формула ампера» для знаходження В\n'
                                       'закон збереження енергії')
                        continue
                    elif get_main_topic() == 'географія':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'найбільше озеро у світі\n'
                                       'де знаходиться Сахара\n'
                                       'найбільше місто за населенням\n'
                                       'знайти координати точки\n'
                                       'Підказка: Знаходженя координат точки В відбувається за допомогою координат точки А (x1,y1), '
                                       'дистанції між двома точкама та азимуту')
                        continue
                    elif get_main_topic() == 'філологія':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'різниця між Present Simple та Present Continuous\n'
                                       'Passive Voice у Present Simple\n'
                                       'роди іменників в українській мові\n'
                                       'Часи в англійській мові\n')

                        continue
                    elif get_main_topic() == 'астрономія':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'космічне випромінювання\n'
                                       'найменші та найбільші орбіти планет сонячної системи\n'
                                       'сонячні процеси та як вони впливають на землю')
                        continue
                    elif get_main_topic() == 'загальні питання':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'який зараз рік\n'
                                       'камінь-ножиці-папір\n'
                                       'зачитати вірш\n'
                                       'виписати цитату (Надихаючу)\n'
                                       'Підказка: Введіть «виписати цитату» для отримання надихаючої цитати')
                        continue
                    elif get_main_topic() == 'програмування':
                        print_response('Я не знаю цієї теми. Натомість, Ви можете поставити мені запитання з таких тем:\n'
                                       'семафори\n'
                                       'змінна\n'
                                       'парсінг\n'
                                       'функція')
                        continue
        else:
            print_response('Я не знаю цієї теми')
            continue


     #Main topic logic
    if topic_history[-1] in topics_dictionary:
        current_topic = topic_history[-1]
        if topic_history[-1] == 'математика':
            print_response('Ви обрали тему «математика»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'квадратні рівняння\n'
                           'скалярний добуток\n'
                           'довжина відрізка між двома точками на площині\n'
                           'площа кола')
        elif topic_history[-1] == 'фізика':
            print_response('Ви обрали тему «фізика»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'формула ампера (Обчислення В)\n'
                           'Підказка: Введіть «формула ампера» для знаходження В\n'
                           'закон збереження енергії')
        elif topic_history[-1] == 'географія':
            print_response('Ви обрали тему «географія»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'найбільше озеро у світі\n'
                            'де знаходиться Сахара\n'
                           'найбільше місто за населенням\n'
                           'знайти координати точки\n'
                           'Підказка: Знаходженя координат точки В відбувається за допомогою координат точки А (x1,y1), '
                           'дистанції між двома точкама та азимуту')
        elif topic_history[-1] == 'філологія':
            print_response('Ви обрали тему «філологія»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'Різниця між Present Simple та Present Continuous\n'
                           'Passive Voice у Present Simple\n'
                           'Роди іменників в українській мові\n'
                           'Часи в англійській мові')
        elif topic_history[-1] == 'астрономія':
            print_response('Ви обрали тему «астрономія»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'космічне випромінювання\n'
                           'найменші та найбільші орбіти планет сонячної системи\n'
                           'сонячні процеси та як вони впливають на землю')
        elif topic_history[-1] == 'загальні питання':
            print_response('Ви обрали тему «загальні питання»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'який зараз рік\n'
                           'камінь-ножиці-папір\n'
                           'зачитати вірш\n'
                           'виписати цитату (Надихаючу)\n'
                           'Підказка: Введіть «виписати цитату» для отримання надихаючої цитати')
        elif topic_history[-1] == 'програмування':
            print_response('Ви обрали тему «програмування»')
            print_response('Ви можете поставити мені запитання з таких тем:\n'
                           'семафори\n'
                            'змінна\n'
                            'парсінг\n'
                            'функція')
        continue




    #Subtopic logic
    if topic_history[-1] in topics_dictionary[current_topic]:
      if current_topic == 'математика':
          # ---------Quadratic Equation ----------------
          if topic_history[-1] == 'квадратні рівняння':
            print_response('Ви обрали тему «квадратні рівняння»')
            print_response('Введіть коефіцієнти через кому (наприклад, 1,2,3):')
            try:
                while True:
                    koeficients = get_user_input()
                    if koeficients.lower() == 'назад' or koeficients.lower() == 'вихід' or koeficients.lower() == 'допомога':
                        set_flag(koeficients)
                        break
                    try:
                        koeficients = [float(x) for x in  koeficients.split(',')]
                        a, b, c =  koeficients
                        quadratic_equation(a, b, c)
                        break
                    except ValueError:
                        print_response('Будь ласка, введіть тільки числа та роздільник (,).')
            except KeyboardInterrupt:
                print_response('Радий був поспілкуватися, до зустрічі.')
                sys.exit(0)



          #---------Scalar Product----------------
          elif topic_history[-1] == 'скалярний добуток':
              print_response('Ви обрали тему «скалярний добуток»')
              print_response('Введіть коефіцієнти першого вектору через кому (наприклад 1,2,3):')
              try:
                  while True:
                      vector1 = get_user_input()
                      if vector1.lower() == 'назад' or vector1.lower() == 'вихід' or vector1.lower() == 'допомога':
                          set_flag(vector1)
                          break
                      print_response('Введіть коефіцієнти другого вектору через кому (наприклад 1,2,3):')
                      vector2 = get_user_input()
                      if vector2.lower() == 'назад' or vector2.lower() == 'вихід' or vector2.lower() == 'допомога':
                          set_flag(vector2)
                          break
                      try:
                          vector1 = [float(x) for x in vector1.split(',')]
                          vector2 = [float(x) for x in vector2.split(',')]
                          if len(vector1) != len(vector2):
                              print_response(
                                  'Кількість елементів у векторах не збігається. Будь ласка, введіть коефіцієнти знову.')
                              continue
                          scalar_product(vector1, vector2)
                          break
                      except ValueError:
                          print_response('Будь ласка, введіть тільки числа та роздільник (,).')
              except KeyboardInterrupt:
                print_response('Радий був поспілкуватися, до зустрічі.')
                sys.exit(0)

          #-------------------------Distance between two points---------------------------
          elif topic_history[-1] == 'довжина відрізка між двома точками на площині':
                print_response('Ви обрали тему «довжина відрізка між двома точками на площині»')
                print_response('Введіть координати першої точки через кому (наприклад, 1,2):')
                try:
                    while True:
                        point1 = get_user_input()
                        if point1.lower() == 'назад' or point1.lower() == 'вихід' or point1.lower() == 'допомога':
                            set_flag(point1)
                            break
                        print_response('Введіть координати другої точки через кому (наприклад, 1,2):')
                        point2 = get_user_input()
                        if point2.lower() == 'назад' or point2.lower() == 'вихід' or point2.lower() == 'допомога':
                            set_flag(point2)
                            break
                        try:
                            point1 = [float(x) for x in point1.split(',')]
                            point2 = [float(x) for x in point2.split(',')]
                            a, b = point1
                            c, d = point2
                            length(a, b, c, d)
                            break
                        except ValueError:
                            print_response('Будь ласка, введіть тільки числа та роздільник (,).')
                except KeyboardInterrupt:
                    print_response('Радий був поспілкуватися, до зустрічі.')
                    sys.exit(0)

          #-----------------Area of Circle---------------------
          elif topic_history[-1] == 'площа кола':
              print_response('Ви обрали тему «площа кола»')
              try:
                  while True:
                      print_response('Введіть радіус кола:')
                      radius = get_user_input()
                      if radius.lower() == 'назад' or radius.lower() == 'допомога' or radius.lower() == 'вихід':
                         set_flag(radius)
                         break
                      try:
                          radius = float(radius)
                          if radius < 0:
                              print_response('Радіус не може бути від\'ємним')
                              continue
                          area(radius)
                          break
                      except ValueError:
                          print_response('Будь ласка, введіть тільки число.')
              except KeyboardInterrupt:
                  print_response('Радий був поспілкуватися, до зустрічі.')
                  sys.exit(0)



      elif(current_topic == 'фізика'):
        #-----------------Amper's Formula---------------------
        if topic_history[-1] == 'формула ампера':
           print_response('Ви обрали тему «формула ампера»')
           print_response('Введіть силу струму')
           try:
               while True:
                I = get_user_input()
                if I.lower() == 'назад' or I.lower() == 'допомога' or I.lower() == 'вихід':
                    set_flag(I)
                    break

                print_response('Введіть довжину до провідника')
                r = get_user_input()
                if r.lower() == 'назад' or r.lower() == 'допомога' or r.lower() == 'вихід':
                    set_flag(r)
                    break
                if len(I.split(',')) == 1 and len(r.split(',')) == 1:
                    try:
                        I = float(I)
                        r = float(r)
                        ampere(I, r)
                        break
                    except ValueError:
                        print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                else:
                    print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
           except KeyboardInterrupt:
               print_response('Радий був поспілкуватися, до зустрічі.')
               sys.exit(0)



        elif topic_history[-1] == 'закон збереження енергії':
            #-----------------Energy---------------------
            print_response('Ви обрали тему «закон збереження енергії»')
            print_response('Ви можете обчислити кінетичну, потенціальну або внутрішню енергію.')
            try:
                while True:
                    print_response('Введіть тип енергії одним словом, наприклад: внутрішня')
                    energy_type = get_user_input().lower()

                    if energy_type.lower() == 'назад' or energy_type.lower() == 'допомога' or energy_type.lower() == 'вихід':
                        set_flag(energy_type)
                        break
                    if energy_type not in ['кінетична', 'потенціальна', 'внутрішня']:
                        print_response('Неправильний тип енергії, спробуйте ще раз.')
                        continue

                    if energy_type == 'кінетична':
                        print_response('Введіть потенційну енергію')
                        potential_energy = get_user_input()
                        if potential_energy.lower() == 'назад' or potential_energy.lower() == 'допомога' or potential_energy.lower() == 'вихід':
                            set_flag(potential_energy)
                            break
                        elif check_argument(potential_energy) == False:
                            print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                            continue
                        print_response('Введіть внутрішню енергію')
                        inner_energy = get_user_input()
                        if inner_energy.lower() == 'назад' or inner_energy.lower() == 'допомога' or inner_energy.lower() == 'вихід':
                            set_flag(inner_energy)
                            break
                        elif check_argument(inner_energy) == False:
                            print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                            continue
                        kinetic_energy = -float(potential_energy) - float(inner_energy)
                        print_response(f'Внутрішня енергія: {kinetic_energy} + const')
                        back_flag = True
                        break

                    if energy_type == 'потенціальна':
                        print_response('Введіть кінетичну енергію')
                        kinetic_energy = get_user_input()
                        if kinetic_energy.lower() == 'назад' or kinetic_energy.lower() == 'допомога' or kinetic_energy.lower() == 'вихід':
                            set_flag(kinetic_energy)
                            break
                        elif check_argument(kinetic_energy) == False:
                            print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                            continue
                        print_response('Введіть внутрішню енергію')
                        inner_energy = get_user_input()
                        if inner_energy.lower() == 'назад' or inner_energy.lower() == 'допомога' or inner_energy.lower() == 'вихід':
                            set_flag(inner_energy)
                            break
                        elif check_argument(inner_energy) == False:
                            print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                            continue
                        potential_energy = -float(kinetic_energy) - float(inner_energy)
                        print_response(f'Внутрішня енергія: {potential_energy} + const')
                        back_flag = True
                        break


                    if energy_type == 'внутрішня':
                        print_response('Введіть кінетичну енергію')
                        kinetic_energy = get_user_input()
                        if kinetic_energy.lower() == 'назад' or kinetic_energy.lower() == 'допомога' or kinetic_energy.lower() == 'вихід':
                            set_flag(kinetic_energy)
                            break
                        elif check_argument(kinetic_energy) == False:
                            print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                            continue
                        print_response('Введіть потенціальну енергію')
                        potential_energy = get_user_input()
                        if potential_energy.lower() == 'назад' or potential_energy.lower() == 'допомога' or potential_energy.lower() == 'вихід':
                            set_flag(potential_energy)
                            break
                        elif check_argument(potential_energy) == False:
                            print_response('Помилка: у коефіцієнтах має бути одне дійсне число')
                            continue
                        inner_energy = -float(kinetic_energy) - float(potential_energy)
                        print_response(f'Внутрішня енергія: {inner_energy} + const')
                        back_flag = True
                        break
            except KeyboardInterrupt:
                print_response('Радий був поспілкуватись, до зустрічі.')
                sys.exit(0)

      elif(current_topic == 'програмування'):
          #---------------------Semaphores-------------------------
          if topic_history[-1] == 'семафори':
              print_response('Ви обрали тему «семафори»')
              print_response('Семафори — це спеціальні об’єкти, '
                             'які використовуються для управління доступом до спільних ресурсів.')
              back_flag = True
              continue
          #------------------------Variable---------------------------
          elif topic_history[-1] == 'змінна':
              print_response('Ви обрали тему «змінна»')
              print_response('Змінна — це іменоване місце в пам’яті, '
                             'яке зберігає певне значення.')
              back_flag = True
              continue
          #----------------------Parsing------------------------------
          elif topic_history[-1] == 'парсінг':
              print_response('Ви обрали тему «парсінг»')
              print_response('Парсінг — це процес аналізу даних, '
                               'який виконується комп’ютером, '
                               'щоб зрозуміти їхню структуру.')
              back_flag = True
              continue
          #----------------------Function-----------------------------
          elif topic_history[-1] == 'функція':
              print_response('Ви обрали тему «функція»')
              print_response('Функція — це певна послідовність дій, '
                             'яку можна викликати з іншого місця програми.')
              back_flag = True
              continue

      elif(current_topic == 'географія'):
            #-------------The biggest lake in the world----------------
            if topic_history[-1] == 'найбільше озеро у світі':
                print_response('Ви обрали тему «найбільше озеро у світі»')
                print_response('Найбільше озеро у світі — Каспійське море')
                back_flag = True
                continue
            #--------------Where is Sahara desert----------------------
            elif topic_history[-1] == 'де знаходиться сахара':
                print_response('Ви обрали тему «де знаходиться Сахара»')
                print_response('Сахара знаходиться в Африці')
                back_flag = True
                continue
            #--------------The biggest city in the world according to population----------------
            elif topic_history[-1] == 'найбільше місто за населенням':
                print_response('Ви обрали тему «найбільше місто за населенням»')
                print_response('Найбільше місто за населенням — Шанхай, Китай. '
                               'У найбільшому фінансовому центрі Піднебесної та одному з провідних у світі проживають 24,9 млн осіб')
                back_flag = True
                continue
            #------------Find a point by coordinates, distance between points and direction------------------
            elif topic_history[-1] == 'знайти координати точки':
                print_response('Ви обрали тему «знайти координати точки»')
                print_response('Ви повинні ввести координати точки А (x1, y1), відстань між точками та напрямок (азимут)')
                try:
                    while True:
                        print_response('Введіть координати точки А (x1, y1) , відстань між точками та напрямок (азимут),через кому наприклад (1,2,3,4)')
                        coordinates = get_user_input()
                        if coordinates.lower() == 'назад' or coordinates.lower() == 'допомога' or coordinates.lower() == 'вихід':
                            set_flag(coordinates)
                            break
                        try:
                            coordinates = [float(x) for x in coordinates.split(',')]
                            a, b, c, d = coordinates
                            if c < 0:
                                print_response('Відстань між точками не може бути від\'ємною')
                                continue
                            if d < 0 or d > 360:
                                print_response('Азимут повинен бути від 0 до 360')
                                continue
                            print_response(f'Ваші координати точок: {a}, {b}  , Ваша відстань між точками: {c}, Ваш азимут: {d}')
                            find_point_b(a,b,c,d)
                            break
                        except ValueError:
                            print_response('Будь ласка, введіть тільки числа та роздільник (,).')
                except KeyboardInterrupt:
                    print_response('Радий був поспілкуватись, до зустрічі.')
                    sys.exit(0)


                continue

      elif(current_topic == 'філологія'):
          #--------------Difference between present simple and present continuous----------------------
          if topic_history[-1] == 'різниця між present simple та present continuous':
              print_response('Ви обрали тему «різниця між Present Simple та Present Continuous»')
              print_response('Present Simple використовується для опису регулярних дій, або дій, які відбуваються постійно, '
                             'або дій, які відбуваються за певний період часу.'
                             'Present Continuous використовується для опису дій, які відбуваються в даний момент, '
                             'або дій, які відбуваються в даний період часу.')
              back_flag = True
              continue
          #-----------------------Passive voice in present simple----------------------------------
          elif topic_history[-1] == 'passive voice у present simple':
              print_response('Ви обрали тему «Passive Voice у Present Simple»')
              print_response('Passive Voice у Present Simple утворюється за допомогою допоміжного дієслова to be '
                             'у Present Simple та третьої форми дієслова.')
              back_flag = True
              continue
          #-----------------------Nouns sex in Ukrainian----------------------------------
          elif topic_history[-1] == 'роди іменників в українській мові':
              print_response('Ви обрали тему «роди іменників в українській мові»')
              print_response('В українській мові існують такі роди іменників: чоловічий, жіночий, середній')
              back_flag = True
              continue

          elif topic_history[-1] == 'часи в англійській мові':
              print_response('Ви обрали тему «часи в англійській мові»')
              print_response('В англійській мові існує 12 часів:\n'
                               'Present Simple, Present Continuous, Present Perfect, Present Perfect Continuous\n'
                               'Past Simple, Past Continuous, Past Perfect, Past Perfect Continuous\n'
                               'Future Simple, Future Continuous, Future Perfect, Future Perfect Continuous')

              back_flag = True
              continue




      elif(current_topic == 'астрономія'):
          #--------------What is the space radiation----------------------
          if topic_history[-1] == 'космічне випромінювання':
              print_response('Ви обрали тему «космічне випромінювання»')
              print_response('Космічне вимпромінювання - випромінювання з космосу, що містить атомні ядра, '
                             'особливо протони з високою енергією, яке досягає поверхні Землі')
              back_flag = True
              continue
          #---------The biggest and the smallest orbits of the planets in the solar system-------
          elif topic_history[-1] == 'найменші та найбільші орбіти планет сонячної системи':
              print_response('Ви обрали тему «найменші та найбільші орбіти планет сонячної системи»')
              print_response('Найбільша орбіта - Нептун, найменша орбіта - Меркурій')

              back_flag = True
              continue
          #------------------Sun processes and how they affect the Earth-----------------------
          elif topic_history[-1] == 'сонячні процеси та як вони впливають на землю':
              print_response('Ви обрали тему «сонячні процеси , та як вони впливають на землю»')
              print_response('Сонячні процеси - це сонячна активність, сонячний вітер, сонячна радіація та магнітні бурі. '
                             'Загалом, сонячні процеси можуть мати як позитивний, так і негативний вплив на наш світ. Наприклад, полярні сяйва є красивим явищем, '
                             'яке можна спостерігати на небі, але сильні сонячні бурі можуть мати шкідливий вплив на електроніку і людське здоров\'я')
              back_flag = True
              continue




      elif(current_topic == 'загальні питання'):
          #--------------What year is it now----------------------
          if topic_history[-1] == 'який зараз рік':
            print_response('Ви обрали тему «який зараз рік»')
            current_date = datetime.date.today()
            current_year = current_date.year
            print_response('Зараз ' + str(current_year) + ' рік')

            back_flag = True
            continue

          #-----------------------Quotes-------------------------
          elif topic_history[-1] == 'виписати цитату':
            print_response('Ви обрали тему «виписати цитату»')
            try:
                while True:
                        random_quotes= random.randint(0, 4)
                        quote= quotes[list(quotes.keys())[random_quotes]]
                        print_response(quote['text'])
                        print_response('Якщо хочете почути ще одну надихаючу цитату, напишіть «цитата»')
                        answer = get_user_input()
                        if answer == 'цитата':
                            continue
                        elif answer.lower() == 'допомога' or answer.lower() == 'вихід':
                            set_flag(answer)
                            break
                        else:
                            print_response('Ви відмовилися від надихаючої цитати, повертаюся до вибору теми')
                            back_flag = True
                            break
            except KeyboardInterrupt:
                print_response('Радий був поспілкуватися, до зустрічі.')
                sys.exit(0)

            #---------Game: Rock-Paper-Scissors----------
          elif topic_history[-1] == 'камінь-ножиці-папір':
              print_response('Ви обрали тему «камінь-ножиці-папір»')
              try:
                  while True:
                      print_response('Час обирати: камінь, ножиці чи папір?')
                      bot_turn = random.choice(['камінь', 'ножиці', 'папір'])
                      turn = get_user_input()
                      if turn == bot_turn:
                          print_response('Нічия')
                          print_response('Якщо хочете зіграти ще раз, напишіть «зіграти»')
                          answer =  get_user_input()
                          if answer == 'зіграти':
                              continue
                          elif answer.lower() == 'назад' or answer.lower() == 'допомога' or answer.lower() == 'вихід':
                              set_flag(answer)
                              break
                          else:
                              print_response('Ви відмовилися від гри, повертаюся до вибору теми')
                              back_flag = True
                              break
                      elif (turn == 'камінь' and bot_turn == 'ножиці') or (turn == 'ножиці' and bot_turn == 'папір') or (turn == 'папір' and bot_turn == 'камінь'):
                          print_response('Ви виграли')
                          print_response('Якщо хочете зіграти ще раз, напишіть «зіграти»')
                          answer =  get_user_input()
                          if answer == 'зіграти':
                              continue
                          elif answer.lower() == 'назад' or answer.lower() == 'допомога' or answer.lower() == 'вихід':
                              set_flag(answer)
                              break
                          else:
                              print_response('Ви відмовилися від гри, повертаюся до вибору теми')
                              back_flag = True
                              break
                      elif (turn == 'ножиці' and bot_turn == 'камінь') or (turn == 'папір' and bot_turn == 'ножиці') or (turn == 'камінь' and bot_turn == 'папір'):
                            print_response('Ви програли')
                            print_response('Якщо хочете зіграти ще раз, напишіть «зіграти»')
                            answer = get_user_input()
                            if answer == 'зіграти':
                                continue
                            elif answer.lower() == 'назад' or answer.lower() == 'допомога' or answer.lower() == 'вихід':
                                set_flag(answer)
                                break
                            else:
                                print_response('Ви відмовилися від гри, повертаюся до вибору теми')
                                back_flag = True
                                break
                      else:
                          if turn.lower() == 'назад' or turn.lower() == 'допомога' or turn.lower() == 'вихід':
                                set_flag(turn)
                                break
                          else:
                                print_response('Ви ввели неправильне значення')
                                continue
              except KeyboardInterrupt:
                       print_response('Радий був поспілкуватися, до зустрічі.')
                       sys.exit(0)

           #------------------Game: Poems-----------------
          elif topic_history[-1] == 'зачитати вірш':
              print_response('Ви обрали тему «зачитати вірш»')
          try:
                  while True:
                    random_poem = random.randint(0, 4)
                    first_poem = poems[list(poems.keys())[random_poem]]
                    print_response(first_poem['text'])
                    print_response('Якщо хочете почути ще один вірш, напишіть «вірш»')
                    answer = get_user_input()
                    if answer == 'вірш':
                        continue
                    elif answer.lower() == 'допомога' or answer.lower() == 'вихід':
                        set_flag(answer)
                        break
                    else:
                        print_response('Ви відмовилися від читання віршів, повертаюся до вибору теми')
                        back_flag = True
                        break
          except KeyboardInterrupt:
              print_response('Радий був поспілкуватися, до зустрічі.')
              sys.exit(0)



print_response('Радий був поспілкуватися, до зустрічі.')
