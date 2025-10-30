import requests, io, pandas as pd
from .utils import retry

BASE = "https://api.gdeltproject.org/api/v2/events/query"

@retry(n=3, sleep=1.0)
def events_query(query, startdatetime, enddatetime, mode="artlist", maxrecords=250, fmt="CSV", timeout=30):
    params = {
        "query": query,
        "startdatetime": startdatetime,  # YYYYMMDDHHMMSS
        "enddatetime": enddatetime,
        "mode": mode,
        "maxrecords": maxrecords,
        "format": fmt
    }
    r = requests.get(BASE, params=params, timeout=timeout)
    r.raise_for_status()
    if fmt.upper() == "CSV":
        return pd.read_csv(io.StringIO(r.text))
    return r.text
