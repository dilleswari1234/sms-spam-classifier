---

# SMS Spam Classifier

This repository contains an **SMS Spam Classifier** project that uses machine learning to identify spam messages. The classifier is trained on SMS messages and can categorize them as **spam** or **ham (not spam)**. 

## Project Overview

- **Dataset**: Uses `mail_data.csv` to train and evaluate the model.
- **Saved Models**: Loads two `.pkl` files for the model and vectorizer in `app.py` for predictions.
- **Streamlit Interface**: Includes a user-friendly interface to classify SMS messages.

## Dependencies

Install the required libraries with:

```bash
pip install -r requirements.txt
```

Key libraries:
- `scikit-learn` for machine learning model building
- `pandas` for data manipulation
- `numpy` for numerical operations
- `nltk` for text preprocessing
- `streamlit` for the interactive interface

## Project Structure

```
sms-spam-classifier/
├── app.py                # Main script to run the classifier with Streamlit interface
├── mail_data.csv     # Dataset for training and evaluating the model
├── model.pkl & vectorizer.pkl      # Serialized machine learning model and text vectorizer
├── SMS_spam_detection.ipynb       # Jupyter notebooks for data exploration and experimentation
├── requirements.txt      # List of dependencies for the project
└── README.md             # Project documentation
```

- **`app.py`**: Loads `model.pkl` and `vectorizer.pkl` files, and runs a Streamlit interface to interact with the classifier.
- **`mail_data.csv`**: Contains `mail_data.csv`, the dataset used for model training and evaluation.
- **`model.pkl & vectorizer.pkl`**: Stores the trained model and vectorizer, saved as `.pkl` files for later use in predictions.
- **`SMS_spam_detection.ipynb`**: Contains notebooks for data exploration, preprocessing, and model training.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dilleswari1234/sms-spam-classifier.git
   cd sms-spam-classifier
   ```

2. **Install Dependencies**:

   Install the required packages from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Classifier**:

   Start the classifier and Streamlit interface with:

   ```bash
   streamlit run app.py
   ```

2. **Interact with the Classifier**:
   - Upload or enter SMS text in the Streamlit interface to classify it as spam or ham.
   - The classifier will load the `model.pkl` and `vectorizer.pkl` files to make predictions based on the input.

## Model Training and Evaluation

- Use `mail_data.csv` to train and evaluate the model. Preprocess this data by removing noise and vectorizing it, then fit the model using `scikit-learn`.
- Save the trained model and vectorizer as `.pkl` files in the `model/` directory for easy loading in `app.py`.

## Notes

- **Models**: Place `model.pkl` and `vectorizer.pkl` in the directory to be loaded by `app.py`.

## Contact

For questions or contributions, reach out via GitHub or [bathularajadilleswari06639@gmail.com].

---

