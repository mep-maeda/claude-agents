# クイックスタートガイド

最短5分で仕様変更支援エージェントを使い始めるためのガイドです。

## 📝 目次

- [前提条件](#前提条件)
- [Step 1: プロンプトテンプレートをコピー](#step-1-プロンプトテンプレートをコピー)
- [Step 2: 変更内容を記入](#step-2-変更内容を記入)
- [Step 3: 実行](#step-3-実行)
- [Step 4: 承認ポイントで確認](#step-4-承認ポイントで確認)
- [完了！](#完了)
- [次のステップ](#次のステップ)

---

## 前提条件

✅ Claude Code CLI がインストール済み
✅ C#/.NETプロジェクトが存在する
✅ `.claude/agents/` フォルダにエージェントファイルが配置済み

確認方法：
```bash
cd your-project
ls -la .claude/agents/
# spec-analyzer.md と spec-doc-generator.md が表示されればOK
```

---

## Step 1: プロンプトテンプレートをコピー

以下のテンプレートをコピーしてください：

```markdown
以下の仕様変更を実施してください。

## 変更要求

【ここに変更内容を記述】

## ソースコードの場所

【プロジェクトとファイルのパスを記載】

## 出力ファイルの保存場所

【生成されるドキュメントの保存先】

## 実施手順

以下の手順で作業を進めてください。各承認ポイントで必ず私の承認を得てから次に進んでください。

### 1. 事前準備
- TodoListを作成し、全体の作業項目を管理
- 各タスクの完了時にTodoを更新

### 2. 影響範囲分析（spec-analyzer使用）
- spec-analyzerエージェントを起動
- コードベース全体への影響を分析
- 以下のファイルを生成：
  - analysis-result.json
  - analysis-summary.md
- **【承認ポイント1】** 分析結果を提示し、承認を待つ

### 3. 実装計画の作成
- 分析結果に基づいて詳細な実装計画を作成
- 優先順位、リスク、工数見積もりを含める
- **【承認ポイント2】** 実装計画を提示し、承認を待つ

### 4. 変更仕様書とフローチャート生成（spec-doc-generator使用）
- spec-doc-generatorエージェントを起動
- 分析結果（analysis-result.json）を参照
- 以下のファイルを生成：
  - SPEC_CHANGES.html（変更仕様書）
  - flowchart_No{番号}.drawio（フローチャート）
- **【承認ポイント3】** 変更仕様書とフローチャートを提示し、承認を待つ

### 5. ソースコード変更の実装
- 承認された仕様書に基づいて実装
- 優先度の高い項目から順に実装
- 後方互換性、エラーハンドリング、リソース管理に注意

### 6. テスト仕様書の作成
- 単体テスト、統合テスト、実機テストのテストケースを作成
- **【承認ポイント4】** テスト仕様書を提示し、承認を待つ

### 7. 完了報告
- 全ての成果物を確認
- 変更内容のサマリーを報告

## 注意事項

- 各承認ポイントで必ず作業を止め、私の指示を待ってください
- 不明点や懸念事項があれば、すぐに質問してください

それでは、作業を開始してください。
```

---

## Step 2: 変更内容を記入

テンプレートの【】部分を実際の内容に置き換えます。

### 例：シンプルなUI変更

```markdown
以下の仕様変更を実施してください。

## 変更要求

エラーダイアログのメッセージに、エラーコードを追加表示したい。

【詳細】
- 現在：エラーメッセージのみ表示
- 変更後：エラーコード（例: E001）をメッセージの前に表示
- 例：「[E001] ファイルが見つかりません」

## ソースコードの場所

- プロジェクト: D:\MyProject\SRC\
- エラーダイアログ: D:\MyProject\SRC\ErrorDialog.cs
- エラーコード定義: D:\MyProject\SRC\ErrorCodes.cs

## 出力ファイルの保存場所

- 分析結果: D:\MyProject\Output\Analysis\
- 変更仕様書: D:\MyProject\Output\Specs\
- テスト仕様書: D:\MyProject\Output\Tests\

## 実施手順

[テンプレートの実施手順をそのままコピー]

## 注意事項

[テンプレートの注意事項をそのままコピー]

それでは、作業を開始してください。
```

---

## Step 3: 実行

### 3.1 Claude Code を起動

```bash
cd your-project
claude
```

### 3.2 プロンプトを貼り付け

作成したプロンプトをClaude Codeに貼り付けて Enter キーを押します。

### 3.3 TodoListが作成される

Claude Codeが自動的にTodoListを作成し、作業を開始します：

```
✓ Create TodoList for specification change
✓ Launch spec-analyzer agent
⏳ Analyze impact of the change
⬜ Generate implementation plan
⬜ Generate SPEC_CHANGES.html
⬜ Implement source code changes
⬜ Generate test specification
```

---

## Step 4: 承認ポイントで確認

### 承認ポイント1: 分析結果の確認

Claude Codeが分析を完了すると、以下のような表示があります：

```
【承認ポイント1】分析結果を提示します。

## 分析サマリー

影響を受けるコンポーネント: 3件
- ErrorDialog.cs (直接影響・高リスク)
- ErrorCodes.cs (直接影響・中リスク)
- Logger.cs (間接影響・低リスク)

リスク評価: 中リスク
見積もり工数: small (1-3日)

詳細は analysis-summary.md を確認してください。

承認しますか？
```

**あなたの対応**：

内容を確認して、以下のいずれかを返答：

- ✅ 承認する場合: 「承認します」または「次へ進んでください」
- ❌ 修正が必要な場合: 「〇〇の部分を△△に修正してください」
- ❓ 質問がある場合: 「〇〇について詳しく説明してください」

### 承認ポイント2: 実装計画の確認

```
【承認ポイント2】実装計画を提示します。

## 実装計画

1. ErrorCodes.cs にエラーコード定義を追加 (優先度: 高)
2. ErrorDialog.cs のメッセージ表示ロジックを変更 (優先度: 高)
3. Logger.cs のログ出力形式を更新 (優先度: 中)

承認しますか？
```

**あなたの対応**: 承認ポイント1と同様

### 承認ポイント3: 変更仕様書の確認

```
【承認ポイント3】変更仕様書とフローチャートを提示します。

生成されたファイル:
- D:\MyProject\Output\Specs\SPEC_CHANGES.html
- D:\MyProject\Output\Specs\flowchart_No001.drawio

ブラウザで SPEC_CHANGES.html を開いて確認してください。
draw.io で flowchart_No001.drawio を開いて確認してください。

承認しますか？
```

**あなたの対応**:

1. SPEC_CHANGES.html をブラウザで開いて確認
2. flowchart_No001.drawio を draw.io で開いて確認
3. 内容に問題がなければ「承認します」

### 承認ポイント4: テスト仕様書の確認

```
【承認ポイント4】テスト仕様書を提示します。

生成されたファイル:
- D:\MyProject\Output\Tests\TEST_SPEC.html

テストケース数:
- 単体テスト: 5件
- 統合テスト: 3件
- 実機テスト: 2件

承認しますか？
```

**あなたの対応**: 承認ポイント3と同様

---

## 完了！

全ての承認ポイントを通過すると、Claude Codeが完了報告を行います：

```
【完了報告】

全ての作業が完了しました。

## 成果物

✓ analysis-result.json
✓ analysis-summary.md
✓ SPEC_CHANGES.html
✓ flowchart_No001.drawio
✓ ErrorDialog.cs (変更済み)
✓ ErrorCodes.cs (変更済み)
✓ Logger.cs (変更済み)
✓ TEST_SPEC.html

## 変更サマリー

- ErrorDialog.cs: エラーコード表示機能を追加
- ErrorCodes.cs: エラーコード定義を追加
- Logger.cs: ログ出力形式を更新

次のステップ:
1. TEST_SPEC.html のテストケースを実行
2. 問題がなければコミット
3. プルリクエストを作成
```

---

## 次のステップ

### より詳しい使い方を学ぶ

- [spec-change-workflow-guide.md](./spec-change-workflow-guide.md) - 詳細なワークフローガイド
- [README.md](./README.md) - エージェント全体の説明

### 実行例を参考にする

- [examples/example-01-simple-change/](./examples/example-01-simple-change/) - シンプルな変更例
- [examples/example-02-complex-change/](./examples/example-02-complex-change/) - 複雑な変更例

### カスタマイズする

- [spec-analyzer.md](./spec-analyzer.md) を編集して分析ルールをカスタマイズ
- [spec-doc-generator.md](./spec-doc-generator.md) を編集して仕様書形式をカスタマイズ

---

## よくある質問（FAQ）

### Q1: プロンプトが長すぎて入力しにくい

**A**: テンプレートを `.txt` ファイルに保存して、毎回コピー&ペーストで使いましょう：

```bash
# テンプレートを保存
cp spec-change-workflow-guide.md my-prompt-template.txt

# 使用時
cat my-prompt-template.txt
# → 内容をコピーして Claude Code に貼り付け
```

### Q2: 承認ポイントをスキップしたい

小規模な変更の場合、承認ポイントを減らすことができます：

```markdown
## 実施手順（簡易版）

### 1. 分析と計画
- spec-analyzerで影響範囲を分析
- 実装計画を作成
- **【承認ポイント1】** 分析結果と計画を提示し、承認を待つ

### 2. 仕様書作成と実装
- spec-doc-generatorで変更仕様書を生成
- ソースコード変更を実装
- テスト仕様書を作成
- **【承認ポイント2】** 全成果物を提示し、承認を待つ
```

### Q3: 分析のみ実施したい

実装せずに分析だけ行うことも可能です：

```markdown
## 実施手順（分析のみ）

### 1. 影響範囲分析
- spec-analyzerで影響範囲を分析
- リスク評価を含める
- **【完了】** 分析結果を提示
```

### Q4: エラーが出た

以下を確認してください：

1. エージェントファイルが正しい場所にあるか
   ```bash
   ls -la .claude/agents/spec-*.md
   ```

2. ファイルパスが正しいか（Windows: `D:\...`, Linux/Mac: `/home/...`）

3. プロンプトに必須項目が含まれているか
   - 変更要求
   - ソースコードの場所
   - 実施手順

---

## Tips

### Tip 1: プロンプトはコンパクトに

最小限のプロンプトでも実行できます：

```markdown
以下の仕様変更を実施してください。

## 変更要求
エラーダイアログにエラーコードを追加

## ソースコードの場所
- D:\MyProject\SRC\

## 実施手順
標準ワークフローに従ってください。各承認ポイントで承認を待ってください。
```

### Tip 2: 変更範囲を限定

特定のファイルのみ変更したい場合：

```markdown
## 変更範囲の制限

以下のファイルのみ変更してください：
- ErrorDialog.cs

以下のファイルは変更しないでください：
- Logger.cs (影響を最小限にするため)
```

### Tip 3: 進捗を確認

作業中に `/tasks` コマンドで進捗を確認できます：

```bash
/tasks
```

表示例：
```
✓ Create TodoList
✓ Analyze impact
⏳ Generate implementation plan
⬜ Generate SPEC_CHANGES.html
⬜ Implement source code
```

---

## まとめ

これで仕様変更支援エージェントの基本的な使い方がわかりました！

**基本の流れ**:
1. プロンプトテンプレートをコピー
2. 変更内容とパスを記入
3. Claude Codeに貼り付け
4. 各承認ポイントで確認・承認
5. 完了！

**困ったときは**:
- [spec-change-workflow-guide.md](./spec-change-workflow-guide.md) を参照
- [examples/](./examples/) の実行例を参考にする
- [README.md](./README.md) のトラブルシューティングを確認

Happy Coding! 🚀
