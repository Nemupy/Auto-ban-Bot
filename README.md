# Auto-ban-Bot
[![Library-discord.py](https://img.shields.io/badge/Python-3.8.0-3778ae?logo=Python&logoColor=ffffff)](https://python.org) 
[![Main Library-discord.py](https://img.shields.io/badge/Main%20Library-discord.py-fecc34?logo=pypi&logoColor=ffffff)](https://github.com/Rapptz/discord.py) 
[![Support](https://img.shields.io/discord/715540925081714788?color=5865f2&label=Discord&logo=Discord&logoColor=ffffff)](https://discord.gg/5fHDJwVhWb)  

# Overview
設定したユーザーを自動でBANするBotのソースコード。セルフホスト専用です。

# Usage
専門用語を多く含みます。またBotを作ったことのある経験がないと非常に分かりづらい説明となっております。  
ご不明な点がございましたら気軽にissuesまたはDiscordにご連絡ください。

Discord https://discord.gg/5fHDJwVhWb
<details> 
  <summary>ネット上でホストする方法（一般向け）</summary>  
  
  ## はじめに
  Railwayという無料で使えるホスティングサービスを使います。  
  下記のリンクからRailwayにアクセスし、アカウント登録を行ってください。  
  
  Discord開発者ポータルからBotのアカウントを作成してください。  
  また、作成したアカウントのtokenを取得してください。  
  参考になる記事を書いておくので分からない方は読んでください。  
  
  Railway https://railway.app/  
  Discord開発者ポータル https://discord.com/developers/applications  
  参考記事 https://discordpy.readthedocs.io/ja/latest/discord.html
  
  ## Githubの準備
  右上のForkボタンからこのリポジトリをフォークしてください。  
  フォークが完了したらそのリポジトリを開いてください。  
  
  config.jsonを開いてください。  
  usersの値に該当するユーザーのIDを入れると自動BANが実行されます。  
  既存の000000000000000000を該当するユーザーのIDに置き換えてください。
  
  ## Railwayの準備
  新規プロジェクトを作成し先ほどフォークしたリポジトリをデプロイします。  
  そして環境変数設定画面で新しくtokenという変数を作り、それの値に先ほど取得したtokenを入力してください。  
  かなりややこしいので他の方の書いた記事を参考にしてください。  
  参考記事 https://zenn.dev/mnonamer/articles/f73386390399f6
  
</details>
<details>
  <summary>パソコンでホストする方法（開発者向け）</summary>
  
  ## 前提
  お使いのパソコンにPython3が入っていることを確認してください。  
  3.8以上である必要があります。  
  
  また、このソースコードをダウンロードしてください。
  
  ## 自動BANをするユーザーの設定
  config.jsonを開いてください。  
  usersの値に該当するユーザーのIDを入れると自動BANが実行されます。  
  既存の000000000000000000を該当するユーザーのIDに置き換えてください。
  
  ## tokenの設定
  Discordの開発者ポータルからBotを作成し、tokenを取得してください。  
  dbot.pyにある変数token、または環境変数tokenの値に取得したtokenを入れてください。
  
  ## 実行
  dbot.pyを実行してください。
  
</details>

# Requirement
・Python    
・discord.py

# Licence
Botを公開し再配布する場合は著作元を明確にしてください。個人利用の場合は大丈夫です。  
MITライセンスで公開しています。詳しくはLICENCEファイルを確認してください。
