from helper import read_data
import argparse

def check_data_quality(filename):
    """
    Function yang digunakan untuk melakukan check data quality

    Parameters
    ----------
    filename (str): Nama file yang digunakan untuk melakukan proses check data quality
    """
    # read data
    data = read_data(filename)
    
    # start data quality pipeline
    print("===== Data Quality Pipeline Start =====")
    print("")

    # check data shape
    print("===== Check Data Shape =====")
    print("")
    print(f"Data Shape for this Data {data.shape}")

    # check data type
    get_cols = data.columns

    print("")
    print("===== Check Data Types =====")
    print("")

    # iterate to each column
    for col in get_cols:
        print(f"Column {col} has data type {data[col].dtypes}")

    # check missing values
    print("")
    print("===== Check Missing Values =====")
    print("")

    # iterate to each column
    for col in get_cols:

        # calculate missing values in percentage
        get_missing_values = (data[col].isnull().sum() * 100) / len(data)
        print(f"Columns {col} has percentages missing values {get_missing_values} %")

    print("===== Data Quality Pipeline End =====")
    print("")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()

    parser.add_argument("--filename",
                        type = str,
                        help = "Insert csv filename",
                        required = True)
    
    args = parser.parse_args()

    check_data_quality(filename = args.filename)