import subprocess
from pathlib import Path

from tqdm import tqdm

ipython = get_ipython()
ipython.magic('%load_ext autoreload')
ipython.magic('%autoreload 2')

dbase = Path('/Users/tom/Others/screenshot_search_data')
d_image = dbase / '1_im'
d_ocr = dbase / '2_ocr'

# %% ocr

for pin in tqdm(list(d_image.glob('*.*'))):
    outputbase = d_ocr / pin.stem
    # args = ['tesseract', str(pin), str(outputbase), '--dpi', '200', '-l', 'chi_sim+eng']
    args = ['tesseract', str(pin), str(outputbase), '--dpi', '200', '-l', 'chi_sim']
    print(f'Run {args}')
    subprocess.run(args)
    print('text:' + Path(str(outputbase) + '.txt').read_text())
    # break
