from dask.distributed import Client

def create_dask_client():
    client = Client()
    print("Dask client created successfully")
    return client
