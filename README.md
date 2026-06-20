# TSPの実装（貪欲法＆2-opt）
## ファイルについて

自身で実装したコード
* google-steo-tsp/solver.py　:　貪欲法＆2-opt

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

## 現状

* 貪欲法も2-optも大分うまく動いているのですが、たまに道同士がクロスしてしまいます。
* 時間計算量がO(N³)と少し大きいので、もう少し良いやり方があるのではと思っています。

<img width="937" height="484" alt="image" src="https://github.com/user-attachments/assets/c69d9428-0dfc-4934-8807-3c644c172d48" />




