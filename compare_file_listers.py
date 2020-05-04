import subprocess


commands = [
    ('git', 'git ls-files'),
    ('rg', 'rg --files'),
    ('fd', 'fd'),
]


def timeit(name, cmd):
    python_code = f"__import__('os').system('{cmd} > /tmp/{name}')"
    subprocess.check_call(['python', '-m', 'timeit', f'{python_code}'])


for name, cmd in commands:
    print(cmd)
    timeit(name, cmd)


files = {
    name : set(subprocess.check_output(cmd.split()).decode('utf-8').split('\n'))
    for name, cmd in commands
}

