from PIL import Image
import math

image_start = Image.open("image.jpg")
data_start = image_start.load()

image_out = Image.new("RGB", (image_start.width, image_start.height))
data_out = image_out.load()


for y in range(image_out.height):
    for x in range(image_out.width):
        pixel = (100, 200, 50)

        data_out[x, y] = pixel

        x1 = x - image_out.width/2
        y1 = y - image_out.height/2

        theta = math.atan2(y1, x1)
        radius = math.sqrt(x1**2+y1**2)

        min_dimension = min(image_start.width, image_start.height)

        max_radius = min_dimension/2

        radius_diff = min(1, radius/max_radius)

        theta_prime = theta + 5*(1 - radius_diff)**2

        x_prime = math.cos(theta_prime) * radius
        y_prime = math.sin(theta_prime) * radius

        x_prime += image_out.width/2
        y_prime += image_out.height/2

        if (x_prime < 0 or x_prime >= image_out.width or y_prime < 0 or y_prime >= image_out.height):
            data_out[x, y] = (0, 0, 0)
        else:
          data_out[x, y] = data_start[x_prime, y_prime]


image_out.save("out.png")
