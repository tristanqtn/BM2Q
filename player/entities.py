import random
import json

# Description: This file contains the Player class which is used to represent a player in the game.
class Player:
    def __init__(self, name):
        self.id = None
        self.name = name
        self.score = 0
        self.cards = []
        self.selected_card = None
        self.is_winner = False
        self.is_ready = False
        self.has_voted = False
        
    def __str__(self):
        return self.name


class QuestionCard:
    def __init__(self, text, blanks):
        self.text = text
        self.blanks = blanks

    def __str__(self):
        return self.text
    
class AnswerCard:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text
    
class Deck: 
    def __init__(self):
        self.cards = []
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw_card(self):
        return self.cards.pop()
    
    def __len__(self):
        return len(self.cards)
    
    def __str__(self):
        return str(self.cards)
    
class Game:

    def load_questions(self):
        with open('./data/questions.json', 'r') as file:
            questions = json.load(file)
            for question in questions:
                self.question_deck.cards.append(QuestionCard(question["text"] , question["pick"]))
            self.question_deck.shuffle()

    def load_answers(self):
        with open('./data/answers.json', 'r') as file:
            answers = json.load(file)
            for answer in answers:
                self.answer_deck.cards.append(AnswerCard(answer))
            self.answer_deck.shuffle()

    def __init__(self):
        self.id = None
        self.players = []
        self.question_deck = Deck()
        self.answer_deck = Deck()
        self.current_question = None
        self.winner = None
        self.round = 1
        self.max_rounds = 20

        self.load_answers()
        self.load_questions()

    def show_decks(self):
        for question in self.question_deck.cards:
            print(question)
        for answer in self.answer_deck.cards:
            print(answer)