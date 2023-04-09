# インターンDay1

## Ruby 及び Ruby on Railsの学習

### Ruby と Ruby on Railsとは
Rubyはまつもとゆきひろ氏によって開発された言語で、日本で開発された言語として世界規格に認証された最初の事例である。<br>
RubyはPythonの登場から4年後に公開され、オブジェクト指向を導入したインタプリタ型言語であるなど一致する点も多い。普及率ではPythonに大きく劣るが、その理由としては言語仕様の明文化が長らく行われなかったことが挙げられる。<br>
RubyはRuby on Railsの登場によりWebアプリケーション開発の言語選択において高い地位を獲得した。Railsは現在でもスタートアップ企業などを中心に利用率が高く、サーバーサイドの言語としてはPython以上の働きをしている。

### Ruby on Railsによるアプリケーション作成
[Rubyの公式サイト](https://ruby-lang.org/ja/)からRubyをダウンロードし、``gem``を利用できるようにする。``gem``はRubyにおけるパッケージ管理用のコマンドであり、Pythonでの``pip``や``conda``に相当する。<br>
Ruby on Railsのインストールと同時に``bundler``というバージョン依存の管理パッケージもインストールする。これにより、依存関係のあるgemを一括でダウンロードしてくることができる。<br>
```gem install rails bundler```でRuby on Railsとbundlerをダウンロードする。<br>
Unix(Linux)のShellでenvironmentディレクトリを作成し、``rails new <appname> -o -skip--bundle``でRailsで開発するWebアプロケーションの土台を作成します。
