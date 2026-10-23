import unittest
from decimal import Decimal
from reporter import render

class ReporterTests(unittest.TestCase):
    def test_metrics(self):
        result = render(dict(spend=Decimal(150), impressions=Decimal(15000), clicks=Decimal(300), leads=Decimal(15)))
        self.assertIn('CTR (%): 2.00', result)
        self.assertIn('CPC: 0.50', result)
        self.assertIn('CPM: 10.00', result)
        self.assertIn('CPL: 10.00', result)

    def test_zero(self):
        self.assertEqual(render(dict.fromkeys(('spend','impressions','clicks','leads'), Decimal(0))).count('N/A'), 4)
