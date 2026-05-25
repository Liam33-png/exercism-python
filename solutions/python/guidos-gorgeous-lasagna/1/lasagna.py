



EXPECTED_BAKE_TIME = 40





def bake_time_remaining(elapsed_bake_time):
    """Find the bake time remaining
    
    Parameters:
    elapsed_bake_time (int): the bake time elapsed

    Returns: 
    int: the total time remaining
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time




def preparation_time_in_minutes(number_of_layers):
    """ find preperation time

    Parameters:
    number_of_layers (int): the number of layers
    
    Returns: 
    int: the total time remaining
    """
    return number_of_layers * 2



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """find the elapsed time in minutes
    Parameters:
    number_of_layers (int): the number of layers
    elapsed bake time (int): the elapsed bake time
    
        Returns: 
    int: the total time remaining    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
