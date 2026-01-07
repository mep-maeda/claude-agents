# spec-doc-generator エージェント用改善プロンプト

このプロンプトは、変更仕様書（SPEC_CHANGES.html）の生成品質を向上させるためのガイドラインです。

## 基本原則

### 1. 事実ベースの記述
- **避けるべき表現**: 「ハイブリッド方式」「革新的」「効率的」などの抽象的・評価的な表現
- **推奨する表現**: 具体的な処理内容、データフロー、計算式を事実として記述
- 例:
  - ❌ 「ハイブリッド方式で高精度な予測を実現」
  - ✅ 「INI設定値から初期予測時間を算出し、Car完了ごとに実測値で再計算」

### 2. 修正前／修正後の対比形式
- 必ず「修正前」と「修正後」の2カラム構成で記載
- 修正前は既存の動作を簡潔に記述
- 修正後は変更内容を<span class="highlight">ハイライト</span>で強調
- 番号付きの階層構造（1)、a)、i)など）を使用

### 3. 詳細度のバランス
- 各項目は具体的かつ簡潔に記述
- コード例、INI設定例、計算式などを含める
- 実装の「何を」「どのように」を明確に記述
- 「なぜ」は背景・目的セクションで記述

## HTML構造のベストプラクティス

### テーブル構造

```html
<table>
<tr>
<td colspan="2" class="change-title">No.X 機能名</td>
</tr>
<tr>
<td class="label-cell">変更点管理番号</td>
<td>No. YYYY-XXX</td>
</tr>
<tr>
<td class="label-cell">ソース・ファイル名</td>
<td>
・ファイル1<br>
・ファイル2<br>
・ファイル3
</td>
</tr>
<tr>
<td class="label-cell">修正内容</td>
<td>
<strong>【背景・目的】</strong><br>
現状の課題を記述<br><br>

<strong>【変更概要】</strong><br>
変更内容の概要を1-2段落で記述
</td>
</tr>
<tr>
<td class="section-header two-column">修正前</td>
<td class="section-header two-column">修正後</td>
</tr>

<!-- 修正内容の詳細 -->
<tr>
<td class="two-column">
<strong>1. 項目名</strong><br>
1) 既存の動作<br>
2) 既存の処理<br>
</td>
<td class="two-column">
<strong>1. 項目名</strong><br>
1) 既存の動作（変更なし）<br>
2) <span class="highlight">新しい処理</span><br>
3) <span class="highlight">追加された処理</span><br>
&nbsp;&nbsp;a) <span class="highlight">詳細1</span><br>
&nbsp;&nbsp;b) <span class="highlight">詳細2</span><br>
</td>
</tr>

<!-- 補足事項は最後の行に統合 -->
<tr>
<td class="two-column">
<strong>補足事項</strong><br>
－
</td>
<td class="two-column">
<strong>補足事項</strong><br>
<br>
<strong>【後方互換性】</strong><br>
・項目1<br>
・項目2<br>
<br>
<strong>【制約事項】</strong><br>
・項目1<br>
・項目2<br>
<br>
<strong>【注意事項】</strong><br>
・項目1<br>
・項目2<br>
<br>
<strong>【計算ロジック・アルゴリズム】</strong><br>
<span class="highlight">◆ケース1</span><br>
&nbsp;&nbsp;・処理内容<br>
&nbsp;&nbsp;・計算式<br>
<br>
<span class="highlight">◆ケース2</span><br>
&nbsp;&nbsp;・処理内容<br>
&nbsp;&nbsp;・計算式<br>
</td>
</tr>
</table>
```

## 記載すべき項目の構成

### 修正前／修正後の表に含める項目例

1. **処理フロー・動作**
   - ダウンロード処理の流れ
   - データ更新のタイミング
   - UI表示の更新

2. **設定ファイル構成**
   - INIファイルのセクション構造
   - 具体的なキー名と値の例
   - データ型と単位

3. **データ構造**
   - クラス・構造体の定義
   - プロパティ・フィールドの一覧
   - 新規追加の項目を明記

4. **通知・イベント処理**
   - メッセージの種類
   - イベントのトリガー条件
   - 通知のタイミング

