#By Kay towner
import math
import numpy as np
import rk4 as method
import matplotlib.pyplot as plt

m = 0.145 #kg
g = np.array([0, -9.8]) #m/s^2 accel of gravity as surface
rho = 1.225 #kg/m^3 density of air (p)
Cd = 0.47 #unitless, drag coefficiant
A = 0.008414 #ms^2, cross sect baseball 

def grav(m=None, g=None):
    """gravity equation. m= mass, g= gravity."""
    grav = -m * g
    return grav

def drag(p=None, vect=None, C=None, A=None):
    """Drag formula.
    p= air density, v= velocity as a vector, C= drag, A= area,
    """
    return -(1/2)* p * np.abs(vect)**2 * C * A * vect

def analytic_projectile_nodrag(t, initial_position=None,
                               initial_velocity=None):
    """Function of the analytical projection without drag. y(t)
    inital_velocity = vector of  velocity"""
    times = t[:,np.newaxis]
    return initial_position + initial_velocity * times + g * 0.5 * times**2

def analytic_projectile_drag(t, initial_position=None,
                             initial_velocity=None):
    """Function of the analytical projection with drag. y(t)
    inital_velocity = vector of  velocity"""
    times = t[:,np.newaxis]
    return initial_position + initial_velocity * times + g * 0.5 * times**2

#rk4 is called from a module
    
if __name__ == "__main__":
#VARIABLES:
    times = np.arange(0, 10, 0.01)
    theta = 45*np.pi/180 
    speed = 10 #m/s
    x0 = np.array([0,0])
    v0 = speed*np.array([np.cos(theta), np.sin(theta)])
    vel = 85 #m/s  #velocity of the ball (for part b.)

#grav and drag:
    Fg = grav(m=m, g=g)
    Fd = drag(p=rho, vect=v0, C=Cd, A=A)
    print("gravity is equal to:", Fg, "Drag is:", Fd)

#a.)
    positions = analytic_projectile_nodrag(times, initial_position=x0,
                               initial_velocity=v0)
    print("Positions without drag:", positions)

    rk4positions = method.rk4(timestep = 0.1, max_time = 100, initial_time = 0,
                        initial_val = v0, deriv = positions, deriv_params = None)
    print("RK4 Positions without drag:", rk4positions)


#b.)
    positionsDrag = analytic_projectile_drag(times, initial_position=x0,
                             initial_velocity=v0)+ Fg
    print("Positions with drag:", positionsDrag)

    #show at the different angles, with air resist vs without.(drag):
    theta30 = np.array([np.cos(45*np.pi/180), np.sin(45*np.pi/180)]) * vel 
    theta45 = np.array([np.cos(45*np.pi/180), np.sin(45*np.pi/180)]) * vel 
    theta60 = np.array([np.cos(60*np.pi/180), np.sin(60*np.pi/180)]) * vel 

    angle30 = method.rk4(timestep = 0.1, max_time = 100, initial_time = 0,
                        initial_val = theta30, deriv = positionsDrag, deriv_params = None)
    
    angle45 = method.rk4(timestep = 0.1, max_time = 100, initial_time = 0,
                        initial_val = theta45, deriv = positionsDrag, deriv_params = None)

    angle60 = method.rk4(timestep = 0.1, max_time = 100, initial_time = 0,
                        initial_val = theta60, deriv = positionsDrag, deriv_params = None)
    
     
#Plotting:
    #a.
    plt.plot(positions)
    plt.plot(rk4positions, 'b--')
    plt.title('Projectile Motion')
    plt.xlabel('time (sec)')
    plt.ylabel('position')
    plt.show()
    plt.savefig('ProjectileMotionGraph.jpeg')
    #b.
    plt.plot(positionsDrag)
    plt.plot(rk4positionsdrag, 'b--')
    plt.plot(angle30)
    plt.plot(angle45)
    plt.plot(angle60)
    plt.title('Projectile Motion')
    plt.xlabel('time (sec)')
    plt.ylabel('position')
    plt.show()
    plt.savefig('ProjectileMotionGraph2.jpeg')

 
