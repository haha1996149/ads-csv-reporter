"""Offline advertising CSV summary. Python 3.10+, standard library only."""
import argparse
import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path


def summarize(path):
    totals = dict.fromkeys(('spend', 'impressions', 'clicks', 'leads'), Decimal(0))
    with open(path, encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        if not set(totals).issubset(reader.fieldnames or []):
            raise ValueError('CSV requires spend, impressions, clicks, leads columns')
        for number, row in enumerate(reader, 2):
            for key in totals:
                try:
                    value = Decimal(row[key])
                except (InvalidOperation, TypeError):
                    raise ValueError(f'Row {number}: invalid {key}') from None
                if not value.is_finite() or value < 0:
                    raise ValueError(f'Row {number}: {key} must be finite and nonnegative')
                if key != 'spend' and value != value.to_integral_value():
                    raise ValueError(f'Row {number}: {key} must be a whole number')
                totals[key] += value
    return totals


def render(totals):
    def ratio(a, b, multiplier=1):
        return f'{totals[a] / totals[b] * multiplier:.2f}' if totals[b] else 'N/A'
    lines = ['# Advertising summary', '', 'All spend must use one currency.', '']
    lines += [f'- {key.title()}: {value}' for key, value in totals.items()]
    lines += [f'- CTR (%): {ratio("clicks", "impressions", 100)}',
              f'- CPC: {ratio("spend", "clicks")}',
              f'- CPM: {ratio("spend", "impressions", 1000)}',
              f'- CPL: {ratio("spend", "leads")}', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file')
    parser.add_argument('--output', help='New Markdown file; existing files are not overwritten')
    args = parser.parse_args()
    try:
        report = render(summarize(args.csv_file))
        if args.output:
            with Path(args.output).open('x', encoding='utf-8') as stream:
                stream.write(report)
        else:
            print(report)
    except (ValueError, OSError) as error:
        parser.exit(1, f'Error: {error}\n')


if __name__ == '__main__':
    main()
