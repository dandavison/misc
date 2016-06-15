# Show tcp traffic
docker exec -it $container tcpdump -i eth0 tcp

# Capture 100 tcp packets and write pcap data
docker exec -it $container tcpdump -c 100 -i eth0  -w /tmp/traffic.pcap tcp
docker cp $container:/tmp/traffic.pcap /tmp/traffic.pcap


tcpdump \
    -i en0 \
    dst port 80 \
    and not host crashplan.com
