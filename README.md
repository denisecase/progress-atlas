# progress-atlas

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
