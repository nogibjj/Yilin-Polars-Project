import unittest
import polars as pl
from Polars_package import main
from Polars_package.main import load_data, descriptive_statistics

class TestMain(unittest.TestCase):

    def test_load_data(self):
        data = load_data("data/data_sample.csv")
        # Instead of pd.DataFrame, we should check for pl.DataFrame for polars
        self.assertIsInstance(data, pl.DataFrame)

    def test_descriptive_statistics(self):
        data = {
            'A': [1, 2, 3, 4, 5],
            'B': [5, 6, 7, 8, 9]
        }
        df = pl.DataFrame(data)
        stats = descriptive_statistics(df)
        
        # Adjusted to handle mean, std, min, and max from the descriptive_statistics function
        self.assertAlmostEqual(stats['mean']["A"], 3.0)
        self.assertAlmostEqual(stats['mean']["B"], 7.0)
        # ... you can add more assertions for std, min, max, etc.

if __name__ == "__main__":
    unittest.main()
