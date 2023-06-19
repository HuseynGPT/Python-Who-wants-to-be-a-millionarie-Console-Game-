import random
import time

indexQuestion = 0
indexAnswer = 1
indexCorrectAnswer = 2
indexBankMoney = 3

questions = [
    ['Azerbyacanin Paytaxti haradir?', ['Baki', 'Gence', 'Şəki', 'Sumqayit'], 'Baki'],
    ['Turkiyenin paytaxti haradir?', ['Ankara', 'Istanbul', 'Konya', 'Erzurum'], 'Ankara'],
    ['Azərbaycan Respublikası necenci ilde yaranmisdir?', ['1918', '1980', '1900', '1939'], '1918'],
    ['Azerbaycan Himninin musiqisi kime aiddir?', ['Ehmed Cavad', 'Huseyn Cavid', 'Uzeyir Hacibeyli', 'Qara Qarayev'], 'Uzeyir Hacibeyli'],
    ['Azerbaycanin texmini ehalisi ne qederdir?', ['8000000', '10000000', '7000000', '50000'], '10000000'],
    ["What is the capital of France?", ['Paris', 'New-York', 'Berlin', 'Amsterdam'], 'Paris'],
    ["How many states does the United States have?", ['50', '80', '70', '65'], '50',],
    ["In what year did the Berlin Wall collapse?", ['1991', '1980', '1939', '2000'], '1991'],
    ["What country is the 'Great Wall' in?", ['Japonia', 'China', 'America', 'Korea'], 'China'],
    ["Canberra is the capital of which country?", ['Australia', 'Amerika', 'Brazilia', 'Italy'], 'Australia'],
    ["What is the name of the largest ocean?", ['Pacific', 'Indian', 'Atlantic', 'Artic'], 'Pacific'],
    ["Elon Musk - in serveti ne qederdir", ["1 milyard", "300 milyard", "277 milyard", "170 milyard"], "170 milyard"],
    ["Deniz ulduzunun nece beyni var?", ["1", "2", "0", "4"], "0"],
    ["\"Bir kere yukselen bayraq, bir daha enmez!\" cümləsi hansı azeri siyasətçisinə aiddir?",["Ebulfez Elcibey", "Mehemmed Emin Resulzade", "Heyder Eliyev", "Ilham Eliyev"], "Mehemmed Emin Resulzade"],
    ["11*11 ifadesinin hasili necedir", ["121", "144", "165", "100"], "121"],
    ]

