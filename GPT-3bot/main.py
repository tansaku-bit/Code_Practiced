import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# botTokenとSocketModeHandlerを使ってアプリを初期化します
app = App(token=os.environ.get(""))