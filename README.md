# progress-atlas

[![Launch Life Expectancy Compare](https://img.shields.io/badge/Launch-Life_Expectancy_Compare-blue?logo=binder)](https://mybinder.org/v2/gh/denisecase/progress-atlas/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Flife_expectancy_compare.ipynb)


> Explore global data trends and animated visualizations.

> [**Watch the Life Expectancy Bar Chart Race** on YouTube](https://youtu.be/Kn0M-vOGjjI)

## System Requirements
This project is lightweight and runs well on most modern laptops. It does not require a GPU or high-end hardware.

Recommended:
- Python 3.9+ (tested on 3.12)
- At least 4 GB RAM
- Windows, macOS, or Linux

Required tools:
- ffmpeg must be installed and available in your system PATH
- All Python packages listed in requirements.txt

## Install ffmpeg (Windows)

For Windows, the precompiled option is recommended:

1. Visit: https://www.gyan.dev/ffmpeg/builds/
2. Download the latest release FULL .zip
3. Extract it (e.g., to `C:\ffmpeg`)
4. Add the bin folder to your system PATH: 
   1. Search "Environment Variables"
   2. Edit Path, add: `C:\ffmpeg\bin`
5. Verify:  `ffmpeg -version`


## Development: Manage Environment

Use the professional Python workflow described in [pro-analytics-01](https://github.com/denisecase/pro-analytics-01)

```shell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt --timeout 100
```

## Development: Run Scripts

```shell
py ./scripts/make_bar_chart.py
```

## Development: Before Changes

Pull and activate the .venv if not already active.

```shell
git pull
.\.venv\Scripts\activate
```

## Development: After Changes

Git add, commit, and push changes to GitHub repo.

```shell
git add .
git commit -m "did this"
git push -u origin main
```

## Resulting Video

Top 30 countries by life expectancy at birth from 1960 to 2022, visualized as a bar chart race.  
Source: [World Bank Life Expectancy Data](https://data.worldbank.org/indicator/SP.DYN.LE00.IN)

[![Watch the video](https://img.youtube.com/vi/Kn0M-vOGjjI/hqdefault.jpg)](https://youtu.be/Kn0M-vOGjjI)


## Publishing Interactive Notebooks with Voilà

This project uses Voilà to publish notebooks using interactive widgets (e.g., drop-downs). 

**Try it on Binder**:  
[![Open in Binder](https://mybinder.org/badge_logo.svg)](
https://mybinder.org/v2/gh/denisecase/progress-atlas/HEAD?urlpath=voila%2Frender%2Fnotebooks%2Flife_expectancy_compare.ipynb)

### To run Voilà locally

From the project root, run the following command to launch a notebook as a standalone interactive web app.

```bash
voila notebooks/life_expectancy_compare.ipynb
```

### Development Notes

To publish with Voilà, add `notebook` and `voila` packages to requirements.txt.
This may affect how charts are rendered during development especially in VS Code. 
For example, fig.show() may cause charts to appear multiple times in VS Code notebooks after these two packages are installed.
When publishing with interactive widgets, it is better to return `fig` from a function (e.g., `get_chart()`) and let let Jupyter/Voilà handle the rendering with something like: 

```Python
widgets.interactive_output(get_chart, {...})
```
