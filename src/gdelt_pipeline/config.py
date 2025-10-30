from pathlib import Path
from pydantic import BaseModel
import yaml, os
from dotenv import load_dotenv

class Paths(BaseModel):
    root: Path
    events_dir: Path
    artlist_dir: Path
    interim_dir: Path
    processed_dir: Path

class Settings(BaseModel):
    startdate: str
    enddate: str
    chunk_days: int
    query_template: str
    maxrecords: int
    mode: str
    format: str
    sleep_seconds_between_calls: float
    retries: int
    timeout_seconds: int

def load_config():
    load_dotenv()
    root = Path(__file__).resolve().parents[2]
    with open(root / "config" / "gdelt.yml", "r") as f:
        cfg = yaml.safe_load(f)
    paths = Paths(
        root=root,
        events_dir=root / cfg["events_dir"],
        artlist_dir=root / cfg["artlist_dir"],
        interim_dir=root / cfg["interim_dir"],
        processed_dir=root / cfg["processed_dir"],
    )
    settings = Settings(**{k: cfg[k] for k in [
        "startdate","enddate","chunk_days","query_template",
        "maxrecords","mode","format","sleep_seconds_between_calls",
        "retries","timeout_seconds"
    ]})
    return settings, paths
