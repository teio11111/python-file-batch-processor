# 导入os处理文件，time生成时间
import os
import time

# 批量处理文件的函数
# 遍历指定目录，筛选指定后缀的文件，批量重命名（加前缀+时间戳）
def batch_rename_files(file_dir, file_suffix, rename_prefix="batch_"):
    # 先检查目标目录是否存在（避免目录不存在导致报错 ）
    if not os.path.exists(file_dir):
        print(f"❌ 错误：目录 {file_dir} 不存在！")
        return
    
    # 遍历目录里的所有文件/文件夹
    file_list = os.listdir(file_dir)
    # 统计处理成功/失败的数量（方便看结果）
    success_count = 0
    fail_count = 0

    for file_name in file_list:
        # 拼接完整的文件路径（不然会找不到文件）
        full_file_path = os.path.join(file_dir, file_name)
        
        # 只处理文件，跳过文件夹（之前没加这个判断，把文件夹也改了名）
        if os.path.isfile(full_file_path):
            # 筛选指定后缀的文件
            if file_name.endswith(file_suffix):
                # 生成时间戳（格式：年月日时分秒，方便区分不同批次的文件）
                time_mark = time.strftime("%Y%m%d_%H%M%S")
                # 拼接新文件名：前缀+时间戳+原文件名
                new_file_name = f"{rename_prefix}{time_mark}_{file_name}"
                new_full_path = os.path.join(file_dir, new_file_name)

                # 尝试重命名，防止文件被占用/权限不够导致脚本崩溃
                try:
                    os.rename(full_file_path, new_full_path)
                    print(f"✅ 成功：{file_name} → {new_file_name}")
                    success_count += 1
                except Exception as err:
                    print(f"❌ 失败：{file_name} 重命名失败，原因：{err}")
                    fail_count += 1

    # 处理完成后打印统计结果
    print(f"\n📊 处理完成！成功：{success_count} 个，失败：{fail_count} 个")

# 主程序入口
if __name__ == "__main__":
    # 配置参数（自己测试用的目录，后续可以改成从外部配置文件读）
    target_dir = "/opt/python-file-batch-processor/test_files"
    target_suffix = ".txt"  # 要处理的文件后缀
    
    # 调用函数执行批量处理
    batch_rename_files(target_dir, target_suffix)
