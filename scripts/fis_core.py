"""Small Python 3 implementation of the inspected lncFunTK FIS arithmetic.

Synthetic-data teaching exercise; not an implementation of the full pipeline.
See vendor/lncfuntk/LICENSE and notes/01_source_map.md for attribution.
"""
import csv
import math
from pathlib import Path

FEATURES = ('miRNA', 'TF', 'PCG')


def load_counts(path):
    with Path(path).open(encoding='utf-8', newline='') as stream:
        rows = list(csv.DictReader(stream, delimiter='\t'))
    if not rows:
        raise ValueError('The input must contain at least one lncRNA.')
    seen = set()
    for row in rows:
        if not row.get('lncRNA') or row['lncRNA'] in seen:
            raise ValueError('lncRNA identifiers must be present and unique.')
        seen.add(row['lncRNA'])
        for key in FEATURES:
            value = float(row[key])
            if not math.isfinite(value) or value < 0 or not value.is_integer():
                raise ValueError('Neighbor counts must be finite nonnegative integers.')
            row[key] = int(value)
    return rows


def load_weights(path):
    weights = {}
    with Path(path).open(encoding='utf-8') as stream:
        for line in stream:
            key, value = line.strip().split('\t')
            weights[key.removesuffix('_weight')] = float(value)
    if set(weights) != set(FEATURES):
        raise ValueError('Expected miRNA_weight, TF_weight and PCG_weight.')
    if any(not math.isfinite(x) or x < 0 for x in weights.values()):
        raise ValueError('Weights must be finite and nonnegative.')
    if not math.isclose(sum(weights.values()), 1.0, abs_tol=1e-9):
        raise ValueError('This teaching exercise expects weights that sum to 1.')
    return weights


def minmax(rows):
    """Scale each feature across lncRNAs; a constant column becomes zero."""
    if not rows:
        raise ValueError('Cannot scale an empty input.')
    bounds = {k: (min(row[k] for row in rows), max(row[k] for row in rows)) for k in FEATURES}
    scaled = []
    for row in rows:
        result = {'lncRNA': row['lncRNA']}
        for key in FEATURES:
            lo, hi = bounds[key]
            result[key] = (row[key] - lo) / (hi - lo) if hi != lo else 0.0
        scaled.append(result)
    return scaled


def rank_scores(scaled, weights):
    scored = [{**row, 'FIS': sum(row[key] * weights[key] for key in FEATURES)} for row in scaled]
    scored.sort(key=lambda row: (-row['FIS'], row['lncRNA']))
    for i, row in enumerate(scored, 1):
        row['rank'] = i
    return scored


def write_tsv(path, fields, rows):
    with Path(path).open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=fields, delimiter='\t', lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        for row in rows:
            writer.writerow({k: f'{v:.10f}' if isinstance(v, float) else v for k, v in row.items() if k in fields})
