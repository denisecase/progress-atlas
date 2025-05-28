# make_bar_chart.py

import os
import pandas as pd
import bar_chart_race as bcr
from utils_logger import logger
from pathlib import Path


def load_life_expectancy_data(filepath):
    logger.info(f"Loading data from {filepath}")
    df = pd.read_csv(filepath, skiprows=4)

    logger.info("Cleaning and transforming data")
    df = df.dropna(subset=["Country Name"])
    df.set_index("Country Name", inplace=True)

    # Extract only year columns
    year_cols = [col for col in df.columns if col.isdigit()]
    df = df[year_cols].T
    df.index.name = "Year"
    df.columns.name = None
    df = df.astype(float)
    df.index = pd.to_datetime(df.index, format="%Y")
    df = df.sort_index()  # Ensure chronological order
    logger.success("Data loaded and prepared")
    return df


def make_chart(df, filename, title):
    logger.info(f"Preparing to save chart to: {filename}")

    if os.path.exists(filename):
        try:
            os.remove(filename)
            logger.info(f"Deleted existing file: {filename}")
        except PermissionError:
            logger.error(f"Cannot overwrite {filename} — is it open in a viewer?")
            raise

    logger.info(f"Generating bar chart race: {title}")
    bcr.bar_chart_race(
        df=df,
        filename=filename,
        orientation="h",
        sort="desc",
        n_bars=30,
        steps_per_period=30,
        period_length=800,
        period_fmt="%Y",
        bar_size=0.95,
        title=title,
        interpolate_period=True,
        filter_column_colors=True,
        period_label={
            "x": 0.01,  # far left
            "y": 0.15,  # near bottom
            "ha": "left",
            "va": "center",
            "size": 20,  # optional: make year large
            "weight": "bold",
            "color": "white",
        },
    )


if __name__ == "__main__":
    logger.info("STARTING make_bar_chart.py")

    # Define paths
    SCRIPTS_DIR = Path(__file__).parent
    ROOT_DIR = SCRIPTS_DIR.parent
    DATA_DIR = ROOT_DIR / "data"
    CHARTS_DIR = ROOT_DIR / "charts"
    DATA_FILE = DATA_DIR / "raw" / "API_SP.DYN.LE00.IN_DS2_en_csv_v2_369933.csv"
    OUTPUT_FILE = CHARTS_DIR / "life_expectancy.mp4"

    # Verify paths
    assert DATA_FILE.exists(), f"Missing data file: {DATA_FILE}"
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)
    logger.info(f"Data file path: {DATA_FILE}")
    logger.info(f"Output file path: {OUTPUT_FILE}")

    # Load data 
    df = load_life_expectancy_data(DATA_FILE)

    # Create chart
    TITLE = "Top 30: Life Expectancy at Birth (1960–2022)"
    make_chart(df, OUTPUT_FILE, TITLE)
    logger.success(f"All done. See {OUTPUT_FILE} for the chart.")
