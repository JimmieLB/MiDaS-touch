import os
import sys
import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
from stl import mesh
from create_stl import create

DEFAULT_MODEL = "MiDaS"


def run(argv):
    args = {'gui': True}
    try:
        argv.index("--nogui")
        args['gui'] = False
    except:
        pass

    try:
        args["model"] = argv[argv.index("--model_type") + 1]
        print(f"model is {args['model']}")
    except:
        args["model"] = DEFAULT_MODEL

    # Load the MiDaS model
    midas = torch.hub.load("intel-isl/MiDaS", args['model'])
    midas.to('cpu')
    midas.eval()

    # Input transformation pipeline for MiDaS
    if args["model"] == "DPT_Large" or args["model"] == "DPT_Hybrid":
        transform = torch.hub.load("intel-isl/MiDaS", "transforms").dpt_transform
    else:
        transform = torch.hub.load("intel-isl/MiDaS", "transforms").small_transform
    # Directory containing the images
    input_dir = 'input'
    output_dir = 'output'

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize a dictionary to store depth data
    depth_data = {}

    # Get list of all image files in the input directory
    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.jpeg', '.png','.webp'))]

    # Process and display each image and its depth map
    for file_name in image_files:
        img_path = os.path.join(input_dir, file_name)

        # Read and convert the image
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Transform the image for MiDaS
        input_batch = transform(img_rgb).to('cpu')

        # Predict the depth
        with torch.no_grad():
            prediction = midas(input_batch)
            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=img_rgb.shape[:2],
                mode='bicubic',
                align_corners=False
            ).squeeze()

            output = prediction.cpu().numpy()


        # Compute depth statistics
        avg_depth = np.mean(output)
        max_depth = np.max(output)
        min_depth = np.min(output)

        if args['gui']:
            # Display the original image and depth map
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 3, 1)
            plt.imshow(img_rgb)
            plt.title('Original Image')
            plt.axis('off')


            plt.subplot(1, 3, 2)
            plt.imshow(output, cmap='inferno')
            plt.title('Depth Map')
            plt.axis('off')


            # Display 3d representation of depth map

            w = len(output[0])
            h = len(output)

            # fig = plt.figure()
            ax = plt.subplot(1,3,3, projection='3d')
            plt.title('3D Preview')
            ax.axes.set_zlim3d(bottom=0, top=max_depth)
            ax.axes.set_xlim3d(left=0, right=max(w,h))
            ax.axes.set_ylim3d(bottom=0, top=max(w,h))

            # ax.grid(False)
            # ax.axis('off')
            x_list = [[x for x in range(w)] for y in range(h)]
            y_list = [[y for x in range(w)] for y in range(h)]
            ax.plot_surface(x_list, y_list,output * 0.5)


            plt.show()

            print(np.array(output).shape)

        create(output, name=file_name.rsplit('.',1)[0])


        # Print depth statistics
        print(f"Depth Data:")
        print(f"  Average Depth: {avg_depth}")
        print(f"  Maximum Depth: {max_depth}")
        print(f"  Minimum Depth: {min_depth}")
        print("\n")

    # Save the depth data to a file
    output_data_path = os.path.join(output_dir, 'depth_data.txt')
    with open(output_data_path, 'w') as file:
        for key, value in depth_data.items():
            file.write(f'{key}: {value}\n')

if __name__ == "__main__":
    run(sys.argv)