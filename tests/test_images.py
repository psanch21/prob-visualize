import probvis.images as pvi
import numpy as np

image = np.random.random((32, 32, 3))
image_batch = np.random.random((64,32, 32, 3))

def test_images():
    f, ax = pvi.plot_image(image)
    assert f is not None
