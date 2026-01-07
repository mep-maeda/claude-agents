# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-01-08

### Added
- spec-analyzer エージェント
  - 仕様変更の影響範囲自動分析
  - リスクレベル評価（High/Medium/Low）
  - 依存関係分析（internal/external）
  - 破壊的変更の検出
  - テスト戦略提案
  - 見積もり工数算出
  - JSON形式の詳細分析結果（analysis-result.json）
  - Markdown形式の分析サマリー（analysis-summary.md）

- spec-doc-generator エージェント
  - 変更仕様書自動生成（HTML形式）
  - draw.ioフローチャート自動生成
  - テスト仕様書自動生成
  - 修正前/修正後の2カラム対比形式
  - 変更箇所の自動ハイライト
  - 三菱電機標準フォーマット準拠
  - 事実ベースの記述スタイル
  - 具体的な設定例・計算式の記載

- プロジェクト構成
  - セットアップスクリプト (setup.sh)
  - 詳細なREADME.md
  - .gitignore（出力ファイルの除外設定）
  - CHANGELOG.md（このファイル）

### Documentation
- エージェントの使用方法
- セットアップ手順
- トラブルシューティングガイド
- 使用例とコマンド例
- ディレクトリ構造の説明

### Technical Details
- C#/.NETプロジェクトに特化した分析ロジック
- 5段階の分析プロセス（理解→影響範囲→依存関係→リスク→推奨事項）
- 修正前/修正後の対比によるわかりやすい変更仕様書
- draw.io XML形式でのフローチャート生成
- 黄色ハイライトによる変更箇所の視覚化

## [Unreleased]

### Planned
- 英語版ドキュメントのサポート
- 他のプログラミング言語（Java, Python等）へのサポート拡張
- CI/CDパイプラインとの統合
- カスタムテンプレートのサポート
- 分析結果のエクスポート機能（PDF, Word）
