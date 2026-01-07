#!/bin/bash

echo "=========================================="
echo "claude-agents セットアップ"
echo "=========================================="
echo ""

# エージェントディレクトリの確認
if [ ! -d ".agents" ]; then
    echo "❌ .agentsディレクトリが見つかりません"
    exit 1
fi

echo "📦 エージェントをインポート中..."
echo ""

# spec-analyzerのインポート
echo "🔍 spec-analyzer をインポート..."
claude-code agents import .agents/spec-analyzer

if [ $? -eq 0 ]; then
    echo "✅ spec-analyzer のインポート完了"
else
    echo "❌ spec-analyzer のインポート失敗"
    exit 1
fi

echo ""

# spec-doc-generatorのインポート
echo "📝 spec-doc-generator をインポート..."
claude-code agents import .agents/spec-doc-generator

if [ $? -eq 0 ]; then
    echo "✅ spec-doc-generator のインポート完了"
else
    echo "❌ spec-doc-generator のインポート失敗"
    exit 1
fi

echo ""
echo "=========================================="
echo "✅ セットアップ完了！"
echo "=========================================="
echo ""
echo "使い方:"
echo "  1. プロジェクトディレクトリに移動"
echo "  2. claude-code run spec-analyzer \"変更内容\""
echo "  3. claude-code run spec-doc-generator"
echo ""
echo "詳細はREADME.mdを参照してください"
echo ""
