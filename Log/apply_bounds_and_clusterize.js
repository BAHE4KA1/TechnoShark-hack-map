function init() {
  var myMap = new ymaps.Map(
    "map",
    {
      center: [45.0448, 38.976],
      zoom: 10,
    },
    {
      searchControlProvider: "yandex#search",
    }
  );
  var result = ymaps.geoQuery(ymaps.geocode("Краснодар, парк Галицкого"));
  myMap.geoObjects.add(result.clusterize());

  map.controls.add(firstButton, { float: "right" });

  var secondButton = new ymaps.control.Button({
    data: {
      content: "Адаптивная кнопка",
      image: "images/error.png",
    },
    options: {
      maxWidth: [28, 150, 178],
      
    },
    
  });
  map.controls.add(secondButton);
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

ymaps.ready(init);
