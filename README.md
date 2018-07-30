# lotka-volterra

This Python code integrates the Lotka-Volterra equations for Predator-Prey systems.

## Lotka-Volterra Systems

The Lotka-Volterra equations are perhaps the simplest expression of predator-prey competition.  If we have *R* prey and *P* predators, and we now the birth rates *b* and death rates *d* of each, then the simplest expression of the Lotka-Volterra System is 

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{dR}{dt}&space;=&space;b_R&space;R&space;-&space;d_R&space;R&space;P&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{dR}{dt}&space;=&space;b_R&space;R&space;-&space;d_R&space;R&space;P&space;\\" title="\frac{dR}{dt} = b_R R - d_R R P \\" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{dP}{dt}&space;=&space;b_P&space;R&space;P&space;-&space;d_P&space;P&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{dP}{dt}&space;=&space;b_P&space;R&space;P&space;-&space;d_P&space;P&space;\\" title="\frac{dP}{dt} = b_P R P - d_P P \\" /></a>

A typical solution to this system gives *R* and *P* being periodic and out of phase.  Prey grow exponentially, then predators feed on the overpopulated prey and grow exponentially until local prey are exhausted.  The predators die off, and then prey are able to return, and the cycle repeats.

If we assume that there is a finite carrying capacity *K* for the prey, then the prey evolution equation becomes

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{dR}{dt}&space;=&space;b_R&space;R(1-\frac{R}{K})&space;-&space;d_P&space;P&space;\\" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{dR}{dt}&space;=&space;b_R&space;R(1-\frac{R}{K})&space;-&space;d_P&space;P&space;\\" title="\frac{dR}{dt} = b_R R(1-\frac{R}{K}) - d_P P \\" /></a>

In this case, the system's oscillations are damped, and eventually an equilibrium prey/predator population is reached.

## Using The Code

The code is written in Python 2.7, and was developed using numpy 1.8.0, matplotlib 1.3.0.  The main code is stored in the module `lotka_volterra.py`, which is accessed by either: 

 1. `solve_system.py` (which integrates the equations assuming exponential growth), or
 2. `solve_system_logistic.py` (which integrates the equations assuming logistic growth towards a finite carrying capacity)

Users need simply edit these scripts to specify the correct initial conditions, and execute them using e.g.

> `python solve_system.py` 

To integrate the system, and to create figures of the system's time evolution.

