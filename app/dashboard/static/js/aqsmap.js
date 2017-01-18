mapboxgl.accessToken = 'pk.eyJ1IjoidGhpc2lzdGhlY2hyaXMiLCJhIjoiWGtjZnRXMCJ9.DJPpDDWnqux6wsFHStG_mQ';

var data_url = "/aqs/geojson/";
var aqs_source = new mapboxgl.GeoJSONSource({data:data_url});

var map = new mapboxgl.Map({
  container: 'map-canvas',
  //style: 'mapbox://styles/thisisthechris/ciqwhdhhb0010h9nplbeb0oja',
  style: "mapbox://styles/mapbox/light-v9",
  //zoomControl: false,
  center: [-4.142, 50.372],
  zoom: 12,
  pitch: 0, // pitch in degrees
  bearing: 0, // bearing in degrees
});

function get_tree_data(id){
  $.getJSON( "/trees/"+id+"/json/", function( data ) {
        console.log(data)
        $('#modal-name').html(data["name"]);
        $('#modal-info').html(data["info"]);
        $('#modal-species').html(data["species"]["name"]);
        $('#modal-dataset').html(data["dataset"]["name"]);
        $('#modal-org').html(data["org"]["name"]);
        $('#modal-age').html(data["age"]);
        $('#modal-link').attr("href", "/trees/"+id+"/");
        if (data["photo"]){
          $('#modal-image').attr("src", data["photo"]);
          $('#modal-image-info').html("");
        }else {
          $('#modal-image').attr("src", "");
          $('#modal-image-info').html("No Image");
        }

  });
}

function switchPitch(){
  if (map.getPitch() == 60){
    map.flyTo({pitch: 0});
  }else if(map.getPitch() == 0){
    map.flyTo({pitch: 60});
  }
}

map.on('load', function(){
  //map.addControl(new mapboxgl.Geocoder({position: 'bottom-left'}));
  map.addControl(new mapboxgl.Navigation({position: 'bottom-left'}));
  map.addControl(new mapboxgl.Geolocate({position: 'bottom-left'}));

  map.addSource("aqs", aqs_source);

  map.addLayer({
        "id": "aqs",
        "type": "circle",
        "source": "aqs",
        "paint": {
            "circle-opacity": 0.4,
            "circle-color": "#009900",
        }
    });

})

map.on('click', function (e) {
    // Use queryRenderedFeatures to get features at a click event's point
    // Use layer option to avoid getting results from other layers
    var features = map.queryRenderedFeatures(e.point, { layers: ['trees'] });
    // if there are features within the given radius of the click event,
    // fly to the location of the click event
    if (features.length) {
        // Get coordinates from the symbol and center the map on those coordinates
        //get_tree_data(features[0]["properties"]["id"])
        //$('#tree-modal').modal();
        map.flyTo({center: features[0].geometry.coordinates, zoom: 18});
    }
});


// Use the same approach as above to indicate that the symbols are clickable
// by changing the cursor style to 'pointer'.
map.on('mousemove', function (e) {
    var features = map.queryRenderedFeatures(e.point, { layers: ['symbols'] });
    //map.getCanvas().style.cursor = features.length ? 'pointer' : '';
});
