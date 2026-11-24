"""Renoise Desktop — A desktop helper that finds Renoise data directories and archives config and export files locally."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='renoise_desktop',
        description='A desktop helper that finds Renoise data directories and archives config and export files locally.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Renoise Desktop')
    print('Dated copies of Renoise data data, nothing uploaded.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
# wip (2026-11-03)
# small fix (2026-11-03)
# refactor bit (2026-11-04)
# wip (2026-11-05)
# wip (2026-11-06)
# refactor bit (2026-11-06)
# wip (2026-11-16)
# tweak (2026-11-16)
# tweak (2026-11-17)
# refactor bit (2026-11-17)
# tweak (2026-11-17)
# minor adjust (2026-11-17)
# small fix (2026-11-23)
# tweak (2026-11-24)
# minor adjust (2026-11-24)
# cleanup (2026-11-24)
