import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def verify_code(width=120, height=30, char_length=5, font_file=r'static/fonts/FreeSans.ttf', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def generate_random_characters():
        """
        生成随机字符（包括大小写字母和数字）
        :return:
        """
        random_nums = str(random.randint(0, 9))
        random_lower = chr(random.randint(65, 90))
        random_upper = chr(random.randint(97, 120))
        return random.choice([random_nums, random_lower, random_upper])

    def generate_random_colors():
        """
        生成随机颜色
        :return:
        """
        return random.randint(0, 255), random.randint(10, 255), random.randint(64, 255)

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    print(font)
    for i in range(char_length):
        char = generate_random_characters()
        code.append(char)
        h = (height - font_size) / 2
        draw.text([i * width / char_length, h], char, font=font, fill=generate_random_colors())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=generate_random_colors())

    # 写干扰圆圈
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=generate_random_colors())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=generate_random_colors())

    # 画干扰线
    for i in range(5):
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=generate_random_colors())

    # 对图像加滤波 - 深度边缘增强滤波
    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    codes = ''.join(code)
    del draw
    return img, codes
