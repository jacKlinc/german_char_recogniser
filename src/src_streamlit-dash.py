from fastai.learner import load_learner
from fastai.vision.core import PILImage

import streamlit as st
from PIL import Image

def load_image(image):
    '''
    Pass    BytesIO image
    Return  PILImage object
    '''
    return Image.open(image)

def predict_img(img):
    '''
    Pass    PILImage object
    Return  prediction[str], prediction_idx[int], probability[tensor]
    '''
    if img is not None:
        return learner_inf.predict(pil_img)

'## German Character Recogniser'
"Here's the [GitHub](https://github.com/jacKlinc/german_char_recogniser) repo"
'Upload a picture of a vowel'

learner_inf = load_learner('./res/AEIOU_model.pkl')

# Upload
pic = st.file_uploader("Upload Image")

'Click Classify to find whether it\'s an A or a B'

probs = []
pred_idx = 1
pred = 'n/a'

# Display image
if pic is not None:
    img = load_image(pic)
    st.image(img)
    
    
    # Parse image
    pil_img = PILImage.create(pic)

    # Predict category
    pred,pred_idx,probs = predict_img(pil_img)

# Classify
if st.button('Classify'):
    'Prediction: ', pred
    'Probability: ', str(round(probs[pred_idx].item(), 5))