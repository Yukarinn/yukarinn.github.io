#!usr/bin/python

import os


IMAGE_FOLDER = "img"

ILLUST_BEGIN = """<DOCTYPE! html>

<html>

<head>
  <link rel="stylesheet" href="../css/main.css">
  <link rel="stylesheet" href="../css/navbar.css">
  <link rel="stylesheet" href="../css/illust.css">
  <title>yukarin.moe</title>
</head>

<body>
  <div class="topnav">
    <a href="/">yukarin.moe</a>
    <div class="dropdown">
      <button class="dropButton">menu</button>
      <div class="dropdownContent">
        <a href="/">home</a>
        <a href="#">stuff</a>
        <a href="#">more stuff</a>
      </div>
    </div>
  </div>

<div class="gridContainer">
"""

ILLUST_END = """</div>

</body>

</html>
"""


files = os.listdir(IMAGE_FOLDER)
file = open("index.html", "w")
file.write(ILLUST_BEGIN)

for item in files:
    file.write('<img src="%s">\n' % os.path.join(IMAGE_FOLDER, item))

file.write(ILLUST_END)
file.close()
