import random #модуль для генерації випадкових чисел та випадкового вибору елементів
import time #модуль для роботи з часом (пауза при виконанні коду довжиною в задану кількість секунд, виведення поточного часу)

def intro():

# def - блок коду, що виконує певне завдання. Йому надається ім'я, яке можна викликати у програмі
# def функція (параметри):
# Тіло функції
# return - результат (необов'язково виводити)
    print("Вітаю! Ви потрапили на дно океану!")
    time.sleep(1) #очікування довжиною в 1 секунду, щоб гравець встигав прочитати текст
    print("Краще вам не знати як! :D")
    time.sleep(1)
    print("Тут може трапитись що завгодно!")
    time.sleep(1)
    ready()

def ready():
    choice = input("Ви готові, діти? \n(1) Так, капітане! \n(2) Ні\n") 
    time.sleep(1)
    if choice == "1": #якщо виконується умова, то викликається функція
        rules()
    elif choice == "2": #наступна умова
        print("Треба завжди бути на чіку!")
        time.sleep(1)
        gamelost()
    else: #якщо жодна з умов не виконується
        print("Введіть лише цифру.")
        ready()


def rules():
    print("Привила гри:")
    time.sleep(1)   
    print("На кожному етапі вам потрібно приймати рішення.")
    time.sleep(1)
    print("Якщо воно вірне, то ви переходите до наступного етапу.")
    time.sleep(1)
    print("А якщо ні, то повертаєтесь до попереднього.")
    time.sleep(1)
    print("Спецзавдання від Губки Боба: ")
    time.sleep(1)
    print("У Сквідварда день народження і ви повинні купити йому шоколадний торт.")
    time.sleep(1)
    print("Але все не так просто!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("На шляху вам трапляється безліч перешкод!")
    time.sleep(1)
    sponge_bob()

def sponge_bob():
    print("Губка Боб у вас вірить!")
    time.sleep(1)
    print("Він дає вам карту, на якій позначено шлях до морської пекарні пані Анни.")
    time.sleep(1)   
    print("Ось як вона виглядає:")
    time.sleep(1)    
    print("""
                    Камінь патріка 
                         |
                         |
                         |
                  Лабораторія Сенді
                         |
                         |
                         |
                    Помийне відро
                         |
                         |
                         |
                    Красті Краб
                         |
                         |
                         |
             Морська пекарня пані Анни               
    """)
    time.sleep(1)
    patrick_stone()

def patrick_stone():
    print("Ви прийшли до Патріка додому.")
    time.sleep(1)
    print("Він вас пригостив пісочним печивом :Р")
    time.sleep(1)
    print("Але потрібно ще чимось запивати...")
    time.sleep(1)
    print("В сухом'ятку несмачно :(")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Патрік вас шантажує.")
    time.sleep(1)
    print("Він дасть вам чай тільки, якщо ... ")
    time.sleep(1)
    print("Ви виграєте в гру камінь-ножниці-папір!")
    print("...")
    time.sleep(1)
    rps()

def rps():
    print("Гра почалась:")
    time.sleep(1)
    print("Ваш вибір?")
    time.sleep(1)
    print("(1) Камінь")
    time.sleep(1)
    print("(2) Ножиці")
    time.sleep(1)
    print("(3) Папір")
    time.sleep(1)
    game = input("?\n")

    if game == "1":
        player_choice = "камінь"
    elif game == "2":
        player_choice = "ножиці"
    elif game == "3":
        player_choice = "папір"
    else: 
        print("Введіть лише цифру.")
        time.sleep(1)
        rps()

    patrick_choice = random.choice(["камінь", "ножиці", "папір"]) #цей метод обирає випадковий елемент зі списку
          
    print(f"Ви обрали {player_choice}, а Патрік - {patrick_choice}.") #вставка значень у рядок
    time.sleep(1)
    
    if player_choice == patrick_choice:
        print("Нічия, спробуйте ще раз!")
        time.sleep(1)
        rps()
    elif (
    (player_choice == "камінь" and patrick_choice == "ножиці") or
    (player_choice == "папір" and patrick_choice == "камінь") or
    (player_choice == "ножиці" and patrick_choice == "папір")
        ): #умови при яких виконується код elif, or -якщо будь-яка умова True, то виконується код
        print("Ви перемогли!")
        time.sleep(1)
        print("Патрік все таки пригостив вас чаєм.")
        time.sleep(1)
        print("Ви перекусили і світ став кольоровішим :)")
        time.sleep(1)
        print("Тепер ви можете рухатись далі!")
        time.sleep(1)
        sandy_lab()

    else:
        print("Патрік переміг!")
        time.sleep(1)
        print("Ви повертаєтесь до Губки Боба для мотивації.")
        time.sleep(1)
        sponge_bob()
    
def sandy_lab():
    print("За картою ви прийшли до Сенді.")
    time.sleep(1)
    print("Вона готуєтся до конкурсу борщів.")
    time.sleep(1)
    print("Допоможіть Сенді визначити скільки чайних ложок солі потрібно додати, \nщоб у результаті вийшов найсмачніший борщ?")
    time.sleep(1)
    guess = input("Вгадайте кількість ложок (між 1 і 30): \n")
    if guess == "30":
        print("Правильно! Морські жителі люблять солений борщ! Ваша інтуїція не підвела!")
        time.sleep(1)
        
        print("...")
        time.sleep(1)
        print("Сюрприз!!!")
        time.sleep(1)
        print("Це ще не все! Це не простий борщ! :D")
        time.sleep(1)
        print("Це борщ-психолог?!")
        time.sleep(1)
        borsch_psyco()
    else:
        print("Неправильно! Морські жителі люблять солений борщ!")
        time.sleep(1)
        print("Прогуляйтесь назад до Патріка.")
        time.sleep(1)
        print("Зберіться з думками.")
        time.sleep(1)
        print("І спробуйте ще раз.")
        time.sleep(1)
        patrick_stone()
# cannot access local variable 'borsch_psyco' where it is not associated with a value 
# спочатку вклала цю функцію всередину функції sandy, 
# тому програма не могла витягти локальне значення і вибило помилку
def borsch_psyco():
    input("Ви можете запитати у борща-психолога що завгодно і він вам дасть цінну пораду: \n")
    time.sleep(1)
        
    pieces_of_advice = [
    "Біг пес через овес. Не нашкодило це псові, не нашкодить і овсові.",
    "Забий)",
    "Я борщ, ти запитуєш у борща?",
    ]

    advice = random.choice(pieces_of_advice) #випадковий вибір із заданого раніше списку
    print("Борщ-психолог: ")
    time.sleep(1)
    print(advice)
    time.sleep(1)
    play_again = input("\nХочеш запитати ще? \nТак (1) \nНі (2) \n")
    if play_again == "1":
        borsch_psyco()
    else:
        print("Ви отримали відповідь на своє питання і можете з впевненістю іти далі!")
        chum_bucket()
    



def chum_bucket():
    print("Наступна точка на вашому шляху - Помийне Відро.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("О, ні!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Планктона не запросили на день народження!")
    time.sleep(1)
    print("Яка незручна ситуація!")
    time.sleep(1)
    print("Її можна вирішити тільки армреслінгом.")
    time.sleep(1)
    aw()

def aw():
    agree = input("(1) Ви ризикнете? \n(2) Чи утримаєтесь?\n")
    if agree == "1":
        print("Планктон сильніший, ніж здається...")
        time.sleep(1)
        if random.randint(0, 1) == 1:  
        #генерується випадкове число від 0 до 1, якщо 1 - то гравець перемагає, якщо 0 - то програє
            print("Але ви всеодно перемогли!")
            time.sleep(1)
            print("Планктон вас благословляє і ви рухаєтесь далі.")
            time.sleep(1)
            print("Вам варто поспішати! Адже пекарня скоро закривається!")
            time.sleep(1)
            krusty_krab()
        else:
            print("Тому він не здається і перемагає.")
            time.sleep(1)
            print("За умовами ви повертаєтесь назад.")
            time.sleep(1)
            print("Допоможіть Сенді, зробіть добре діло, покращіть свою карму і вам пощастить наступного разу!")
            time.sleep(1)
            print("Поїжте для сили борщу!")
            time.sleep(1)
            sandy_lab()
            
    elif agree == "2":
        print("Бездіяльність нічого не дає.")
        time.sleep(1)
        aw()
    else:
        print("Введіть лише цифру.")
        time.sleep(1)
        aw()

def krusty_krab():
    print("Ви заходите до Красті Крабу.")
    time.sleep(1)
    print("Тут ви зустрічаєте містера Крабса, який метушиться!")
    time.sleep(1)
    name = input("Містер Крабс: Привіт! Як тебе звати?")
    print(f"Містер Крабс: {name.capitalize()}, дуже потрібна твоя допомога.")
    time.sleep(1)
    print("Містер Крабс: Цього року команда Красті Крабу має представляти \nБікіні Боттом на міжміському футбольному матчі.")
    time.sleep(1)
    print(f"Містер Крабс:Я зламав ногу і не можу грати.")
    time.sleep(1)
    play = input(f"Містер Крабс: {name.capitalize()}, ти вийдеш за мене?\n(1) Так \n(2) Ні\n")
    if play == "1":
        play_football()
    elif play == "2":
        print("Це не пропозиція руки і серця.")
        time.sleep(1)
        print("Погоджуйтесь!")
        krusty_krab()
    else:
        print("Введіть лише цифру.")
        time.sleep(1)
        krusty_krab()

def play_football():

    print("Гра Бікіні Боттом - Івано-Франківськ.")
    time.sleep(1)
    print("Після надзвичайно напруженої гри додали 5 хвилин додаткового часу.")
    time.sleep(1)
    print("Вибуло по 10 гравців з кожної команди.")
    time.sleep(1)
    print("Залишились тільки ви і Марцінків.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Небезпечний момент!!!")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Марцінків випадково зіграв рукою.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    shoot_penalty()
    
def shoot_penalty():
    print("Суддя назначає пенальті.")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Ви б'єте пенальті!")
    time.sleep(1)
    print("Куди будете бити?")
    time.sleep(1) 
    print("вліво (1)")
    time.sleep(1)
    print("в центр (2)")
    time.sleep(1)
    print("вправо (3)")
    time.sleep(1)
    player_choosing = input("?")
    if player_choosing == "1":
        player_choice = "вліво" #вибір гравця отримує значення у грі
    elif player_choosing == "2":
        player_choice = "в центр"
    elif player_choosing == "3":
        player_choice = "вправо"
    else:
        print("Введіть лише цифру!")
        time.sleep(1)
        shoot_penalty()

    goalkeeper_choice = random.choice(["вліво", "в центр", "вправо"])

    print(f"Ви б'єте {player_choice}, і Марцінків робить стрибок {goalkeeper_choice}.")
    time.sleep(1)

    if player_choice == goalkeeper_choice:
        print("Марцінків зловив!")
        time.sleep(1)
        main_game()
    else:
        print("ГООООООООООЛ!!!")
        time.sleep(1)
        your_victory()
                    
def main_game():
        print("Ви побачили, що Марцінків знову зіграв рукою.")
        time.sleep(1)
        print("Скажете судді?")
        play_again = input("Так (1), Ні (2)?")
        if play_again == "1":
            shoot_penalty()
        else: 
            print("Ви посумнівались трохи, а потім вирішили сказати.")
            shoot_penalty()
            
    
def your_victory():
    print("Ну ви даєте! Ви перемогли!!!")
    time.sleep(1)
    print("А також...")
    time.sleep(1)
    print("Ви виграли пожиттєвий запас бруківки від Марцінківа!")
    time.sleep(1)
    print("Тепер рушайте до останньої точки - пекарні пані Анни!")
    time.sleep(1)
    anna_bakery()

def anna_bakery():
    print("Ще трішки і ви купите шоколадний торт для Сквідварда!")  
    time.sleep(1)
    print("По карті це має бути десь тут...")
    time.sleep(1)
    print("Ви на роздоріжжі.")
    time.sleep(1)
    print("Перед вами вказівник:")
    time.sleep(1)
    print("""
                  Морська пекарня пані Анни
                              ^
                              |
                              |
                              |
Морська пекарня Ані Панни     |    Морська кав'ярня пані Анни
<----------------------------------------------------------->   
                                      
    """)
    print("Куди підете?")
    time.sleep(1)
    print("(1) ліворуч")
    time.sleep(1)
    print("(2) прямо")
    time.sleep(1)
    print("(3) праворуч")
    time.sleep(1)
    where = input("?\n")
    if where == "1":
        print("Щось ви не туди зашли.")
        time.sleep(1)
        print("Тут не продається шоколадний торт :(")
        time.sleep(1)
        print("Поверніться назад і подивіться в карту.")
        time.sleep(1)
        sponge_bob()

    elif where == "2":
        print("Який тут аромат випічки!")
        time.sleep(1)
        print("Але ви зосереджені на завданні.")
        time.sleep(1)
        print("Ви купили шоколадний торт для Сквідварда і виконали місію!!!")
        time.sleep(1)
        game_won()


    elif where == "3":
        print("Щось ви не туди зашли.")
        time.sleep(1)
        print("Тут не продається шоколадний торт :(")
        time.sleep(1)
        print("Поверніться назад і подивіться в карту.")
        time.sleep(1)
        sponge_bob()

    else:
        print("Введіть лише цифру!")
        time.sleep(1)
        anna_bakery()
        

def gamelost():
    print("Ви програли!")
    time.sleep(1)
    print("Сквідвард сумний :(")
    time.sleep(1)
    print("""
        .--'''''''''--.
     .'      .---.      '.
    /    .-----------.    |
   /        .-----.        |
   |       .-.   .-.       |
   |      /   \ /   \      |
    \    | .-. | .-. |    /
     '-._| | | | | | |_.-'
         | '-' | '-' |
          \___/ \___/
       _.-'  /   \  `-._
     .' _.--|     |--._ '.
     ' _...-|     |-..._ '
            |     |
            '.___.'
              | |
             _| |_
            /\( )/|
           /  ` '  |
          | |     | |
          '-'     '-'
          | |     | |
          | |     | |
          | |-----| |
       .`/  |     | |/`.
       |    |     |    |
       '._.'| .-. |'._.'
             \ | /
             | | |
             | | |
             | | |
            /| | ||
          .'_| | |_`.
          `. | | | .'
       .    /  |  \    .
      /o`.-'  / \  `-.`o|
     /o  o\ .'   `. /o  o|
     `.___.'       `.___.'
        """)
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Хочете спробувати ще разочечок?")
    time.sleep(1)
    try_again()

def game_won():
    print("""  
           .--..--..--..--..--..--.
         .' \  (`._   (_)     _   |
       .'    |  '._)         (_)  |
       \ _.')\      .----..---.   /
       |(_.'  |    /    .-\-.  \  |
       \     0|    |   ( O| O) | o|
        |  _  |  .--.____.'._.-.  |
        \ (_) | o         -` .-`  |
         |    \   |`-._ _ _ _ _\ /
         \    |   |  `. |_||_|   |
         | o  |    \_      \     |     -.   .-.
         |.-.  \     `--..-'   O |     `.`-' .'
       _.'  .' |     `-.-'      /-.__   ' .-'
     .' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
     `-._  `.  |________/\_____|    `-.'
        .'   ).| '=' '='\/ '=' |
        `._.`  '---------------'
                //___\   //___/
                  ||       ||
                  ||_.-.   ||_.-.
                 (_.--__) (_.--__)
    """)
    time.sleep(1)
    print("Губка Боб вами пишається! :D ")
    time.sleep(1)
    print("Ви перемогли!")


def try_again():
    again = input("(1) Так, (2) Ні?")
    if again == "1":
        print("Гаразд!")
        time.sleep(1)
        intro()
    elif again == "2":
        print("Нє, то нє... :)")
    else:
        print("Введіть лише цифру.")
        time.sleep(1)
        try_again()

intro()
