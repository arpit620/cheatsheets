from tqdm import tqdm
import time

for _ in tqdm(range(40), desc='Processing'):
    time.sleep(0.1)

    