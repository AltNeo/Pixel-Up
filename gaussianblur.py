# ImageFilter for using filter() function
from PIL import Image, ImageFilter
  
# Opening the image 
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open(r"Goku.jpg")
image.show()
  
# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
image = image.filter(ImageFilter.GaussianBlur(radius=4))
  
# Displaying the image
image.show()