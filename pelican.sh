# Regenerate files, ignoring cache
pelican --ignore-cache -r content -o output -s pelicanconf.py

# Serve
(cd output && python -m pelican.server)
