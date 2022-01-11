class Word:
    def __init__(self, value):
        self.value = value
        self.hidden_value = ['_' for _ in self.value]

    def set_word_piece(self, word_piece):
        for index, char in enumerate(self.value):
            if char == word_piece:
                self.hidden_value[index] = char

    def check_word_piece(self, word_piece):
        return word_piece in self.value

    def is_complete(self):
        return self.value == ''.join(self.hidden_value)