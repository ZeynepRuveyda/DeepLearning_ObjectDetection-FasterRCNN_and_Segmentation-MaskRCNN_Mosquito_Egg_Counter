# Mosquitoes' Eggs Counting with Computer Vision Technologies Internship Project
file:///home/criuser/Desktop/CRI%20Internship/coco%20json%20photos/task_eggl6-2020_08_20_14_39_22-coco%201.0/images/200728_eggs0006.tif![image](https://user-images.githubusercontent.com/72027409/122667401-12d17480-d1b3-11eb-9eb9-c442847351e0.png)

# Description of the project

Female mosquitoes lay their eggs in water, and after hatching mosquito larvae spend a week in this aquatic environment before they fly away as adults. The microbial and chemical composition of the water in which they spend their childhood affects the health of the larvae and the adult mosquitoes they will turn into.

Previous research has shown that specific microbes or nutrients in the larval environment make for very healthy adult mosquitoes, whereas larval exposure to other compounds and bacterial strains decreases e.g the life-span of adult mosquitoes. It is unknown if/how female mosquitoes evaluate a body of water before she lays her precious eggs.

In our project, the calculation of the eggs in the next stage after the mosquitoes lay their eggs on the white plates in the cages that are per-formed and designed for reproduction. The main goal of the project is to detect the eggs on the plates with Computer Vision technologies, and to avoid wasting time by not dealing with egg counting.

# Our expectations

Our expectation from this project is that with the deep learning models I apply, the best accuracy rate can be achieved and the best eggs number calculation can be made.

# Main challenges that I have faced

The main challenge in the project is that our datasets is very small. I have many overlapping and clustered eggs, and usually due to the ambient conditions (light reflection or staying in a dark spot) when photographing the nested eggs in the pictures, some of the eggs could not be displayed clearly, making it difficult for our model to learn the position of the eggs.

# Preliminary results

FASTER-RCNN MODEL RESULTS

![image](https://user-images.githubusercontent.com/72027409/122668172-27b00700-d1b7-11eb-8c1c-8ae75499328d.png)
![image](https://user-images.githubusercontent.com/72027409/122668173-2f6fab80-d1b7-11eb-97d4-7b55bd954d1a.png)
![image](https://user-images.githubusercontent.com/72027409/122668174-34ccf600-d1b7-11eb-9e0e-4a6c3ca74614.png)
![image](https://user-images.githubusercontent.com/72027409/122668178-38f91380-d1b7-11eb-9e39-884df669a090.png)

RESUNET MODEL RESULT

![image](https://user-images.githubusercontent.com/72027409/122668239-6776ee80-d1b7-11eb-8292-caf361d75829.png)

MASK-RCNN MODEL RESULT

![image](https://user-images.githubusercontent.com/72027409/122668249-72318380-d1b7-11eb-9342-9a3418de5d05.png)

# Project Roadmap

I tried the Mask-RCNN and Resunet models for segmentation, and the Faster-RCNN and Retinanet models for object detection within a period of 4 months. By updating the stages of our project, I aimed to improve our egg counting project only with object detection models, not by segmentation. And related to this, I tried the following methods to improve our model. For the datasets part(I spent most of our effort to improve our datasets),

*Mask-RCNN model; cropping image method and masking these images , Resunet model; use big image size and their masks images before loading datasets( I had just 13 images for train and validation datasets :) )

*Faster-RCNN and Retinanet model;

-Divided each image into 6 part 

-I got 1728x1728  image size

-Resized images to 1024x1024 size

-Finished 303 images with bounding box annotation

-inverted all train  and test images

-Splitted the dataset %80 train, %20validation

    Augmentation Part

-I used horizontally and vertically flip, changing gray scale image, brigtness and rotates methods

    Transfer Learning

-Used the COCO Datasets weights

-For the Faster-RCNN , I used 10 different weights with backbone resnet50 and resnet101

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

Notion(https://www.notion.so/Project-management-26c800e772294358a464b1abc9236d03)

# Our Website
file:///home/criuser/Downloads/WhatsApp%20Image%202021-06-20%20at%2010.26.39%20AM.jpeg![image](https://user-images.githubusercontent.com/72027409/122667324-88891080-d1b2-11eb-80c3-f04a0de5a15d.png)
