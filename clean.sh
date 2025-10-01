#!/bin/bash
# 清理编译文件

echo "正在清理编译文件..."

# 删除 build 目录
if [ -d "build" ]; then
    rm -rf build
    echo "✓ 已删除 build 目录"
fi

# 删除其他可能的编译产物
find . -name "*.o" -delete
find . -name "*.a" -delete
find . -name "*.self" -delete
find . -name "*.vpk" -delete
find . -name "*.velf" -delete
find . -name "*.elf" -delete

echo "✓ 清理完成"
echo ""
echo "现在可以运行 ./build.sh 重新编译项目"
