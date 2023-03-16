$(document).ready(function () {
    // init map
    doWork();
  
});
  
function doWork() {
    // Store our API endpoint as queryUrl.
    let queryUrl = `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson`;
    let geoURL = "static/data/PB2002_boundaries.json"

    // reset map container
    $("#mapContainer").empty();
    $("#mapContainer").append("<div style='height:800px' id='map'></div>")

    // Perform a GET request to the query URL.
    d3.json(queryUrl).then(function(data){
        console.log(data);

        makeMap(data);
    });
}
  
function makeCircleRadius(mag){
    return mag**8
}

function getColor(depth){
    if (depth > 90) {
        return "#580040";
    }
    else if (depth > 70) {
        return "#920330";
    }
    else if (depth > 50) {
        return "#F24697";
    }
    else if (depth > 30) {
        return "#FF8337";
    }
    else if (depth > 10) {
        return "#FCB80D";
    }
    else {
        return "#E1FF3A"
    }
}

// make map
function makeMap(data) {

    // STEP 1: CREATE THE BASE LAYERS

    let street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    })

    let topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
    });


    // STEP 2: CREATE THE OVERLAY/DATA LAYERS
    let circleMarkers = [];

    for (let i = 0; i < data.features.length; i++) {
        let quake = data.features[i];
        let location = quake.geometry.coordinates;

        if (location) {
            let circle = L.circle([location[1], location[0]], {
                                fillOpacity: 0.75,
                                color: getColor(location[2]),
                                weight: 7,
                                fillColor: getColor(location[2]),
                                radius: makeCircleRadius(quake.properties.mag)
                                }).bindPopup(`<h1>Earthquake</h1> <hr>
                                            <h1> ${quake.properties.title} </h1> <hr> 
                                            <h3>Magnitude: ${quake.properties.mag}</h3> <hr>
                                            <h3>Depth: ${location[2]}<h3>`);

            circleMarkers.push(circle);
        }
    }

    let circleLayer = L.layerGroup(circleMarkers)

    // STEP 3: CREATE THE LAYER CONTROL OBJECTS
    let baseMaps = {
        Street: street,
        Topography: topo
    };

    // Overlays that can be toggled on or off
    let overlayMaps = {
        Markers: circleLayer
    };

    // STEP 4: INITIALIZE MAP
    let myMap = L.map("map", {
        center: [37.7749, -122.4194],
        zoom: 3,
        layers: [street, circleLayer]
    });

    // STEP 5: ADD LAYER CONTROL TO MAP
    // Create a layer control that contains our baseMaps and overlayMaps, and add them to the map.
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

    // Step 6: ADD LEGEND TO MAP
    var legend = L.control({ position: "bottomleft" });
    legend.onAdd = function(map) {
        var div = L.DomUtil.create("div", "legend");
        div.innerHTML += "<h4>Magnitude Legend:</h4>";
        div.innerHTML += '<i style="background: #580040"></i><span>>90</span><br>';
        div.innerHTML += '<i style="background: #920330"></i><span>70 - 90</span><br>';
        div.innerHTML += '<i style="background: #F24697"></i><span>50 - 70</span><br>';
        div.innerHTML += '<i style="background: #FF8337"></i><span>30 - 50</span><br>';
        div.innerHTML += '<i style="background: #FCB80D"></i><span>10 - 30</span><br>';
        div.innerHTML += '<i style="background: #E1FF3A"></i><span><10</span><br>';
        
        return div;
    };
    legend.addTo(myMap);
}