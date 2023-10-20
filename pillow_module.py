from PIL import Image,ImageEnhance, ImageFilter
import os

img1= Image.open('flower.jpg')
# img1.save('flower1.png')
# img1.show()


# for i in os.listdir():
#     if i.endswith('.jpg'):
#         img1= Image.open(i)
#         filemane,extension= os.path.splitext(i)
#         img1.save(f'{filemane}.png')
# Max_size=(250,250)
# img1.thumbnail(Max_size)
# img1.save('flower2.jpg')


# enhancer= ImageEnhance.Sharpness(img1)
# enhancer.enhance(10).save('flower_enh.jpg')


# enhancer= ImageEnhance.Color(img1)
# enhancer.enhance(10).save('flower_enh.jpg')



# enhancer= ImageEnhance.Brightness(img1)
# enhancer.enhance(10).save('flower_enh.jpg')



# enhancer= ImageEnhance.Contrast(img1)
# enhancer.enhance(10).save('flower_enh.jpg')



img1.filter(ImageFilter.GaussianBlur()).save('flower_1.jpg')


