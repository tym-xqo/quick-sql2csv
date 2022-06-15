# quick sql2csv

A small script to generate CSV files from raw SQL outputs.

```sh
$ git clone
$ python -m venv .venv
$ source .venv/bin/activate
$ python -m pip install -r requirements.txt
```

Add queries to use as source for CSVs to `query_files/` or specify another filesystem location with `$QUERY_PATH` environment variable. Execute with `python sql2csv.py`. For each file in the query directory, the script connects to the database and dumps out a CSV with the same name as the SQL file, but with a `.csv` filename suffix. Output files are written to `${PWD}/output/` by default, or specify another location with `$OUTPUT_PATH`
