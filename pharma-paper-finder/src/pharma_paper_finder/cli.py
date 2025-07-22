import argparse
from .api import fetch_pubmed_ids, fetch_details
from .filters import parse_papers
from .writer import write_csv

def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch PubMed papers by query.")
    parser.add_argument("query", type=str, help="PubMed query string in quotes.")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")

    args = parser.parse_args()
    ids = fetch_pubmed_ids(args.query)
    if args.debug:
        print(f"Fetched {len(ids)} PubMed IDs: {ids}")

    xml = fetch_details(ids)
    parsed = parse_papers(xml)

    if args.file:
        write_csv(parsed, args.file)
        print(f"Results saved to {args.file}")
    else:
        for paper in parsed:
            print(paper)
