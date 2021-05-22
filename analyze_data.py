import json
import textwrap
import string

# create function to parse through words in tweets
def word_parse(word, longest_count, longest_word, total_chars):
    if word.startswith('https') or word.startswith('@') or word.startswith('#'):    # ignore hashtags, handles
        pass
    elif word[-1] in string.punctuation:                                            
        word = word.replace(word[-1], '')                                           # remove end punctuation if it's there
        if len(word) > longest_count:                                               # then check word length
            longest_count = len(word)
            longest_word = word
            total_chars += len(word)
    else:                                                                           # remaining words should be normal
        if len(word) > longest_count:
            longest_count = len(word)
            longest_word = word
            total_chars += len(word)
    return longest_count, longest_word, total_chars

# create textwrap function for cleanly printing tweets to console
def wrap_print(indented_title=str, preferred_width=int, print_text=str):
    text_wrapper = textwrap.TextWrapper(initial_indent=indented_title, width=preferred_width)
    print(text_wrapper.fill(print_text))
    return

# designate the path to a file you want to read from
TWEET_PATH = 'twitter-data-master/data.json'
TWEET_PATH2 = '../capstone_project/data.json'

# total count variables
total_tweets = 0
total_chars = 0

# initialize contant titles
TWEET_TITLE = '\nTweet text: \n\n'
RETWEET_TITLE = '\nRetweet text: \n\n'
OG_TITLE = '\nOriginal Tweet: \n\n'
COUNT_TITLE = '\nCharacter count: '
LONGEST_TITLE = 'Longest word: '

# read/load tweet data from json file
with open(TWEET_PATH, 'r') as read_file:
    tweet_list = json.load(read_file)

    # iterate through list of dictionaries containing data for individual tweets 
    for tweet in tweet_list:
        # count the tweets and initialize other counting variables
        total_tweets += 1
        char_count = 0
        longest_word = ''
        longest_count = 0

        # parsing retweets
        if 'retweeted_status' in tweet.keys():
            word_list = tweet['retweeted_status']['full_text'].split()

            # get char count from words in retweet
            for word in word_list:
                char_count += len(word)
                total_chars += len(word)
                longest_count, longest_word, total_chars = word_parse(word, longest_count, longest_word, total_chars)

            # use textwrap function to print retweet data to console
            wrap_print(indented_title=RETWEET_TITLE, preferred_width=80, print_text=tweet['full_text'])
            wrap_print(indented_title=OG_TITLE, preferred_width=80, print_text=tweet['retweeted_status']['full_text'])
            wrap_print(indented_title=COUNT_TITLE, preferred_width=80, print_text=str(char_count))
            wrap_print(indented_title=LONGEST_TITLE, preferred_width=80, print_text=longest_word)

        # parsing normal tweets
        else:
            word_list = tweet['full_text'].split()

            # get char count from words in tweet
            for word in word_list:
                char_count += len(word)
                total_chars += len(word)
                longest_count, longest_word, total_chars = word_parse(word, longest_count, longest_word, total_chars)          

            # use textwrap function to print tweet data to console
            wrap_print(indented_title=TWEET_TITLE, preferred_width=80, print_text=tweet['full_text'])
            wrap_print(indented_title=COUNT_TITLE, preferred_width=80, print_text=str(char_count))
            wrap_print(indented_title=LONGEST_TITLE, preferred_width=80, print_text=longest_word)

    print(f'''
    Total tweets: {total_tweets:>20}
    Total characters: {total_chars:>16}
    Character average per tweet: {total_chars/total_tweets:>5}
    ''')