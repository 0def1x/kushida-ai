import settings as st
import random
import time
import words
import search_words as swords


def Start():
    print(f"Запуск бота {st.bot_name}")
    print("Основаная информация:\n\
          Version: {}\n\
          Developer & Contacts: {} & {}".format(st.bot_ver, st.bot_developer, st.contacts_developers))

    print("\n\n\n")
    Say("Я успешно запустилась!")


def RandomNumber():
    number = random.randint(1, 100)
    while True:
        time.sleep(1.2)  # Задержка, чтобы игрок не путал да и красивее
        Say("Вводи число!")
        player_choose = int(input(""))

        if player_choose > number:
            Say(random.choice(words.number_higest))
        elif player_choose < number:
            Say(random.choice(words.number_lower))
        if player_choose == number:
            Say(random.choice(words.number_win))
            time.sleep(2)
            break


def CalculateExc():
    num_a = random.randint(0, 1000)
    num_b = random.randint(0, 1000)
    answer_all = int(num_a) * int(num_b)

    Say("Сможешь решить пример? {} {} {} = ?".format(num_a, "*", num_b))

    while True:
        answer = int(input("Ответ: "))
        if answer == answer_all:
            Say(random.choice(words.number_win))
            time.sleep(2)
            break
        else:
            Say("Попробуй еще раз!")


def Say(*args):
    remove_board1 = str(args).replace("(", "")
    remove_board2 = remove_board1.replace("'", "")
    remove_board3 = remove_board2.replace(",", "")
    finally_string = remove_board3.replace(")", "")
    print(" - {}: {}".format(st.bot_name, finally_string))


Start()

while True:
    text_saying = str(input("Что будем делать?: "))

    if text_saying.lower() in swords.close_text:
        Say("До встречи, друг!")
        break

    if text_saying.lower() in swords.playing_words:
        Say(random.choice(words.playing_choose))
        what_playing = str(input(""))

        if what_playing.lower() in swords.first_game:
            RandomNumber()

        elif what_playing.lower() in swords.second_game:
            CalculateExc()

    if text_saying.lower() in swords.words_talk:

        Say("О чем будем говорить?")
        dialog_about = str(input(""))  # Спрашиваем игрока, скобки не трогать

        if dialog_about.lower() in swords.close_text:
            Say(random.choice(words.answer_none))

        elif dialog_about.lower() in swords.weather:

            string_about_clouds = random.choice(words.about_weather_clouds)
            string_about_sun = random.choice(words.about_weather_sun)
            string_about_temp = random.choice(words.about_weather_temp)

            finally_string1 = string_about_clouds, " / ", string_about_sun, " / ", string_about_temp
            Say(finally_string1)

        elif dialog_about.lower() in swords.about_love:
            Say(random.choice(words.about_love))
            and_you = str(input(""))
            Say(random.choice(words.understand))
    else:
        Say(random.choice(words.not_found))
