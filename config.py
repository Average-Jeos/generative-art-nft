# This file MUST be configured in order for the code to run properly

# Make sure you put all your input images into an 'assets' folder. 
# Each layer (or category) of images must be put in a folder of its own.

# CONFIG is an array of objects where each object represents a layer
# THESE LAYERS MUST BE ORDERED.

# Each layer needs to specify the following
# 1. id: A number representing a particular layer
# 2. name: The name of the layer. Does not necessarily have to be the same as the directory name containing the layer images.
# 3. directory: The folder inside assets that contain traits for the particular layer
# 4. required: If the particular layer is required (True) or optional (False). The first layer must always be set to true.
# 5. rarity_weights: Denotes the rarity distribution of traits. It can take on three types of values.
#       - None: This makes all the traits defined in the layer equally rare (or common)
#       - "random": Assigns rarity weights at random. 
#       - array: An array of numbers where each number represents a weight. 
#                If required is True, this array must be equal to the number of images in the layer directory. The first number is  the weight of the first image (in alphabetical order) and so on...
#                If required is False, this array must be equal to one plus the number of images in the layer directory. The first number is the weight of having no image at all for this layer. The second number is the weight of the first image and so on...

# Be sure to check out the tutorial in the README for more details.                

CONFIG = [
    {
        'id': 1,
        'name': 'background',
        'directory': 'Background',
        'required': True,
        'rarity_weights': [10, 10, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40],
    },
    {
        'id': 2,
        'name': 'who_dis?',
        'directory': 'Who Dis',
        'required': True,
        'rarity_weights': None,
    },
    {
        'id': 3,
        'name': 'body',
        'directory': 'Body',
        'required': True,
        'rarity_weights': [10, 10, 10, 20, 20, 20, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40],
    },
    {
        'id': 4,
        'name': 'face',
        'directory': 'Face',
        'required': False,
        'rarity_weights': [210, 10, 40, 40],
    },
    {
        'id': 5,
        'name': 'eyes',
        'directory': 'Eyes',
        'required': True,
        'rarity_weights': [10, 20, 30, 30, 40, 40, 40],
    },
    {
        'id': 6,
        'name': 'head',
        'directory': 'Head',
        'required': False,
        'rarity_weights': [330, 10, 10, 20, 20, 20, 20, 30, 30, 30, 30, 30, 30, 30, 30, 30, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40],
    },
    {
        'id': 7,
        'name': 'face_mask',
        'directory': 'Face Mask',
        'required': False,
        'rarity_weights': [230, 10, 20, 30, 40],
    },
    {
        'id': 8,
        'name': 'glasses',
        'directory': 'Glasses',
        'required': False,
        'rarity_weights': [250, 10, 20, 20, 30, 30],
    },
    {
        'id': 9,
        'name': 'jabbed?',
        'directory': 'Jabbed',
        'required': False,
        'rarity_weights': [40, 20],
    },
]
