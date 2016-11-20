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

def reset():
    global num
    for p in range(5):
        num = 0
        for i in range(ROWS):
            for k in range(COLUMNS):
                mc.setBlock(x+i, y, z+k, block.AIR.id)
                states[num] = Vec3(x+i, y, z+k)
                num += 1
        time.sleep(0.5)
        num = 0
        for i in range(ROWS):
            for k in range(COLUMNS):
                mc.setBlock(x+i, y, z+k, random.choice(blocks))
                states[num] = Vec3(x+i, y, z+k)
                num += 1
        time.sleep(0.5)

def flash(play_list):
    for x in play_list:
        orig = mc.getBlock(states[x])
        mc.setBlock(states[x], block.AIR.id)
        time.sleep(0.75)
        mc.setBlock(states[x], orig)
        time.sleep(0.75)


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
reset()
time.sleep(5)
mc.postToChat("Start Game")
mc.postToChat('Round ' + str(game.get_num_rounds()))
flash(game.get_round())

while True:    
    # wait for input
    hitted = poll()
    flash([hitted])
    game.input(hitted)

    if game.get_state() == Response.FAIL:
        mc.postToChat('Game Over!')
        mc.postToChat('You completed ' + str(game.get_num_rounds()-1) + ' rounds.')
        reset()
        game.reset()
    elif game.get_state() == Response.SUCCESS:
        game.next_round()
        mc.postToChat('Round ' + str(game.get_num_rounds()))
        time.sleep(1)
        flash(game.get_round())

