from keras.models import load_model

# Load the model
model = load_model('my_model.hdf5')

# Print model summary

print(model.summary())