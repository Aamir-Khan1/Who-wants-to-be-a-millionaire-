import random
print("WELCOME TO.....")
print("Who wants to be a Millionaire!!")
name = input("Please enter your name: ")
print("I will now tell you the instructions for the game. If you understand them properly, please reply \"Yes\" and"
      "if you didn't understand them please reply \"No\"")


def ask_confirmation():
    confirmation = input("The contestant must answer 15 multiple-choice questions correctly"
                         "\nin a row to win the jackpot."
                         "\nThe contestant may quit at any time and keep their earnings."
                         "\nFor each question, they are shown the question and four possible answers in advance "
                         "\nbefore deciding whether to play on or not."
                         "\nIf they do decide to offer an answer, it must be correct to stay in the game."
                         "\n\n*** The money tree ***"
                         "\nCurrently, this contestant is at £500."
                         "\nAnswering the next question correctly earns them a guaranteed £1,000 "
                         "\n- no matter what happens thereafter."
                         "\nIf at any stage they answer incorrectly, they fall back to the last \"guarantee point\""
                         "\n - either £1,000 or £32,000 - "
                         "\nand their game is over. For example, a contestant failing on question 13 would win £32,000."
                         "\nAnswering incorrectly before reaching the first guarantee point (£1,000) loses everything."
                         "\nA new player is picked from the remaining pool of 10. "
                         "\nIf time runs out on a particular programme,"
                         "\nthe next programme continues that player's game."
                         "\nWhen the money starts getting really serious (£32,000 and over), "
                         "\nthe host will reach for the appropriate cheque and sign it."
                         "\nWhilst this is mainly used as a theatrical device, the cheques can be cashed in"
                         "\nby the contestants for real."
                         "\n \n \n"
                         "***Lifelines***"
                         "\nAt any point, the contestant may use up one( or more) of their three\"lifelines\"."
                         "These are:"
                         "\n50:50 - two of the three incorrect answers are removed.Originally,"
                         "\nthese answers were chosen in advance by"
                         "\nthe question - setters( and so would invariably be the two you knew it couldn't be),"
                         "\nbut this was later changed to a random selection."
                         "\nPhone - A - friend - the contestants may speak to a friend or relative on the phone"
                         "\nfor 30 seconds to discuss the question."
                         "\nAsk the audience - the audience votes with their keypads on their choice of answer."
                         "\nEach lifeline may only be used once during a contestant's entire game.\n")
    return confirmation


user_confirmation = ask_confirmation()

while user_confirmation != "Yes":
    print("May be taking  another look will help :)")
    user_confirmation = ask_confirmation()

print("Let's start the Game Sir / Ma'am "+name)


money = 0


def question_on_screen(count):
    if count <= 3:
        money = count * 100

    elif count == 4:
        money = 500


    elif count == 12:
        money = 125000

    elif count < 12 and count > 4:
        money = 500 * 2 ** (count - 4)

    elif count < 16 and count > 12:
        money = 125000 * 2 ** (count - 12)
    print("Your {count}th question for $ {money} is on your computer screen:\n".format(count=count, money=money))
    return money


def get_question(random_no):
    print(question_bank[random_no])


def give_option(random_no):
    options = choice_bank[random_no]
    for key, option in options.items():
        print(key, option)


def get_answer(random_no,money):
    answer = input("Enter your answer:")
    if answer == answer_bank[random_no]:
        print("\nCongratulations!!\nYou have won ${money}".format(money=money))
        return True
    else:
        print("Sorry you lost.\n**Game Over**")
        return False


question_bank = {
    1: "Which of these states is also known for 'Aligarh ke taale', 'Bareilly ka surma' and 'Firozabad ki chudiyan'?",
    2: "In 2008, Rajasthan Royals became the first winner of which annual sporting event?",
    3: "What are the terms 3G, 4G and 5G related to?",
    4: "Which of the following will be heavier than 1450 g of iron?",
    5: "Which of these songs about rain does not have any rain sequence?",
    6: "The politician heard in this audio clip is the president of which party?",
    7: "Dadra, Nagar Haveli, Daman and the island of Diu were all under which European colonial power?",
    8: "Agni Ki Udaan is the Hindi translation of which personality's autobiography?",
    9 :"During the Battle of Kurukshetra, Krishna deceived the Kauravas by hiding the sun behind clouds to enable "
        "Arjuna to kill whom?",
    10: "Which company is the world's largest manufacturer of vaccines by number of doses produced (volume)",
    11: "The film in which this song features is based on which battle?"
         "\nHost Amitabh Bachchan played the video clip of \"Teri Mitti\" from Akshay Kumar starrer Kesari.",
    12: "Which Indian hockey player holds the record for the most number of goals scored in an Olympic final?",
    13: "In which state did a politician named P Subhash Chandra Bose become deputy chief minister in 2019?",
    14: "The International Literacy Day is observed on",
    15: "The language of Lakshadweep. a Union Territory of India, is",
    16: "In which group of places the Kumbha Mela is held every twelve years?",
    17: "Bahubali festival is related to",
    18: "Which day is observed as the World Standards Day?"
}


