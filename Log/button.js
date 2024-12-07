ymaps.ready(init);
function init() {
  var map = new ymaps.Map("map", {
      center: [59.93772, 30.313622],
      zoom: 10,
      controls: [],
    }),
    firstButton = new ymaps.control.Button("Кнопка");

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
