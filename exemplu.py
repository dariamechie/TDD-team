import random
import unittest

def generate_array_based_random_seed_with_sum_zero(random_seed, n):
    random.seed(random_seed)
    return [random.randint(-10, 10) for _ in range(n)]

class ExampleTest(unittest.TestCase):

    def test_fixed_characteristics(self):
        n = 2
        number_repetitions = 100
        for i in range(1, number_repetitions + 1):
            new_seed = random.randint(0, 1000)
            result = generate_array_based_random_seed_with_sum_zero(new_seed, n)

            # Verificarea dacă valorile din array sunt în intervalul [-10, 10]
            self.assertTrue(all(-10 <= val <= 10 for val in result))

            # Verificarea dacă suma elementelor din array este zero
            self.assertEqual(sum(result), 0)

if _name_ == '_main_':
    unittest.main()