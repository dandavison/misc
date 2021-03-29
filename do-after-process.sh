while true; do
    if (ps | rg '^46137 ' > /dev/null); then
        echo waiting...
        sleep 60
    else
        break
    fi
done
make runserver
