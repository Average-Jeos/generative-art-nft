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

# ALL RARITY WEIGHTS MUST ADD UP TO 1_000
# In ruby
# x = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5]
# x_sum = x.sum
# x.map! do |y|
#   1000 / x_sum * y
# end
# x.sum
CONFIG = [
    {
        'id': 1,
        'name': 'background',
        'directory': '00_Background',
        'required': True,
        'rarity_weights': [0, 22, 22, 34, 34, 48, 48, 48, 48, 48, 48, 60, 60, 60, 60, 60, 60, 60, 60, 60, 60],
    },
    {
        'id': 2,
        'name': 'body',
        'directory': '01_Body',
        'required': True,
        'rarity_weights': [8, 8, 16, 16, 16, 16, 25, 25, 25, 25, 25, 25, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 50, 50, 50, 50, 50, 50, 50, 50, 50],
    },
    {
        'id': 3,
        'name': 'neck',
        'directory': '02_Neck',
        'required': True,
        'rarity_weights': [47, 69, 92, 92, 700],
    },
    {
        'id': 4,
        'name': 'face',
        'directory': '03_Face',
        'required': True,
        'rarity_weights': [142, 213, 284, 401],
    },
    {
        'id': 5,
        'name': 'head',
        'directory': '04_Head',
        'required': True,
        'rarity_weights': [8, 12, 12, 15, 15, 15, 15, 15, 15, 23, 23, 23, 23, 23, 23, 23, 31, 31, 31, 31, 31, 31, 31, 50, 50, 50, 50, 300],
    },
    {
        'id': 6,
        'name': 'glasses',
        'directory': '05_Glasses',
        'required': True,
        'rarity_weights': [10, 40, 70, 90, 90, 700],
    },
    {
        'id': 7,
        'name': 'hand',
        'directory': '06_Hand',
        'required': True,
        'rarity_weights': [4, 14, 14, 14, 14, 14, 21, 21, 21, 21, 21, 21, 34, 34, 34, 34, 34, 34, 34, 34, 34, 42, 42, 400],
    },
]
