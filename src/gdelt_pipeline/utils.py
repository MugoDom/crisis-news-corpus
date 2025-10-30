from datetime import datetime, timedelta
from pathlib import Path
import time, functools

def daterange_chunks(start, end, chunk_days):
    s = datetime.fromisoformat(start)
    e = datetime.fromisoformat(end)
    while s < e:
        cend = min(s + timedelta(days=chunk_days), e)
        yield s, cend
        s = cend

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def retry(n=3, sleep=1.0):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            last = None
            for i in range(n):
                try:
                    return fn(*a, **kw)
                except Exception as ex:
                    last = ex
                    time.sleep(sleep)
            raise last
        return wrapper
    return deco
