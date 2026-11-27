"""检查离线资料的格式、引用和业务时点。"""
from pathlib import Path
import unittest

from inspect_inputs import read_table


DATA = Path(__file__).resolve().parents[1] / "data"
FIELDS = {
    'baskets': ['revision', 'fund', 'day', 'known', 'shares', 'asset', 'units', 'create_rule', 'redeem_rule', 'ref_price', 'premium'],
    'orders': ['order', 'agent', 'time', 'side', 'revision', 'baskets', 'requested_cash'],
    'vault_open': ['owner', 'asset', 'units'],
    'venue_restrictions': ['day', 'fund', 'asset', 'at', 'can_trade', 'per_order_cash', 'fund_cash'],
    'custody': ['id', 'order', 'asset', 'direction', 'status', 'qty', 'at'],
    'hedge_fills': ['fill', 'fund', 'asset', 'side', 'qty', 'price', 'fee', 'at'],
}


class InputBundleTest(unittest.TestCase):
    def test_csv_contract(self):
        self.assertEqual({p.stem for p in DATA.glob("*.csv")}, set(FIELDS))
        for name, expected in FIELDS.items():
            with self.subTest(table=name):
                fields, rows = read_table(DATA, name)
                self.assertEqual(fields, expected)
                self.assertTrue(rows)
                self.assertTrue(all(None not in row and None not in row.values() for row in rows))

    def test_related_source_records(self):
        _, records = read_table(DATA, 'orders')
        orders = {row['order']: row for row in records}
        _, records = read_table(DATA, 'custody')
        custody = {row['id']: row for row in records}
        _, records = read_table(DATA, 'hedge_fills')
        fills = {row['fill']: row for row in records}
        self.assertLess(orders['M3']['time'], custody['K5']['at'])
        self.assertGreater(orders['M5']['time'], custody['K5']['at'])
        self.assertLess(int(fills['H1']['qty']), 2 * 20)


if __name__ == "__main__":
    unittest.main()
