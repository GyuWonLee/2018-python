import random
class Card(object):
    def __init__(self,kind,number):
        self.kind = kind
        self.number = number
    
    def __str__(self):
        number = [1, 11, 12, 13]
        kind = ["spades", "heats", "diamonds", "clubs"]
        if self.number == 1:
             return 'A'
        elif self.number == 11:
             return 'J'
        elif self.number == 12:
             return 'Q'
        elif self.number == 13:
             return 'K'
    
    def __eq__(self, other):
        return self.number  == other.number 
    
    def __gt__(self, other):
        return self.number  > other.number
    
    def __ge__(self, other):
        return self.number  >= other.number
    
    def __lt__(self, other):
        return self.number  < other.number
    
    def __le__(self, other):
        return self.number  <= other.number 
            
"""Deck class card 52장으로 구성 
생성자: 52장의 카드 초기화 
pick(index): index번째 카드를 반환
pick(): 랜덤하게 카드 반환  
shuffle() 카드의 순서를 섞음, 첫째 카드와 임의 위치의 카드를 천번 바꿈 
출력내용 : 카드 생성 후 첫째 카드 출력, 카드 셔플 후 첫째 카드 출력"""
 
class Deck:
    def __init__(self):
        self.numbers = range(1,53)
        self.cards = []
    def pick(index):
        for index in 52
        return index.card
    def shuffle(card, index):
        for i in range(index):
            random.randint(1,53)
            
            