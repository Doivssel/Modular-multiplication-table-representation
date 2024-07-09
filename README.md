# Modular multipliaction table representation

This code produce a tkinter window that allow you to animate/draw a nice representation of modular tables. Here are some graphs as an example, there is also a gif that show some animation.

<img src="https://github.com/Doivssel/Modular-table-representation/assets/172904759/0a7c9c9c-46c1-40fc-b746-945ab1c671e4" width="600" height="400">
<img src="https://github.com/Doivssel/Modular-table-representation/assets/172904759/d3dc39a4-f01c-4456-baa2-5d65ea114f9c" width="600" height="400">

## Parameters

The tkinter window is of the following form.

![window_mod](https://github.com/Doivssel/Modular-table-representation/assets/172904759/4ea2d6f0-5438-4201-84c0-131844440bd3)

Here is an explanation of the parameters

1. **modulo**: integer, self explanatory
2. **table**: integer, self explanatory
3. **speed**: integer, change the speed of the animation, represent the time between each frame update in ms
4. **animation modulo**: if checked, animate the modulo by updating every **speed** ms the graph and increasing the modulo from 0 to **modulo**. For example if **modulo**=10 and **table**=5, this will show **modulo**=0, **table**=5, then update to **modulo**=1, **table**=5 then update... until **modulo**=10, **table**=5
5. **animation table**: does the same thing as **animation modulo** but for **table**
6. **calculate**: if clicked, draw/animate
7. **stop**:  if clicked, stop the current animation
8. **download**: self explanatory
9. **quit**: self explanatory

## How it work

Before explaining how this work, you must get familiar with the concept of the modulo. It is a simple operation, that give out the remainder of an euclidian division.
For example computing 5 modulo 2 give 1. A more intuitive approach, would be how clocks work, to get the minutes you actually perform a modulo operation, well not only the minutes in fact. For example, if its 14h45 and you want know wich minutes it will be in 30 minutes. You usually compute 45 plus 30, that is 75 but this is not on the clock. So you then substract 60 to get 15, the right answer. Well what you performed here is a modulo operation in base 60. Mathematicaly we write it like that $75 \equiv 15 \ (\textrm{mod}\ 60)$.

Now you need to apply this modulo operation on the usual multiplication tables to get the nice graphs. For example let's do the table 5 modulo 10,

1. $5 \times 1=5$ and $5 \equiv 5 \ (\textrm{mod}\ 10)$
2. $5 \times 2=10$ and $10 \equiv 0 \ (\textrm{mod}\ 10)$
3. $5 \times 3=15$ and $15 \equiv 5 \ (\textrm{mod}\ 10)$
4. $5 \times 4=20$ and $20 \equiv 0 \ (\textrm{mod}\ 10)$
5. $5 \times 5=25$ and $25 \equiv 5 \ (\textrm{mod}\ 10)$
6. $5 \times 6=30$ and $30 \equiv 0 \ (\textrm{mod}\ 10)$
7. $5 \times 7=35$ and $35 \equiv 5 \ (\textrm{mod}\ 10)$
8. $5 \times 8=40$ and $40 \equiv 0 \ (\textrm{mod}\ 10)$
9. $5 \times 9=45$ and $45 \equiv 5 \ (\textrm{mod}\ 10)$
10. $5 \times 10=50$ and $50 \equiv 0 \ (\textrm{mod}\ 10)$

Then you put ten evenly distributed points on a circle, and draw a line between point representing the number of time 5 has been multiplied and the result of the modulo operation. For example there is a line between 1 and 5, between 2 and 0... In the end that give the following graph,

<img src="https://github.com/Doivssel/Modular-table-representation/assets/172904759/85e9058c-e226-4037-aef1-129bfc024c9c" width="600" height="400">

## Note

When you download a graph the tkinter window may be unresponsive for a few seconds, I have no idea why it does that. But just waiting a few seconds solve the problem.
