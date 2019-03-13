A program is a set of instructions that makes your computer do a specific task or tasks

Variables can store numbers, words, and even complete sentences

To create a variable in Python, you’ll use a variable name, an equal sign (=), and a value.
```
numOfPickaxes = 12 
```

- **numOfPickaxes** is the variable name 
- **12** is the value of that variable

You can use almost any name for a variable, but it’s best to use a name that describes the variable’s purpose so you’ll understand what’s going on in your program. Although it’s not a rule, you should start variable names
with a lowercase letter instead of a capital letter.

#### Note: 
Although the value of a variable is stored, it is not saved. The value of a variable is stored in the computer’s temporary memory, meaning that when the computer is switched off or the program stops running, the value of the variable is no longer stored. 

#### The structure of Programming Languages
Syntax is the set of rules that describes the grammar and punctuation of a programming language, similar to the grammar and punctuation in a human language. However, if you don’t use correct syntax, the computer won’t understand what you’re telling it to do.

Think of a single instruction in your code as a sentence. To end a sentence in English, you use a period (called a full stop in the United Kingdom). Instead of a period, Python uses a new line to indicate the end of an instruction and the start of the next. Each instruction on a new line is
called a statement.

Notice that each statement is on its own line. Because of the new lines, Python will understand that you want to keep track of three different items. But if you don’t put each statement on a new line, Python gets confused and gives you a syntax error:
``` numOfPickaxes = 12 iron = 30 cobblestone = 25 ```
<span style="color:red"> SyntaxError: invalid syntax</span>

A syntax error is Python’s way of telling you it doesn’t understand.

Python also won’t know what to do if you start lines with a space: 
```[space]   iron = 30 ```

<span style="color:red"> SyntaxError: unexpected indent </span>


#### Syntax Rules for Variables
 You need to know a few syntax rules for naming variables so Python can understand them:
• Don’t include symbols in your variable names, except for underscores (_), or you’ll get a syntax error.
• Don’t start a variable name with a number, as in 9bread. Using numbers elsewhere in a variable name is fine, as in bread9.
• You don’t need to add spaces on either side of the equal sign: your program will run fine without them. But they do make the code easier to
read, so it’s a good idea to add them.

#### Changing the Values of Variables 
You can change the value of a variable at any time in the same way you’d declare a variable.

```
numOfPickaxes = 10
numOfPickaxes = 20 # updating the value
```

When you ask Python for the new value of num, it’s no longer 10! Now when you use the **numOfPickaxes** variable in a program, it will use the new value of 20.

#### Integers 
Integers are positive or negative whole numbers. Values such as 10, 32, −6, 194689, and −5 are integers, but 3.14 and 6.025 are not

 #### Comments Comments are useful statements in code that describe what the code does but are ignored by Python. In other words, when you run the program, Python passes commented lines without doing anything. A single-line com-
ment begins with a hash mark (#)

<hr></hr>
#### Setting the players positon 

In the file SettingPlaterPosition.py the setTilePos() part of the program is a **function**, which is a prewritten and reusable piece of code. The setTilePos(x, y, z) function tells Minecraft to change the player’s position using the three **variables** you just set. The **values** inside the parentheses are called **arguments**. You passed the variables you just created to the function as **arguments** so the function can use the values of **x**, **y**, and **z** when it runs.

```
# Connect to Minecraft
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# Set x, y, and z variables to represent coordinate
x = 100
y = 120
z = 1000

# Change the player's position
mc.player.setTilePos(x, y, z)
```

<hr>  </hr>

#### Floats 
Not all numbers are whole numbers. Decimal points are used to represent values that can’t be described with whole numbers. For example, you might have half (0.5) of an apple. Numbers that use decimal points are called **floating point numbers**, or **floats**. This is another data type that Python uses. Floating point numbers are used instead of integers when you want to be more precise. Floats can also represent whole numbers (as in 3.0), but integers can’t represent numbers with decimal places

<hr></hr>
 The setPos() **function** is a little different—it uses floats to tell the game the position of the block as well as the precise position on that
block that you want to teleport to.
