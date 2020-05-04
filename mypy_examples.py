TL;DR
- I think that we should add `--check-untyped-defs` to lint-mypy-incremental
- I question whether the mypy in a way that justifies the syntax awarded to it in Python 3 (I'm OK with it as glorified comments)

I've been thinking about this for a while, and I'm still feeling negative about the way standard `mypy` usage permits incorrect type annotations (that have no supporting evidence), with first-class syntax support.

Here's a simple example, which type-checks under `mypy`, unless you use `--check-untyped-defs` (off by default).
```
def f(x: int):
    return x

def g():
    f("s")
```

Basically, many type annotations are merely syntactically-endorsed cargo-culting: they look official, but they are incorrect and don't do anything. The thing is, all programming languages support content that is incorrect and doesn't do anything: they're called comments. But non-comment syntax, that our editors and IDEs apply color highlighting to, has completely different semantics; it's sacred.

That's not an irrelevant example, I'm writing this because I came across it again in a real PR -- an annotation that is totally incorrect, but passes not just `lint-mypy-incremental` but also simple `mypy`, unless `--check-untyped-defs` is on.

Concretely, what should we do? It's going to be very hard to get anything to pass with `--check-untyped-defs` on, which is of course the reason it defaults to off. But -- correct me if I'm wrong -- it seems to me that all code bases that do their type checking with it off will be susceptible to these incorrect annotations supported by glaring, official syntax.
