# README #

My solution files for identifying dance form challenge-
https://www.hackerearth.com/challenges/competitive/hackerearth-deep-learning-challenge-identify-dance-form/problems/

### What is this repository for? ###

The problem is a classification problem. But I framed the challenge as object detection and recognition problem,
and solved it using a Darknet based system- YOLOv4
You can find all details related to this system in below url-
https://github.com/AlexeyAB/darknet

### How do I get set up? ###

This project has been created in following environment
1. Anaconda(Python 3.7.3 version)
2. Windows 10
3. CUDA 10.1
4. cuDNN 7.6.5
5. Visual Studio 2017


### How to train data from scratch ###
Follow below post-
http://dsbyprateekg.blogspot.com/2020/06/identify-eight-types-of-indian.html


### How to run ###
1. Install and build Darkent in your system by following below post-
http://dsbyprateekg.blogspot.com/2020/05/how-to-install-and-compile-yolo-v4-with.html
2. Once build successfully put the obj folder inside the vcpkg-master\installed\x64-windows\tools\darknet\data folder
3. Copy obj.data, obj.names, train.txt and test.txt files also inside the vcpkg-master\installed\x64-windows\tools\darknet\data folder
4. Download the trained weights from below url and put inside the vcpkg-master\installed\x64-windows\tools\darknet\backup folder-
https://www.kaggle.com/iamprateek/yolo4dance-weights
5. Open windows powershell, go to the Darknet root directory and run below command-
./darknet detector test data/obj.data cfg/yolo-obj.cfg backup/yolo-obj_final.weights -ext_output -dont_show -out data/dance_result.json < data/test.txt
6. Above command will generate prediction in json format, now to prepare the submit file run the json_csv_submission2.py file


### My Github Repo link ###
https://github.com/dsbyprateekg/hackerearth-deep-learning-challenge-identify-dance-form

