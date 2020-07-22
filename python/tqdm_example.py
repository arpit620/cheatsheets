from tqdm import tqdm
import time

# In case of iterations through df.iterrows()
# Use parameter: total = df.shape[0]
for _ in tqdm(range(40), desc='Processing'):
    time.sleep(0.1)

    