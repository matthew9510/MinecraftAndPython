# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x, y, and z variables to represent coordinate
x = 100
y = 120
z = 1000

# Change the player's position
mc.player.setTilePos(x, y, z)
