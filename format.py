import os
import re


if __name__ == "__main__":
    albums = ['red', 'green', 'blue'] # ,  'yellow', 'purple']
    for album in albums:
        folder = f"./{album.capitalize()}"  # Thay bằng đường dẫn thư mục ảnh

        # Dùng để theo dõi mỗi `a` đã có bao nhiêu ảnh (tối đa 2: red_a_1 và red_a_2)
        count_per_a = {}

        for filename in sorted(os.listdir(folder)):
            match = re.match(rf"{album}_(\d+)_(\d+)\.png", filename)
            if match:
                a, b = match.groups()
                a = int(a)

                # Bỏ qua nếu đã có 2 ảnh cho a rồi
                if count_per_a.get(a, 0) >= 2:
                    continue

                # Xác định tên mới
                new_b = count_per_a.get(a, 0) + 1  # 1 hoặc 2
                new_name = f"{album}_{a}_{new_b}.png"

                src = os.path.join(folder, filename)
                dst = os.path.join(folder, new_name)

                print(f"Đổi tên: {filename} → {new_name}")
                os.rename(src, dst)

                count_per_a[a] = new_b
