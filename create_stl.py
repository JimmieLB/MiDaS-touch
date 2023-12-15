import numpy as np
from stl import mesh

def in_range(index, list):
  return index >= 0 and index < len(list)


# raw_data: nxn matrix representing depth levels of an image
def create(raw_data, name="cube", shrink=True, z_max=20, xy_max=200):
  verts = []
  indexes = []
  i = 0
  xy_scale = 1
  z_scale = 1
  if shrink:
    xy_data_max = max([len(raw_data), len(raw_data[0])])
    xy_scale = xy_max / xy_data_max
    z_data_max = np.max(raw_data)
    z_scale = z_max / z_data_max
    print("Z scale:", z_scale)

  print(raw_data.shape,  xy_scale, z_scale)
  print("Creating Vertices...")
  for y in range(len(raw_data)):
    indexes.append([])
    for x in range(len(raw_data[y])):
      verts.append([x * xy_scale, y * xy_scale, 0])
      verts.append([x * xy_scale, y * xy_scale, raw_data[y][x] * z_scale])
      indexes[y].append(i)
      i += 2

  vertices = np.array(verts)

  # Define the triangles composing the cube

  faces = []

  print("Creating Faces...")
  for y in range(len(indexes)):
    for x in range(len(indexes[y])):
      x = len(indexes[y]) - x - 1
      y = len(indexes) - y - 1
      x_up = in_range(x + 1, indexes[y])
      y_up = in_range(y + 1, indexes)
      x_down = in_range(x - 1, indexes[y])
      y_down = in_range(y - 1, indexes)

      x_max = len(indexes[y]) - 1
      y_max = len(indexes) - 1

      #Top & Bottom
      if(x_up and y_up):
        faces.append([indexes[y][x], indexes[y+1][x], indexes[y][x+1]])
        faces.append([indexes[y][x]+1, indexes[y][x+1]+1, indexes[y+1][x]+1])
      if(x_down and y_down):
        faces.append([indexes[y][x], indexes[y-1][x], indexes[y][x-1]])
        faces.append([indexes[y][x]+1, indexes[y][x-1]+1, indexes[y-1][x]+1])

      #Front & Back
      if(x == 0 and y_up):
        faces.append([indexes[y][x], indexes[y][x]+1, indexes[y+1][x]])
        faces.append([indexes[y][x]+1, indexes[y+1][x]+1, indexes[y+1][x]])

        faces.append([indexes[y][x_max], indexes[y+1][x_max], indexes[y][x_max]+1])
        faces.append([indexes[y][x_max]+1, indexes[y+1][x_max], indexes[y+1][x_max]+1])

      #Side Faces
      if(y == 0 and x_up):
        faces.append([indexes[y][x], indexes[y][x+1], indexes[y][x]+1])
        faces.append([indexes[y][x]+1, indexes[y][x+1], indexes[y][x+1]+1])

        faces.append([indexes[y_max][x], indexes[y_max][x]+1, indexes[y_max][x+1]])
        faces.append([indexes[y_max][x]+1, indexes[y_max][x+1]+1, indexes[y_max][x+1]])

  print("Creating Mesh...")

  faces = np.array(faces)

  # Create the mesh
  cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
  for i, f in enumerate(faces):
      for j in range(3):
          cube.vectors[i][j] = vertices[f[j],:]

  # Write the mesh to file "cube.stl"
  print("Saving Mesh...")

  cube.save(f'./output/{name}.stl')

  print("Mesh Saved")

  return (faces, vertices)
