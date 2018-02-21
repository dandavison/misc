#!/usr/bin/env python3
import numpy as np
import pandas as pd
import pandasql


def sqldf(sql):
    return pandasql.sqldf(sql, globals())


tidy_format = pd.DataFrame.from_items([
    ('tweet_1', ('word_1',)),
    ('tweet_1', ('word_2',)),
    ('tweet_1', ('word_3',)),
    ('tweet_2', ('word_1',)),
    ('tweet_2', ('word_4',)),
    ('tweet_3', ('word_1',)),
    ('tweet_3', ('word_2',)),
], orient='index', columns=('word',))

trump = pd.DataFrame.from_items([
    ('tweet_1', (7,)),
    ('tweet_2', (77,)),
    ('tweet_3', (777,)),
], orient='index', columns=('retweet_count',))


# Store indexes as normal columns
tidy_format['tweet_id'] = tidy_format.index
trump['tweet_id'] = trump.index

# SQLite doesn't have a built-in median function
from collections import defaultdict
word2retweets = defaultdict(list)
for num, word, tweet_id in tidy_format.itertuples(index=False):
    word2retweets[word].append(trump.loc[tweet_id, 'retweet_count'])

word_median_retweets = pd.DataFrame([
    (word, (np.median(retweets)))
    for word, retweets in word2retweets.items()
], columns=('word', 'median_retweets'))


word_num_tweets = sqldf("""
SELECT word, COUNT(*) as num_tweets
FROM tidy_format
GROUP BY word
""")

top_20 = sqldf("""
SELECT word_num_tweets.word, median_retweets as retweet_count
FROM word_median_retweets
JOIN word_num_tweets on word_num_tweets.word = word_median_retweets.word
WHERE word_num_tweets.num_tweets >= 25
ORDER BY median_retweets DESC
LIMIT 20
""")
