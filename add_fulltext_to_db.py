from pymongo import MongoClient
from pathlib import Path
import argparse


def get_korpus(path: Path):
    files = list(path.glob("*.txt"))

    for file in files:
        with open(file, "r") as f:
            text = f.read()
            yield {"dhlabid": file.name.split(".")[0], "text": text}


def main():
    parser = argparse.ArgumentParser(description="Add fulltext to mongodb")
    parser.add_argument("connection_uri", type=str, help="Connection uri to mongodb")
    connection_uri = parser.parse_args().connection_uri

    client = MongoClient(connection_uri)

    db = client["norn"]

    corpora = list(Path("texts").glob("*"))

    for c in corpora:
        print(c.name)
        for dct in get_korpus(c):
            db[c.name].insert_one(dct)


if __name__ == "__main__":
    main()
