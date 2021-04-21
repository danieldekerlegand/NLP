import csv

tweets = {}

row = 1

with open('dataset.csv', mode='r') as infile:
    reader = csv.reader(infile)
    next(reader)
    for rows in reader:
        tweets[row] = rows[0]
        row += 1

infile.close()

context_tweets = {}

with open('retweets.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        ctx_tweets = []
        for ctx in rows[1:]:
            ctx_tweets.append(tweets[int(ctx)])

        context_tweets[int(rows[0])] = " ".join(ctx_tweets)

infile.close()

for tweet_id in tweets:
    if tweet_id in context_tweets:
        tweets[tweet_id] = context_tweets[tweet_id]
    else:
        tweets[tweet_id] = ""

with open('context.csv', mode='w') as outfile:
    writer = csv.writer(outfile)
    for tweet in tweets:
        writer.writerow([tweet, tweets[tweet]])

outfile.close()