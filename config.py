# paths
qa_path = ''  # directory containing the question and annotation jsons
train_path = ''  # directory of training images
val_path = ''  # directory of validation images
test_path = ''  # directory of test images
preprocessed_path = ''  # path where preprocessed features are saved to and loaded from
vocabulary_path = ''  # path where the used vocabularies for question and answers are saved to

task = 'OpenEnded' # open end or not
dataset = ''

# preprocess config
preprocess_batch_size = 64
image_size = 448  # scale shorter end of image to this size and centre crop
output_size = image_size // 32  # size of the feature maps after processing through a network
output_features = 2048  # number of feature maps thereof
central_fraction = 0.875  # only take this much of the centre when scaling and centre cropping

# training config
epochs = 50
batch_size = 128
initial_lr = 1e-3  # default Adam lr
lr_halflife = 50000  # in iterations
data_workers = 8
max_answers = 3000