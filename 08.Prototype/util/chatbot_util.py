import json, os
import requests, base64
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont

def proc_yolo(static_folder, img_file, color, linewidth, fontsize):
    colordict = {'red':(255,0,0), 'green':(0,255,0), 'blue':(0,0,255)}
    color = colordict[color]
    img_type = img_file.split('.')[-1]
    if img_type == 'jfif':
        img_type = 'jpg'

    with open(os.path.join(static_folder, 'keys/etriAiKey.txt')) as f:
        accessKey = f.read()
    with open(img_file, 'rb') as f:
        img_content = base64.b64encode(f.read()).decode("utf8")
    
    openApiURL = "http://aiopen.etri.re.kr:8000/ObjectDetect"
    headers={"Content-Type": "application/json; charset=UTF-8","Authorization": accessKey}
    requestJson = { "argument": {"type": img_type, "file": img_content}}
    result = requests.post(openApiURL, headers=headers, data=json.dumps(requestJson)).json()
    obj_list = result['return_object']['data']

    img = Image.open(img_file)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('malgun.ttf', fontsize)
    for obj in obj_list:
        name = obj['class']
        x, y = int(obj['x']), int(obj['y'])
        w, h = int(obj['width']), int(obj['height'])
        draw.rectangle(((x, y), (x+w, y+h)), outline=color, width=linewidth)
        draw.text((x+10, y+10), name, font=font, fill=color)
    
    savefile = os.path.join(static_folder, 'result/yolo.png')
    plt.figure()    # 새로운 이미지를 끼워 넣겠다
    plt.imshow(img)
    plt.axis('off')
    plt.savefig(savefile, dpi=180, bbox_inches='tight')             # format='png'
    mtime = os.stat(savefile).st_mtime
    return mtime