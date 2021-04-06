#By: Kay Towner


def rk4(timestep = None,
        max_time = None,
        initial_time = None,
        initial_val = None,
        deriv = None,
        deriv_params = None):
    """This function returns the RK9 method. h = distance
    f= the derivative, x=the maximum time, x0=the initial value,
    t=the inital time.
    """
    h=timestep
    x0=initial_time
    xn=max_time
    y0= initial_val
    f= deriv
    n = 100
    
    h = (xn-x0)/n
    for i in range(n):
        k1 = h*f(x0, y0)
        k2 = h*f(x0+(h/2), y0+k1/2)
        k3 = h*f(x0+(h/2), y0+k2/2)
        k4 = h*f(x0+h, y0+k3)
        k = (k1 + 2*k2 + 2*k3 + k4)/6

        yn = y0 + k
        y0 = yn
        x0 = x0+h
    return(xn, yn)












