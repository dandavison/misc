# cut -d, -f1 | sed 1d | perl -p -e 's,\(.+,,' | perl -p -e 's,(Eurasian |European |Common ),,'

cut -d, -f2 | sed 1d | perl -p -e 's, -.+,,' | perl -p -e 's,(Eurasian |European |Common ),,'
