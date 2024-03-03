document.addEventListener('DOMContentLoaded', function () {
    const mymap = L.map('map').setView([31.69, 35.33], 8); // Set initial view                        

    // Add base map tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
    }).addTo(mymap);

    coordinateForm.addEventListener('submit', async function (event) {
        event.preventDefault();
        const startPoint = document.getElementById('startPoint').value;
        const endPoint = document.getElementById('endPoint').value;
        const data = JSON.stringify({
            'start_point': startPoint,
            'end_point': endPoint
        });
        try {
            res = await fetch('/shortest_path', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: data
            });
            if (res.status >= 200 && res.status < 300) {
                // Remove any warning if present 
                let data = await res.json();
                let warningContainer = document.getElementById('warning');
                warningContainer.innerText = ''
                if (!warningContainer.classList.contains('hide'))
                    warningContainer.classList.add('hide');

                // Show Results
                if ('shortest_path' in data)
                    document.getElementById('result').innerHTML = '<p class="alert alert-success" >Result: ' + JSON.stringify(data.shortest_path) + '</p>';
                    showGraphOnMap(mymap, graphData, data.shortest_path, startPoint, endPoint);

                // Create download kml button
                if ('kml' in data)
                    downloadKml(data.kml);
                
            }
            // on failure Show warning message 
            else {
                warning = await res.text()
                warningContainer = document.getElementById('warning');
                warningContainer.innerText = warning;
                warningContainer.classList.remove('hide')
            }
        }
        catch (error) {
            console.error('Error:', error);
            warningContainer = document.getElementById('warning');
            warningContainer.innerText = 'Somthing went wrong  , Cheack your network connection';
            warningContainer.classList.remove('hide')
        }
    })
})

function downloadKml(kmlText) {
    var blob = new Blob([kmlText], { type: 'text/kml' });
    downloadContainer = document.getElementById('download');
    downloadContainer.innerHTML = '';
    var a = document.createElement('a');
    a.innerText = "Download Kml"
    a.download = 'results.kml';
    a.className = "btn btn-outline-primary"
    a.href = URL.createObjectURL(blob);
    a.dataset.downloadurl = ["kml", a.download, a.href].join(':');
    downloadContainer.appendChild(a);
}

function showGraphOnMap(map, graph, shortest_path, startPoint, endPoint) {
    map.eachLayer(function (layer) {
        if (layer instanceof L.Marker || layer instanceof L.Path) {
            map.removeLayer(layer);
        }
    });

    let junctions = []
    // Add paths as blue lines
    for (const [junction, coordinates] of Object.entries(graph)) {
        let parsedJunction = JSON.parse(junction.replace('(', '[').replace(')', ']'));
        junctions.push(parsedJunction)
        for (let i = 0; i < coordinates.length; i++) {
            L.polyline([
                [parsedJunction[0], parsedJunction[1]],
                [coordinates[i][0], coordinates[i][1]]
            ], { color: 'blue' ,opacity:0.2}).addTo(map).bindPopup(`<b>${coordinates[i]}</b>`);;
        }
    }
    junctions.forEach(junction => {
        // Add junctions as green circles    
        const latlng = L.latLng(junction[0], junction[1]);
        L.circleMarker(latlng, { color: 'green',opacity:0.6, fillOpacity: 0, radius: 3 })
            .addTo(map)
            .bindPopup(`<b>${junction}</b>`);
    });

    debugger;
    // Add new markers for coordinates
    const startCoords = shortest_path[0];
    const endCoords = shortest_path[shortest_path.length - 1];
    L.marker(startCoords).addTo(map).bindPopup(`Start Point <br/> ${startCoords}`);
    L.marker(endCoords).addTo(map).bindPopup(`End Point <br/> ${endCoords} `);
    L.polyline(shortest_path, { color: 'red' }).addTo(map);

    // Set map bounds
    const bounds = L.latLngBounds(Object.values([...Object.values(graph), startCoords, endCoords]).flat());
    map.fitBounds(bounds);

}

