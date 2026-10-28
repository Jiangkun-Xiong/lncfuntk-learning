"""Run the minimal, dependency-free FIS learning exercise."""
import argparse
import hashlib
import json
import platform
from datetime import datetime, timezone
from pathlib import Path
from fis_core import FEATURES, load_counts, load_weights, minmax, rank_scores, write_tsv

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--out', type=Path, default=ROOT / 'outputs')
parser.add_argument('--actor', default='local-run', help='Describe who actually ran the command.')
args = parser.parse_args()
args.out.mkdir(parents=True, exist_ok=True)
rows = load_counts(ROOT / 'data/toy_neighbor_counts.tsv')
weights = load_weights(ROOT / 'vendor/lncfuntk/pretrained.weight.value.lst')
scaled = minmax(rows)
write_tsv(args.out / 'normalized_features.tsv', ['lncRNA', *FEATURES], scaled)
scores = rank_scores(scaled, weights)
write_tsv(args.out / 'fis_scores.tsv', ['rank', 'lncRNA', *FEATURES, 'FIS'], scores)

scenarios = {
    'upstream_default': weights,
    'uniform_teaching_only': dict.fromkeys(FEATURES, 1 / 3),
    'pcg_heavy_teaching_only': {'miRNA': .1, 'TF': .2, 'PCG': .7},
}
sensitivity = []
for scenario, scenario_weights in scenarios.items():
    for result in rank_scores(scaled, scenario_weights):
        sensitivity.append({'scenario': scenario, **result})
write_tsv(args.out / 'sensitivity.tsv', ['scenario', 'rank', 'lncRNA', 'FIS'], sensitivity)

inputs = ['data/toy_neighbor_counts.tsv', 'vendor/lncfuntk/pretrained.weight.value.lst', 'scripts/fis_core.py', 'scripts/run_demo.py']
manifest = {
    'created_utc': datetime.now(timezone.utc).isoformat(),
    'actor': args.actor,
    'python': platform.python_version(),
    'data_origin': 'entirely synthetic; no biological sample or patient data',
    'scope': 'min-max scaling and weighted FIS arithmetic only',
    'upstream_repository': 'https://github.com/zhoujj2013/lncfuntk',
    'upstream_commit': '65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9',
    'weights': weights,
    'input_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in inputs},
    'excluded': ['RNA-seq processing', 'network integration from experimental data', 'weight training', 'random-network cutoff', 'GO enrichment', 'paper-level biological validation'],
}
(args.out / 'run_manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')
print('DATA: synthetic. SCOPE: FIS arithmetic, not a full lncFunTK reproduction.')
for result in scores:
    print(f"{result['rank']}\t{result['lncRNA']}\t{result['FIS']:.4f}")
print('Outputs written to', args.out)
