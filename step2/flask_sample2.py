from flask import Flask  # Flaskクラスから、module flaskをimportしている。
app = Flask(__name__, static_folder=".", static_url_path="") 
#変数appに、Flaskクラスのインスタンスを作成し、代入しています。
#__name__は現在のスクリプトの名前を示します。
#static_folder="."は静的ファイル(CSSや、JavaScriptファイルなど)を格納するフォルダを指定しており、ここではカレントディレクトリを指定しています。
#static_url_pathは、静的ファイルにアクセスするためのURLパスを指定しており、ここではルートディレクトリを指定しています。
@app.route("/")  #このデコレータは、指定されたURL（ここではルートURL/）にアクセスがあった際に、直後の関数を実行するようFlaskに指示します。
def index():
    return app.send_static_file("index.html")

@app.route("/hello/<name>")
def hello(name):
    return name

app.run(port=8000, debug=True)