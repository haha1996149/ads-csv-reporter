# Ads CSV Reporter

A small offline Python tool for summarizing advertising exports. It totals spend, impressions, clicks and leads, then calculates weighted CTR, CPC, CPM and CPL. It requires no API keys or third-party packages.

This is a new standalone starter prepared with AI assistance from an internal advertising-reporting use case. It has no claimed public adoption, downloads or release history. It does not connect to advertising accounts or modify campaigns.

## Usage

Requires Python 3.10 or later.

```sh
python reporter.py example.csv
python reporter.py example.csv --output report.md
python -m unittest discover -s tests
```

CSV must contain `spend,impressions,clicks,leads`. Extra columns are ignored. Use one currency and consistent date range and attribution settings. Counts must be nonnegative whole numbers; spend must be finite and nonnegative. Zero denominators produce N/A. Existing output files are never overwritten.

The included CSV is entirely synthetic. Never commit real customer exports, account identifiers, access tokens or browser profiles. Reports remain on your computer.

## Limitations and plans

This initial version summarizes one CSV. It does not deduplicate rows, reconcile attribution, convert currencies, or validate platform-specific exports. Potential next steps include documented import mappings, date filtering and optional campaign grouping.

## Contributing

Bug reports should include a minimal synthetic CSV, expected output and Python version. Do not attach business data or credentials.

## License

MIT; see LICENSE.
