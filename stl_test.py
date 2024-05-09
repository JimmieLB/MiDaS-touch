from create_stl import create
import numpy as np
from perlin_noise import PerlinNoise
def test_stl(shrink=False):

  vertices = np.array([\
    [1,1,1,1,1,1],
    [1,2,2,2,2,1],
    [1,2,3,3,2,1],
    [1,2,3,3,2,1],
    [1,2,2,2,2,1],
    [1,1,1,1,1,1]])
  test1 = create(vertices, shrink=shrink)

  print("vertices\n", test1[1])
  print("faces\n", test1[0])

def test_stl2(shrink=False):
  noise = PerlinNoise()
  w = 100
  h = 100
  vertices = np.zeros((w,h))
  vertices = [[abs(noise([i/w, j/h])) * 20 + 10 for j in range(w)] for i in range(h)]
  vertices = np.array(vertices)
  test2 = create(vertices, shrink=shrink)
  print("vertices\n", test2[1])
  print("faces\n", test2[0])

def test_stl3(shrink=False):
  noise = PerlinNoise()
  w = 500
  h = 500
  print("Defining vertices...")
  vertices = [[noise([i/60, j/60]) * 10 + 20  for j in range(w)] for i in range(h)]
  vertices = np.array(vertices)
  print("Starting Mesh...")
  test2 = create(vertices, shrink=shrink)
  print("vertices\n", test2[1])
  print("faces\n", test2[0])



test_stl3(shrink=True)