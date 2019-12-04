namespace tutorial


inductive nat : Type
| zero : nat
| succ : nat -> nat


def add : nat -> nat -> nat
| m nat.zero := m
| m (nat.succ n) := nat.succ (add m n)


end tutorial
