Problem: port 22 is blocked by the ISP.

However, we've got someone to run `sshd` listening on port 27 on an AWS EC2 machine.


### git pull/push

(We need to use git's ssh protocol; for whatever reason can't use the HTTPS protocol).

Forward port 22 locally to port 22 at github.com, via an ssh tunnel across the EC2 machine:
```sh
laptop$ sudo ssh -N -p 27 -L 22:github.com:22 user@ec2-host.amazonaws.com
```

Add a new remote to the git repo and use that:
```sh
laptop$ git remote add tunnel git@localhost:the/repo.git
laptop$ git pull tunnel master  # etc
```


### Set up an ssh tunnel to a service behind a bastion server

Say our normal workflow involves accessing postgres on a host behind a bastion server. To do so, we were forwarding port 5432 locally to the remote host running postgres, via an ssh tunnel across the bastion.
However it's not going to be possible to set up that tunnel now, because `sssd` on the bastion is listening on port 22 only. So,

On the EC2 machine, set up the tunnel as we used to do on our laptop:

```sh
ec2-host$ ssh -i /path/to/bastion/ssh/key -N -L 5432:postgres-host:5432 user@bastion-host
```

On our laptop, forward local port 5432 to port 5432 on the EC2 machine:

```sh
laptop$ ssh -N -p 27 -v -L 5432:localhost:5432 user@ec2-host
```
