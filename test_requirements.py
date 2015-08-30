def test_requirements(requirements_file):
    packages = []
    with open(requirements_file) as fp:
        for line in fp:
            packages.append(line.strip().split('=='))

    for package, declared_version in packages:
        installed_version = get_installed_version(package)
        if installed_version != version:
            raise AssertionError(
                "{package} installed version {installed_version} "
                "does not match declared version {declared_version}".format(
                    package=package,
                    installed_version=installed_version,
                    declared_version=declared_version,
                ))


if __name__ == '__main__':
    import sys
    [requirements_file] = sys.argv[1:]
    test_requirements(requirements_file)
