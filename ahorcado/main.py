from ahorcado.word.word_manager import WordManager
from ahorcado.game import Game


word_manager = WordManager('word/words.txt')
game = Game(word_manager)
game.play()
