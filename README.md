 To play game run python3.5 main.py.
 Mario:
 To move sidewards use a,d.To jump use w.
 I have implemented jump using quadratic equation.So as to get gravity like feeling.
 Obstacles:
 I have implemented pipes,bridges,springs.
 I have created pits where you can fall and die.
 You get extra jump height from string
 Enemies:
 I have created two kinds of enemies tortise and boss.
 Tortise have a fixed motion.There are 2 tortises each moves at different velocity.
 My Boss is strong and clever.He follows mario.He has additional powerup.He can
 decrease health of mario if he stays on ground for more than 8 seconds continously.
 To kill enemy:
 Jump on enemy
 IF Enemy hits you your health decreases by 1 unit.
 Score:
 I increase scores for coins and enemies.But my score increments with time differently.
 It firsts increases uptill some time and then decreases.So complete game as fast as
 possible.I gave bonus score for completing game fast.
 Kill tortise 100 points
 Kill boss 200 points
 Collect coins 50 points
 Complete before expected time 100 points
Level:
Hybrid Level.
You go from level 1 to level 2.You cant go back unless you die or kill boss.
If boss is killed you win.If you are out of lives you lose.
