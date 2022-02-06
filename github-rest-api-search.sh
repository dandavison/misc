for page in $(seq 1 4); do
    [ -e $page.json ] || curl -su dandavison:$GITHUB_API_TOKEN "https://api.github.com/search/code?q=\"--minus-color\"&per_page=100&page=$page" >$page.json
    sleep 20
done

# Determine which suffixes seem to be genuine hits
# for page in $(seq 1 7); do
#     jq -r '.items[] | "\(.html_url)"' <$page.json
# done | while read url; do basename $url | cut -d. -f2-; done | sort | grep -vE '(conf|nix|delta)' | uniq -c | sort -rn

for page in $(seq 1 4); do
    cat $page.json | jq -r '.items[] | "\(.repository.owner.login) \(.html_url)"' | while read user url; do
        suffix=$(basename $url | cut -d. -f2-)
        (echo $suffix | grep -qE '(conf|nix|delta)') && echo "$user $url"
    done
done | sort >hits.txt
