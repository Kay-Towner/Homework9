#finished by Kay Towner

import numpy as np
import rk4 as method 
import matplotlib.pyplot as plt


#FUNCTIONS:
def analytic_solution(t, K=1, P0=1, r=0.01):
    """K = maximum carrying capacity of ecosystem
       P0 = initial population at time t=0
       r = population growth rate (eg, 1% = 0.01
       t = time """
    numer = K * P0 * np.exp(r*t)
    denom = K  + P0*(np.exp(r*t)-1)
    return numer / denom

def dP_dt(P, K=1, r=0.01):
    """Differential equation that is important in ecology.
    Takes in P, K and r
    P= population size
    K= carrying capacity 
    r= population growth rate
    """
    return r*P*(1-(P/K))

def forward_euler(timestep = None,
                  max_time = None,
                  initial_time = None,
                  initial_val = None,
                  deriv = None, #pass dP_dt
                  deriv_params = None):
    """Forward Euler method to run on the dP_dt function:
    """
    initial_time = 0
    timerange = np.arange(initial_time, max_time)
    euler = []
    x = initial_val
    for t in timerange:
        euler.append(x)
        x += timestep * deriv(x)

    # x(t)+h*f(x,t)
    return euler

#(def rk4 is imported as a module. I've written it in it's own .py file)

#MAIN:
if __name__ == "__main__":
    K = 10 #10 billion
    P0 = 1 #billion, population at year 1800
    r = 0.014 #1.4% growth rate
    start_year = 1800
    max_year = 2300
    max_time = max_year - start_year
    years_since_start = np.arange(0, max_time)
    timestep = 25
#a.)
    analytic_sol = analytic_solution(years_since_start, K=K, P0=P0, r=r)

#b.)    
    eulersol = forward_euler(timestep = timestep,
                  max_time = max_time,
                  initial_time = years_since_start,
                  initial_val = P0,
                  deriv = dP_dt,
                  deriv_params = {'K':K, 'r':r})
#c.)
    rk4sol = method.rk4(timestep = timestep, max_time = max_time,
                        initial_time = years_since_start,
                        initial_val = P0, deriv = dP_dt,
                        deriv_params = {'K':K, 'r':r})

#PLOTTING:

#a: plot the analytic solution:
    t = np.array(range(1800, 2300))
    y = analytic_sol #K * P0 * np.exp(r*t) / K  + P0*(np.exp(r*t)-1)
    plt.plot(t, y)
    plt.title('Analytic Solution')
    plt.xlabel('Years')
    plt.ylabel('Population [Billions]')
    #plt.show()
    plt.savefig('PartaHW9.jpeg')

#b: solve with the Euler method:  
    t = np.array(range(1800, 2300))
    y = analytic_sol #K * P0 * np.exp(r*t) / K  + P0*(np.exp(r*t)-1)
    y2 = eulersol
    plt.plot(t, y)
    plt.plot(t, y2, 'b--')
    plt.title('Part b of 1')
    plt.legend(["Analytic", "EulerMethod"])
    plt.xlabel('Years')
    plt.ylabel('Population [Billions]')
    #plt.show()
    plt.savefig('PartbHW9.jpeg')    

#c: plot with RK4 method:
    t = np.array(range(1800, 2300))
    y = analytic_sol #K * P0 * np.exp(r*t) / K  + P0*(np.exp(r*t)-1)
    y2 = eulersol
    y3 = rk4sol
    plt.plot(t, y)
    plt.plot(t, y2, 'b--')
    plt.plot(t, y3, 'b--')
    plt.title('Part c HW1')
    plt.legend(["Analytic", "EulerMethod", "RK4"])
    plt.xlabel('Years')
    plt.ylabel('Population [Billions]')
    plt.show()
    plt.savefig('PartcHW9.jpeg')







