print("Importing module: this_module_is_present_locally_but_not_on_worker")


def example_task(i):
    print("In function: example_task")
    return i + 1
