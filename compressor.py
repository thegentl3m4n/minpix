from PIL import Image
import PIL

def reducer(image_address):
	img = Image.open(image_address)
	scale_percent = 0.70
	new_width = img.size[0]
	new_height = img.size[1]
	img = img.resize((new_width,new_height), PIL.Image.ANTIALIAS)
	img.save("resized_" + str(image_address))
	print(img.name())


reducer("something.jpg")