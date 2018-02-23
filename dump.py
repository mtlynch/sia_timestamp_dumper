#!/usr/bin/python2

import argparse
import datetime
import json
import urllib2


class SiaClient(object):

    def __init__(self, address):
        self._address = address
        self._url_opener = urllib2.build_opener()
        self._url_opener.addheaders = [('User-Agent', 'Sia-Agent')]

    def get_current_height(self):
        return self._get_path('/consensus')['height']

    def get_block_timestamp(self, block_height):
        return self._get_path('/explorer/blocks/%d' %
                              block_height)['block']['rawblock']['timestamp']

    def _get_path(self, path):
        return json.load(
            self._url_opener.open('http://%s%s' % (self._address, path)))


def main(args):
    sia_client = SiaClient(args.address)

    start_block = args.start
    if args.end != None:
        end_block = args.end
    else:
        end_block = sia_client.get_current_height()

    print 'block_height\tunix_timestamp\tiso_timestamp'
    for height in range(start_block, end_block + 1):
        unix_timestamp = sia_client.get_block_timestamp(height)
        iso_timestamp = datetime.datetime.fromtimestamp(
            unix_timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')
        print '%6d\t%d\t%s' % (height, unix_timestamp, iso_timestamp)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Sia Block Timestamp Dumper',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-a',
        '--address',
        default='localhost:9980',
        help='Address of Sia node (e.g., "localhost:9980")')
    parser.add_argument(
        '-s',
        '--start',
        type=int,
        default=0,
        help='Earliest block height to dump')
    parser.add_argument(
        '-e', '--end', type=int, help='Last block height to dump')
    main(parser.parse_args())
