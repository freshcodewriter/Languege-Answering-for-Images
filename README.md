# Languege-Answering-for-Images-
Implementing a system capable of answering open-ended questions about a given image. Image features are generated using a pre-trained CNN and text features are extracted using an RNN with GRUs.
Train
The basic usage is python train.py, the model to train is model.py. 
The batch size and the number of epochs can also be specified using the options -num_epochs and -batch_size. The default batch size and number of epochs are 128 and 25 respectively.

Prediction
The options -question and -image are used to specify the question and address of the image respectively.  An example of usage is: python config.py -image=“xxxx/xxxxx.jpg" -question="Which animal is this?"


