[Checkout the code that goes along with these notes]()

#### Expressions and Statements
When you’re having a conversation with someone, you want them to understand what you’re telling them. You use short phrases, such as “three diamonds” or “behind a tree,” to give information to the person you’re talking to. However, the phrases don’t make sense on their own unless they’re combined into sentences, such as “I found three diamonds behind a tree.”

Python programming has concepts similar to **phrases** and **sentences**, which are called **expressions** and **statements**. You can combine values, variables, and operators to create small pieces of code called expressions, like 
```
2 + 2 
```
Expressions can be combined into statements.

Statements are single lines or short blocks of code that do something in a program

shells can interpret output with expressions,however when using text editor instead of the Python shell, be sure to write entire statements. When you’re using a text editor, Python won’t do anything with the expression because it’s not part of a complete statement. To turn this expression into a complete statement, you could assign its value to a variable.

For example: 
```
sum = 2 + 2
```

<hr></hr>

#### Getting Players position
```
from mcpi.minecraft import Minecraft mc = Minecraft.create()
position = mc.player.getTilePos() 
x = position.x 
y = position.y
z = position.z
```

The dot between the position variable and the x, y, and z is called **dot notation**. Dot notation is used by certain variables and functions, such as all of the functions you use in the Minecraft Python API (for example, mc.setTilePos()).

Once you have the player’s position, you can set the x, y, and z variables to the player’s current coordinates, which are represented by position.x, position.y, and position.z. You can then teleport the player anywhere you want in relation to the current coordinates.

<span style="color:red">Note: You’ll learn more about dot notation in Chapters 11 and 12 </span>
<hr></hr>

#### Using Math operators in arguments 
When you use a function, such as setBlock() or setTilePos(), you give the function arguments, which specify the values you want the function to use when it runs.

So far, you’ve been introduced to the addition and subtraction operators. You can use these operators inside a function’s parentheses to set
the values of arguments.  It will add two values together within the parentheses without the need for an extra statement

```
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x = 6
y = 5 
z = 28
blockType = 103
mc.setBlock(x, y, z, blockType)
mc.setBlock(x, y + 1, z, blockType)
```

 The last line uses y + 1 as an argument in the function u. Although the value of this argument is 6 (5 + 1), the value of the y variable is still 5. The argument lets you add to the y variable without actually changing its value, which is useful if you want to use y again somewhere else in your code. You can also add two variables together and use them as a single argument.

```
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
x = 6
y = 5 
z = 28
blockType = 103 
up = 1
mc.setBlock(x, y, z, blockType)
u mc.setBlock(x, y + up, z, blockType
```

#### setBlocks() Function
You’ve used setBlock() to create a single block, but setBlock() has a friend called setBlocks(), which creates several blocks in the shape of a cuboid. A cuboid is a 3D rectangle. A cuboid’s length, width, and height can all be different values. The setBlocks() function lets you (12, 10, 32) create many blocks in a large area. To use setBlocks(), just pass it two sets of coordinates and the block type. The first set of coordinates identifies where you want one corner of the cuboid, and the second set specifies where you want the opposite corner.

```
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 
width = 10 
height = 5 
length = 6
blockType = 41
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType) 
```

 We have a problem with out cuboid, it’s completely solid! After I ran the program, I punched a hole in the side of the building so you can see that it’s solid in the center. This cuboid is a great start, though, and now you’ll be in charge of hollowing it out so the player can actually go inside. Your mission is to change the program to create a building with walls, a ceiling, and a floor at the player’s position. To accomplish this, you’ll create a cuboid made of air inside the solid cuboid you just made. The two cuboids together should produce an empty box.

**HINT**
To create the air cuboid one block inside the walls, you can use the addition and subtraction operators. Create the air cuboid using setBlocks() and increase the first x, y, and z arguments by 1. Then subtract 1 from the x + width, y + height, and z + length arguments
```
from mcpi.minecraft import Minecraft 
mc = Minecraft.create()
pos = mc.player.getPos()
x = pos.x 
y = pos.y 
z = pos.z 
width = 10 
height = 5 
length = 6
blockType = 41
air = 0
mc.setBlocks(x, y, z, x + width, y + height, z + length, blockType) 

# Make the new structure hollow
mc.setBlocks(x+1, y+1, z+1, x + width-1, y + height-1, z + length-1, air) 
```
