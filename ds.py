#!/usr/bin/env python
from random import *
import time

basebet = 1
betincrement = 1
bank = 1
odds = 2.00
round = 1

bet = basebet

maxbank = bank
minbank = bank

wincount = 0

while round < 1001:
  outcome = random()     # Generate a pseudo-random number between 0 and 1.
  if outcome > 0.5250:
    win = True
    wintext = "WIN!"
    wincount = wincount + 1.00
    bank = bank + (bet * (odds - 1.0))
    if bet-betincrement >= basebet:
      bet = bet - betincrement
    else:
      bet = basebet
  else:
    win = False
    wintext = "LOSE"
    bank = bank - bet
    bet = bet + betincrement
  if bank > maxbank:
    maxbank = bank
  elif bank < minbank:
    minbank = bank
  print("This is round: %s, %s, next bet is %s, current bank is %s, high: %s, low: %s, win percentage: %s" % (round, wintext, bet, bank, maxbank, minbank, wincount/round))
  round = round + 1
#  time.sleep(0.25)