count = 1
choice_bank = {}


def add_choice(choices):
    choice_count = count

    split_choices = choices.split(';')
    opt_choice = {}
    for line in split_choices:
        key_value = line.split('.')
        opt_choice[key_value[0]] = key_value[1]
    choice_bank[choice_count] = opt_choice
    return count+ 1

count = add_choice("A. Uttar Pradesh;B. Madhya Pradesh;C. Himachal Pradesh;D. Bihar")
count =add_choice("A. PKL;B. ISL;C. PHL;D. IPL")
count =add_choice("A. Population Generations;B. Phone Networks;C. Digital Camera;D. Grading in Schools.")
count =add_choice("A. 1 kg of rice;B. 1,4 kg of paper;C. 1,7 kg of cotton;D. 1,3 kg of husk.")
count =add_choice("A. Tip tip barsa paani (Mohra);B. Rimjhim ghire saawan (Manzil);C. Barso re (Guru);"
           "D. Ghanan ghanan (Lagaan)")
count =add_choice("A. Samajwadi Party;B. Bahujan Samaj Party;C. Rashtriya Lok Dal;D. Communist Party of India")
count =add_choice("A. Denmark;B. France;C. Britain;D. Portugal")
count =add_choice("A. Homi Jehagir Bhabha;B. Kalpana Chawla;C. APJ Abdul Kalam;D. Vikram Sarabhai")
count =add_choice("A. Shakuni;B. Dronacharya;C. Dushasana;D. Jayadratha.")
count =add_choice("A. Biocon;B. Serum Institute;C. Indian Immunologicals;D. Bharat Biotech")
count =add_choice("A. Battle of Saragarhi;B. Battle of Chamkaur;C. Battle of Plassey;D. Battle of Buxar")
count =add_choice("A. Gurbux Singh;B. Leslie Claudius;C. Balbir Singh Senior;D. Keshav Dutt")
count =add_choice("A. Andhra Pradesh;B. West Bengal;C. Telangana;D. Karnataka")
count =add_choice("A. Sep 8;B. Nov 28;C. May 2;D. Sep 22")
count =add_choice("A. Tamil;B.	Hindi;C. Malayalam;D. Telugu")
count =add_choice("A. Ujjain. Purl; Prayag. Haridwar;B. Prayag. Haridwar, Ujjain,. Nasik;"
           "C. Rameshwaram. Purl, Badrinath. Dwarika;D. Chittakoot, Ujjain, Prayag,'Haridwar")
count =add_choice("A. Islam;B. Hinduism;C.	Buddhism;D. Jainism")
count =add_choice("A. Ujjain. Purl; Prayag. Haridwar;B. Prayag. Haridwar, Ujjain,. Nasik;"
           "C. Rameshwaram. Purl, Badrinath. Dwarika;D. Chittakoot, Ujjain, Prayag,'Haridwar")

answer_bank= {
    1: "A",
    2: "A",
    3: "B",
    4: "C",
    5: "D",
    6: "D",
    7: "B",
    8: "A",
    9: "B",
    10: "A",
    11: "C",
    12: "D",
    13: "C",
    14: "C",
    15: "B",
    16: "B",
    17: "C",
    18: "D"
}




random_no_list = []
while len(random_no_list) != 15:
    random_no = random.randint(1, 18)
    if random_no not in random_no_list:
        random_no_list.append(random_no)


def lets_play():
    count = 0
    answer = True
    for random_no in random_no_list:
        if answer == True:
            count += 1
            money = question_on_screen(count)
            get_question(random_no)
            give_option(random_no)
            answer = get_answer(random_no,money)

lets_play()




