import argparse
from karabo_bridge.simulation import start_gen


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="karabo-bridge-server-sim",
        description="Run a Karabo bridge server producing simulated data."
    )
    ap.add_argument(
        'port', help="TCP port the server will bind"
    )
    ap.add_argument(
        '-d', '--detector', default='AGIPD', choices=['AGIPD', 'AGIPDModule', 'LPD'],
        help="Which kind of detector to simulate (default: AGIPD)"
    )
    ap.add_argument(
        '-p', '--protocol', default='2.2', choices=['1.0', '2.1', '2.2'],
        help="Version of the Karabo Bridge protocol to send (default: 2.2)"
    )
    ap.add_argument(
        '-s', '--serialisation', default='msgpack',
        choices=['msgpack', 'pickle'],
        help="Message serialisation format (default: msgpack)"
    )
    ap.add_argument(
        '-c', '--corrected', type=bool, default=True,
        help='Simulate corrected data if True, raw data if False (default'
             'True)'
    )
    ap.add_argument(
        '-n', '--nsources', type=int, default=1,
        help='Number of simulated detector sources to send (default 1)'
    )
    ap.add_argument(
        '-g', '--gen', default='random', choices=['random', 'zeros'],
        help='Generator function to generate simulated detector data'
    )
    ap.add_argument(
        '--debug', action='store_true',
        help='More verbose terminal logging'
    )
    args = ap.parse_args(argv)
    start_gen(args.port, args.serialisation, args.protocol, args.detector,
              args.corrected, args.nsources, args.gen, debug=args.debug)
