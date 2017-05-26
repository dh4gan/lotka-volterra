# Written 26/5/17 by dh4gan
# Module containing functions for Lotka-Volterra systems
# (Predator-Prey models)

import numpy as np
import matplotlib.pyplot as plt

predlabel = 'Predator Count (Thousands)'
preylabel = 'Prey Count (Thousands)'
timelabel = 'Time'

predcolor = 'red'
preycolor = 'blue'

class Lotka_Volterra(object):
    '''Sets up a simple Lotka_Volterra system'''
    
    def __init__(self, pdgrow,pddie,pygrow,pydie,tmax,timestep):
        '''Create Lotka-Volterra system'''
        
        self.n = int(tmax/timestep)
        self.dt = timestep
        self.time = np.zeros(self.n)
        self.prey = np.zeros(self.n)
        self.predator = np.zeros(self.n)
        self.preygrow = pygrow
        self.preydie = pydie
        self.predgrow = pdgrow
        self.preddie = pddie
        
    def set_initial_conditions(self,pdzero,pyzero, tzero=0.0):
        '''set initial conditions'''
        self.prey[0] = pyzero
        self.predator[0] = pdzero
        self.time[0] = tzero
        
    def integrate(self):
        '''integrate vanilla Lotka-Volterra system (simple Euler method)'''
        for i in range(self.n-1):
                        
            self.time[i+1] = self.time[i] + self.dt
            self.predator[i+1] = self.predator[i] + self.dt*self.predator[i]*(self.predgrow*self.prey[i] - self.preddie)
            self.prey[i+1] = self.prey[i] + self.dt*self.prey[i]*(self.preygrow - self.predator[i]*self.preydie)

        
    def integrate_stochastic(self):
        '''integrate vanilla Lotka-Volterra system (simple Euler method)'''
        for i in range(self.n-1):
                        
            self.time[i+1] = self.time[i] + self.dt
            self.predator[i+1] = self.predator[i] + self.dt*self.predator[i]*(self.predgrow*self.prey[i] - self.preddie*(1-0.1)*np.random.rand())
            self.prey[i+1] = self.prey[i] + self.dt*self.prey[i]*(self.preygrow*(1-0.1)*np.random.rand() - self.predator[i]*self.preydie)

            
    def plot_vs_time(self, filename='populations_vs_time.png'):
        
        '''Plot both populations vs time'''
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        ax2 = ax1.twinx()
        ax1.set_xlabel('Time')
        ax1.set_ylabel(predlabel,fontsize=22, color=predcolor)
        ax1.tick_params('y', colors=predcolor)
        ax2.set_ylabel(preylabel,fontsize=22, color=preycolor)
        ax2.tick_params('y', colors='blue', color=preycolor)
        ax1.plot(self.time, self.predator, label='Predator', color=predcolor)
        ax2.plot(self.time, self.prey, label = 'Prey', color = preycolor)
        
        plt.show()
        fig1.savefig(filename)
        
    def plot_predator_vs_prey(self, filename = 'predator_vs_prey.png'):
        
        '''Plot predators vs prey'''
        fig1 = plt.figure()
        ax1 = fig1.add_subplot(111)
        
        ax1.set_xlabel(predlabel,fontsize=22)
        ax1.set_ylabel(preylabel,fontsize=22)
        ax1.plot(self.predator,self.prey, color='black')
        plt.show()
        fig1.savefig(filename)
        
    def plot_both_figures(self):
        
        '''Plot both populations vs time & predators vs prey'''
        fig1 = plt.figure()
        
        ax1 = fig1.add_subplot(211)
        ax2 = ax1.twinx()
        ax1.set_xlabel(timelabel)
        ax1.set_ylabel(predlabel, color=predcolor)
        ax2.set_ylabel(preylabel, color =preycolor)
        ax1.plot(self.time, self.predator, label='Predator', color=predcolor)
        ax2.plot(self.time, self.prey, label = 'Prey', color = preycolor)
        ax1.legend()
        
        ax3 = fig1.add_subplot(212)
        
        ax3.set_xlabel(predlabel)
        ax3.set_ylabel(preylabel)
        ax3.plot(self.predator,self.prey, color = 'black')
        
        plt.show()
        
        
        