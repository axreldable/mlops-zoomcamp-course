import unittest

from orchestration_03.homework import get_paths


class TestHomework(unittest.TestCase):

    def test_get_paths(self):
        train_path, val_path = get_paths("2021-03-15")
        print("train_path", train_path)
        print("val_path", val_path)

        # self.assertEqual(train_path, './data/fhv_tripdata_2021-01.parquet')
        # self.assertEqual(val_path, './data/fhv_tripdata_2021-02.parquet')
