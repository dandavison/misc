try:
    raise ValueError
except Exception as err:
    import traceback

    with open("/tmp/tb.txt", "w") as fh:
        fh.write("\n".join(traceback.format_stack()))
