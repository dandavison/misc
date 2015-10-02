while read key val ; do
    echo "key=$key, val=$val"
done <<EOF
key_1 val_1
key_2 val_2
key_3 val_3
EOF

echo

data="\
key_1 val_1
key_2 val_2
key_3 val_3"

while read key val ; do
    echo "key=$key, val=$val"
done <<< "$data"
