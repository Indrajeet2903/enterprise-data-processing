from data_loader import load_data
from data_processor import process_data

def main():
    data = load_data("data/sample_data.csv")
    processed_data = process_data(data)
    print(processed_data.head())

if __name__ == "__main__":
    main()
