import random

from sympy import false, true
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
    total = sum([card.value for card in self.cards])
    return total
  
  def has_ace(self):
    for card in self.cards:
      if card.rank == 'Ace': 
        return true
    else:
      return false

def play_game():
# Game setup ->
  deck = Deck()
  deck.shuffle_deck()

  def deal_hand():
    card1 = deck.deal_card()
    card2 = deck.deal_card()
    return  Hand([card1, card2])

  player_hand = deal_hand()
  dealer_hand = deal_hand()

  player_card1, player_card2 = player_hand.cards
  dealer_card1, dealer_card2= dealer_hand.cards


  # Game logic ->
 
  # Inital deal ->
  if dealer_hand.get_total() == 21:
    print(f'The dealer got Blackjack with a {dealer_card1} and the {dealer_card2} ')
    print('You lose, goodbye')
    return
  elif player_hand.get_total() == 21:
    print(f"The {player_card1} and the {player_card2}, Blackjack!")
    print('You win, goodbye')
    return
  else:
    print(f"The dealer shows an {dealer_card1}")
    print(f"You got the {player_card1} and the {player_card2} for a total of {player_hand.get_total()}")
    hit_or_stay = input("Press 'h' to get another card or 's' to stand: ")

    # Main loop ->

    while hit_or_stay == 'h':
      player_hand.add_card(deck.deal_card())
      if player_hand.get_total() > 21:
        print(f'Your total is {player_hand.get_total()}, sorry you lose')
        return
      elif player_hand == 21:
        print('21, you win')
        return
      else:
        print(f'your total is {player_hand.get_total()}')
        hit_or_stay = input("Press 'h' to get another card or 's' to stand: ")
    if hit_or_stay == 's':
      print('Dealers turn')
      print(f'Dealer shows {dealer_card1} {dealer_card2} for a total of {dealer_hand.get_total()}')
      if dealer_hand.get_total() >= 17:
        if dealer_hand.get_total() > player_hand.get_total():
          print(f'Dealer wins with {dealer_hand.get_total()} over {player_hand.get_total()}')
        elif dealer_hand.get_total() < player_hand.get_total():
          print(f'Player wins with {player_hand.get_total()} over {dealer_hand.get_total()}')
        elif dealer_hand.get_total() == player_hand.get_total():
          print(f'We push with {dealer_hand.get_total()}')
    elif dealer_hand.get_total() < 17:
      print('Dealer takes a card')
      dealer_hand.add_card(deck.deal_card())
      print(f'Dealer has {dealer_hand.get_total()}')
      return



      

play_game()