5. **リソース管理**
   - 初期化処理
   - 解放処理
   - タイマーやスレッドの管理

6. **補足事項（必ず最後の行に統合）**
   - 後方互換性
   - 制約事項
   - 注意事項
   - 計算ロジック・アルゴリズム詳細

### 補足事項の記載ガイドライン

**【後方互換性】**
- 既存機能への影響なし、を明記
- フォールバック処理の説明
- 既存データ・設定ファイルの扱い

**【制約事項】**
- 精度・性能の限界
- 環境依存の条件
- 最小値・最大値などの制約

**【注意事項】**
- デプロイ時の手順
- 設定値の調整が必要な項目
- 命名規則・データ形式の制約

**【計算ロジック・アルゴリズム】**
- ケースごとに「◆」で分類
- 計算式を明記
- 条件分岐を明確に記述

## ハイライトの使用方法

### ハイライトを使用すべき箇所
- 新規追加された処理・機能
- 変更された処理・設定
- 重要な計算式・条件
- 注意が必要な項目

### ハイライトを使用しない箇所
- 修正前の既存処理
- 変更のない項目
- 説明文の一般的な記述

```html
<!-- 良い例 -->
<span class="highlight">残り時間 = 実測時間 × 残りcar数</span>

<!-- 悪い例（不要なハイライト） -->
<span class="highlight">ダウンロード処理を実行します</span>
```

## インデント・階層の使い方

```html
<!-- 2階層の例 -->
1) <span class="highlight">メイン処理</span><br>
&nbsp;&nbsp;a) <span class="highlight">サブ処理1</span><br>
&nbsp;&nbsp;b) <span class="highlight">サブ処理2</span><br>

<!-- 3階層の例 -->
1) <span class="highlight">メイン処理</span><br>
&nbsp;&nbsp;a) <span class="highlight">サブ処理1</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;i) <span class="highlight">詳細処理1</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;ii) <span class="highlight">詳細処理2</span><br>
```

## 具体例の記載方法

### INI設定の記載例

```html
<strong>3. 設定ファイル構成</strong><br>
1) MDS_PTE.ini [Timer]セクション（既存維持）<br>
2) <span class="highlight">MDS_PTE.ini [EstimatedDownloadTime]セクション</span><br>
&nbsp;&nbsp;a) <span class="highlight">EventLog=25000（1car当たりミリ秒）</span><br>
&nbsp;&nbsp;b) <span class="highlight">RTDM=60000</span><br>
&nbsp;&nbsp;c) <span class="highlight">Diagnostic=180000</span><br>
&nbsp;&nbsp;d) <span class="highlight">DATA_KIND列挙体のメンバ名をキーとして定義</span><br>
```

### 計算式の記載例

```html
<strong>【残り時間計算ロジック】</strong><br>
<span class="highlight">◆ダウンロード開始時</span><br>
&nbsp;&nbsp;・INIファイルから1car当たりの予測時間を読み込み<br>
&nbsp;&nbsp;・残り時間 = 総car数 × 1car当たり予測時間<br>
&nbsp;&nbsp;・最小値は1分<br>
<br>
<span class="highlight">◆1両目完了時</span><br>
&nbsp;&nbsp;・実測ダウンロード時間を記録<br>
&nbsp;&nbsp;・残り時間 = 実測時間 × 残りcar数<br>
```

### データ構造の記載例

```html
<strong>7. データ構造</strong><br>
1) ProgressInfoクラス<br>
&nbsp;&nbsp;a) Message（進捗メッセージ）<br>
&nbsp;&nbsp;b) Current、Total（進捗カウント）<br>
&nbsp;&nbsp;c) <span class="highlight">CarTimeInfo（car完了時の時間情報）</span><br>
2) <span class="highlight">CarDownloadTimeInfoクラス（新規）</span><br>
&nbsp;&nbsp;a) <span class="highlight">Request（リクエスト情報）</span><br>
&nbsp;&nbsp;b) <span class="highlight">StartTime（開始時刻）</span><br>
&nbsp;&nbsp;c) <span class="highlight">EndTime（終了時刻）</span><br>
&nbsp;&nbsp;d) <span class="highlight">ElapsedTime（経過時間）</span><br>
```

