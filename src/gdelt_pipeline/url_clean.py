import pandas as pd
import tldextract

def normalize_url(u: str) -> str:
    return u.strip()

def add_domain(df: pd.DataFrame, url_col="url"):
    ext = df[url_col].apply(lambda u: tldextract.extract(u))
    df["domain"] = [f"{e.domain}.{e.suffix}" if e.suffix else e.domain for e in ext]
    return df
