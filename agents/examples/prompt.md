# プロンプトテンプレート

以下をコピーして使用してください。

```markdown
以下の仕様変更を実施してください。

## 変更要求

【何を、どのように変更するか具体的に記述】
【変更の目的や背景があれば記載】
【条件や制約があれば記載】

## ソースコードの場所

- プロジェクト: 【プロジェクトのルートパス】
- 対象ファイル:
  - 【ファイルパス】（関数名: XXX、行番号: XXX〜XXX）
  - 【ファイルパス】

## 参照仕様書

- ./Docs/に配置、またはフルパスで指定
- 【ファイルパス】（参照項番: X.X.X）
- なし（参照仕様書がない場合）
  ※PDF可（推奨: 30ページ以内）、大きい場合はMarkdown化推奨
  ※項番指定がある場合、その項番を重点的に参照
  ※なしの場合は、「なし」と記載しておく

## 変更点管理番号

- No. 【番号】（例: No. 43）
  ※この番号で出力フォルダを作成し、フローチャートのファイル名にも使用

## 出力ファイルの保存場所

- 出力先: ./Output/【番号3桁フォーマット】/（例: ./Output/043/）
  ※変更点管理番号でフォルダを作成
  ※分析結果（analysis-result.json、analysis-summary.md）と変更仕様書（SPEC_CHANGES.html等）の両方をこのフォルダに出力
  ※別の場所に出力する場合はフルパスで記載

## 実施手順

以下の手順で作業を進めてください。各承認ポイントで必ず私の承認を得てから次に進んでください。

### 1. 影響範囲分析（spec-analyzer使用）
- spec-analyzerエージェントを起動
- コードベース全体への影響を分析
- **【承認ポイント1】** 分析結果を提示し、承認を待つ

### 2. 変更仕様書とフローチャート生成（spec-doc-generator使用）
- spec-doc-generatorエージェントを起動
- 以下のファイルを生成：
  - SPEC_CHANGES.html（変更仕様書）
  - flowchart_No{番号}.drawio（フローチャート）
  - TEST_SPECIFICATION.html（テスト仕様書）
- **【承認ポイント2】** 変更仕様書、フローチャート、テスト仕様書を提示し、承認を待つ

### 3. ソースコード修正の確認
- **【承認ポイント3】** ユーザーにソースコード修正を実施するか確認
  - 「ソースコードの修正を実施しますか？（はい/いいえ）」と質問
  - 「いいえ」の場合 → 作業完了
  - 「はい」の場合 → 手順4へ進む

### 4. ソースコード修正の実施（承認時のみ）
- 分析結果と変更仕様書に基づいてソースコードを修正
- 修正完了後、以下のファイルを生成：
  - SOURCE_DIFF.html（ソース変更差分レポート）
    - WinMerge風の差分表示形式
    - 変更箇所は黄色マーカーでハイライト
    - 削除行は赤背景、追加行は緑背景
    - ファイル単位で変更前/変更後を並べて表示
- **【承認ポイント4】** 差分レポートを提示し、修正内容の最終確認を行う

## 差分レポート（SOURCE_DIFF.html）の形式

差分レポートは以下の形式で出力してください：

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>ソース変更差分レポート - No.{番号}</title>
  <style>
    .diff-container { font-family: 'Consolas', monospace; margin: 20px; }
    .file-header { background: #333; color: #fff; padding: 10px; font-weight: bold; }
    .diff-table { width: 100%; border-collapse: collapse; }
    .line-num { width: 50px; background: #f0f0f0; text-align: right; padding: 2px 8px; color: #666; }
    .line-content { padding: 2px 8px; white-space: pre-wrap; }
    .unchanged { background: #fff; }
    .modified { background: #ffff99; }  /* 黄色マーカー：変更箇所 */
    .deleted { background: #ffdddd; }   /* 赤背景：削除行 */
    .added { background: #ddffdd; }     /* 緑背景：追加行 */
    .old-side { border-right: 2px solid #ccc; }
    .section-title { background: #e0e0e0; padding: 8px; font-weight: bold; margin-top: 20px; }
  </style>
</head>
<body>
  <h1>ソース変更差分レポート</h1>
  <p>変更点管理番号: No.{番号}</p>
  <p>生成日時: {日時}</p>
  <!-- ファイルごとの差分を表示 -->
</body>
</html>
```

## 注意事項

- 各承認ポイントで必ず作業を止め、私の指示を待ってください
- 不明点や懸念事項があれば、すぐに質問してください
- ソースコード修正は承認がある場合のみ実施します
- 修正後は必ず差分レポートで変更内容を確認できるようにします

それでは、作業を開始してください。
```
