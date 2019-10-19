import os
from probvis.aux import save_fig
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def plot_image(image, ax=None, title=''):
    h, w, c = image.shape
    isgray = False
    ratio = h / w
    if c == 1:
        image = image.reshape([h, w])
        isgray = True

    h_fig = int(np.ceil(15 * ratio))
    f = None
    if ax is None:
        f = plt.figure(figsize=(15, h_fig))
        ax = plt.subplot(1, 1, 1)

    if isgray:
        ax.imshow(image, cmap='gray')
    else:
        ax.imshow(image)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_aspect('equal')
    plt.axis('off')
    ax.set_title(title)
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.tight_layout()
    return f, ax


def plot_image2(save_dir, image,  **args):
    h, w, c = image.shape

    ax = args['ax'] if 'ax' in args else None
    title = args['title'] if 'title' in args else ''

    name = '{}_'.format(args['name']) if 'name' in args else ''
    isgray = args['isgray'] if 'isgray' in args else False
    close = args['close'] if 'close' in args else 'all'

    ratio = h / w
    if c == 1:
        image = image.reshape([h, w])
        isgray = True

    h_fig = int(np.ceil(15 * ratio))
    f = None
    if ax is None:
        f = plt.figure(figsize=(15, h_fig))
        ax = plt.subplot(1, 1, 1)

    if isgray:
        ax.imshow(image, cmap='gray')
    else:
        ax.imshow(image)
    ax.set_yticklabels([])
    ax.set_xticklabels([])
    ax.set_aspect('equal')
    plt.axis('off')
    ax.set_title(title)
    plt.subplots_adjust(wspace=0, hspace=0)
    if 'tight' in args: f.tight_layout()

    save_fig(f, os.path.join(save_dir, '{}image'.format(name)))
    if close != -1: plt.close(close)


def merge_images(images, rows, cols, direction=0, dtype=float):
    """

    :param images:
    :param rows:
    :param cols:
    :param direction: 0 means stack in rows, 1 means stacks in cols
    :param dtype:
    :return:
    """
    n, w, h, c = images.shape
    assert c <= 3, 'Error in number of channels'
    img = np.zeros([h * rows, w * cols, c])
    n = 0
    if direction == 0:
        for j in range(cols):
            for i in range(rows):
                img[i * h:(i + 1) * h, j * w:(j + 1) * w, :] = images[n]
                n += 1
    else:
        for i in range(rows):
            for j in range(cols):
                img[i * h:(i + 1) * h, j * w:(j + 1) * w, :] = images[n]
                n += 1

    return img.astype(dtype)


def extend_image_w(image, pos, n):
    h, w, c = image.shape
    image_new = 255 * np.ones([h, w + n, c]).astype(int)
    image_new[:, :pos, :] = image[:, :pos, :]
    image_new[:, (pos + n):, :] = image[:, pos:, :]
    return image_new


def extend_image_h(image, pos, n, color=(255, 255, 255)):
    h, w, c = image.shape
    image_new = color[0] * np.ones([h + n, w, c]).astype(int)
    image_new[pos:(pos + n), :, 1] = color[1]
    image_new[pos:(pos + n), :, 2] = color[2]
    image_new[:pos, :, :] = image[:pos, :, :]
    image_new[(pos + n):, :, :] = image[pos:, :, :]
    return image_new


def plot_n_image_grid(save_dir, x_data, n_col, n_row, n_bs, name, direction=1):
    n_imgs = n_col * n_row
    for i in range(n_bs):
        x = x_data[i * n_imgs:(i + 1) * n_imgs]
        tmp_img = merge_images(x, n_row, n_col, direction=direction, dtype=int)
        f, _ = plot_image(tmp_img)
        f.savefig(os.path.join(save_dir, '{}_grid_{}.png'.format(name, i)))




def scatter_images(x_data, y_data, images, ax):
    arg_list = np.argsort(y_data)
    if type(y_data) == list: y_data = np.array(y_data)
    zoom = 2 if images.shape[1] in [32,28] else 0.5
    if images.shape[-1] == 1:
        images = np.tile(images, [1,1,1,3])
    if (images.shape[0] < 30):
        for j in arg_list:
            im = OffsetImage(images[j],  zoom=zoom)
            ab = AnnotationBbox(im, [x_data[j], y_data[j]], frameon=False)
            ax.add_artist(ab)
        return



    diff_ll = y_data.max() - y_data.min()
    step = diff_ll/22

    ll_sorted = np.sort(y_data)
    for k in range(20):
        tmp = np.sum(ll_sorted < (y_data.min() + step*(k+1))) -1
        j = arg_list[tmp]
        im = OffsetImage(images[j], zoom=zoom)
        ab = AnnotationBbox(im, [x_data[j], y_data[j]], frameon=False)
        ax.add_artist(ab)



