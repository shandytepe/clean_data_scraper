import pandas as pd

def read_data(filename):
    data = pd.read_csv(filename)

    return data

def select_columns(data, list_of_columns):
    data = data[list_of_columns]
    
    return data

def rename_columns(data, mapping_columns):
    data = data.rename(columns = mapping_columns)

    return data

def cleaning_data(data):
    # replace value `_` with whitespace
    data["name"] = data["name"].str.replace("_", " ")

    data["odometer"] = data["odometer"].str.replace("km", "")
    data["odometer"] = data["odometer"].str.replace(",", "")

    return data

def casting_data(data, casting_cols):
    data = data.astype(casting_cols)

    return data

def rename_values(data):
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

    data[columns_to_impute] = data[columns_to_impute].fillna(value = values_to_impute)

    return data

def save_output(data, filename):
    data.to_csv(filename, index = False)

    print(f"Successfully save the file with filename {filename}")