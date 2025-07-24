# Yoga Pose Detection (PoseNet)
This project is based on the pose estimation model
[PoseNet](https://github.com/tensorflow/tfjs-models/tree/master/posenet), [ml5js](https://ml5js.org/getting-started/hello-ml5) and [KNN classifier model](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm#:~:text=In%20pattern%20recognition%2C%20the%20k,examples%20in%20the%20feature%20space.&text=In%20k%2DNN%20classification%2C%20the%20output%20is%20a%20class%20membership.)


![Figure](https://github.com/forhadsidhu/Yoga-pose-detection/blob/master/Images/Yoga.jpg)




## Basic Theory

Pose estimation is a hot topic now-a-days. It is being used in video-surveillance system to sport analysis tasks. Some of the classical problem can be solved using pose estimation like: person count in a frame, fall detection, smart fitness tracking app etc. Basicly by using pose estimation we can observe the movement of human and take any decision. Before of deep learning arena [HoG](https://lear.inrialpes.fr/people/triggs/pubs/Dalal-cvpr05.pdf) and [SIFT](http://www.scholarpedia.org/article/Scale_Invariant_Feature_Transform) based approach used in feature extraction. But because of CNN these feature extraction process become more accurate using lots of data. 

<p align="center">
  <img width="600" height="500" src="https://github.com/forhadsidhu/Yoga-pose-detection/blob/master/Images/posenet.gif">
</p>

So,Using PoseNet we get key points of human limbs. Output of keypoints is (x,y) co-ordinate value. Then using these keypoints we can determine angles of different limb of our body or can use these point in classifier model for human acitivity detection. There are some out performing model for pose estimation like: OpenPose pose estimation model which can also be inferenced in CPU.

## Installation

* Python >= 3.6
* Dependencies: ```pip install -r requirements.txt```
* Javascript
* [p5.js](https://p5js.org/download/)

## Running
```python manage.py runserver```


## Code Structure
- **data-preparion**: Data preparation files
  - **resize.py**:  code for resizing the collected images.
  - **video.py**:  code for making video from these images.
- **Yoga_prediction**: All the scripts for prediction with pretrain model
  - **index.html**: Open it in broser for prediction using webcam
- **Yoga_training**: All the scripts for training the classifier model with pose estimation
  - **index.html**: Open it in broser for start training using UI
  - **pose.js**: This javascript file contain all beackend logic for pose estimation and training .


## Data Preparation
Data Preparation
Yoga pose images are resized using resize.py and compiled into a video at 1 FPS using video.py.

I collected yoga pose images from various sources (Flickrs,Youtube videos etc),Resize the images using ```resize.py``` . Considering these images as frame made a video using ```video.py``` by setting FPS=1.
## DataSet
[Data](https://drive.google.com/file/d/1n5qpMEGmW_-urhTatfRecva8dHQMTgdK/view?usp=sharing)

## Training

I prepared the training procedure using UI. By clicking the button we can select current frame considering this as level. Open ```index.html``` in editor from training folder, some thing will apear like below




Training and Prediction 
Training: Managed through the UI in the Yoga_training/index.html file.

Prediction: Open index.html from the Yoga_prediction folder for real-time pose detection.

