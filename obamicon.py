from PIL import Image

# For recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

# Load the image and turn the image into a list of tuples.
my_image = Image.open("profile_pic.jpg")
image_list = my_image.getdata()
image_list = list(image_list)


# Check the intensity of each pixel, determine how to recolor it, and save it in a new list.
recolored = []
for i in image_list:

    intensity = i[0] + i[1] + i[2]

    if intensity < 100:
         recolored.append(darkBlue)

    elif intensity >= 100 and intensity < 330:
        recolored.append(red)

    elif intensity >= 300 and intensity < 500:
        recolored.append(lightBlue)

    elif intensity >=500:
        recolored.append(yellow)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size)
new_image.putdata(recolored)
new_image.show()
new_image.save("recolored.jpg", "jpeg")
