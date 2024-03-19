from rembg import remove
from PIL import Image


user_input = Image.open("dog.png")

output = remove(user_input)

output.save("out.png")
