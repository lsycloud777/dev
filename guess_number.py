# 猜数字游戏 —— 最简单的 Python 入门示例
# 运行方法：python guess_number.py

import random

def main():
    # 生成 1~100 的随机答案
    answer = random.randint(1, 100)
    tries = 0

    print("欢迎玩猜数字游戏！我心里想了一个 1~100 的数字。")

    while True:
        # 用户输入
        text = input("请猜一个数字（输入 q 退出）：")

        if text.lower() == "q":
            print(f"再见！正确答案是 {answer}。")
            break

        # 判断输入是不是数字
        if not text.isdigit():
            print("请输入数字哦！")
            continue

        guess = int(text)
        tries += 1

        # 比较大小
        if guess < answer:
            print("太小了，再大一点。")
        elif guess > answer:
            print("太大了，再小一点。")
        else:
            print(f"恭喜你！猜对了，答案是 {answer}，一共猜了 {tries} 次。")
            break

if __name__ == "__main__":
    main()
