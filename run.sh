#!/bin/bash
# Linux 环境下一键运行文件批量处理脚本
# 适配 Linux 文件路径与权限模型

# 切换到脚本所在目录（避免相对路径报错）
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd "${SCRIPT_DIR}" || exit

echo "🔧 正在 Linux 环境下运行 Python 批量处理脚本..."
echo "📂 目标目录：/opt/python-file-batch-processor/test_files"
echo "----------------------------------------"

# 执行 Python 脚本
python3 batch_processor.py

echo -e "\n✅ Linux 环境运行完成，脚本适配大批量文件处理逻辑"
