import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

WIDTH = 1000
HEIGHT = 1000


def make_image():
    font = ImageFont.truetype('resources/font.ttf', size=50, encoding='UTF-8')

    now_date = datetime.datetime.today()
    new_year_date = datetime.datetime(day=1, year=now_date.year + 1, month=1, minute=0, hour=0)
    raw_interval = new_year_date - now_date
    interval = f'{int(raw_interval.total_seconds() // 60 // 60)} часов'

    img = Image.open('resources/image.jpg')

    draw_text = ImageDraw.Draw(img)
    msg = 'До нового года осталось:'
    W, H = WIDTH, 300
    size = font.getbbox(msg, language='ru')
    w, h = size[2], size[3]
    draw_text.text(((W - w) / 2, (H - h) / 2), msg, fill="white", font=font)

    draw_text = ImageDraw.Draw(img)
    msg = interval
    W, H = WIDTH, HEIGHT + 750
    size = font.getbbox(msg, language='ru')
    w, h = size[2], size[3]
    draw_text.text(((W - w) / 2, (H - h) / 2), msg, fill="white", font=font)

    img.save('result.jpg')

# img = Image.new(mode='RGB', size=(WIDTH, HEIGHT))
# img1 = Image.open('tree.png')

# img.paste(img1, (244, 244))
# img.save('image.jpg')
# img.show()
