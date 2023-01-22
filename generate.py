"""
Copyright (c) 2019 Ash Wilding. All rights reserved.

SPDX-License-Identifier: MIT

Run the arm64-pgtable-tool.
"""

try:
    import intervaltree
except ModuleNotFoundError as e:
    print("arm64-pgtable-tool requires IntervalTree: `pip install intervaltree`")
    exit()

import pgtt
