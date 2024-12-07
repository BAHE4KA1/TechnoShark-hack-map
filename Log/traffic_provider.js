ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [56.136, 40.390],
            zoom: 10,
            controls: []
        });
    var actualProvider = new ymaps.traffic.provider.Actual({}, { infoLayerShown: true });
    actualProvider.setMap(myMap)}