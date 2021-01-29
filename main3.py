import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model('math_predictions.h5')

test_data = np.array([16,2,1,1,2,0,5,3,4,1,1,2,8,8,9])#10
print(model.predict(test_data.reshape(1, 15), batch_size=1))
