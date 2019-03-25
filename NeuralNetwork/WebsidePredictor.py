import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow import keras
import numpy as np
import pandas as pd

FILENAME = 'new_script.txt'

# word_to_id = <COPY FROM NOTEBOOK>
# trope_list =  <COPY FROM NOTEBOOK>
# padding = <COPY FROM NOTEBOOK>


#############################################################################################


model = load_model('TropeClassifier_.model')

with open(FILENAME, 'r') as f:
    test_text = f.read()

text_processor = lambda t: keras.preprocessing.text.text_to_word_sequence(t, filters='!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~\t\n', lower=True, split=' ')

test_text_clean = text_processor(test_text)

test_array = []
for script in [test_text_clean]:
    s = [0]*padding
    for word in script:
        if word in word_to_id:
            s[word_to_id[word]] = 1
    test_array.append(s)
test_array = np.array(test_array)

predictions = model.predict(test_array)

L = sorted([(trope_list[i], trope) for i, trope in enumerate((predictions[0]*100).astype('uint32'))], key=lambda x: x[1], reverse=True)[:10]
L = [' - '.join([str(ll) for ll in l]) for l in L]
L

df_out = pd.DataFrame({'Results': L})
df_out.to_csv(r'Results.csv', index=None)
