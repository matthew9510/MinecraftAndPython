from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()



#for(x = 0; x < 100; x++): # Not Java 
y = 77  
for x in range(1010,1014):
    for z in range(1009,1011):
        time.sleep(.5)
        mc.player.setPos(x, y, z)
        

