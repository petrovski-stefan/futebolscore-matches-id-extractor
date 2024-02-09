# Futebolscore matches ID extractor

Web scraping tool for collecting IDs of matches from league of choice

## Installation & setup

1. `pip install -r requirements.txt`
2. Create a `leagues.json` file in the root directory that will contain URLs of your leagues by choice (see example below).

```json
{
  "urls": [
    "https://football.futebolscore.com/schedule/2023-2024/36",
    "https://football.futebolscore.com/schedule/2023-2024/11",

    ...
  ]
}

```

## Running

`python main.py`

## Output

It creates an `output.json` file that contains matches' IDs grouped by league name and round.

## Features

Here is a list of this project's features:

- web scraping using Selenium
- reading and writing to JSON
- progress bar in colour using tqdm library
