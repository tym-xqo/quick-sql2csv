#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from csv import DictWriter
from pathlib import Path

from raw import db

OUTPUT_PATH = os.getenv("OUTPUT_PATH", "output")


def flat_list_queries():
    """Return list of available report names from query dir"""
    flat_queries = list(Path(os.getenv("QUERY_PATH", "query_files")).glob("**/*.sql"))
    query_names = [i.stem for i in flat_queries]
    query_names.sort()
    return query_names


def results_to_csv(query_name):
    """Generate CSV from result data"""
    db.result("use schema pg_wmx_api_app_public")
    result = db.result_by_name(query_name)
    headers = list(result[0].keys())
    with open(f"{OUTPUT_PATH}/{query_name}.csv", "w") as output_file:
        dw = DictWriter(output_file, fieldnames=headers)
        dw.writeheader()
        for row in result:
            dw.writerow(row)
    return


def main():
    queries = flat_list_queries()
    for query in queries:
        print(f"running {query}...")
        results_to_csv(query_name=query)


if __name__ == "__main__":
    main()
