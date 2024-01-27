"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:
    def __init__(self, words):
        dict_file = open(path)
        self.words = words
    
    def parse(self, dict_file):
        return [w.strip() for w in dict_file]
    
    def random(self):
        return random.chice(self.words)

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith('#')]

