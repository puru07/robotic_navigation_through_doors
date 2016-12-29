# Navigating a Robot though Spring Loaded (pull) doors:

<h3>Report: </h3><b>final-robot-navigation-spring.pdf </b><br>
Details on implementation are in section : IV '<b>Implementation</b>'

<h3>Problem:</h3>
A planning algorithm to make a mobile manipulator
<br>pull open a spring loaded door and navigate through it. 

<h3>Solution:</h3> Lattice Based planne, using Astar .
<hr>
<h3>Robot Specs: </h3> <b>main.py</b> (cpp version in on the way)
<br>Single Arm mobile manipulator.
<br> The planner only depends on the workspace of the manipulator
<br> (not joint configuration) which could be set in <b>'main.py'</b>
<br>The type of locomotion (holonomic/non-holonomic) could be set
<br>by modifying the motion primitives in '<b>astar.py</b>' (cpp version is on the way).

<h3>Running the Planner: </h3>
run:  <b>main.py</b>  
<br><b>main.py</b> would use <b>astar.py</b> to find the states, as per the problem
<br>specs in main.py . 
<br>The solution is printed in <b>tree.txt</b>.

<h3>Visualtisation:</h3> <b>vismain.m </b>(needs matlab 2016a or later version)
<br>vismain.m reads tree.txt
<br>robot specs have to manually changed in vismain.m


