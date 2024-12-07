ymaps.ready(init);

function init() {
  var myMap = new ymaps.Map('map', {
    center: [45.0448, 38.976],
    zoom: 10,
  });

  // Пробки
  var actualProvider = new ymaps.traffic.provider.Actual({}, { infoLayerShown: true });
  actualProvider.setMap(myMap);

  //Поиск
  myMap.controls.add('searchControl');

  var placemarks = [
    { coords: [45.03, 38.98], hintContent: 'Метка 1', balloonContent: 'Информация о метке 1' },
    { coords: [45.05, 39.00], hintContent: 'Метка 2', balloonContent: 'Информация о метке 2' },
    { coords: [45.06, 38.97], hintContent: 'Метка 3', balloonContent: 'Информация о метке 3' }
  ];

  placemarks.forEach(placemarkData => {
    var myPlacemark = new ymaps.Placemark(placemarkData.coords, {
      hintContent: placemarkData.hintContent,
      balloonContent: placemarkData.balloonContent
    });
    myMap.geoObjects.add(myPlacemark);
  });


  // Кнопки
  var firstButton = new ymaps.control.Button("Кнопка");
  myMap.controls.add(firstButton, { float: "right" });

  var secondButton = new ymaps.control.Button({
  });

  // Изменение размера кнопки
  function changeSize() {
    var oldSize = secondButton.options.get("size"),
      newSize;
    switch (oldSize) {
      case "small":
        newSize = "medium";
        break;
      case "medium":
        newSize = "large";
        break;
      case "large":
        newSize = "small";
        break;
      default:
        newSize = "small";
    }
    secondButton.options.set("size", newSize);
  }
  window.setInterval(changeSize, 1000);
}