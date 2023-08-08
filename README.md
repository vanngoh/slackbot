# slackbot

## Step 1: Set up the Python Virtual Environment

Initial the python `venv` with the following command:

```
$ python3 -m venv venv
```

## Step 2: Set up the required variables for Slack API

Get the following variables from Slack and set them as environment variables in `activate` script:

- SLACK_APP_CLIENT_ID
- SLACK_APP_CLIENT_SECRET
- SLACK_SIGNING_SECRET
- SLACK_APP_TOKEN

> [Pending] Add the variables into GitHub Action Secret for CI/CD to build the docker image

## Step 3: Activate the Python Virtual Environment

Activate the `venv`

```
$ . ./activate
(venv)$
```

## Step 4: Run the server

Last but not least, run the server with the following command:

```
(venv)$ python main.py
```
