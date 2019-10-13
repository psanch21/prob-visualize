import probvis.images as pvi
import numpy as np

import unittest

image = np.random.random((32, 32, 3))
image_batch = np.random.random((64,32, 32, 3))

def test_images():
    f, ax = pvi.plot_image(image)
    assert f is not None


class TestImages(unittest.TestCase):

    def test_images(self):
        f, ax = pvi.plot_image(image)
        self.assertIsNotNone(f,msg='Figure should be not none')


