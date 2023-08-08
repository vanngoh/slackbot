import os
# import openai
from slack_bolt import App
from slack_bolt.oauth.oauth_settings import OAuthSettings
from slack_sdk.oauth.installation_store import FileInstallationStore
from slack_sdk.oauth.state_store import FileOAuthStateStore
from slack_bolt.adapter.socket_mode import SocketModeHandler
import server

oauth_settings = OAuthSettings(
    client_id=os.environ.get("SLACK_APP_CLIENT_ID"),
    client_secret=os.environ.get("SLACK_APP_CLIENT_SECRET"),
    scopes=[
        "channels:read",
        "groups:read",
        "chat:write",
    ],
    user_scopes=["chat:write"],
    installation_store=FileInstallationStore(base_dir="./data/installations"),
    state_store=FileOAuthStateStore(expiration_seconds=600, base_dir="./data/states"),
)

# app = App(token=os.environ.get("SLACK_BOT_TOKEN"),
#           signing_secret=os.environ.get("SLACK_SIGNING_SECRET"))
app = App(signing_secret=os.environ.get("SLACK_SIGNING_SECRET"), oauth_settings=oauth_settings)


@app.command("/en")
def translate_to_en(ack, say, command):
    ack()
    try:
        # #Implementation of DeepL version
        pass
        # #Implementation of OpenAI version
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     temperature=0.3,
        #     messages=[{
        #         "role":
        #         "user",
        #         "content":
        #         f"Translate the following into English: {command['text']}"
        #     }])
        # say(text=
        #     f"{command['text']}{response['choices'][0]['message']['content']}",
        #     as_user=True)
    except Exception as e:
        print(f"Error sending message: {e}")
        say(f"Failed to send message. Error: {str(e)}")


@app.command("/jp")
def translate_to_jp(ack, say, command):
    ack()
    print(command)
    try:
        # #Implementation of DeepL version
        pass
        # #Implementation of OpenAI version
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     temperature=0.3,
        #     messages=[{
        #         "role":
        #         "user",
        #         "content":
        #         f"Translate the following into Japanese: {command['text']}"
        #     }])
        # say(text=
        #     f"{command['text']}{response['choices'][0]['message']['content']}",
        #     as_user=True)
    except Exception as e:
        print(f"Error sending message: {e}")
        say(f"Failed to send message. Error: {str(e)}")


@app.event("message")
def handle_message_events(body, logger):
    pass


@app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


if __name__ == "__main__":
    server.run_background()
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
