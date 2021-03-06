# Languege-Answering-for-Images-
Implementing a system capable of answering open-ended questions about a given image. Image features are generated using a pre-trained CNN and text features are extracted using an RNN with LSTM.

Train

The basic usage is python train.py, the model to train is model.py. 
The batch size and the number of epochs can also be specified using the options -num_epochs and -batch_size. The default batch size and number of epochs are 128 and 25 respectively.

Prediction

The options -question and -image are used to specify the question and address of the image respectively.  An example of usage is: python config.py -image=“xxxx/xxxxx.jpg" -question="Which animal is this?"

Model

Intuitively, the convolutional neural network will give us a feature of vector representation for every block of the image. So in the end, the image we get as an input will chop into a 14 by 14 grid, and we have a feature vector of each of this 14 by 14 grids. So what we get from the image net is a feature embedding of each block of images. We could treat these embedding as a word in RNN model, and propagate everything. We pass these image embeddings as a semantic memory model. And then basically we have a recurrent neural network, like LSTM or GRU, and just compute the hidden state of every hidden representation at each image embedding. So, this is independent to the question. And we will also have a LSTM model for the question, we basically use a LSTM to compute a vector of question model, which is going to be to last state when it goes through every word in the question. And we have a very interesting attention mechanism, which is essentially triggers by the question to go over the input. So maybe we have a question about where the dogs are. And we may assume that football is mentioned in these questions, and location is asked, which is stored somewhere in the hidden state. And we use the question to trigger the attention mechanism. Wherever there is a strong attention paid to a specific representation, we going to give this latent representation yet another input of an LSTM, and it is in the episodic memory module. So it seems a filter that will only keep track of the representation of the image that is relative to the question. And we will define the end of the filtering LSTM as a vector, and we call softmax classifier at every hidden state to produce an answer for the question. 
