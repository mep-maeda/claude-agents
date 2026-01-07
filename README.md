# claude-agents

仕様変更作業を効率化するClaude Codeエージェント集

## プロジェクト概要

claude-agentsは、C#/.NETプロジェクトにおける仕様変更作業を自動化・効率化するためのClaude Codeエージェントコレクションです。コードベース全体への影響分析から、変更仕様書・フローチャート・テスト仕様書の生成まで、仕様変更に伴う一連の作業を支援します。

## 含まれるエージェント

### spec-analyzer (v1.0.0)

仕様変更の影響範囲を自動分析するエージェントです。

**出力ファイル:**
- `analysis-result.json` - 詳細な分析結果（JSON形式）
- `analysis-summary.md` - 分析サマリー（Markdown形式）

**主要機能:**
- 影響を受けるコンポーネントの自動特定
- リスクレベル評価（High/Medium/Low）
- 依存関係の分析（internal/external）
- 破壊的変更の検出
- テスト戦略の提案
- 見積もり工数の算出

**分析内容:**
- 直接影響と間接影響の区別
- ファイル・クラス・メソッドレベルの影響範囲
- 後方互換性への影響
- セキュリティ・パフォーマンスへの影響

### spec-doc-generator (v1.0.0)

変更仕様書とフローチャートを自動生成するエージェントです。

**出力ファイル:**
- `SPEC_CHANGES.html` - 変更仕様書（HTML形式）
- `flowchart_*.drawio` - フローチャート（draw.io形式）
- `TEST_SPECIFICATION.html` - テスト仕様書（HTML形式）

**主要機能:**
- 修正前/修正後の2カラム対比形式
- 変更箇所の自動ハイライト
- draw.io形式のフローチャート自動生成
- テスト仕様書の自動生成
- 三菱電機標準フォーマット準拠

**出力形式:**
- 事実ベースの記述（抽象的表現を排除）
- 具体的な設定例・計算式・データ構造
- 階層構造とインデントによる見やすい表示
- 後方互換性・制約事項・注意事項の明記

## セットアップ手順

### 前提条件

- Git がインストールされていること
- Claude Code がインストールされていること

### インストール手順

```bash
# 1. リポジトリをクローン
git clone https://github.com/mep-maeda/claude-agents.git
cd claude-agents

# 2. セットアップスクリプトを実行
./setup.sh
```

### 確認

エージェントが正しくインストールされたか確認します：

```bash
claude-code agents list
```

以下のように表示されればOKです：

```
- spec-analyzer (v1.0.0)
- spec-doc-generator (v1.0.0)
```

## 使い方

### 基本的な使用フロー

```bash
# 1. プロジェクトディレクトリに移動
cd /path/to/your/project

# 2. 影響範囲を分析
claude-code run spec-analyzer "変更内容の説明"

# 3. 変更仕様書を生成
claude-code run spec-doc-generator

# 4. 生成されたファイルを確認
open SPEC_CHANGES.html
open flowchart_*.drawio
```

### 詳細な使用例

#### 例1: 基本的な分析

```bash
claude-code run spec-analyzer "ダウンロード進捗に残り時間表示を追加"
```

このコマンドで以下のファイルが生成されます：
- `analysis-result.json` - 影響を受けるファイル、リスクレベル、依存関係などの詳細情報
- `analysis-summary.md` - エグゼクティブサマリー、推奨事項、テスト戦略

#### 例2: 特定ファイルを指定

```bash
claude-code run spec-analyzer \
  "イベントハンドラのメモリリーク修正" \
  --target-file "frmDiagnosis.cs"
```

特定のファイルに焦点を当てた分析を実行できます。

#### 例3: 変更仕様書の生成

```bash
# spec-analyzerの実行後に実行
claude-code run spec-doc-generator
```

このコマンドで以下のファイルが生成されます：
- `SPEC_CHANGES.html` - 修正前/修正後の対比形式の変更仕様書
- `flowchart_No*.drawio` - 処理フローのビジュアル化
- `TEST_SPECIFICATION.html` - テストケース仕様書

## 更新方法

エージェントを最新版に更新する場合：

```bash
cd /path/to/claude-agents
git pull
claude-code agents reload spec-analyzer
claude-code agents reload spec-doc-generator
```

## トラブルシューティング

### setup.shが実行できない

実行権限を付与してから再実行してください：

```bash
chmod +x setup.sh
./setup.sh
```

### エージェントが見つからない

セットアップスクリプトを再実行してください：

```bash
./setup.sh
```

### 分析結果が期待と異なる

プロンプトの内容を確認してください：

```bash
cat .agents/spec-analyzer/prompt.md
claude-code agents show spec-analyzer
```

必要に応じてプロンプトをカスタマイズできます。

### 出力ファイルが生成されない

以下を確認してください：
1. カレントディレクトリに書き込み権限があるか
2. 必要な入力ファイルが存在するか（spec-doc-generatorの場合）
3. エージェントが正常に実行されているか（エラーログを確認）

## ディレクトリ構造

```
claude-agents/
├── .agents/
│   ├── spec-analyzer/
│   │   ├── agent.json          # エージェント定義
│   │   └── prompt.md           # システムプロンプト
│   └── spec-doc-generator/
│       ├── agent.json          # エージェント定義
│       └── prompt.md           # システムプロンプト
├── .gitignore                  # Git除外設定
├── README.md                   # このファイル
├── setup.sh                    # セットアップスクリプト
└── CHANGELOG.md                # 変更履歴
```

## バージョン履歴

詳細な変更履歴は [CHANGELOG.md](CHANGELOG.md) を参照してください。

### v1.0.0 (2026-01-08)
- 初版リリース
- spec-analyzerエージェント追加
- spec-doc-generatorエージェント追加

## ライセンス

社内利用限定

## 貢献

改善提案やバグ報告は Issues または Pull Request でお願いします。

### 貢献ガイドライン

1. Issueで問題を報告または機能提案
2. フォークしてfeatureブランチを作成
3. 変更を実装
4. Pull Requestを作成

### プロンプトのカスタマイズ

各エージェントのプロンプトは `.agents/<agent-name>/prompt.md` で管理されています。
プロジェクトの特性に合わせてカスタマイズできます。

## サポート

問題が発生した場合は、以下の情報を添えてIssueを作成してください：

- 実行したコマンド
- エラーメッセージ
- 環境情報（OS, Claude Codeバージョン）
- 再現手順

## 関連リソース

- [Claude Code ドキュメント](https://docs.anthropic.com/claude/docs)
- [draw.io](https://www.diagrams.net/) - フローチャート編集ツール
