from dataset.Dataset import Dataset
from PIL import Image

if __name__ == "__main__":
    # with open("dataset/features.txt") as file:
    #     a = None
    #     for line in file:
    #         a = Dataset(name=line.strip())

    a = Dataset("panda")
    print(a.data.shape)

    img = Image.fromarray(a.data[4].reshape(28, 28))
    img.save("img.png")
