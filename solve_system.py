# Written 26/5/17 by dh4gan

from lotka_volterra import Lotka_Volterra

tmax = 30
timestep = 0.0001

predator_growth = 1
predator_death = 1
predator_initial = 1.8

prey_growth = 0.6666
prey_death = 1.3333
prey_initial = 1.8


L = Lotka_Volterra(predator_growth, predator_death, prey_growth,prey_death,tmax,timestep)
L.set_initial_conditions(predator_initial, prey_initial)
L.integrate()
L.plot_vs_time(filename = 'LT_vs_time.png')
L.plot_predator_vs_prey(filename = 'LT_PvsP.png')
