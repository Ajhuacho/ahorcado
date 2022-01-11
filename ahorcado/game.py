class Game:

    def __init__(self, word_manager):
        self.word_man = word_manager
        self.life = 6

    def play(self):
        word = self.word_man.get_random_word()
        print(word.value)
        self.print_secret_word(word)
        while self.life > 0:
            self.execute(word)
            if word.is_complete():
                self.print_winner()
                break
        if self.life == 0:
            self.print_game_over()

    def execute(self, word):
        piece_word = input('ingrese una letra: ')
        if word.check_word_piece(piece_word):
            word.set_word_piece(piece_word)
            self.print_win(word)
        else:
            self.life = self.life - 1
            self.print_error(word)

    def print_win(self, word):
        print('acertaste')
        self.print_secret_word(word)

    def print_error(self, word):
        print('fallaste')
        self.print_secret_word(word)

    def print_secret_word(self, word):
        print(''.join(word.hidden_value))

    def print_game_over(self):
        print('GAME OVER')

    def print_winner(self):
        print('YOU WIN')