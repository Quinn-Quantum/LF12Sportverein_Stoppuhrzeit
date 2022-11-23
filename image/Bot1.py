import keras_ocr
from matplotlib import pyplot as plt

images = [
    keras_ocr.tools.read(url) for url in [
        "https://www.google.de/search?q=stoppuhr+digital&tbm=isch&ved=2ahUKEwjqlOD2wMT7AhVinv0HHVvPBrIQ2-cCegQIABAA&oq=stoppuhr+digital&gs_lcp=CgNpbWcQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBwgAEIAEEBgyBwgAEIAEEBg6BAgjECc6BggAEAUQHjoGCAAQCBAeUKIGWIAWYIsZaABwAHgAgAGEAogB5wmSAQUxLjQuM5gBAKABAaoBC2d3cy13aXotaW1nwAEB&sclient=img&ei=Ti1-Y-q1MuK89u8P256bkAs&bih=608&biw=640&hl=de#imgrc=HQLxtyFlWTeV5M"
        ]
]

prediction_groups = pipeline.recognize(images)

#plot the prediction
fig, axs = plt.subplots(nrows=len(images), figsize= (20,20))
for ax, image, predictions in zip(axs, images, prediction_groups):
     keras_ocr.tools.drawAnnotations(image=image,predictions = predictions)
     x_max =0
     temp_str =""
     myfile= open("my_file.txt", "a+")
     for i in prediction_groups[0]:
         x_max_local = i[1][:,0].max()
         temp_str = temp_str + " "+ i[0].ljust(15)
     else:
             x_max = 0
             temp_str = temp_str+ "\n"
             myfile.write(temp_str)
             print(temp_str)
             temp_str = ""
myfile.close()