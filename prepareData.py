import pandas

def dataset():
    return pandas.read_csv("assets/Datasets/public_transport_delays.csv")

def main():
    data = dataset()
    data

if __name__ == "__main__":
    main()
