# Deep Learning
## Project: Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds



### Install

This project requires **Python 3.x** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [pytorch](https://pytorch.org/)
- [matplotlib](http://matplotlib.org/)
- [argparse](https://docs.python.org/3/library/argparse.html)

You will also need to have software installed to run and execute an python scripts like Atom, pycharm or VS code

### Objectives
1. identify which pet images are of dogs (even if breed is misclassified) and which pet images aren't of dogs.
 
2. classify the breed of dog, for the images that are of dogs.
 
3. Determine which CNN model architecture (ResNet, AlexNet, or VGG), "best" achieve the objectives 1 and 2.
 
4. Consider the time resources required to best achieve objectives 1 and 2, and determine if an alternative solution would have given a "good enough" result, given the amount of time each of the algorithms take to run.

### Program Outline

1. Time your program

2. Get program Inputs from the user (using command line)
3. Create Pet Images Labels
4. Create Classifier Labels and Compare Labels
5. Classifying Labels as "Dogs" or "Not Dogs"
6. Calculate the Results
7. Print the Results

### Usage

to run the program, you should run `check_images.py` script. you should pass the following to command line
* image directory
* model arch
* file that store names of dogs (dognames.txt)
* file to store info about the result of model

```
> python check_images.py --dir pet_images/ --arch resnet  --dogfile dognames.txt resnet_pet-images.txt
> python check_images.py --dir pet_images/ --arch alexnet  --dogfile dognames.txt alexnet_pet-images.txt
> python check_images.py --dir pet_images/ --arch vgg  --dogfile dognames.txt vgg_pet-images.txt
```

To run file run_models_batch.sh in the workspace, open a terminal window (in Unix/Linux/OSX/Lab Workspace) and type the following:
```
sh run_models_batch.sh
```
