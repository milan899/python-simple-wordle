import random


def check_pos(target_str, original_str):
    for letter in range(0, (len(target_str))):
        if target_str[letter] == original_str[letter]:
            return True

    return False


def main():
    word = random.choice(open("words").read().split("\n"))
    guesses = 0
    console_output = ""

    while guesses < 6:
        guessed_word = input("Please take a guess: ").lower()

        if len(guessed_word) != 5:
            print("Not enough letters!")
            continue

        if not open("words").read().split("\n").__contains__(guessed_word):
            print("Not in word list!")
            continue

        guesses += 1

        if guessed_word == word:
            exit("Guess is correct!")

        for i in guessed_word:
            if i in word:
                if check_pos(guessed_word, word):
                    console_output = console_output + "🟩"
                else:
                    console_output = console_output + "🟨"
            else:
                console_output = console_output + "🟫"

        console_output = console_output + " - " + guessed_word
        print(console_output)
        console_output = console_output + "\n"
        guessed_word = ""

    exit("Word was " + word)


if __name__ == '__main__':
    main()
