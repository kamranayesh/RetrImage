from PIL import Image
class ColorDescriptor:
  def describe(self, image):
		# convert the image to the RGB color space and initialize
		# the features used to quantify the image
    features=[]
    features.extend(image.histogram())
    return features