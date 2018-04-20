# Written 26/5/17 by dh4gan

from lotka_volterra import Lotka_Volterra

tmax = 100.0
timestep = 0.0001

predator_growth = 1.0
predator_death = 2.0
predator_initial = 1.0e-2
predcap = 1.0e9

prey_growth = 10
prey_death = 0.1
prey_initial = 100
preycap = 70


L = Lotka_Volterra(predator_growth, predator_death, prey_growth,prey_death,tmax,timestep,prey_capacity = preycap, predator_capacity = predcap)
L.set_initial_conditions(predator_initial, prey_initial)
L.integrate_logistic()
L.plot_vs_time(filename = 'LT_vs_time_logistic.png')
L.plot_predator_vs_prey(filename = 'LT_PvsP_logistic.png')
