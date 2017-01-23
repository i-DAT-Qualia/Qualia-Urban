mapboxgl.accessToken = 'pk.eyJ1IjoidGhpc2lzdGhlY2hyaXMiLCJhIjoiWGtjZnRXMCJ9.DJPpDDWnqux6wsFHStG_mQ';

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

  //map.addSource("aqs",{
  //      type: "geojson",
  //      data: data_url,
  //})
  map.addSource("aqs", aqs_source);;

    var layers = [
        [0, '#9CFF9C'],
        [12, '#31FF00'],
        [24, '#31CF00'],
        [36, '#FFFF00'],
        [42, '#FFCF00'],
        [48, '#FF9A00'],
        [54, '#FF6464'],
        [59, '#FF0000'],
        [65, '#990000'],
        [71, '#CE30FF'],
    ];


    layers.forEach(function (layer, i) {
        map.addLayer({
            "id": "cluster-" + i,
            "type": "circle",
            "source": "aqs",
            "paint": {
                "circle-color": layer[1],
                "circle-radius": 20,
                "circle-opacity": 0.4,
                "circle-blur": 1 // blur the circles to get a heatmap look
            },
            "filter": i === layers.length - 1 ?
                [">=", "pm2point5con", layer[0]] :
                ["all",
                    [">=", "pm2point5con", layer[0]],
                    ["<", "pm2point5con", layers[i + 1][0]]]
        }, 'waterway-label');
    });


})
