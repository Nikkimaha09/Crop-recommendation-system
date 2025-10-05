# 🌱 Crop Recommendation System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-green)](https://flask.palletsprojects.com/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0.2-orange)](https://scikit-learn.org/stable/)

A Machine Learning-based web application that recommends the most suitable crops to grow based on various soil and climate parameters.

## 🌟 Features

- **Smart Crop Recommendations**: Get personalized crop suggestions based on soil and weather conditions
- **Detailed Crop Information**: View comprehensive details about recommended crops
- **User-friendly Interface**: Simple and intuitive web interface
- **Responsive Design**: Works on both desktop and mobile devices

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, NumPy, Pandas
- **Data Processing**: Pandas, NumPy

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Project Structure

```
crop-recommendation-system
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── forms.py
│   ├── templates
│   │   ├── index.html
│   │   └── result.html
│   └── static
│       └── style.css
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd crop-recommendation-system
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```
   python run.py
   ```

2. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:5000/`.

3. **Input Parameters:**
   Fill in the form with the required parameters for crop prediction.

4. **View Results:**
   After submitting the form, the recommended crop and its details will be displayed on the results page.


## License

This project is licensed under the MIT License. See the LICENSE file for more details.
