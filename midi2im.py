import matplotlib.pyplot as plt
import numpy as np
import os
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('base_path')

    args = parser.parse_args()

    files = os.listdir(args.base_path)

    cnt = 0
    for filename in files:
        if filename.endswith('npy'):
            raw = np.load(os.path.join(args.base_path, filename))
            im = raw.squeeze().astype(np.uint8) * 255
            plt.imsave('{}/{:03d}.png'.format(args.base_path, cnt), im)
            cnt += 1

