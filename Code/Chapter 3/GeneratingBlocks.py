from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 1010
y = 77
z = 1009
blockType = 41 # Type 41 == Gold Block

# Get player position 
position = mc.player.getTilePos()
x = position.x 
y = position.y
z = position.z

# shift x so that we are not generating blocks at the position of the player
x = x + 1


# Generate blocks stacked on top of each other 
for newy in range(y, y+10):
    mc.setBlock(x, newy, z, blockType)

# implementing the setBlocks function 
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 
width = 10 
height = 5 
length = 6
blockType = 4 
gold = 41
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType) 
# Make the new structure hollow
mc.setBlocks(x+1, y+1, z+1, x + width-1, y + height-1, z + length-1, air) 

