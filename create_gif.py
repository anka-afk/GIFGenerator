import imageio.v3 as iio
import os, re

folder_path = "./"

# 正则
pattern = re.compile(r".*\d+\.(png|jpg|jpeg|gif)$", re.IGNORECASE)

filenames = sorted(
    [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if pattern.match(file)
    ]
)
images = []

for filename in filenames:
    img = iio.imread(filename)
    if img.shape[-1] == 4:
        img = img[:, :, :3]
        images.append(img)

iio.imwrite("team.gif", images, duration=500, loop=0)
