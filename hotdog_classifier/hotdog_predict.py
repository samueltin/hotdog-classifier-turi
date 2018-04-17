import turicreate as tc
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'test_data')
MODEL_SAVE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'model', 'model.tc')

test_data = tc.image_analysis.load_images(DATA_DIR)

loaded_model = tc.load_model(MODEL_SAVE)


# Use the model to predict the class of the test_data
predictions = loaded_model.predict(test_data)
# Print the predictions
for image in zip(test_data,predictions):
    print image[0]['path'],image[1]