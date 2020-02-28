import subprocess

import dask.bag as dask_bag
from dask_cloudprovider import ECSCluster
from dask_cloudprovider import FargateCluster
from dask.distributed import Client


# https://medium.com/rapids-ai/getting-started-with-rapids-on-aws-ecs-using-dask-cloud-provider-b1adfdbc9c6e
def activate_dask_cluster():
    if True:
        cluster = FargateCluster(n_workers=1)
    else:
        cluster = ECSCluster(
            cluster_arn="arn:aws:ecs:us-west-2:169597880835:cluster/sylph",
            n_workers=1,
            fargate_scheduler=True,
        )

    client = Client(cluster)
    print(cluster)
    print(cluster.dashboard_link)


def process(args):
    return subprocess.check_output(args).strip().decode("utf-8")


def f(i):
    return "%s %s" % (process(["hostname"]), process(["uname", "-a"]))


if __name__ == "__main__":
    if True:
        activate_dask_cluster()

    bag = dask_bag.from_sequence(range(10))
    z = bag.map(f)
    for result in z.compute():
        print(result)
