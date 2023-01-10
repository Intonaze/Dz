import random

class Card():       
    def __init__(self, dignity, suit) -> None:
        self.suit = suit
        self.dignity = dignity
        match dignity:
            case 'Jack': self.number = 10
            case 'Queen': self.number = 11
            case 'King': self.number = 12
            case 'Ace': self.number = 13
            case _: self.number = int(dignity)
        self.description = f'{self.dignity} of {self.suit}'

class CardPlay():
    def __init__(self, *players) -> None:
        self.trump = None
        if len(players) > 8:
            print('Слишком много игроков')
        else:
            self.players = players

    def distirbution(self):
        self.cards = {i: None for i in self.players}
        suit = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        cards = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
        self.deck = [Card(i, j) for i in cards for j in suit]
        random.shuffle(self.deck)
        self.players_cards = {i:[] for i in self.players}
        for i in range(6):
            for j in self.players_cards.keys():
                self.players_cards[j].append(self.deck.pop())
        trump = self.deck.pop()
        
    def card_check(self):
        for i in self.players_cards.keys():
            print(i)
            for j in self.players_cards[i]:
                print(j.suit, j.dignity)
    
    def cards_comparison(self, player_1, cardpos_1, player_2, cardpos_2):
        if self.players_cards[player_1][cardpos_1].suit != self.players_cards[player_2][cardpos_2].suit:
            return 'Карты разных мастей'
        elif self.players_cards[player_1][cardpos_1].number > self.players_cards[player_2][cardpos_2].number:
            return player_1
        else:
            return player_2 
       