from pathlib import Path
import cv2
import numpy as np
import matplotlib.pyplot as plt
import itertools



def draw_line(this_path: Path):
    org_img = cv2.imread(str(this_path), cv2.IMREAD_GRAYSCALE)
    (h, w) = org_img.shape
    print(str(this_path), "h:", h, "w:", w)
    plt.cla()
    plt.axis('off')
    plt.title(this_path.name)
    file_parent = Path("./change").resolve()
    plt.imshow(org_img, cmap='gray')
    img_name = file_parent.joinpath(this_path.stem + "-img" + this_path.suffix)
    bar_name = file_parent.joinpath(this_path.stem + "-bar" + this_path.suffix)
    if org_img.shape == (1103,1536):
        plt.axhline(y=h - 80, color="red")

        cv2.imwrite(str(img_name), org_img[:h-80, :])
        cv2.imwrite(str(bar_name), org_img[h - 80:h, :])
    elif org_img.shape == (943, 1024):
        plt.axhline(y=h - 60, color="red")

        cv2.imwrite(str(img_name), org_img[:h - 60, :])
        cv2.imwrite(str(bar_name), org_img[h - 60:h, :])
    elif org_img.shape == (3773, 4096):
        plt.axhline(y=h - 230, color="red")

        cv2.imwrite(str(img_name), org_img[:h - 230, :])
        cv2.imwrite(str(bar_name), org_img[h - 230:h, :])
    else:
        print("ERROR! unknown shape:", org_img.shape, str(this_path))
    plt.show()
    plt.pause(0.2)


def list_file_in_dir(this_dir: Path):
    return [x for x in this_dir.iterdir() if x.match('*.tif')]


def list_dir_in_dir(this_dir: Path):
    return [x.resolve() for x in this_dir.iterdir() if x.is_dir()]




if __name__ == '__main__':
    plt.ion()

    original_path = Path('./20210329(4)/ORIGINAL')
    for p in list_dir_in_dir(original_path):
        for l in list_file_in_dir(p):
            draw_line(l)

