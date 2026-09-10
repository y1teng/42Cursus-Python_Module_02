# Module 02 設計判断メモ（defense対策）

各演習で「他にどんな選択肢があったか」と「なぜそれを選んだか」を整理。
評価官に "why did you write it this way?" と聞かれたときの回答材料。

## ex0: ft_first_exception.py

- **例外の粒度**: `except Exception:` で何でも受けるか、`except ValueError:` で対象を絞るか
  → **ValueError を選択**。`int()`が失敗する原因は基本的にValueErrorなので、原因を具体的に絞れる。Tipにも「baseのExceptionでも良い」とあったが、より正確な方を選んだ。
- **エラーメッセージの出し方**: 自分で文言を作るか、例外オブジェクトが持つメッセージ(`{e}`)をそのまま使うか
  → **`{e}`をそのまま使用**。Pythonの`int()`が既に分かりやすいメッセージ("invalid literal for int() with base 10: 'abc'")を持っているので、それを再利用する方がシンプル。

## ex1: ft_raise_exception.py

- **範囲外エラーの型**: 自作のカスタム例外を作るか、`ValueError`を流用するか
  → **ValueErrorを流用**。ex0の「変換失敗」も「範囲外」もどちらも"入力値が不正"という同じ系統の問題なので、例外の種類を1つに統一した方が`except`側もシンプルになる。
- **上限/下限のチェック**: `if not (0 <= temp <= 40):` と1本化するか、上限用と下限用でif文を分けるか
  → **2つのifに分割**。「暑すぎ」と「寒すぎ」でメッセージを変えたかった（課題のExample出力がそれぞれ別文言だったため）。

## ex2: ft_different_errors.py

- **複数例外の捕まえ方**: `except (ValueError, ZeroDivisionError, ...) as e:` と1つのexceptでタプルにまとめるか、型ごとに`except`を分けるか
  → **型ごとに分割**。課題のTipで「`type()`は使えない」と制約があり、タプルでまとめると「今どの型が捕まったか」をメッセージに出すのに`type(e).__name__`が要る。型ごとに分ければ、各`except`ブロックにハードコードした文言で自然に表現できる。これが「1つのtryで複数型を捕まえる」の課題が求めていた形。
- **garden_operationsの構造**: 5パターンをif/elifで1関数にまとめるか、operation_numberごとに別関数にするか
  → **if/elifで1関数**。課題のシグネチャが`garden_operations(operation_number)`と明示されているので、それに従った。

## ex3: ft_custom_errors.py

- **デフォルトメッセージの実装**: 基底クラス(GardenError)だけ`__init__`を書いて、サブクラスは`pass`で継承に任せるか、サブクラスそれぞれに`__init__`を書くか
  → **サブクラスごとに書く**。`pass`だとサブクラス全部が基底クラスのデフォルトメッセージを継承してしまい、`WaterError()`でも"Unknown plant error"のような無関係な文言が出てしまうことを実際に検証して確認した。「クラスごとに固有のデフォルトメッセージ」という要件を満たすには、各クラスで上書きが必要。
- **メッセージの保持方法**: `self.message`を自前で持って`__str__`をオーバーライドするか、`super().__init__(message)`でExceptionの標準機構に乗せるか
  → **super().__init__(message)を選択**。Exceptionクラスが元々持っている仕組みに乗せることで、`str(e)`や`print(e)`が特別なコード無しでそのまま動く。車輪の再発明を避けた。

## ex4: ft_finally_block.py

- **テスト関数の設計**: `test_watering_system()`を引数なしにして内部に正常系/異常系を決め打ちで書くか、`plants: list[str]`を引数で受け取る形にするか
  → **引数で受け取る形**。正常系と異常系を呼び出し側(main)で管理でき、`test_watering_system`自体は「渡されたリストを順に水やりする」という1つの責務に絞れる。Exampleの出力も"Testing valid plants..."/"Testing invalid plants..."という2回の別ラベル付き呼び出しになっているので、この構造と自然に対応する。
- **エラー時の脱出方法**: フラグ変数でループを制御するか、`except`ブロックの中で`return`するか
  → **`return`を選択**。課題文が「stop the test and immediately return to main」と明記しており、`return`が最も素直にその要求を表現する。
- **finallyの実演方法**: 正常系だけでなく異常系でも同じ関数を呼び、両方で"Closing watering system"が出ることを対比させた
  → finallyが「エラーの有無に関係なく必ず実行される」ことを、1回の実行だけでなく2パターン見せることで実証している。
