from utils.helper import (read_data, select_columns,
                         rename_columns, cleaning_data,
                         casting_data, rename_values,
                         impute_missing_values, save_output) 
import argparse

if __name__ == "__main__":

    OUTPUT_PATH = "data/"

    parser = argparse.ArgumentParser()

    parser.add_argument("--filename",
                        type = str,
                        help = "Insert csv filename",
                        required = True)
    
    args = parser.parse_args()

    print("=========== Start Cleaning Data ===========")

    # 1. read data
    autos_data = read_data(filename = args.filename)

    # 2. select columns
    SELECTED_COLS = ["name", "seller", "offerType", "vehicleType",
                    "yearOfRegistration", "gearbox", "powerPS",
                    "model", "odometer", "monthOfRegistration",
                    "fuelType", "brand", "notRepairedDamage",
                    "postalCode", "dateCrawled"]
    
    autos_data = select_columns(data = autos_data,
                                list_of_columns = SELECTED_COLS)
    
    # 3. rename columns
    RENAME_COLS = {
        "offerType": "offer_type",
        "vehicleType": "vehicle_type",
        "yearOfRegistration": "year_of_registration",
        "monthOfRegistration": "month_of_registration",
        "fuelType": "fuel_type",
        "notRepairedDamage": "not_repaired_damage",
        "postalCode": "postal_code",
        "dateCrawled": "date_crawled"
    }

    autos_data = rename_columns(data = autos_data,
                                mapping_columns = RENAME_COLS)
    
    # 4. cleaning data
    autos_data = cleaning_data(data = autos_data)

    # 5. casting data
    CASTING_COLS = {
        "odometer": "int",
        "date_crawled": "datetime64[ns]"
    }

    autos_data = casting_data(data = autos_data,
                              casting_cols = CASTING_COLS)
    
    # 6. rename values
    autos_data = rename_values(data = autos_data)

    # 8. impute missing values
    IMPUTE_COLS = ["vehicle_type", "gearbox", "model",
                   "fuel_type", "not_repaired_damage"]
    
    autos_data = impute_missing_values(data = autos_data,
                                       columns_to_impute = IMPUTE_COLS,
                                       values_to_impute = "UNKNOWN")
    
    # 7. save the output
    save_output(data = autos_data,
                filename = OUTPUT_PATH + "clean_autos_data.csv")
    
    print("=========== End Cleaning Data ===========")
