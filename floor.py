from mcpi.minecraft import Minecraft
import mcpi.block as block
from time import *

mc = Minecraft.create()

x,y,z = mc.player.getPos()
for i in range(10):
    for j in range(10):
        mc.setBlock(x+i, y, z+j, block.DIAMOND_BLOCK.id)


