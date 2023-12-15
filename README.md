# MiDaS Touch

This program takes an image file as an input and creates a 3D representation of the image for use in a 3d printer. 
The purpose is to automate the creation of tactile representations of paintings for blind or visually impaired people.

A depth-map estimation ai is used called "MiDaS" and the result of the depth map is extruded from a rectangle. The project uses
the MiDaS ai and is used to create a 3d-printed object hence the name "MiDaS-touch"

<img width="1204" alt="image" src="https://github.com/JimmieLB/MiDaS-touch/assets/60014163/a8fdcd29-9438-4ba5-b189-68e7be6dbb15">
### STL File
<img width="1037" alt="image" src="https://github.com/JimmieLB/MiDaS-touch/assets/60014163/2d1c9cc7-3e64-4bce-b86a-6ea84d5056d3">


## Getting Started

### Installation


1. Clone repo
  ```git clone https://github.com/JimmieLB/MiDaS-touch.git```
2. Install pip packages
   ```pip install numpy torch opencv-python numpy-stl```
3. Add image files to "input" folder
4. Run "run.py"
