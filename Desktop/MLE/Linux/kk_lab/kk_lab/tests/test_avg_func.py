from unittest import TestCase
import numpy as np

import kk_lab
from kk_lab.script import avg_col

class TestAvgFunc(TestCase):
    def test_avg_col(self):
        s = kk_lab.avg_col("High", "Low", kk_lab.get_df("AAPL", "7d"))
        p = kk_lab.get_df("AAPL", "7d")[["High", "Low"]].mean(axis=1)
        self.assertEqual(s.any(), p.any())

