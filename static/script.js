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
                        let data = await res.json();
                        let warningContainer = document.getElementById('warning');
                        warningContainer.innerText = ''
                        if (!warningContainer.classList.contains('hide'))
                            warningContainer.classList.add('hide');
                        document.getElementById('result').innerHTML = '<p>Result: ' + JSON.stringify(data.shortest_path) + '</p>';

                         // Clear previous markers
                         mymap.eachLayer(function (layer) {
                            if (layer instanceof L.Marker || layer instanceof L.Path) {
                                mymap.removeLayer(layer);
                            }
                        });

                        // Add paths as blue lines
                        for (const [junction, coordinates] of Object.entries(data.graph)) {
                            for (let i = 1; i < coordinates.length; i++) {
                                L.polyline([
                                    [coordinates[i - 1][0], coordinates[i - 1][1]],
                                    [coordinates[i][0], coordinates[i][1]]
                                ], { color: 'blue' }).addTo(mymap).bindPopup(`<b>${junction}</b>`);;
                            }
                        }
                        // Add junctions as green circles
                        for (const [junction, coordinates] of Object.entries(data.graph)) {
                            const latlng = L.latLng(coordinates[0][0], coordinates[0][1]);
                            L.circleMarker(latlng, { color: 'green', fillColor: 'green', fillOpacity: 1, radius: 5 })
                                .addTo(mymap)
                                .bindPopup(`<b>${junction}</b>`);
                        }

                        
                        // Add new markers for coordinates
                        const startCoords = JSON.parse('[' + startPoint + ']');
                        const endCoords = JSON.parse('[' + endPoint + ']');
                        L.marker(startCoords).addTo(mymap).bindPopup(`Start Point <br/> ${startCoords}`);
                        L.marker(endCoords).addTo(mymap).bindPopup('End Point');
                        L.polyline(data.shortest_path, { color: 'red' }).addTo(mymap);

                        // Set map bounds
                        const bounds = L.latLngBounds(Object.values([...Object.values(data.graph),startCoords,endCoords]).flat());
                        mymap.fitBounds(bounds);
                    }
                    else {
                        warning = await res.text()
                        warningContainer = document.getElementById('warning');
                        warningContainer.innerText = warning;
                        warningContainer.classList.remove('hide')


                    }
                }
                catch (error) {
                    console.error('Error:', error);
                }
            })
        })
