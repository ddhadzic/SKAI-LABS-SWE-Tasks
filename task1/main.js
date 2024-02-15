//function that retruns polygon values from JSON file or API specified with 'jsdon_URL'
function readJSON(json_URL){
    return fetch(json_URL)
        .then((response) => response.json())
        .then((json) => {
            return json.polygon;
        })
        .catch((error) => {
            console.error('Error fetching JSON:', error); 
            return [0,0] // returns a point in the center of the map as a fallback.
        });
}

//function to calculate the zoom level and center point based on the polygon's bounding box.
function calculateZoomAndCenter(poly){

    //Finds edge bounds of polygon and then calculates the middle of those 2 points 
    var min= {x:poly[0][0], y:poly[0][1]}
    var max= {x:poly[0][0], y:poly[0][1]}

    for (var i = 0; i < poly.length; i++) {
        var point = poly[i];
        if(point[0]<min.x){
            min.x=point[0]
        }
        else if(point[0]>max.x){
            max.x=point[0]
        }
        if(point[1]<min.y){
            min.y=point[1]
        }
        else if(point[1]>max.y){
            max.y=point[1]
        }
    }

    var center = [Math.abs(max.x + min.x),Math.abs(max.y + min.y)];

    // Calculate size of bounding box
    var deltaY = Math.abs(max.y - min.y);
    var deltaX = Math.abs(max.x - min.x);

    //to calculate zoom we need tile size and how many tiles the map uses (area)
    //increasing zoom by 1 halves the displayed area. Or by doubling deltaX or deltaY we have to zoom out by one, that's why log2 is used
    var tile_size =256;
    var area = 360 * 600;
    var zoomY = Math.log2(area / deltaY / tile_size);
    var zoomX = Math.log2(area / deltaX / tile_size);
    var zoom = Math.min(zoomX, zoomY);

    return {center:center, zoom:zoom};
}

document.addEventListener('DOMContentLoaded', function () {
    readJSON('polygon.json')
    .then(poly => {
        map_display =calculateZoomAndCenter(poly); //used to determine how to best display the map (zoom, center) 
        var map = new ol.Map({
            target: 'map',
            layers: [
                new ol.layer.Tile({
                    source: new ol.source.OSM()
                })
            ],
            view: new ol.View({
                center: ol.proj.fromLonLat(map_display.center),
                zoom: map_display.zoom
            })
        });

        //standard OpenLayers Polygon 
        var polygon = new ol.geom.Polygon([poly]);
        polygon.transform('EPSG:4326', 'EPSG:3857'); //transforming to Mercator projection
      
        var feature = new ol.Feature(polygon);
        var vectorSource = new ol.source.Vector();
        vectorSource.addFeature(feature);
        var vectorLayer = new ol.layer.Vector({
            source: vectorSource
        });
      
        // Add the vector layer to the map.
        map.addLayer(vectorLayer);
    })
    .catch(error => {
        console.error('Error:', error);
    });
        
});
