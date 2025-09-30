import os
import sys
from PIL import Image

def convert_to_8bit_rgba(input_path, output_path):
    """
    将图像转换为8位带透明通道的PNG（修复PA模式保存问题）
    适配PS Vita图标要求：128×128、8位、非隔行扫描、保留透明
    """
    try:
        with Image.open(input_path) as img:
            # 确保尺寸为128×128
            if img.size != (128, 128):
                print(f"警告：图像尺寸不是128×128，自动调整")
                img = img.resize((128, 128), Image.Resampling.LANCZOS)
            
            # 确保图像为RGBA模式（避免PA模式源头）
            if img.mode != "RGBA":
                print(f"将图像转换为RGBA模式")
                img = img.convert("RGBA")
            
            # 第一步：生成256色的调色板（从RGBA图像中提取）
            # 使用RGBA生成P模式图像（不带Alpha通道）
            img_p = img.convert(
                "P",
                palette=Image.Palette.ADAPTIVE,
                colors=256  # 8位最多256色
            )
            
            # 第二步：提取原始Alpha通道
            alpha = img.split()[-1]  # RGBA的第四个通道是Alpha
            
            # 第三步：将Alpha通道转为掩码（用于P模式的透明信息）
            # 生成与P模式图像匹配的透明掩码
            mask = Image.eval(alpha, lambda a: 255 if a > 128 else 0)  # 二值化透明通道
            
            # 第四步：将掩码应用到P模式图像，生成带透明的8位图像
            img_8bit = img_p.copy()
            img_8bit.putalpha(mask)
            
            # 关键修复：保存前先转为RGBA再转回P模式（规避PA模式）
            # 临时转为RGBA再转回P模式，确保保存格式兼容
            img_8bit = img_8bit.convert("RGBA").convert(
                "P",
                palette=Image.Palette.ADAPTIVE,
                colors=256
            )
            img_8bit.putalpha(mask)  # 重新应用透明掩码
            
            # 保存为非隔行扫描的PNG
            img_8bit.save(
                output_path,
                "PNG",
                interlace=0,  # 非隔行扫描
                optimize=True,
                transparency=0  # 明确指定透明色索引
            )
            
            # 验证结果
            with Image.open(output_path) as converted_img:
                mode = converted_img.mode
                # 推断位深度（8位）
                bit_depth = 8 if mode == "P" else converted_img.bit_depth
                print(f"转换成功！输出图像信息：")
                print(f"  尺寸：{converted_img.size[0]}×{converted_img.size[1]}")
                print(f"  模式：{mode}")
                print(f"  位深度：{bit_depth}位")
                print(f"  隔行扫描：{'是' if converted_img.info.get('interlace', 0) else '否'}")
            return True
            
    except Exception as e:
        print(f"转换失败：{str(e)}")
        return False

def main():
    if len(sys.argv) != 3:
        print("用法：python convert_to_8bit_fixed.py <输入icon0.png路径> <输出路径>")
        print("示例：python convert_to_8bit_fixed.py ./icon0.png ./icon0_8bit.png")
        sys.exit(1)
    
    input_path = os.path.normpath(sys.argv[1])
    output_path = os.path.normpath(sys.argv[2])
    
    if not os.path.isfile(input_path):
        print(f"错误：输入文件不存在 - {input_path}")
        sys.exit(1)
    
    if not input_path.lower().endswith('.png'):
        print(f"错误：输入文件必须是PNG格式 - {input_path}")
        sys.exit(1)
    
    convert_to_8bit_rgba(input_path, output_path)

if __name__ == "__main__":
    main()
