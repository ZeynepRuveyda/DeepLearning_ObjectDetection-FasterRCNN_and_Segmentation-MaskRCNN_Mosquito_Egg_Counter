# Counting Mosquito Eggs using Computer Vision Internship Project
[image](https://user-images.githubusercontent.com/72027409/122667401-12d17480-d1b3-11eb-9eb9-c442847351e0.png)

# Description of the project

Female mosquitoes lay their eggs near or in water, and after hatching mosquito larvae spend a week in this aquatic environment before they fly away as adults. The microbial and chemical composition of the water in which they spend their childhood affects the health of the larvae and the adult mosquitoes they will turn into. Previous research has shown that specific microbes or nutrients in the larval environment make for very healthy adult mosquitoes, whereas larval exposure to other compounds and bacterial strains decreases e.g the life-span of adult mosquitoes. It is unknown how female mosquitoes evaluate a body of water before she lays her precious eggs.

To characterize the environmental cues that influence the oviposition choices of mosquitoes, laboratory experiments in which mosquitoes can choose between several potential egg laying sites are often performed. In these experiments mosquitoes deposit eggs on an 'egg paper' that is partly submerged in the water of the egg laying site. It is common practice that the number of eggs deposited on the paper is counted by hand. This method is very labor intensive and prevents large-scale egg laying experiments. In our project, we aim to develop a computer vision pipeline that takes a photograph of an egg paper as input, and accurately determines the number of eggs deposited on the paper. One challenge is that eggs are often deposited in clusters and individual eggs may overlap, providing an interesting computer vision challenge. 

# Our expectations

We expect that applying a variety of deep learning models to this problem will result in an accurate algorithm to determine the number of eggs present on the image.


# Main challenges that we have faced

The main challenge in the project is that our datasets is very small. We have many overlapping and clustered eggs, and usually due to the ambient conditions (light reflection or uneven illumination) when photographing the eggs, some of the eggs are not clearly visible, making it difficult for our model to learn the position of the eggs, and separate overlapping/clustered eggs.

# Project Roadmap

We tried the Mask-RCNN and Resunet models for segmentation, and the Faster-RCNN and Retinanet models for object detection within a period of 4 months. By updating the stages of our project, We aimed to improve our egg counting project only with object detection models, not by segmentation. And related to this, We tried the following methods to improve our model. For the datasets part(I spent most of our effort to improve our datasets),

*Mask-RCNN model; cropping image method and masking these images , Resunet model; use big image size and their masks images before loading datasets( I had just 13 images for train and validation datasets :) )

*Faster-RCNN and Retinanet model;

-Divided each image into 6 part 

-I got 1728x1728  image size

-Resized images to 1024x1024 size

-Finished 303 images with bounding box annotation

-inverted all train  and test images

-Splitted the dataset %80 train, %20validation

    Augmentation Part

-We used horizontally and vertically flip, changing gray scale image, brigtness and rotates methods

    Transfer Learning

-Used the COCO Datasets weights

-For the Faster-RCNN , We used 10 different weights with backbone resnet50 and resnet101

    Configurations

*MaskRCNN

-MaxGTInstances: the maximum number of instances that can be detected in one image ( 100 -> 200)

-DetectionMinConfidence: the confidence level threshold ( 0,7-> 0,5)

-ImageMinDim and ImageMaxDim:

Changed -ImageMinDim:512, ImageMaxDim:1024

The ideal approach would be to train all the initial models on smaller image sizes for faster updation of weights and use higher sizes during final stage to fine tune the final model parameters.

-LOSS_WEIGHTS: Mrcnnmaskloss: This corresponds to masks created on the identified objects, If identification at pixel level is of importance, this weight is to be increased

*Faster-RCNN

-Changed batchsize from 2 to 8

-Play with learning rate

-Changing backbone (resnet50,resnet101)

-Play with iteration and epochs

FASTER-RCNN MODEL RESULTS

file:///home/criuser/Downloads/detectron_resnet50/faster_rcnn_R_50_DC5_1x.yaml/epoch40(97).png![image](https://user-images.githubusercontent.com/72027409/122831042-95f4e680-d2e9-11eb-8191-c8339c8ec18b.png)
![image](https://user-images.githubusercontent.com/72027409/122668173-2f6fab80-d1b7-11eb-97d4-7b55bd954d1a.png)
![image](https://user-images.githubusercontent.com/72027409/122668174-34ccf600-d1b7-11eb-9e0e-4a6c3ca74614.png)
![image](https://user-images.githubusercontent.com/72027409/122668178-38f91380-d1b7-11eb-9e39-884df669a090.png)

RESUNET MODEL RESULT

![image](https://user-images.githubusercontent.com/72027409/122668239-6776ee80-d1b7-11eb-8292-caf361d75829.png)

MASK-RCNN MODEL RESULT

![image](https://user-images.githubusercontent.com/72027409/122668249-72318380-d1b7-11eb-9342-9a3418de5d05.png)


# The Digital Sciences methods

The Digital Sciences methods that I have used are :

    -Programming

    -Deep Learning

    -Machine Learning

    -Project Management

# The technical environment

I have used a lot of libraries when I am writing my codes.
Pycharm, Google Colab Pro, Streamlit

# List of hard/soft skills developed

Deep Learning, OpenCV, Streamlit, Segmentation and object detection models, Python skills

(For Project Management)
Notion(https://www.notion.so/Project-management-26c800e772294358a464b1abc9236d03)

# Projet video for last user
[Download the video]([path/to/video.mp4](https://github.com/user-attachments/assets/fed3c235-00b3-464f-8ff8-3cd8e147495b))

# Reference Letter from Felix Hol
[Reference Letter](./RefLetter_ZROzel_FH-1.pdf)





https://github.com/user-attachments/assets/436721c3-2901-46a1-b00c-7b40f27f304d

