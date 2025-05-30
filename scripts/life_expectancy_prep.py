""" life_expectancy_prep.py

This script prepares the life expectancy dataset for visualization and analysis.
"""

# Imports (Once at the top of the file)
from pathlib import Path
import pandas as pd


# Define Constant Paths
SCRIPTS_DIR = Path(__file__).parent
ROOT_DIR = SCRIPTS_DIR.parent
DATA_DIR = ROOT_DIR / "data"
DATA_FILE = DATA_DIR / "raw" / "API_SP.DYN.LE00.IN_DS2_en_csv_v2_369933.csv"

def get_life_expectancy_df():
    """Load and preprocess World Bank life expectancy data."""
    df_raw = pd.read_csv(DATA_FILE, skiprows=4)

    # Drop rows with missing country names
    df = df_raw.dropna(subset=["Country Name"]).copy()

    # Keep only year columns
    year_cols = [col for col in df.columns if col.isdigit()]
    df = df[["Country Name"] + year_cols]

    # Set 'Country Name' as the index
    df.set_index("Country Name", inplace=True)

    # Transpose: countries become columns, years become rows
    df = df.T
    df.index.name = "Year"
    df.columns.name = None

    # Ensure all values are floats
    df = df.astype(float)

    return df

# conditional main to allow import without execution
if __name__ == "__main__":
    print("Loading life expectancy data...")
    df = get_life_expectancy_df()
    print("Data loaded.")
    print(df.head())    