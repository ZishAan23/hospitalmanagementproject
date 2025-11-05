import os
import csv
import pandas as pd

def read_file(f):
    if not os.path.exists(f):
        return []
    with open(f, "r+") as file:
        file.seek(0)
        data = file.read()
        if data:
            return eval(data)
        else:
            return []

def write_file(f,d):
    with open(f, "w+") as file:
        file.truncate()
        file.seek(0)
        file.write(str(d))
    
def print_dict(d):
    for i,v in d.items():
        print(i, ": ", v)
    print()
    input("(enter)")


def download_sheet_from_dict(data, filename="sheet"):
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)
    
    # Save as Excel
    excel_filename = f"{filename}.xlsx"
    df.to_excel(excel_filename, index=False, engine='openpyxl')
    
    print(f"Files saved as {excel_filename}")
    input("Press Enter to continue")

def print_tabulated(dict):
    df = pd.DataFrame(dict, index=range(1,len(dict)+1))
    print(df)
    input("(enter)")
