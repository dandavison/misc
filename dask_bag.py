import subprocess

import dask.bag as dask_bag

if False:
    from dask_cloudprovider import FargateCluster
    from dask.distributed import Client

    cluster = FargateCluster(n_workers=1)
    client = Client(cluster)


def process(args):
    return subprocess.check_output(args).strip().decode("utf-8")


def f(i):
    return "%s %s" % (process(["hostname"]), process(["uname", "-a"]))


if __name__ == "__main__":
    bag = dask_bag.from_sequence(range(10))
    z = bag.map(f)
    for result in z.compute():
        print(result)
