#!usr/bin/python

import os


IMAGE_FOLDER = "img"

ILLUST_BEGIN = """<DOCTYPE! html>

<html>

<head>
  <link rel="stylesheet" href="../css/main.css">
  <link rel="stylesheet" href="../css/navbar.css">
  <link rel="stylesheet" href="../css/subsec.css">
  <link rel="stylesheet" href="../css/illust.css">
  <title>yukarin.moe</title>
</head>

<body>
  <div class="topnav">
    <a class="navhome" href="/">yukarin.moe</a>
    <div class="dropdown">
      <button class="dropButton">menu</button>
      <div class="dropdownContent">
        <a href="/">home</a>
        <a href="#">stuff</a>
        <a href="#">more stuff</a>
      </div>
    </div>
  </div>

  <div class"subsec">
    <div class="subsecTitle">
      <img src="../img/profile-180.png" alt="Avatar" class="imageProfile">
      <div class="subsecText">
        <p class="yukarin">Yukarin</p>
        <p>------------------- *</p>
        <p>illustration</p>
      </div>
    </div>
    <div class="subsecDesc">
      <p>To go partway is easy, but mastering anything requires hard fucking work. Design as if your fucking life depended on it. Dedicate yourself to lifelong fucking learning. Someday is not a fucking day of the week. Widows and orphans are terrible fucking tragedies, both in real life and definitely in typography.</p>
    </div>
  </div>


  <div class="illustGrid">
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
