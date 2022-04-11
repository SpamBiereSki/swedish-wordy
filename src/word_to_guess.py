from .word_state import GameState
from .letter_states import Misplaced, Right, Wrong
from json import load
from random import randint


class WordToGuess:
    def __init__(self, path, length=5, tries=5) -> None:
        self.game_state = GameState(length)
        self.word = self.select_word(path)
        self.tries_remaining = tries
        self.won = False
        self.done = False

    def check_letter(self, pos, letter):
        if self.word[pos] == letter:
            self.game_state.set_state(pos, Right())
        elif letter in self.word:
            self.game_state.set_state(pos, Misplaced())
        else:
            self.game_state.set_state(pos, Wrong())

        return self.game_state

    def play_a_word(self, word):
        for pos, letter in enumerate(word):
            self.check_letter(pos, letter)

        self.tries_remaining = self.tries_remaining - 1
        self.check_done()
        self.check_win()
        return self.game_state.print_state(word)

    def select_word(self, path):
        with open(path, "r+", encoding="utf-8") as ioin:
            all_words = load(ioin)
        selected_index = randint(0, len(all_words))
        return all_words[selected_index]

    def check_win(self):
        self.won = self.game_state.check_win()
        return self.won

    def check_done(self):
        self.done = (self.tries_remaining <= 0)
        return self.done
