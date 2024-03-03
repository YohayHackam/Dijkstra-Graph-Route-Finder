
def data_cleanup_and_parsing(graph_data) -> dict:
    """
    The function `data_cleanup_and_parsing` takes graph data, cleans it up, and parses it into a
    dictionary format.
    
    :param graph_data: It looks like the code you provided is a function called
    `data_cleanup_and_parsing` that takes in a dictionary `graph_data` as input. The function seems to
    be cleaning up and parsing the data in the `graph_data` dictionary to create a new data structure
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
            

        
