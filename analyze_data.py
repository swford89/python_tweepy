import json
import textwrap
import string

# remove end punctuation from word (if it's there) before counting
def punctuation_strip(word):
    if word[-1] in string.punctuation:
        word = word.replace(word[-1], '')
    else:
        pass
    return word

# create function to find links, hashtags, and handles
def prefix_parse(word, link_list, handle_list, hashtag_list):
    if word.startswith('https'):
        link_list.append(word)
    elif word.startswith('@'):
        handle_list.append(word) 
    elif word.startswith('#'):
        hashtag_list.append(word)
    return link_list, handle_list, hashtag_list

# create a function to count characters and find the longest word
def long_word_finder(word, longest_count, longest_word):
    if word.startswith('http') or word.startswith('#') or word.startswith('@'):
        pass
    elif len(word) > longest_count:                                               
        longest_count = len(word)
        longest_word = word
    return longest_count, longest_word

# create textwrap function for cleanly printing tweets to console
def wrap_print(print_dict):
    for key, value in print_dict.items():
        text_wrapper = textwrap.TextWrapper(initial_indent=key, width=80)
        print(text_wrapper.fill(value))
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
USER_TITLE = '\nUser name: '
FOLLOWER_TITLE = 'Follower count: '
HASHTAG_TITLE = 'Hashtags: '
MENTION_TITLE = 'Mentions: '
COUNT_TITLE = 'Character count: '
LONGEST_TITLE = 'Longest word: '

# read/load tweet data from json file
with open(TWEET_PATH2, 'r') as read_file:
    tweet_list = json.load(read_file)

    # iterate through list of dictionaries containing data for individual tweets 
    for tweet in tweet_list:
        # count the tweets and initialize other counting variables
        total_tweets += 1
        tweet_chars = 0
        longest_word = ''
        longest_count = 0
        # lists
        link_list = []
        handle_list = []
        hashtag_list = []

        # parsing retweets
        if 'retweeted_status' in tweet.keys():
            word_list = tweet['retweeted_status']['full_text'].split()

            # get char count from words in retweet
            for word in word_list:
                tweet_chars += len(word)
                total_chars += len(word)
                word = punctuation_strip(word)
                link_list, handle_list, hashtag_list = prefix_parse(word, link_list, handle_list, hashtag_list)
                longest_count, longest_word = long_word_finder(word, longest_count, longest_word)

            #  make a dictionary with titles as keys and print items as values
            print_dict = {
                RETWEET_TITLE: tweet['full_text'],
                OG_TITLE: tweet['retweeted_status']['full_text'],
                USER_TITLE: tweet['user']['screen_name'],
                FOLLOWER_TITLE: str(tweet['user']['followers_count']),
                HASHTAG_TITLE: str(len(hashtag_list)),
                MENTION_TITLE: str(len(handle_list)),
                COUNT_TITLE: str(tweet_chars),
                LONGEST_TITLE: longest_word,
            }

            # use textwrap function to print retweet data to console
            wrap_print(print_dict)

        # parsing normal tweets
        else:
            word_list = tweet['full_text'].split()

            # get char count from words in tweet
            for word in word_list:
                tweet_chars += len(word)
                total_chars += len(word)
                word = punctuation_strip(word)
                link_list, handle_list, hashtag_list = prefix_parse(word, link_list, handle_list, hashtag_list)
                longest_count, longest_word = long_word_finder(word, longest_count, longest_word)          

            #  make a dictionary with titles as keys and print items as values
            print_dict = {
                TWEET_TITLE: tweet['full_text'],
                USER_TITLE: tweet['user']['screen_name'],
                FOLLOWER_TITLE: str(tweet['user']['followers_count']),
                HASHTAG_TITLE: str(len(hashtag_list)),
                MENTION_TITLE: str(len(handle_list)),
                COUNT_TITLE: str(tweet_chars),
                LONGEST_TITLE: longest_word,
            }

            # use textwrap function to print tweet data to console
            wrap_print(print_dict)

    print(f'''
    Total tweets: {total_tweets:>20}
    Total characters: {total_chars:>16}
    Character average/tweet: {total_chars/total_tweets:>9}
    ''')