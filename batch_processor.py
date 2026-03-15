import os
import time

def batch_process_files(source_dir, target_format, new_prefix="processed_"):
    # 遍历目录
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        # 跳过文件夹，只处理文件
        if os.path.isfile(file_path):
            # 筛选格式
            if filename.endswith(target_format):
                # 重命名（示例：加前缀+时间戳）
                timestamp = time.strftime("%Y%m%d%H%M%S")
                new_filename = f"{new_prefix}{timestamp}_{filename}"
                new_file_path = os.path.join(source_dir, new_filename)
                os.rename(file_path, new_file_path)
                print(f"处理完成：{filename} → {new_filename}")

if __name__ == "__main__":
    # 配置参数
    source_dir = "/opt/test_files"  # 你的文件目录
    target_format = ".txt"          # 要处理的文件格式
    batch_process_files(source_dir, target_format)
