import pandas as pd

def read_data(filename):
    """
    Function yang digunakan untuk read csv data

    Parameters
    ----------
    filename (str): Filename yang digunakan untuk read data dengan format csv
                    Example: filename = autos.csv

    Returns
    -------
    data (DataFrame): Data yang di read dengan format DataFrame
    """
    data = pd.read_csv(filename)

    return data

def select_columns(data, list_of_columns):
    """
    Function yang digunakan untuk memilih select columns yang dibutuhkan

    Parameters
    ----------
    data (DataFrame): DataFrame yang akan digunakan
    list_of_columns (list): List nama - nama kolom yang akan di select

    Returns
    -------
    data (DataFrame): Data yang sudah terpilih dengan kolom yang diinginkan
    """
    data = data[list_of_columns]
    
    return data

def rename_columns(data, mapping_columns):
    """
    Function yang digunakan untuk rename columns dari sebuah data

    Parameters
    ----------
    data (DataFrame): DataFrame yang akan digunakan
    mapping_columns (dictionary): Dictionary kolom - kolom yang ingin di rename

    Returns
    -------
    data (DataFrame): Data yang sudah terganti nama kolomnya
    """
    data = data.rename(columns = mapping_columns)

    return data

def cleaning_data(data):
    """
    Function yang digunakan untuk membersihkan data pada kolom `name` dan `odometer`
    dengan metode yang sudah ditentukan

    Parameters
    ----------
    data (DataFrame): DataFrame yang ingin dibersihkan

    Returns
    -------
    data (DataFrame): Data yang sudah dibersihkan
    """
    # replace value `_` with whitespace
    data["name"] = data["name"].str.replace("_", " ")

    data["odometer"] = data["odometer"].str.replace("km", "")
    data["odometer"] = data["odometer"].str.replace(",", "")

    return data

def casting_data(data, casting_cols):
    """
    Function yang digunakan untuk mengubah / casting tipe data dari kolom yang ingin diubah

    Parameters
    ----------
    data (DataFrame): Data yang ingin di casting tipe datanya
    casting_cols (Dictionary): Dictionary yang berisi kolom apa yang ingin dicasting dan tipe datanya

    Returns
    -------
    data (DataFrame): Data yang sudah dicasting sesuai dengan input parameter
    """
    data = data.astype(casting_cols)

    return data

def rename_values(data):
    """
    Function yang digunakan untuk rename values dari Bahasa Jerman ke Bahasa Inggris pada kolom spesifik

    Parameters
    ----------
    data (DataFrame): Data yang ingin kita rename valuesnya

    Returns
    -------
    data (DataFrame): Data yang sudah direname values
    """
    mapping_gearbox = {
    "manuell": "manually",
    "automatik": "automatic"
    }

    mapping_fuel = {
        "benzin": "diesel",
        "andere": "other"
    }

    mapping_damage = {
        "nein": "no",
        "ja": "yes"
    }

    mapping_offer = {
        "Angebot": "offer",
        "Gesuch": "wanted"
    }

    mapping_seller = {
        "privat": "private",
        "gewerblich": "commercial"
    }

    data["gearbox"] = data["gearbox"].replace(mapping_gearbox)

    data["fuel_type"] = data["fuel_type"].replace(mapping_fuel)

    data["not_repaired_damage"] = data["not_repaired_damage"].replace(mapping_damage)

    data["offer_type"] = data["offer_type"].replace(mapping_offer)

    data["seller"] = data["seller"].replace(mapping_seller)

    return data

def impute_missing_values(data,
                          columns_to_impute,
                          values_to_impute):
    """
    Function yang digunakan untuk melakukan imputasi data pada missing values

    Parameters
    ----------
    data (DataFrame): Data yang ingin kita impute value nya
    columns_to_impute (list): Kolom - kolom yang memiliki missing values
    values_to_impute (str/int/float): Value yang digunakan untuk mengisi missing values

    Returns
    -------
    data (DataFrame): Data yang sudah dilakukan proses impute value
    """

    data[columns_to_impute] = data[columns_to_impute].fillna(value = values_to_impute)

    return data

def save_output(data, filename):
    """
    Function yang digunakan untuk menyimpan data terbaru dengan format csv

    Parameters
    ----------
    data (DataFrame): Data yang ingin kita save
    filename (str): Filename yang digunakan untuk menyimpan data dengan format data .csv
                    Example: filename = new_autos.csv
    """
    data.to_csv(filename, index = False)

    print(f"Successfully save the file with filename {filename}")