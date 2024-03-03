
def data_cleanup_and_parsing(graph_data) -> dict:
    """
    The function `data_cleanup_and_parsing` takes graph data as input, cleans it up, and parses it into
    a dictionary format.
    
    :param graph_data: The function `data_cleanup_and_parsing` takes a dictionary `graph_data` as input,
    where the keys are string representations of coordinates and the values are lists of paths. The
    function cleans up and parses this data to create a new dictionary where the keys are tuples of
    coordinates and the values are lists
    :return: The function `data_cleanup_and_parsing` returns a dictionary where the keys are source
    points represented as tuples of float coordinates, and the values are lists of target points also
    represented as tuples of float coordinates. The function processes the input `graph_data` to clean
    up and parse the data into this dictionary format.
    """
    data={}    
    for str_cords, path_list in graph_data.items():        
        source_point = tuple(float(cord) for cord in str_cords.strip('()').split(','))
        if not source_point in data:
            data[source_point] = []
        for path in path_list:
            target_point = (path[0],path[1])
            if not target_point in data[source_point]:
                data[source_point].append(target_point)
            if not target_point in data:
                data[target_point] =[source_point]
            else:
                data[target_point].append(source_point)
    return data
            

        
