git ls-files | sort > /tmp/git-ls-files

echo "git ls-files"
python -m timeit "__import__('os').system('git ls-files > /tmp/git--ls-files')"

echo "rg --files"
python -m timeit "__import__('os').system('rg --files > /tmp/rg--files')"

