# **Graph-Based Route Finder Installation Guide:**


## To install the Graph-Based Route Finder, please follow these steps:

1. Install the latest stable version of Python.
   
2. Install the Python requirements by running the following command in your terminal: ```pip install -r requirements.txt```.\
   It is recommended to install the requirements in a virtual environment.

## Usage

1. Activate the server by running the command ``python app.py`` in your terminal.
   
2. To access the user interface, go to http://localhost:5000/ in your web browser.
3. Alternatively, you can send a POST request to http://localhost:5000/shortest_path with a JSON body containing the `start_point` and `end_point` key:value pairs.    
   The request headers should include  `Content-Type: application/json`.

   If the request is successful, you will receive a JSON response with the following keys:\
   `shortest_path`: array of coordinates from `start_point` to `end_point`.\
   `kml`: KML format representation of the shortest path.\
   `graph`: the original predefined graph (which is used by the UI).
