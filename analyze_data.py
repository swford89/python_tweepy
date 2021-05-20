import json
import textwrap
import string

# create textwrap function for cleanly printing tweets to console
def wrap_print(indented_title=str, preferred_width=int, print_text=str):
    text_wrapper = textwrap.TextWrapper(initial_indent=indented_title, width=preferred_width)
    print(text_wrapper.fill(print_text))
    return

# designate the path to the file you want to read from
tweet_path = 'twitter-data-master/data.json'

# read/load tweet data from json file
with open(tweet_path, 'r') as read_file:
    tweet_list = json.load(read_file)

    total_tweets = 0
    total_chars = 0

    # iterate through list of dictionaries containing data for individual tweets 
    for tweet in tweet_list:
        # count the tweets
        total_tweets += 1

        # parsing retweets
        if 'retweeted_status' in tweet.keys():
            retweet_title = '\nRetweet text: \n\n'
            og_title = '\nOriginal Tweet: \n\n'
            count_title = '\nCharacter count of retweet: '
            longest_title = 'Longest word: '
            word_list = tweet['full_text'].split()
            char_count = 0
            longest_word = ''
            longest_count = 0

            # get char count for tweet
            for word in word_list:
                char_count += len(word)
                if word.startswith('https') or word.startswith('@') or word.startswith('#'):    # ignore hashtags, handles
                    pass
                elif word[-1] in string.punctuation:                                            # remove end punctuation before printing longest word
                    word = word.replace(word[-1], '')                                           # then check word length
                    if len(word) > longest_count:
                        longest_count = len(word)
                        longest_word = word
                        total_chars += len(word)
                else:
                    if len(word) > longest_count:
                        longest_count = len(word)
                        longest_word = word
                        total_chars += len(word)

            # use textwrap function to print tweet data to console
            wrap_print(indented_title=retweet_title, preferred_width=80, print_text=tweet['full_text'])
            wrap_print(indented_title=og_title, preferred_width=80, print_text=tweet['retweeted_status']['full_text'])
            wrap_print(indented_title=count_title, preferred_width=80, print_text=str(char_count))
            wrap_print(indented_title=longest_title, preferred_width=80, print_text=longest_word)

        # parsing normal tweets
        else:
            full_text_title = '\nTweet text: \n\n'
            char_title = '\nCharacter count of tweet: '
            longest_title = 'Longest word: '
            word_list = tweet['full_text'].split()
            char_count = 0
            longest_count = 0
            longest_word = ''

            # get char count
            for word in word_list:
                char_count += len(word)
                if word.startswith('https') or word.startswith('@') or word.startswith('#'):    # ignore hashtages, handles
                    pass
                elif word[-1] in string.punctuation:                                            
                    word = word.replace(word[-1], '')                                           # remove end punctuation
                    if len(word) > longest_count:                                               # then check word length
                        longest_count = len(word)
                        longest_word = word
                        total_chars += len(word)
                else:
                    if len(word) > longest_count:
                        longest_count = len(word)
                        longest_word = word 
                        total_chars += len(word)           

            wrap_print(indented_title=full_text_title, preferred_width=80, print_text=tweet['full_text'])
            wrap_print(indented_title=char_title, preferred_width=80, print_text=str(char_count))
            wrap_print(indented_title=longest_title, preferred_width=80, print_text=longest_word)

    print(f'''
    Total tweets: {total_tweets:>20}
    Total characters: {total_chars:>16}
    Character average per tweet: {total_chars/total_tweets:>7}
    ''')