## 避けるべき記述

### ❌ 抽象的な表現
- 「高度な技術を使用」
- 「最適化された処理」
- 「ハイブリッドアプローチ」
- 「革新的な実装」

### ❌ 曖昧な表現
- 「適切に処理」
- 「必要に応じて」
- 「場合によっては」

### ❌ 技術的すぎる詳細
- ソースコードの行番号への過度な言及
- 実装の細かすぎる技術詳細
- 内部変数名の詳細な説明

## 推奨する記述

### ✅ 具体的な動作
- 「1car完了ごとに実測時間を記録」
- 「残り時間 = 平均時間 × 残りcar数」
- 「[EstimatedDownloadTime]セクションから読み込み」

### ✅ 明確な条件
- 「1car当たり時間が1分以上の場合」
- 「全car完了時」
- 「CarTimeInfo情報が提供されない場合」

### ✅ ビジネスレベルの説明
- 「ユーザーに正確な残り時間を表示」
- 「ダウンロード進捗に応じて予測時間を更新」
- 「既存のダウンロード機能への影響なし」

## チェックリスト

変更仕様書を生成する際は、以下をチェックしてください：

- [ ] 修正前／修正後の2カラム構成になっているか
- [ ] 変更箇所がハイライトで強調されているか
- [ ] 具体的な設定例・計算式が記載されているか
- [ ] 補足事項が修正前／修正後の表の最後の行に統合されているか
- [ ] 補足事項が4つのカテゴリ（後方互換性、制約事項、注意事項、計算ロジック）に分類されているか
- [ ] 抽象的・評価的な表現を避け、事実ベースで記述されているか
- [ ] 階層構造（番号付きリスト）が適切に使用されているか
- [ ] インデント（&nbsp;&nbsp;）が適切に使用されているか
- [ ] データ構造、設定ファイル、処理フローが具体的に記載されているか
- [ ] 後方互換性への配慮が明記されているか

## エージェントへの指示例

spec-doc-generatorエージェントを呼び出す際は、以下のように指示してください：

```
変更仕様書（SPEC_CHANGES.html）を生成してください。

以下のガイドラインに従って記述してください：
1. 事実ベースで記述し、「ハイブリッド」などの抽象的表現は避ける
2. 修正前／修正後の2カラム構成で対比を明確にする
3. 変更箇所は<span class="highlight">でハイライト
4. 補足事項は修正前／修正後の表の最後の行に統合
5. 補足事項は【後方互換性】【制約事項】【注意事項】【計算ロジック】の4カテゴリに分類
6. 具体的な設定例、計算式、データ構造を記載
7. 階層構造とインデントを適切に使用

変更内容：
[実装内容の詳細を記載]
```

## 参考：良い変更仕様書の例

D:\Home\MCR\R211\.agent-context\SPEC_CHANGES.html を参照してください。
この変更仕様書は、上記ガイドラインに沿って作成された良い例です。


## フローチャート生成ルール

### 基本方針
変更仕様書（SPEC_CHANGES.html）と一緒に、フローチャート（.drawio形式）を必ず生成してください。

### ファイル命名規則
```
flowchart_No{変更点番号}.drawio
```
例: flowchart_No143.drawio

### 必須要素

#### 1. レイアウト構成
```
+------------------+------------------+
|     修正前       |     修正後       |
+------------------+------------------+
| 既存のフロー     | 変更後のフロー   |
| (通常色)         | (変更箇所黄色)   |
+------------------+------------------+
```

#### 2. 図形要素の種類と色

