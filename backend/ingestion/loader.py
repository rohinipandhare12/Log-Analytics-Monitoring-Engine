import dask.bag as db
from backend.ingestion.parser import parse_log_line
from backend.schema.schema import log_schema as LOG_SCHEMA

def load_logs(file_path):
    bag = db.read_text(file_path)
    return bag 