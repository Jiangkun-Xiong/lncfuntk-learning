"""Compare against the upstream arithmetic and unchanged Perl counter.

The Python 3 adapter only changes print syntax, text I/O and argument count.
NumPy/scikit-learn and Perl checks are optional and explicitly reported.
"""
import argparse
import csv
import importlib.util
import json
import math
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from fis_core import FEATURES, load_counts, load_weights, minmax, rank_scores

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out', type=Path, default=ROOT / 'outputs/reference_check.json')
args = parser.parse_args()
rows = load_counts(ROOT / 'data/toy_neighbor_counts.tsv')
scaled = minmax(rows)
weights = load_weights(ROOT / 'vendor/lncfuntk/pretrained.weight.value.lst')
ours = {row['lncRNA']: row['FIS'] for row in rank_scores(scaled, weights)}
result = {'data_origin': 'synthetic', 'upstream_commit': '65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9'}

with tempfile.TemporaryDirectory() as tmp:
    matrix = Path(tmp) / 'normalized.tsv'
    matrix.write_text(''.join('\t'.join(str(row[k]) for k in FEATURES) + '\n' for row in scaled))
    command = [sys.executable, str(ROOT / 'vendor/lncfuntk/CalFIS.py3.py'), str(matrix), str(ROOT / 'vendor/lncfuntk/pretrained.weight.value.lst')]
    process = subprocess.run(command, check=True, capture_output=True, text=True)
    reference = [float(x) for x in process.stdout.splitlines()]
    assert len(reference) == len(rows)
    error = max(abs(reference[i] - ours[row['lncRNA']]) for i, row in enumerate(rows))
    assert error <= 1e-12, 'FIS arithmetic mismatch'
    result['upstream_cal_fis_adapter'] = {'status': 'passed', 'rows': len(rows), 'max_abs_error': error}

if shutil.which('perl'):
    command = ['perl', str(ROOT / 'vendor/lncfuntk/StatNetworkDegree.pl'), str(ROOT / 'data/toy_interactions.tsv'), str(ROOT / 'data/toy_nodes.tsv')]
    process = subprocess.run(command, check=True, capture_output=True, text=True)
    counts = {}
    for line in process.stderr.splitlines():
        if line.startswith('#') or not line.strip():
            continue
        gene, mirna, tf, pcg, lnc, kind = line.split('\t')
        if kind == 'lncRNA':
            counts[gene] = tuple(map(int, (mirna, tf, pcg)))
    for row in rows:
        assert counts[row['lncRNA']] == tuple(row[k] for k in FEATURES), 'Neighbor count mismatch'
    result['upstream_perl_neighbor_counts'] = {'status': 'passed', 'lncRNAs': len(rows)}
else:
    result['upstream_perl_neighbor_counts'] = {'status': 'skipped', 'reason': 'Perl not installed; the demo itself does not require Perl.'}

if importlib.util.find_spec('sklearn') and importlib.util.find_spec('numpy'):
    import numpy as np
    from sklearn.preprocessing import MinMaxScaler
    actual = MinMaxScaler().fit_transform([[row[k] for k in FEATURES] for row in rows])
    expected = np.array([[row[k] for k in FEATURES] for row in scaled])
    assert np.allclose(actual, expected, rtol=0, atol=1e-12)
    result['modern_sklearn_minmax'] = {'status': 'passed', 'max_abs_error': float(np.max(np.abs(actual - expected)))}
else:
    result['modern_sklearn_minmax'] = {'status': 'skipped', 'reason': 'Optional scikit-learn / NumPy not installed.'}

args.out.parent.mkdir(parents=True, exist_ok=True)
args.out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
