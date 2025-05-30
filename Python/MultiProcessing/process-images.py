
import time
import concurrent.futures
from PIL import Image, ImageFilter
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1564135624576-c5c88640f235.jpg',

]



size = (1200, 1200)


def process_image(img_name):
    img = Image.open(img_name)

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f'{img_name} was processed...')

if __name__ ==  '__main__':
    
    t1 = time.perf_counter()
    
    # Create a directory to save processed images
    if not os.path.exists('processed'):
        os.makedirs('processed')
        
    # 2.3 seconds    
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_names)


    # #took 7.5 seconds
    # for img_name in img_names: 
    #     process_image(img_name)

    t2 = time.perf_counter()

    print(f'Finished in {t2-t1} seconds')
