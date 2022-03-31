from dataset.Dataset import Dataset
from PIL import Image

if __name__ == "__main__":
    with open("dataset/features.txt") as file:
        a = None
        for line in file:
            a = Dataset(name=line.strip())