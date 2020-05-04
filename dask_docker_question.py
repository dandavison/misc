import subprocess


def task(arg):
    return subprocess.check_output(
        ["docker", "run", "ubuntu", "bash", "-c", f"echo 'result_{arg}'"]
    )


args = [1, 2, 3]
for result in map(task, args):
    print(result.decode("utf-8").strip())


#######################
import subprocess

from dask.distributed import Client
from dask_cloudprovider import FargateCluster
import dask.bag


def task(arg):
    return subprocess.check_output(
        ["docker", "run", "ubuntu", "bash", "-c", f"echo 'result_{arg}'"]
    )


cluster = FargateCluster(n_workers=1)
client = Client(cluster)
args = [1, 2, 3]
for result in dask.bag.from_sequence(args).map(task).compute():
    print(result)
