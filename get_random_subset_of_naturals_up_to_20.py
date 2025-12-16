def get_random_subset_of_naturals_up_to_20():
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    #use binary representation
    import numpy as np
    
    random = np.random.randint(0, 2**20)
    
    bits = np.array(list(np.binary_repr(random, width=20)), dtype=int)
    
    subset = np.arange(1, 21)[bits == 1]
    
    return subset
    pass
    ### Replace with your own code (end)   ###


