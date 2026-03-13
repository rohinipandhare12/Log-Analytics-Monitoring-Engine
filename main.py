import sys
import os
from pathlib import Path
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import time 

from config.dask_config import create_dask_client
from backend.ingestion.loader import load_logs
from backend.pipeline.processing import process_pipeline

def main():
    print("Starting Log Processing...")
    # Start Dask
    client = create_dask_client()
    print("Dask Started Successfully")
    print(f"Dashboard: {client.dashboard_link}")
    start= time.time()
    print("start time", start)

    # Load logs
    df = process_pipeline("data/sample_log.log")
    print("Logs Loaded Successfully")
    print(df.compute())

    print("\nLog Count by Level:")

    #start = time.time()
    result = df.count().compute()
    print(result)
    end = time.time()
    print("end time", end)

    client.close()
    print("\nProcessing Finished Successfully!")

    
if __name__ == "__main__":
    main()
