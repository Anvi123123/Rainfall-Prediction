# Rainfall-Prediction

The main motive of the project is to predict the amount of rainfall in Andaman & Nicobar region. 
We predict average rainfall using past data (1901-2015).

![alt text](static/workFlow.png)

## Tech Stack

* Front-End: HTML, CSS
* Back-End: Flask
* IDE: Jupyter notebook, vscode

## How to Run the Project

1. **Clone the repository**

2. **Set up a virtual environment (optional but recommended):**
   ```
   python -m venv env
   source env/bin/activate  # On Windows, use `env\Scripts\activate`
   ```

3. **Install required dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Train the model and create pickle file:**
   ```
   python app.py
   ```
   This will train the model using the provided dataset and save it as a pickle file.

5. **Run the Flask app:**
   ```
   python main.py
   ```
   The Flask app will start running, typically on `http://127.0.0.1:5000/`.

## CONCLUSION
The hybrid model improves rainfall prediction accuracy by combining regression and classification techniques, 
capturing linear and non-linear data relationships. 
It addresses temporal variability better than traditional models and adapts to diverse regions. 

## Improvements that can be done:

More data and more computational power could be a great help.
Further enhancements, such as adding temperature and humidity, 
could make it an essential tool for precise rainfall forecasting.
