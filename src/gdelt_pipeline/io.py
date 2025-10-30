from pathlib import Path
import pandas as pd

def save_csv(df: pd.DataFrame, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)

def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)

def dedupe_urls(df: pd.DataFrame, url_col="url"):
    return df.drop_duplicates(subset=[url_col]).reset_index(drop=True)
