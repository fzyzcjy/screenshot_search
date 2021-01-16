from pathlib import Path

import pytesseract
from PIL import Image
from tqdm import tqdm

ipython = get_ipython()
ipython.magic('%load_ext autoreload')
ipython.magic('%autoreload 2')

dbase = Path('/Users/tom/Others/screenshot_search_data')
d_image = dbase / '1_im'
d_ocr = dbase / '2_ocr'

# %%

pins = list(d_image.glob('*.*'))
print(len(pins))

pins_stem = [x.stem for x in pins]

# %% ocr

# NOTE 尝试关闭字典，发现效果更差... https://github.com/tesseract-ocr/tessdoc/blob/master/ImproveQuality.md#dictionaries-word-lists-and-patterns
# my_config_path = dbase / 'my_config'
# my_config_path.write_text('''
# load_system_dawg 0
# load_freq_dawg 0
# ''')
# output_str = pytesseract.image_to_string(Image.open(str(pin)), lang='chi_sim', config=str(my_config_path))

for pin in tqdm(list(d_image.glob('*.*'))):
    output_str = pytesseract.image_to_string(Image.open(str(pin)), lang='chi_sim')
    print(pin.stem, '=>', output_str.replace('\n', r'\n'))
    (d_ocr / f'{pin.stem}.txt').write_text(output_str)
