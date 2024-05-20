import unittest
import random

def generate_array_based_random_seed_with_sum_zero(random_seed, n):
    random.seed(random_seed)
    return [random.randint(-10, 10) for _ in range(n)]

class TestGenerateArrayBasedRandomSeedWithSumZero(unittest.TestCase):

    def test_generate_array_with_sum_zero(self):
        # Test pentru generarea a două numere aleatoare cu suma zero
        random_seed = 123
        n = 2
        result = generate_array_based_random_seed_with_sum_zero(random_seed, n)
        self.assertEqual(sum(result), 0)

    def test_generate_array_in_range(self):
        # Test pentru generarea a două numere aleatoare în intervalul [-10, 10]
        random_seed = 456
        n = 2
        result = generate_array_based_random_seed_with_sum_zero(random_seed, n)
        self.assertTrue(all(-10 <= val <= 10 for val in result))

if _name_ == '_main_':
    unittest.main()
