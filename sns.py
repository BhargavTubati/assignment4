import boto3
import json
import configparser
import os

# Read configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Get topic name, email addresses from config
topic_name = config.get('sns', 'topic_name')
email1 = config.get('sns', 'email1')
email2 = config.get('sns', 'email2')

# Create SNS client
sns = boto3.client('sns')

# Create topic
response = sns.create_topic(Name=topic_name)

# Get topic ARN
topic_arn = response['TopicArn']

# Add email addresses as subscribers
sns.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=email1)
sns.subscribe(TopicArn=topic_arn, Protocol='email', Endpoint=email2)

os.system('git init')
print('Git repository created')

remote_repo_url = 'https://github.com/yourusername/your-repo.git'  # Replace with your actual repository URL
os.system(f'git remote add origin {remote_repo_url}')
os.system('git push -u origin master')
print(f'Git repository {remote_repo_url} shared successfully')