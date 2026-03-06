from PIL import Image

# 读取你的高清 PNG 图片
img = Image.open('src/yae.ico')

# 强制生成包含所有 Windows 标准尺寸的 ICO 文件
icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
img.save('src/yae.ico', format='ICO', sizes=icon_sizes)

print("全尺寸 yae.ico 生成成功！")