from dask.distributed import Client


def start_dask():
    client = Client()
    print("Dask client started successfully")
    return client