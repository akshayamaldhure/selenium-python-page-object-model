import argparse

from slackclient import SlackClient

cli = argparse.ArgumentParser()
cli.add_argument('-t',
                 '--slacktoken',
                 type=str)
cli.add_argument('-c',
                 '--channel',
                 type=str)
cli.add_argument('-m',
                 '--message',
                 type=str)
args = cli.parse_args()
slack_token = args.slacktoken
slack_channel = args.channel
message = args.message
sc = SlackClient(slack_token)
sc.api_call("chat.postMessage", channel=slack_channel, text=message)
