from src.word_to_guess import WordToGuess


if __name__ == '__main__':
    word_to_guess = WordToGuess("./data/selected-words.json")

    print("Let the game begin! Make a proposition:")

    while not word_to_guess.done and not word_to_guess.won:
        guess = input(">>>   ")
        guess = guess.strip().lower()[:5]
        printed_state = word_to_guess.play_a_word(guess)
        print(printed_state)

        if word_to_guess.won:
            print("You won the game!")
        elif word_to_guess.done:
            print(
                "You don't have any tried left :( The word was: " + word_to_guess.word + ".")

    exit()
