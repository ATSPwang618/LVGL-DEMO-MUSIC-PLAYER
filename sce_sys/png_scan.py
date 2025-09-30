import os
import sys
import math
from PIL import Image

def get_file_size(path):
    """获取文件大小，转换为人类可读格式"""
    size = os.path.getsize(path)
    if size == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size / p, 2)
    return f"{s} {size_name[i]}"

def get_bit_depth_from_mode(mode):
    """通过图像模式推断位深度（兼容旧版Pillow）"""
    mode_mapping = {
        '1': 1,    # 1位黑白
        'L': 8,    # 8位灰度
        'P': 8,    # 8位索引色
        'RGB': 24, # 24位真彩色
        'RGBA': 32,# 32位带透明真彩色
        'CMYK': 32,# 32位CMYK
        'YCbCr': 24,# 24位YCbCr
        'I': 32,   # 32位整数
        'F': 32    # 32位浮点数
    }
    return mode_mapping.get(mode, "未知")

def get_png_info(png_path):
    """提取PNG图像的格式信息（兼容旧版Pillow）"""
    png_path = os.path.normpath(png_path)
    info = {
        "路径": png_path,
        "文件名": os.path.basename(png_path),
        "状态": "有效",
        "尺寸": "未知",
        "颜色模式": "未知",
        "位深度": "未知",  # 通过模式推断，不依赖bit_depth属性
        "隔行扫描": "未知",
        "文件大小": get_file_size(png_path),
        "错误信息": ""
    }
    
    try:
        with Image.open(png_path) as img:
            # 验证是否为PNG格式
            if img.format != "PNG":
                info["状态"] = "无效"
                info["错误信息"] = "不是PNG格式的图像"
                return info
                
            # 获取基本信息（关键：通过模式推断位深度）
            info["尺寸"] = f"{img.width}×{img.height} 像素"
            info["颜色模式"] = img.mode
            info["位深度"] = f"{get_bit_depth_from_mode(img.mode)} 位"  # 兼容旧版本
            
            # 检查是否隔行扫描
            interlace = img.info.get('interlace', 0)
            info["隔行扫描"] = "是" if interlace != 0 else "否"
            
    except Exception as e:
        info["状态"] = "损坏"
        info["错误信息"] = str(e)
        
    return info

def display_info(info):
    """格式化显示PNG信息"""
    print(f"\n[文件信息] {info['文件名']}")
    print("-" * 50)
    for key, value in info.items():
        if value not in ["未知", ""]:
            print(f"{key:>8}: {value}")

def process_directory(directory):
    """处理目录中的所有PNG文件"""
    directory = os.path.normpath(directory)
    if not os.path.isdir(directory):
        print(f"错误: {directory} 不是有效的目录")
        return
        
    png_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.png'):
                png_path = os.path.join(root, file)
                info = get_png_info(png_path)
                display_info(info)
                png_count += 1
    
    print(f"\n处理完成，共发现 {png_count} 个PNG文件")

def main():
    if len(sys.argv) != 2:
        print("用法: python png_scan_compatible.py <目标目录>")
        print("示例: python png_scan_compatible.py ./sce_sys")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    print(f"开始扫描目录: {target_dir} 中的PNG文件...")
    process_directory(target_dir)

if __name__ == "__main__":
    main()
    