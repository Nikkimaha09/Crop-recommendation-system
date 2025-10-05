# Crop Recommendation System

This project is a web-based crop recommendation system built using Flask. It allows users to input various parameters related to soil and climate conditions and provides recommendations for suitable crops based on the input data.

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

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.