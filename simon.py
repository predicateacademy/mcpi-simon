import random
from enum import Enum

class Response(Enum):
   FAIL = -1
   OK = 0
   SUCCESS = 1
   INVALID = -2

class Simon:

   def __init__(self, states=4):
      self.states = range(states)
      self.round = [random.choice(self.states)]
      self.player = []

   def get_round(self):
      return list(self.round)

   def get_num_rounds(self):
      return len(self.round)
   
   def input(self, state):
      if state not in self.states:
         return Response.INVALID

      self.player.append(state)

      for x in range(len(self.round)) :
         if x < len(self.player) :
            if self.round[x] != self.player[x] :
               self.round = [random.choice(self.states)]
               self.player = []
               return Response.FAIL

      if len(self.player) == len(self.round):
         self.player = []
         self.round.append(random.choice(self.states))
         return Response.SUCCESS
      else:
         return Response.OK
