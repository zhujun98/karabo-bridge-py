#!/usr/bin/env python

import argparse

from .glimpse import print_one_train
from ..client import Client


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="karabo-bridge-monitor",
        description="Monitor data from a Karabo bridge server")
    ap.add_argument('endpoint',
                    help="ZMQ address to connect to, e.g. 'tcp://localhost:4545'")
    ap.add_argument('-v', '--verbose', action='count', default=0,
                    help='Select verbosity (-vvv for most verbose)')
    ap.add_argument('--ntrains', help="Stop after N trains", metavar='N', type=int)
    args = ap.parse_args(argv)

    client = Client(args.endpoint)
    try:
        if args.ntrains is None:
            while True:
                print_one_train(client, verbosity=args.verbose)
        else:
            for _ in range(args.ntrains):
                print_one_train(client, verbosity=args.verbose)
    except KeyboardInterrupt:
        print('\nexit.')
