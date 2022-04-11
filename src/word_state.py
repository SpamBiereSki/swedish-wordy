from .letter_states import Unknown, Right


class GameState:
    def __init__(self, length=5) -> None:
        self.letter_states = []
        for _ in range(length):
            self.letter_states.append(Unknown())
        self.length = length
        self.done = False

    def check_state(self, pos):
        if pos > self.length:
            raise ValueError(
                "This word is not that long! The word length is " + self.length + ".")
        return self.letter_states[pos]

    def set_state(self, pos, newState):
        if pos > self.length:
            raise ValueError(
                "This word is not that long! The word length is " + self.length + ".")

        self.letter_states[pos] = newState
        return self.letter_states

    def check_win(self):
        game_done = True
        for letter_state in self.letter_states:
            if not letter_state.is_equal_to_state(Right()):
                game_done = False
        self.done = game_done
        return self.done

    def print_state(self, word):
        all_letters_colored = []
        for pos, letter in enumerate(word):
            all_letters_colored.append(
                self.letter_states[pos].print_state(letter))

        return " ".join(all_letters_colored)
