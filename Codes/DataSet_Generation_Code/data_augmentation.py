import imgaug.augmenters as iaa
import imgaug as ia
import cv2
import os
import numpy as np

cnt = 0

# Define your augmentations
seq = iaa.Sequential([
    iaa.AdditiveGaussianNoise(scale=(5, 20)),  # add gaussian noise to images
    iaa.Fliplr(0.5),
    iaa.Affine(scale=(0.7, 0.9))
], random_order=True)

# Base directory containing the images and labels
base_dir = '.\\yeah'

# Loop over all directories ('train', 'test', 'valid')
for dir_name in ['train', 'test', 'valid']:
    print(f'Processing {dir_name} data...')

    # Directories containing the images and labels
    images_dir = os.path.join(base_dir, dir_name, 'images')
    labels_dir = os.path.join(base_dir, dir_name, 'labels')

    # Loop over all files in the images directory
    for filename in os.listdir(images_dir):
        if filename.endswith('.jpg'):  # or '.png' or whatever format your images are in
            # Load the image
            img_path = os.path.join(images_dir, filename)
            image = cv2.imread(img_path)

            # Load the labels
            label_path = os.path.join(labels_dir, filename.replace('.jpg', '.txt'))
            with open(label_path, 'r') as file:
                lines = file.readlines()

            my_id = []
            # Convert the labels to imgaug.BoundingBoxesOnImage
            bounding_boxes = []
            for line in lines:
                class_id, x_center, y_center, width, height = map(float, line.split())
                my_id.append(class_id)
                x1 = (x_center - width / 2) * image.shape[1]
                x2 = (x_center + width / 2) * image.shape[1]
                y1 = (y_center - height / 2) * image.shape[0]
                y2 = (y_center + height / 2) * image.shape[0]
                bounding_boxes.append(ia.BoundingBox(x1=x1, y1=y1, x2=x2, y2=y2, label=class_id))
            bounding_boxes = ia.BoundingBoxesOnImage(bounding_boxes, shape=image.shape)
            # print(class_id)
            # if class_id in [0, 2, 3, 4]:
            # if class_id in [0, 2]:
            
            if 4 in my_id:
                print(class_id)
                # Only augment these classes
                # for _ in range(4):  # Number of augmented versions to create
                #     # Augment the image and the bounding boxes
                #     image_aug, bounding_boxes_aug = seq(image=image, bounding_boxes=bounding_boxes)

                #     # Save the augmented image
                #     cv2.imwrite(img_path.replace('.jpg', '_aug.jpg'), image_aug)

                #     # Convert the augmented bounding boxes back to YOLO format and save them
                #     lines_aug = []
                #     for bb in bounding_boxes_aug.bounding_boxes:
                #         x_center = (bb.x1 + bb.width / 2) / image_aug.shape[1]
                #         y_center = (bb.y1 + bb.height / 2) / image_aug.shape[0]
                #         width = bb.width / image_aug.shape[1]
                #         height = bb.height / image_aug.shape[0]
                #         lines_aug.append(f'{int(bb.label)} {x_center} {y_center} {width} {height}\n')
                #     with open(label_path.replace('.txt', '_aug.txt'), 'w') as file:
                        # file.writelines(lines_aug)
                for i in range(3):  # Number of augmented versions to create
                    cnt+=1
    # Augment the image and the bounding boxes
                    image_aug, bounding_boxes_aug = seq(image=image, bounding_boxes=bounding_boxes)

    # Save the augmented image
                    cv2.imwrite(img_path.replace('.jpg', f'_aug{i}.jpg'), image_aug)

    # Convert the augmented bounding boxes back to YOLO format and save them
                    lines_aug = []
                    for bb in bounding_boxes_aug.bounding_boxes:
                        x_center = (bb.x1 + bb.width / 2) / image_aug.shape[1]
                        y_center = (bb.y1 + bb.height / 2) / image_aug.shape[0]
                        width = bb.width / image_aug.shape[1]
                        height = bb.height / image_aug.shape[0]
                        lines_aug.append(f'{int(bb.label)} {x_center} {y_center} {width} {height}\n')
                    with open(label_path.replace('.txt', f'_aug{i}.txt'), 'w') as file:
                        file.writelines(lines_aug)

    print("cnt is: ",cnt)
print('Data augmentation completed.')