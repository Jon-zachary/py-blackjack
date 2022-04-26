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
      self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
      self.ranks = ["Two", "Three", "Four", "Five",
                   "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
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


class Hand:
  def __init__(self, cards):
    self.cards = cards

  def add_card(self, card):
    self.cards.append(card)
  
  def get_total(self):
    total = sum(card.value for card in self.cards)
    return total

def play_game():
  deck = Deck()
  deck.shuffle_deck()
  player_card1 = deck.deal_card()
  player_card2 = deck.deal_card()
  dealer_card1 = deck.deal_card()
  dealer_card2 = deck.deal_card()

  dealer_hand = Hand([dealer_card1, dealer_card2])
  player_hand = Hand([player_card1, player_card2])

  if dealer_hand.get_total() == 21:
    print(f"The dealer got Blackjack with a {dealer_card1} and the {dealer_card2} ")
  if player_hand.get_total() == 21:
    print(f"The {player_card1} and the {player_card2}, Blackjack!")
  else:
    print(f"The {player_card1} and the {player_card2} for a total of {player_hand.get_total()}")


play_game()

