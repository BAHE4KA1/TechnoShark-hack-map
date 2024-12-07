ymaps.ready(init);

function init () {
    var myMap = new ymaps.Map('map', {
            center: [56.136, 40.390],
            zoom: 10,
            controls: []
        });
    var trafficControl = new ymaps.control.TrafficControl({ state: {
            providerKey: 'traffic#actual',
            trafficShown: true
        }});
    myMap.controls.add(trafficControl);
    trafficControl.getProvider('traffic#actual').state.set('infoLayerShown', true);    
}