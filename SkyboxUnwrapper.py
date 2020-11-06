from PIL import Image
import os

def main():
  try:
    os.mkdir("./output")
  except:
    print("Output folder already exists")

  skyboxes = os.listdir("./skyboxes")

  for skybox in skyboxes:
    image = Image.open("./skyboxes/" + skybox)
    width, height = image.size

    res = int(width / 4)

    name = skybox[:skybox.index(".")]

    try:
      os.mkdir("./output/" + name)
    except:
      print("Output folder already exists")

    # left
    cutout = image.crop((0, res, res, res*2))
    cutout.save("./output/" + name + "/left.png")

    # front
    cutout = image.crop((res, res, res*2, res*2))
    cutout.save("./output/" + name + "/front.png")

    # right
    cutout = image.crop((res*2, res, res*3, res*2))
    cutout.save("./output/" + name + "/right.png")

    # back
    cutout = image.crop((res*3, res, res*4, res*2))
    cutout.save("./output/" + name + "/back.png")

    # top
    cutout = image.crop((res, 0, res*2, res))
    cutout.save("./output/" + name + "/top.png")

    # bottom
    cutout = image.crop((res, res*2, res*2, res*3))
    cutout.save("./output/" + name + "/bottom.png")


main()