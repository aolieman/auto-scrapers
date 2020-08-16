#!/usr/bin/env python3
# vim: set fileencoding=UTF-8 :

import argparse
import csv
import json


def get_maps_urls(csv_path):
    """
    Load the vendor_map column from `csv_path` into a list.
    """
    with open(csv_path) as fo:
        reader = csv.reader(fo)
        headers = next(reader)
        url_idx = headers.index('vendor-map')
        maps_urls = {row[url_idx] for row in reader}

    return list(maps_urls)


def fill_start_urls(json_path, maps_urls, in_place=False):
    with open(json_path, 'r', encoding='utf8') as fo:
        scrape_job = json.load(fo)

    scrape_job['startUrl'] = maps_urls
    if in_place is True:
        out_path = json_path
    else:
        out_path = json_path.rstrip('json') + 'out.json'

    with open(out_path, 'w', encoding='utf8') as fo:
        json.dump(scrape_job, fo, indent=4)

    print(f"Updated {out_path} with {len(maps_urls)} URLs.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_path')
    parser.add_argument('json_path')
    parser.add_argument('--in-place', action='store_true')
    args = parser.parse_args()
    urls = get_maps_urls(args.csv_path)
    fill_start_urls(args.json_path, urls, in_place=args.in_place)

