from flask import Flask, request

app = Flask(__name__)


# サーバールートへアクセスがあった時 --- (*1)
@app.route('/')
def index():
    # フォームを表示する --- (*2)

    return """
        <html><body>
        <form action="/hello" method="GET">
          名前: <input type="text" name="name">
          <input type="text" name="hitokoto">
          <input type="submit" value="送信">
        </form>
        </body></html>
    """


# /hello へアクセスがあった時 --- (*3)
@app.route('/hello')
def hello():
    # nameのパラメータを得る --- (*4)
    name = request.args.get('name')
    hitokoto = request.args.get('hitokoto')
    if name is None: name = '名無し'
    # 自己紹介を自動作成
    return f"""
    <h1>{name}さん、こんにちは！</h1>
    <p>{hitokoto}</p>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0')
