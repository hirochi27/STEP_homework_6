# TSPの実装（貪欲法＆2-opt＆2.5-opt）
## ファイルについて

自身で実装したコード
* google-step-tsp/solver.py　:　貪欲法＆2-opt
* google-step-tsp/solver_2.py :　貪欲法＆2-opt＆2.5opt
* google-step-tsp/run_random_start_input6.py :　スタート位置をランダムに変更してひたすら貪欲法＆2-opt＆2.5optを回すコード　

その他、```https://github.com/hayatoito/google-step-tsp```よりcloneしたコード
* google-step-tsp/input_{0~6}.csv : 都市の座標、solver.pyに渡す値
* google-step-tsp/output_{0~6}.csv　: inputを受け取ったsolver.pyの実行結果


## 実行方法
実行結果をoutput_{0~6}.csvに保存
```
python3 solver.py input_0.csv > output_0.csv
```

ビジュアライザーの起動
```
python3 -m http.server 8000
```

URL
```
http://localhost:8000/visualizer/build/default/
```

## solver_2.pyについて
* 貪欲法と2-optを行った後に、2.5-optを更に行い最適化
* input_7に向けて、できる限り計算量を減らすため、それぞれのヒューリスティクスでは近くの20ノードのみを探索している。

## 宿題2
***先週の TSP のプログラムを改善して、Challenge 6 のベストスコアを更新してください！***

**40700.49**

~~* 2.5optを追加したことで、スコアが　43262.45　から　41576.26　に改善しました！！~~
* スタート位置を変更して、ひたすら試したところ40700.49まで改善しました！！


* 貪欲法＆2-optの時間計算量がO(N³)で、更に2.5-optもO(N³)と大きい気がしています。もっと良い方法はあるでしょうか？
* 現在の2.5optは、最初に見つかった距離の短くなる改善を見つけたら、都市の入れ替えを行っています。全候補を調べて最大の結果を採用する方法にしたいのですが、このままだと遅くなりすぎる気がしています

## 宿題3
***Challenge 7（都市数＝8192）のベストスコアを目指してください！！***

**82135.64**

* input_6同様、スタート位置をランダムにして最短距離を見つけたかったが、時間がなかったため未実装
* いろいろ高速化を試したら20分くらいで一周終わるようになりました
  
* 訪問リストの改善(listにappend/popする形から、都市数分のTrue/Falseで管理する形に変更)
* `neighbor list`の実装（一番最初に、任意の都市に近い都市＊20をリストに保存。貪欲法やoptはこのリスト内の値だけを使用）


## ランダムスタートについて（run_random_start_input6.py）

`run_random_start_input6.py` で、スタート都市をランダムに変更しながら `solver_2.py` を繰り返し実行

各試行の結果は `random_start_input6_log.csv` に保存され、最も距離が短かった経路は `best_output_6.csv` と `output_6.csv` に保存されます

 






