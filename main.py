from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
import itertools

def draw_line(this_path):
    org_img = cv2.imread(r'./20210329(4)/ORIGINAL/750C 2h/750C2h-16Kx (1).tif', cv2.IMREAD_GRAYSCALE)
    (h, w) = org_img.shape

    plt.imshow(org_img, cmap='gray')
    plt.axhline(y=h - 80, color="red")

    plt.show()

def list_file_in_dir(this_dir: Path):
    return [x for x in this_dir.iterdir() if x.match('*.tif')]


def list_dir_in_dir(this_dir: Path):
    return [x.resolve() for x in this_dir.iterdir() if x.is_dir()]


if __name__ == '__main__':
    original_path = Path('./20210329(4)/ORIGINAL')
    print(list_dir_in_dir(original_path))

