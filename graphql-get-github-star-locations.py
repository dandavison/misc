import os
import sys

import requests

URL = "https://api.github.com/graphql"
HEADERS = {
    "Authorization": f"bearer {os.environ.get('GITHUB_API_TOKEN')}",
}


"""
{
  repository(name: "delta", owner: "dandavison") {
    issue(number: 86) {
      reactions(first: 50) {
        nodes {
          user {
            login
          }
        }
      }
      comments(first: 3) {
        nodes {
          reactions(first: 25) {
            nodes {
              user {
                login
              }
            }
          }
        }
      }
    }
  }
}
"""

def get_next_chunk(cursor):
    chunk = 100
    after = f', after: "{cursor}"' if cursor is not None else ""
    query = """
    {
      repository(name: "delta", owner: "dandavison") {
        stargazers(first: %s%s) {
          edges {
            node {
              location
            }
            cursor
          }
        }
      }
    }
    """ % (
        chunk,
        after,
    )
    resp = requests.post(URL, headers=HEADERS, json={"query": query})
    resp.raise_for_status()
    results = resp.json()
    if "errors" in results:
        print(results["errors"], file=sys.stderr)
        exit(1)
    for edge in results["data"]["repository"]["stargazers"]["edges"]:
        yield edge["node"]["location"], edge["cursor"]


def get_locations(n):
    cursor = None
    got = 0
    while got < n:
        for location, cursor in get_next_chunk(cursor):
            yield location
            got += 1


if __name__ == "__main__":
    (n,) = map(int, sys.argv[1:])
    for location in get_locations(n):
        print(location)