jokers = ['50-50', 'Call Friend', 'Auditoriya']
balance = [0, 100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
friends = ['Orxan', 'Cavid', 'Ismayil']


def menu_print():
    print(" *************************************************")
    print(" *            // Kim olmaq isteyer \\\           *")
    print(" *            ||     MILYONER       ||           *")
    print(" *            \\\ Kim olmaq isteyer //           *")
    print(" *************************************************\n")


def yukleme_menu():
    print('.', end=' ')
    time.sleep(0.5)
    print('.', end=' ')
    time.sleep(0.5)
    print('.', end=' ')
    time.sleep(0.5)
    print()


def dosta_zeng():
    rand_dost = random.choice(friends)
    print(f'{rand_dost} bey, Milyoncu proqramina xos geldiniz!')
    print(f'Zehmet olmasa {questions_count} - da {username} e komek edin')
    ehtimal = random.randint(1, 100)
    if ehtimal >= 85:
        print(f'Mence cavab budur: {questions[0][2]}')
    else:
        print(f'Mence cavab budur: {questions[0][1][2]}')


def fifty_fifty():
    questions[0][1].remove(questions[0][2])
    yari_yari = random.choice(questions[0][1])
    netice = [yari_yari, questions[0][2]]
    random.shuffle(netice)
    print(f"Cavab asagidakilardan biridir:\nA){netice[0]}\nB){netice[1]}")


def audutoria():
    chance = random.randint(0, 100)
    if chance <= 85:
        dogru_cavab = questions[0][3]
        print(f'Audutoriyanin cavabi ----> {dogru_cavab}')
    else:
        questions[0][1].remove(questions[0][2])
        dogru_cavab = questions[0][1][0]

        print(f'Audutoriyanin cavabi ----> {dogru_cavab}')


questions_count = 0
username = input("Adinizi daxil edin: ")
print(f"{username} Miliyonçuya Xoş Gəlmisiniz!")
start_input = input("Oyuna baslamaq isteyirsinizmi y/n: ")

if start_input == 'y':
    yukleme_menu()
    menu_print()
    while questions_count <= 15:

        questions_count += 1
        if 5 < questions_count < 10:
            mebleg = balance[4]
        elif questions_count > 10:
            mebleg = balance[9]

        random.shuffle(questions)
        random.shuffle(questions[0][1])
        print(f"Sual {questions_count}".center(30, "="))
        print(f'{questions[0][0]}\nA){questions[0][1][0]}\tB){questions[0][1][1]}\nC){questions[0][1][2]}\tD){questions[0][1][3]}')
        joker_answer = input('Joker istifdade etmek isteyirsiniz y/n: ')
        if joker_answer == 'y':
            yukleme_menu()
            if len(jokers) == 3:
                joker_choice = input(f'1){jokers[0]}\n2){jokers[1]}\n3){jokers[2]}\nHansi jokeri isletmek isteyirsiniz: ')

            elif len(jokers) == 2:
                joker_choice = input(f'1){jokers[0]}\n2){jokers[1]}\nHansi jokeri isletmek isteyirsiniz: ')

            elif len(jokers) == 1:
                joker_choice = input(f'1){jokers[0]}\nHansi jokeri isletmek isteyirsiniz: ')

            if joker_choice.lower() == '50-50':
                fifty_fifty()
                question_answer = input('Cavab: ')
                if question_answer.lower() == questions[0][2].lower():
                    print('Tebrikler!!! Dogru bildiniz!!')
                    print(f"Bu turdan {balance[questions_count - 1]} qazandiniz!!")
                    questions.pop(0)
                    jokers.remove("50-50")
                    if questions_count > 5:
                        continue_or_ok = input('Davam etmek isteyirsinizmi y/n: ')
                        if continue_or_ok.lower() == 'y':
                            pass
                        elif continue_or_ok.lower() == "n":
                            print(f"======Qazandığınız məbləğ======:\n\t===={balance[questions_count - 1]}====")
                            break
                    elif questions_count == 15 and question_answer.lower() == questions[0][2].lower():
                        for row in range(50):
                            for column in range(50):
                                print('$', end='  ')
                            print()
                        print()
                else:
                    print('!!!Yanlis Cavab!!!')
                    break

            elif joker_choice.lower() == 'dosta zeng':
                dosta_zeng()
                question_answer = input('Cavab: ')
                if question_answer.lower() == questions[0][2].lower():
                    print('Tebrikler!!! Dogru bildiniz!!')
                    print(f"Bu turdan {balance[questions_count - 1]} qazandiniz!!")
                    questions.pop(0)
                    jokers.remove("Call Friend")
                    if questions_count > 5:
                        continue_or_ok = input('Davam etmek isteyirsinizmi y/n: ')
                        if continue_or_ok.lower() == 'y':
                            pass
                        elif continue_or_ok.lower() == "n":
                            print(f"======Qazandığınız məbləğ======:\n\t===={balance[questions_count - 1]}====")
                            break
                    elif questions_count == 15 and question_answer.lower() == questions[0][2].lower():
                        for row in range(50):
                            for column in range(50):
                                print('$', end='  ')
                            print()
                        print()
                else:
                    print('!!!Yanlis Cavab!!!')
                    break

            elif joker_choice.lower() == 'auditoriya':
                audutoria()
                question_answer = input('Cavab: ')
                if question_answer.lower() == questions[0][2].lower():
                    print('Tebrikler!!! Dogru bildiniz!!')
                    print(f"Bu turdan {balance[questions_count - 1]} qazandiniz!!")
                    questions.pop(0)
                    jokers.remove("Auditoriya")

                    if questions_count > 5:
                        continue_or_ok = input('Davam etmek isteyirsinizmi y/n: ')
                        if continue_or_ok.lower() == 'y':
                            pass
                        elif continue_or_ok.lower() == "n":
                            print(f"======Qazandığınız məbləğ======:\n\t===={balance[questions_count - 1]}====")
                            break
                    elif questions_count == 15 and question_answer.lower() == questions[0][2].lower():
                        for row in range(50):
                            for column in range(50):
                                print('$', end='  ')
                            print()
                        print()
                else:
                    print('!!!Yanlis Cavab!!!')
                    break


        elif joker_answer == 'n':
            question_answer = input('Cavab: ')
            if question_answer == questions[0][2].lower():
                print('Tebrikler!!! Dogru bildiniz!!')
                print(f"Bu turdan {balance[questions_count - 1]} qazandiniz!!")
                questions.pop(0)
                if questions_count > 5:
                    continue_or_ok = input('Davam etmek isteyirsinizmi y/n: ')
                    if continue_or_ok.lower() == 'y':
                        pass
                    elif continue_or_ok.lower() == "n":
                        print(f"======Qazandığınız məbləğ======:\n\t===={balance[questions_count - 1]}====")
                        break
            elif questions_count == 15 and question_answer.lower() == questions[0][2].lower():
                for row in range(30):
                    for column in range(30):

                        print('$', end='  ')

                    print()
                print()
                time.sleep(1)
            else:
                print('!!!Yanlis Cavab!!!')
                break
        else:
            print('wrong input!!!')
            break
else:
    print('Bye.')
    time.sleep(0.7)
    print('Bye..')
    time.sleep(0.7)
    print('Bye...')
    time.sleep(0.7)
