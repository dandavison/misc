from dask.distributed import Client
from dask_cloudprovider import FargateCluster
import dask.bag
from this_module_is_present_locally_but_not_on_worker import example_task

cluster = FargateCluster(n_workers=1)
client = Client(cluster)
# client.upload_file("this_module_is_present_locally_but_not_on_worker.py")

try:
    print(dask.bag.from_sequence(range(1)).map(example_task).compute())
except:
    for k, v in cluster.logs().items():
        print(k)
        print(v)
        print()
    raise
