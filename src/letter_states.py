from .constants import BColors


class LetterState:
    def __init__(self) -> None:
        pass

    terminal_color = BColors.White
    name = "state"

    def is_equal_to_state(self, other_state):
        return self.name == other_state.name

    def print_state(self, letter):
        return self.terminal_color + letter + BColors.ENDC


class Wrong(LetterState):
    def __init__(self) -> None:
        super().__init__()

    terminal_color = BColors.White
    name = "wrong"


class Right(LetterState):
    def __init__(self) -> None:
        super().__init__()

    terminal_color = BColors.Green
    name = "right"


class Misplaced(LetterState):
    def __init__(self) -> None:
        super().__init__()

    terminal_color = BColors.Yellow
    name = "misplaced"


class Unknown(LetterState):
    def __init__(self) -> None:
        super().__init__()

    terminal_color = BColors.White
    name = "unknown"
