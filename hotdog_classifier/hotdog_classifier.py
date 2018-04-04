import turicreate as tc
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'data')

MODEL_SAVE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'model', 'model.tc')

data = tc.image_analysis.load_images(DATA_DIR, with_path=True)

data['label'] = data['path'].apply(
    lambda path: 'hotdog' if '/hotdog/' in path else 'nothotdog'
)

print data.groupby('label', [tc.aggregate.COUNT])

train_data, test_data = data.random_split(0.8)

model = tc.image_classifier.create(
    train_data,
    target='label',
    model='squeezenet_v1.1',
    max_iterations=50
)

model.evaluate(test_data)
results = model.evaluate(data)
print results['accuracy']

model.save(MODEL_SAVE)