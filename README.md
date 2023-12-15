# MiDaS Touch

This program takes an image file as an input and creates a 3D representation of the image for use in a 3d printer. 
The purpose is to automate the creation of tactile representations of paintings for blind or visually impaired people.

A depth-map estimation ai is used called "MiDaS" and the result of the depth map is extruded from a rectangle. The project uses
the MiDaS ai and is used to create a 3d-printed object hence the name "MiDaS-touch"

<img width="1204" alt="image" src="https://github.com/JimmieLB/MiDaS-touch/assets/60014163/a8fdcd29-9438-4ba5-b189-68e7be6dbb15">
## STL File
<img width="1037" alt="image" src="https://github.com/JimmieLB/MiDaS-touch/assets/60014163/2d1c9cc7-3e64-4bce-b86a-6ea84d5056d3">


## Getting Started

### Prerequisites
1. Latest version of python and pip

### Installation
1. Clone repo
  ```sh
  git clone https://github.com/JimmieLB/MiDaS-touch.git
  ```
3. Install pip packages
  ```sh
  pip install numpy torch opencv-python numpy-stl
  ```
5. Add image files to "input" folder
6. Enter
   ```sh
   python3 run.py
   ```
8. Optional parameters
   ```sh
   python3 run.py --model <model_type> --nogui
   ```
   Model_Types are:
     "DPT_Large"    # MiDaS v3 - Large     (highest accuracy, slowest inference speed)  
     "DPT_Hybrid"   # MiDaS v3 - Hybrid    (medium accuracy, medium inference speed)  
     "MiDaS_small"  # MiDaS v2.1 - Small   (lowest accuracy, highest inference speed)  

