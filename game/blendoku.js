function toHex(num) {
  hexString = num.toString(16);
  if (hexString.length % 2) {
    hexString = '0' + hexString;
  }
  return hexString;
}

function randSingleColor() {
  return Math.round((Math.random())*255);
}

function shuffle(array) {
  var currentIndex = array.length;
  var randomIndex, tempVal;
  while (0 !== currentIndex) {
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    tempVal = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = tempVal;
  }

  return array;
}

class Color {
  constructor(r, g, b) {
    if (r===undefined || g===undefined || b===undefined) {
      this.r = randSingleColor();
      this.g = randSingleColor();
      this.b = randSingleColor();
    }
    else {
      this.r = r;
      this.g = g;
      this.b = b;
    }
  }

  randColor() {
    this.r = randSingleColor();
    this.g = randSingleColor();
    this.b = randSingleColor();
  }
}

class Rect {
  constructor(order, color) {
    this.order = order;
    this.hex = '#' + toHex(color.r) + toHex(color.g) + toHex(color.b);
  }
}

class ColorOffset {
  constructor(r, g, b) {
    this.r = r;
    this.g = g;
    this.b = b;
  }
}

var canvas = document.getElementById('canvas');
var width = document.documentElement.clientWidth;
var height = document.documentElement.clientHeight;
var context = canvas.getContext('2d');

var board = [];
var numOfRects = 5;

var origin = new Color(0, 0, 0);
var rectOrigin = new Rect(0, origin);

// context.fillStyle = rectOrigin.hex;
// context.fillRect(0, 0, 100, 100);

var offset = new ColorOffset(30, 0, 0);
var i;
for (i=0; i<numOfRects; i++) {
  var color = new Color(origin.r+i*offset.r, origin.g+i*offset.g, origin.b+i*offset.b);
  var rect =  new Rect(i, color);
  board.push(rect);
}
shuffle(board);
for (i=0; i<numOfRects; i++) {
  var rect = board[i];
  context.fillStyle = rect.hex;
  context.fillRect(i*100, 0, 100, 100);
}
