from simon import *
from mcpi.minecraft import Minecraft, Vec3
import mcpi.block as block
import time
import random
blocks = [1,2,3,4,14,15,21,22,46]
mc = Minecraft.create()
x, y, z = mc.player.getPos()
x = int(x)
y = int(y)
z = int(z)

ROWS = 5
COLUMNS = 5
game = Simon(ROWS * COLUMNS)
states = {}
num = 0
for i in range(ROWS):
   for k in range(COLUMNS):
      mc.setBlock(x+i, y, z+k, random.choice(blocks))
      states[num] = Vec3(x+i, y, z+k)
      num += 1

def flash(play_list):
    for x in play_list:
        orig = mc.getBlock(states[x])
        mc.setBlock(states[x], block.AIR.id)
        time.sleep(0.6)
        mc.setBlock(states[x], orig)
        time.sleep(0.6)

def check(pos):
    for x in states:
        if pos == states[x]:
            return x
    return -1

def poll():
    while True:
        for evt in mc.events.pollBlockHits():
            ret = check(evt.pos)
            if ret > -1:
                return ret
        time.sleep(0.1)

# - wait a few ticks to get started
time.sleep(5)
mc.postToChat("Start Game")

while True:    
    flash(game.get_round())

    # - wait for input
    state = poll()
    flash([state])
    ret = game.input(state)

    while ret == Response.OK or ret == Response.INVALID:
        state = poll()
        flash([state])
        ret = game.input(state)
        
    if ret == Response.FAIL:
        mc.postToChat('Game Over!')
        mc.postToChat('You completed ' + str(game.get_num_rounds()) + ' rounds.')
    else:
        mc.postToChat('Round ' + str(game.get_num_rounds()))	

