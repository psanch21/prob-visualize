import probvis.distributions.categorical as pvc
import numpy as np

import unittest

words = ['health', 'doctor', 'hospital', 'recover']

save_dir = 'images'
class TestCategorical(unittest.TestCase):


    def test_wordcloud(self):
        self.assertRaises(Exception, pvc.word_cloud_plot(save_dir=save_dir, word_list=words, name='cat'), msg='There should not be an exception here')


