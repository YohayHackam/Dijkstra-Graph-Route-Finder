import html
from flask import Flask, request, jsonify,render_template,Response
import json
from graph import Graph
from kml import generate_kml
from util import data_cleanup_and_parsing

app = Flask(__name__)

with open('graph_example.json') as f:
    graph_data = json.load(f)
    graph_data = data_cleanup_and_parsing(graph_data)
    graph = Graph(graph_data)

@app.route('/')
def index():
    parsed_graph={str(k):v for k,v in graph_data.items()}
    return render_template('index.html',graph_data=parsed_graph)


@app.route('/shortest_path', methods=['POST'])
def post_shortest_path():
    graph.reset_graph()
    try:
        data = request.get_json()
        start_point = html.escape(data['start_point'])
        end_point = html.escape(data['end_point'])        
        start_point = tuple(float(cord) for cord in start_point.strip("[{()}]").split(','))
        end_point = tuple(float(cord) for cord in end_point.strip("[{()}]").split(','))
        if not(len(start_point)==2 and len(end_point)==2):
            raise(ValueError)
        # Find the closest vertices to the start and end points
        start_vertex = graph.find_closest_coordinate(*start_point)
        end_vertex = graph.find_closest_coordinate(*end_point)
        # Compute the shortest path
        shortest_path = graph.find_path( start_vertex, end_vertex)
        # Add start & end points if outside graph
        if start_vertex.get_cords() != start_point:
            shortest_path.insert(0,start_point)
        if end_vertex.get_cords() != end_point:
            shortest_path.append(end_point)        
        # Genarate Kml
        kml =generate_kml(shortest_path)
    except ValueError:
        return Response("Bad input",422)
    except Exception:
        return Response("Somthing went wrong",500)
    
    return jsonify({"shortest_path": shortest_path, "kml":kml})


if __name__ == '__main__':
    app.run(debug=True)
