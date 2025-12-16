def estimate_pi(num_samples):
    """
    Replace the code below with your own implementation.
    """

    ### Replace with your own code (begin) ###
    import numpy as np
    p = 0
    
    for n in range(0, num_samples):    
        x = np.random.rand()
        y = np.random.rand()
        
        d = (x*x + y*y)**0.5
    
        if d < 1:
            p += 1
        
    pi = 4 * p/num_samples
    
    return pi

    pass
    ### Replace with your own code (end)   ###
