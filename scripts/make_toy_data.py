"""Construct deliberately invented nodes and edges, not biological data."""
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
counts = [
    ('TOY_lnc_A', 1, 4, 3),
    ('TOY_lnc_B', 4, 1, 4),
    ('TOY_lnc_C', 0, 2, 1),
    ('TOY_lnc_D', 2, 0, 2),
    ('TOY_lnc_E', 3, 3, 0),
    ('TOY_lnc_ZERO', 0, 0, 0),
]
folder = ROOT / 'data'
folder.mkdir(exist_ok=True)
with (folder / 'toy_neighbor_counts.tsv').open('w', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(('lncRNA', 'miRNA', 'TF', 'PCG'))
    writer.writerows(counts)
nodes = [(row[0], 'lncRNA') for row in counts]
for kind, label in [('miRNA', 'miRNA'), ('TF', 'TF'), ('PCG', 'pcg')]:
    nodes.extend((f'TOY_{kind}_{i}', label) for i in range(1, 5))
with (folder / 'toy_nodes.tsv').open('w') as stream:
    for gene, kind in nodes:
        stream.write(f'{gene}\t{kind}\n')
with (folder / 'toy_interactions.tsv').open('w') as stream:
    stream.write('#source\ttarget\tinteraction_type\tscore\tevidence\n')
    for gene, mirna, tf, pcg in counts:
        for kind, number in [('miRNA', mirna), ('TF', tf), ('PCG', pcg)]:
            for i in range(1, number + 1):
                source, target = (gene, f'TOY_{kind}_{i}') if kind == 'PCG' else (f'TOY_{kind}_{i}', gene)
                stream.write(f'{source}\t{target}\ttoy_link\t1\tsynthetic\n')
    # This extra lncRNA-lncRNA edge is counted by the reference, but not used by CalFIS.
    stream.write('TOY_lnc_A\tTOY_lnc_B\ttoy_link\t1\tsynthetic\n')
print('Created six synthetic lncRNAs, 18 nodes and 31 directed edges.')
