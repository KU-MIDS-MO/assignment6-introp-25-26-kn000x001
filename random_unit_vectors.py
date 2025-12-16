def random_unit_vectors(num_vectors, dim):
    """
    Replace the code below with your own implementation.
    """
    ### Replace with your own code (begin) ###
    import numpy as np

    M = np.random.randn(num_vectors, dim)
    
    norm = np.linalg.norm(M, axis=1, keepdims=True)
    
    M_unit = M / norm
    
    return M_unit
    pass
    ### Replace with your own code (end)   ###
