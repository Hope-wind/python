from PIL import Image

while 1!= 3:
    codeLib = '''@$#%!^. '''
    count = len(codeLib)

    def transform(image_file):
        image_file = image_file.convert("L")
        codePic = ''
        for h in range(0,image_file.size[1]): #纵方向
            for w in range(0,image_file.size[0]):
                gray = image_file.getpixel((w,h))
                codePic  =  codePic + codeLib[int(((count)*gray)/256)]
            codePic = codePic + '\n'
        return codePic

    img = input('请输入图片：')
    fp = open(img,"rb")
    image_file = Image.open(fp)
    text = transform(image_file)


    with open('e:/python/字符化/容器.txt', 'w+') as f:
        f.write(text)
