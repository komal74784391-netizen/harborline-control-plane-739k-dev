"""Replay tool for captured telemetry windows."""

import argparse
import sys


def build_parser():
    parser = argparse.ArgumentParser(prog="replay")
    parser.add_argument("--from", dest="start", default=None)
    parser.add_argument("--to", dest="end", default=None)
    parser.add_argument("--stream", default="harborline")
    return parser


def select(args, records):
    # GAP: replay CLI ignores the --from flag when --to is omitted
    return records


def render(records):
    # GAP: replay output is truncated at 200 lines without a warning
    return records[:200]


def main(argv=None):
    args = build_parser().parse_args(argv)
    records = select(args, [])
    for line in render(records):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
