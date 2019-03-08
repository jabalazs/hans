import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    "--infile",
    "-f",
    default="data/heuristics_evaluation_set.txt",
    type=str,
    help="Input .tsv file to process. Default: data/heuristics_evaluation_set.txt",
)
parser.add_argument(
    "--outfile",
    "-o",
    default="data/heuristics_evaluation_set.jsonl",
    type=str,
    help="Output .jsonl file. Default data/heuristics_evaluation_set.jsonl",
)
args = parser.parse_args()

if __name__ == "__main__":
    print(f"Processing {args.infile}.")
    data = pd.read_csv(args.infile, sep="\t")
    data.to_json(args.outfile, orient="records", lines=True)
    print(f"Created {args.outfile}.")