**プロセス（処理）**
- 図形: 角丸矩形
- 画面処理: 緑色 (#d5e8d4)
- システム処理: 青色 (#dae8fc)
- 変更された処理: 黄色 (#fff2cc)

**判定（分岐）**
- 図形: ひし形
- 色: 白色 (#ffffff)

**接続線**
- 通常: 黒色実線
- 削除された箇所: グレー点線

#### 3. 修正前と修正後の対比ルール

**修正前（左側）**
- 既存のフローをそのまま描く
- すべて通常色

**修正後（右側）**
- 変更なし: 通常色
- 追加された処理: 黄色背景 (#fff2cc)
- 変更された処理: 黄色背景 (#fff2cc)
- 削除された処理: グレー点線枠（表示するが目立たなくする）

### draw.io XMLテンプレート

フローチャートは以下のdraw.io XML形式で生成してください：
```xml
<mxfile host="app.diagrams.net">
  <diagram name="修正前後フロー比較">
    <mxGraphModel dx="1422" dy="794">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        
        <!-- 左側：修正前 -->
        <mxCell id="title_before" value="修正前" 
                style="text;fontSize=16;fontStyle=1" 
                vertex="1" parent="1">
          <mxGeometry x="50" y="20" width="100" height="30" as="geometry"/>
        </mxCell>
        
        <!-- 右側：修正後 -->
        <mxCell id="title_after" value="修正後" 
                style="text;fontSize=16;fontStyle=1" 
                vertex="1" parent="1">
          <mxGeometry x="450" y="20" width="100" height="30" as="geometry"/>
        </mxCell>
        
        <!-- 以下、実際のフロー要素 -->
        <!-- プロセスの例 -->
        <mxCell id="process1" value="画面表示処理&#xa;ShowForm()" 
                style="rounded=1;whiteSpace=wrap;fillColor=#d5e8d4;strokeColor=#82b366;" 
                vertex="1" parent="1">
          <mxGeometry x="50" y="80" width="150" height="60" as="geometry"/>
        </mxCell>
        
        <!-- 変更箇所（黄色ハイライト） -->
        <mxCell id="process2_changed" value="イベントハンドラ解放&#xa;-= EventHandler" 
                style="rounded=1;whiteSpace=wrap;fillColor=#fff2cc;strokeColor=#d6b656;" 
                vertex="1" parent="1">
          <mxGeometry x="450" y="200" width="180" height="60" as="geometry"/>
        </mxCell>
        
        <!-- 判定の例 -->
        <mxCell id="decision1" value="Online?" 
                style="rhombus;whiteSpace=wrap;fillColor=#ffffff;strokeColor=#000000;" 
                vertex="1" parent="1">
          <mxGeometry x="450" y="300" width="120" height="80" as="geometry"/>
        </mxCell>
        
        <!-- 接続線の例 -->
        <mxCell id="arrow1" value="" 
                style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;" 
                edge="1" parent="1" source="process1" target="decision1">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

### フローチャート生成の具体例

**例: イベントハンドラ解放の変更**

修正前:
```
[画面を開く] → [イベント登録] → [処理] → [画面を閉じる]
```

修正後:
```
[画面を開く] → [イベント登録] → [処理] → [★イベント解放★] → [画面を閉じる]
```
★マークの部分を黄色でハイライト

### PDFサンプルとの対応

添付されたPDFサンプル（変更仕様書サンプル.pdf）のNo.143, 2ページ目のフローチャートを参考にしてください。

- 左側: 修正前のフロー
- 右側: 修正後のフロー（変更箇所が黄色）
- 点線: イベント呼び出し
- 黄色の箱: 追加/変更された処理

### チェックリスト

フローチャートを生成する際、以下を確認してください：

- [ ] ファイル名が flowchart_No{番号}.drawio になっているか
- [ ] 修正前と修正後が左右に並んでいるか
- [ ] 変更箇所が黄色でハイライトされているか
- [ ] 画面処理は緑色、システム処理は青色になっているか
- [ ] 判定はひし形になっているか
- [ ] 接続線が適切に引かれているか
- [ ] draw.io XML形式になっているか

### SPEC_CHANGES.htmlからのリンク

SPEC_CHANGES.htmlの中で、フローチャートへのリンクを以下のように記載してください：
```html
<tr>
<td class="label-cell">フローチャート</td>
<td>
<a href="flowchart_No{変更点番号}.drawio">フローチャート参照</a><br>
※draw.ioで開いて確認してください
</td>
</tr>
```

