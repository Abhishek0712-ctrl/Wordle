class LetterState:
    def __init__(self,character:str):
        self.character:str= character
        self.is_in_word:bool=False
        self.is_in_position:bool=False

    def __repr__(self) -> str:
        return f"[{self.character} is in:{self.is_in_word}at position:{self.is_in_position}]"