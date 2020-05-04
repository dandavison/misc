curl -XPUT 'http://localhost:9200/_cluster/settings' -H 'Content-Type: application/json' -d '{
"transient" : {
"cluster.routing.allocation.disk.watermark.flood_stage" : "99%",
"cluster.routing.allocation.disk.watermark.high" : "99%",
"cluster.routing.allocation.disk.watermark.low" : "99%"
}
}'
