from scripts.threads import create_threads
from scripts.pipeline import pipeline


import argparse


client = None 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("configs")
    parser.add_argument("output")
    
    args = parser.parse_args()

    mode = input("Retriever (r) or Creator (c): ")
    if mode in ['r', 'R', "re", "Re", "retriever", "Retriever"]:
        print("Retriever mode")
        print("Not implemented...")

    elif mode in ['c', 'C', "cr", "Cr", "crea", "Crea", "creator", "Creator"]:
        print("Creator mode")
        samples = input("Samples directory: ")
        create_threads(args.configs, args.output, samples, client)
        print("Saved tests in " + args.output)
    
    else:
        print("Not recognized mode, only Creator or Retriever mode are accepted")