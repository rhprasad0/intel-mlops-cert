# support bot logic

def test_support_bot(query:str):
    """_summary_

    Parameters
    ----------
    temperature : int
        test parameter for temperature sensor readings

    Returns
    -------
    str
        'Approved' or 'Denied' based on temperature readings
    """
    maintenance_status = 'bring the harvester in for maintenance' if query == 'help' else 'do not bring in harvester'
    
    return maintenance_status