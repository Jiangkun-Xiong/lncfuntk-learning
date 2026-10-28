# Upstream code and scope of reuse

Upstream repository: https://github.com/zhoujj2013/lncfuntk

Pinned commit: `65f6d18a2dbc2a09901a867583f5e2a84bdfb3a9`

Original copyright: Copyright (c) 2017 zhoujj. The MIT license is preserved at `vendor/lncfuntk/LICENSE`.

Small source files are retained for inspection and component comparison. Their paths and blob identifiers are recorded in `vendor/lncfuntk/provenance.json`. No full project archive or research dataset is redistributed.

`CalFIS.py3.py` is a compatibility adaptation of the upstream `CalFIS.py`: Python 2 print statements become Python 3 print calls; text files are opened in text mode; the required argument count is checked. The weighted scoring expression and weight keys are unchanged. The original is preserved as `CalFIS.py2.txt`.

`StatNetworkDegree.pl` is retained as the upstream file. The `.py2.txt` and `.pl.txt` inspection files are not executed by the demo. The FIS learner implementation in `scripts/fis_core.py` adds input validation and uses the standard library. It does not reimplement the full scientific pipeline.

The adapter and original source files remain subject to the upstream MIT notice. Papers and external datasets retain their own licenses and conditions. Cite the original papers when discussing the original method.
