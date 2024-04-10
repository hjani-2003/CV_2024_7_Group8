import imgaug.augmenters as iaa
import imgaug as ia
import cv2
import os
import numpy as np
import random

# Base directory containing the images and labels
base_dir = '.\\yeah'

# List to store file paths of images with label 0 and 5
files_to_delete = []

# Loop over all directories ('train', 'test', 'valid')
for dir_name in ['train', 'test', 'valid']:
    print(f'Processing {dir_name} data...')

    # Directories containing the images and labels
    images_dir = os.path.join(base_dir, dir_name, 'images')
    labels_dir = os.path.join(base_dir, dir_name, 'labels')

    # Loop over all files in the images directory
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):  # or '.png' or whatever format your images are in
            # Load the labels
            label_path = os.path.join(labels_dir, filename.replace('.jpg', '.txt'))
            with open(label_path, 'r') as file:
                lines = file.readlines()

            # Check if the image has both labels 0 and 5
            labels = [float(line.split()[0]) for line in lines]
            if 2 in labels and 5 in labels:
                files_to_delete.append((os.path.join(images_dir, filename), label_path))

# Randomly select 20 files to delete
files_to_delete = random.sample(files_to_delete, 60)

# Delete the selected files
for img_path, label_path in files_to_delete:
    os.remove(img_path)
    os.remove(label_path)

print('Deletion completed.')
