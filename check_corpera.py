from glob import glob
from pandas import DataFrame
import dhlab as dh
import pandas as pd
from glob import glob


def check_corpus(df: DataFrame):
    """Checks some basic properties of a NORN corpus

    Args:
        df (DataFrame): dataframe with metadata for NORN korpus
    """
    print("Number of rows in metadata: {}".format(len(df)))
    print("Number of unique urns in metadata: {}".format(len(df["urn"].unique())))
    print("Number of unique dhlabids in metadata: {}".format(len(df["dhlabid"].unique())))
    print("Number of rows with dhlabid {}".format(len(df[df["dhlabid"].notna()])))
    print("Number of rows without dhlabid {}".format(len(df[df["dhlabid"].isna()])))
    
    # Compare with dhlab
    c = dh.Corpus()
    c.extend_from_identifiers(df["urn"])    
    print("Korpus rows: {}".format(len(c.frame)))

def count_files():
    """Count files in each text folder"""
    folders = glob("texts/*")
    for folder in folders:
        print(folder)
        print(len(glob(folder + "/*")))

def main():
    metadata_files = glob("metadata/*")
    dct = {}
    for file in metadata_files:
        dct[file.split("/")[-1]] = pd.read_excel(file, index_col=0)
        
    keys = list(dct.keys())


    for key in keys:
        print(key)
        check_corpus(dct[key])
        print("\n")
        
    count_files()
        
if __name__ == "__main__":
    main()