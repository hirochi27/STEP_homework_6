# TSPの実装（貪欲法＆2-opt）
## ファイルについて

自身で実装したコード
* google-step-tsp/solver.py　:　貪欲法＆2-opt
* google-step-tsp/solver_2.py :　貪欲法＆2-opt＆2.5opt

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

## 前回からの発展
* 貪欲法と2-optを関数に分け、距離計算の関数も別で作り直しました
* 2-optの後に、更に2.5optを行っています
* 一度焼きなまし法も実装したのですが、貪欲法と2-optでかなり最適化できているようであまり変化がありませんでした。

## 現状（宿題２ができました）
***先週の TSP のプログラムを改善して、Challenge 6 のベストスコアを更新してください！***


* 2.5optを追加したことで、スコアが　43262.45　から　41576.26　に改善しました！！
```
Challenge 6
output          :   41576.26
sample/random   : 1374393.14
sample/sa       :   44393.89
```

* 貪欲法＆2-optの時間計算量がO(N³)で、更に2.5-optもO(N³)と大きい気がしています。もっと良い方法はあるでしょうか？
* 現在の2.5optは、最初に見つかった距離の短くなる改善を見つけたら、都市の入れ替えを行っています。全候補を調べて最大の結果を採用する方法にしたいのですが、このままだと遅くなりすぎる気がしています

## 宿題3について
***Challenge 7（都市数＝8192）のベストスコアを目指してください！！***

* 都市数2048の現状でだいぶ時間がかかっているので、もう少し早い方法を考えたいです！

 






