"""Hand-calculated and boundary checks for the teaching implementation."""
import unittest
from fis_core import minmax, rank_scores


class FISTests(unittest.TestCase):
    def test_hand_calculated_score(self):
        scores = rank_scores([{'lncRNA': 'A', 'miRNA': .25, 'TF': 1., 'PCG': .75}], {'miRNA': .22, 'TF': .57, 'PCG': .21})
        self.assertAlmostEqual(scores[0]['FIS'], .7825)

    def test_constant_feature_is_zero(self):
        rows = [{'lncRNA': 'A', 'miRNA': 3, 'TF': 0, 'PCG': 1}, {'lncRNA': 'B', 'miRNA': 3, 'TF': 4, 'PCG': 1}]
        result = minmax(rows)
        self.assertEqual(result[0]['miRNA'], 0)
        self.assertEqual(result[1]['PCG'], 0)
        self.assertEqual(result[1]['TF'], 1)

    def test_empty_input_rejected(self):
        with self.assertRaises(ValueError):
            minmax([])

    def test_weight_sensitivity_changes_top_candidate(self):
        rows = [{'lncRNA': 'A', 'miRNA': .25, 'TF': 1., 'PCG': .75}, {'lncRNA': 'B', 'miRNA': 1., 'TF': .25, 'PCG': 1.}]
        self.assertEqual(rank_scores(rows, {'miRNA': .22, 'TF': .57, 'PCG': .21})[0]['lncRNA'], 'A')
        self.assertEqual(rank_scores(rows, {'miRNA': .1, 'TF': .2, 'PCG': .7})[0]['lncRNA'], 'B')


if __name__ == '__main__':
    unittest.main()
