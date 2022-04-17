import random
class Card:
  def __init__(self, suit, rank, value):
    self.suit = suit
    self.rank = rank
    self.value = value
  
  def __str__(self):
    return f'{self.rank} of {self.suit}'



class Deck:
  def __init__(self):
      self.suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
      self.values = range(1, 14)
      self.ranks = ["Ace", "Two", "Three", "Four", "Five",
                   "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
      self.cards = []

      for s in self.suits:
        for idx, v in enumerate(self.values):
          self.cards.append(Card(s, self.ranks[idx], v))

  def __len__(self):
    return len(self.cards)

  def __str__(self):
    res = ""
    for card in self.cards:
      res += f'{card.rank} of {card.suit} \n'
    return res
  
  def deal_card(self):
    return self.cards.pop()
  
  def shuffle_deck(self):
    return random.shuffle(self.cards)


deck = Deck()
card = deck.deal_card()
print(card)





