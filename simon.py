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
      self.reset()

   def get_round(self):
      return list(self.round)

   def get_num_rounds(self):
      return len(self.round)
   
   def next_round(self):
      self.player = []
      self.round.append(random.choice(self.states))

   def reset(self):
      self.round = [random.choice(self.states)]
      self.player = []      

   def get_state(self):

      #player hit too many buttons
      if len(self.player) > len(self.round):
         return Response.FAIL

      #check partial results
      for x in range(len(self.player)):
         if self.player[x] != self.round[x]:
            return Response.FAIL

      #either success or ready for more input
      if len(self.player) == len(self.round):
         return Response.SUCCESS
      else:
         return Response.OK

   def input(self, state):
      if state not in self.states:
         return Response.INVALID

      self.player.append(state)

      return self.get_state()
