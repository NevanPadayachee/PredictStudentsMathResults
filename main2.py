import tensorflow as tf
import numpy as np
import pandas as pd
import warnings
warnings.simplefilter('ignore')

data = pd.read_csv('data/student-mat.csv')

categorical_columns = ['school', 'sex', 'address', 'famsize', 'Pstatus', 'Mjob', 'Fjob',
                       'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities',
                       'nursery', 'higher', 'internet', 'romantic']

for feature_name in categorical_columns:
    data.pop(feature_name)

y_test = data.iloc[:, -1]
data = data.drop(['G3'], axis=1)

print(data.head())

model = tf.keras.Sequential()

model.add(tf.keras.layers.Dense(15, activation='relu', input_shape=(15,)))
model.add(tf.keras.layers.Dense(15, activation='relu'))
model.add(tf.keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(data, y_test, epochs=30)

test_data = np.array([15,4,4,1,1,0,5,4,3,2,4,5,8,12,12])#12
print(model.predict(test_data.reshape(1, 15),batch_size=1))

model.save('math_predictions.h5')