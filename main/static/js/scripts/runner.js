var rangeElem = document.getElementById('range');
var thumbMin  = document.getElementById('thumb-min');
var thumbMax = document.getElementById('thumb-max');

var rangeCoords = getCoords(rangeElem);
var rangeEnd = rangeElem.offsetWidth - thumbMax.offsetWidth;
var min = parseInt(getComputedStyle(thumbMin).left);


console.log(parseInt(min))

thumbMin.onmousedown = function(e) {
  var thumbCoords = getCoords(thumbMin);
  var shiftX = e.pageX - thumbCoords.left;

  document.onmousemove = function(e){
    var newLeft = e.pageX - shiftX - rangeCoords.left;
    if (newLeft < 0){
      newLeft = 0;
    } 

    if (newLeft > max - thumbMin.offsetWidth / 2) {
      newLeft = max - thumbMin.offsetWidth / 2;
    }


    min = newLeft;
    thumbMin.style.left = newLeft + 'px'
  }

  document.onmouseup = function() {
    console.log(getCoords(thumbMin))
    document.onmousemove = document.onmouseup = null;
  }

  return false
}

thumbMax.onmousedown = function(e) {
  var thumbCoords = getCoords(thumbMax);
  var shiftX = e.pageX - thumbCoords.left;

  document.onmousemove = function(e){
    var newLeft = e.pageX - shiftX - rangeCoords.left;
    if (newLeft < min + thumbMin.offsetWidth / 2) {
      newLeft = min + thumbMin.offsetWidth / 2;
    }

    if (newLeft > rangeEnd) {
      newLeft = rangeEnd;
    }

    max = newLeft;

    thumbMax.style.left = newLeft + 'px';
  }

  document.onmouseup = function() {
    document.onmousemove = document.onmouseup = null;
  }
  return false;
}



function getCoords(elem) {
  var box = elem.getBoundingClientRect();

  return {
      top: box.top + pageYOffset,
      left: box.left + pageXOffset
  };
}