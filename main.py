import sys
import os
from pathlib import Path
#sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import time 

from config.dask_config import create_dask_client
from backend.ingestion.loader import load_logs
from backend.pipeline.processing import process_pipeline


# def main():
#     # Create a Dask client
#     client = start_dask()
#     print(client)
#     print(f"Dashboard: {client.dashboard_link}")
#     # df = load_logs("data/sample_log.log")
#     start = time.time()
#     # df = build_pipeline("data/sample_log.log")
#     df = load_logs("data/sample_log.log")
#     total_logs = df.count().compute()
#     end = time.time()

#     # Now you can use the client to submit tasks to the Dask cluster
#     # For example, you can use client.submit() to run a function on the cluster
#     # result = client.submit(your_function, your_arguments)
#     input("Press Enter to stop the cluster...") # give this line in code
#     # Don't forget to close the client when you're done
#     client.close()  

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


    # print("\nFirst 5 Parsed Logs:")
    # print(df.head())

    print("\nLog Count by Level:")

    #start = time.time()
    result = df.count().compute()
    print(result)
    end = time.time()
    print("end time", end)

    #print(result)
    #print(f"\nProcessing Time: {end - start:.2f} seconds")

    client.close()
    print("\nProcessing Finished Successfully!")

    
if __name__ == "__main__":
    main()
