# Bollywood Movie Recommendation System

This repository contains a movie recommendation system built using Streamlit and trained on a Bollywood movie dataset. The system provides movie suggestions based on user preferences.

#Link for demo posted using streamlit:
https://movierecommendationmodel-dekho.streamlit.app/

## Files Included

- **`app.py`**: The main Streamlit application file for running the recommendation system.
- **`movie_hindi.pkl`**: Pickle file containing the trained recommendation model.
- **`hindi_model.ipynb`**: Jupyter notebook used to train the recommendation model.

## Setup and Usage

### Prerequisites

Ensure you have Python 3.x installed on your machine. It is recommended to use a virtual environment to manage dependencies.

### Installation Steps

1. **Clone the Repository**

   Clone the repository from GitHub and navigate to the project directory.

2. **Create and Activate a Virtual Environment**

   Set up a virtual environment to isolate your project's dependencies.

3. **Install Required Packages**

   Generate a `requirements.txt` file if it does not already exist by freezing your environment’s current packages. Install the packages listed in `requirements.txt` using your package manager.

4. **Run the Streamlit Application**

   Execute the Streamlit application script to start the recommendation system.

5. **Access the Application**

   Open your web browser and go to the local URL provided by Streamlit to interact with the application.

## Model Details

- **Model File:** `movie_hindi.pkl`
  - This file contains the trained recommendation model used by the Streamlit app to generate movie suggestions.

- **Training Notebook:** `hindi_model.ipynb`
  - This Jupyter notebook contains the code and steps for training the recommendation model, including data preprocessing, model training, and evaluation.

## Demo

To see the movie recommendation system in action, you can refer to the screenshots below:

1. **Homepage**
   - 
   -![Screenshot 2024-09-02 164911](https://github.com/user-attachments/assets/30e5978b-20b4-4ccf-a77e-e4c63e30411b)
 Description: This is the main page of the application where users can interact with the recommendation system.

2. **Movie Recommendations**
   - ![Screenshot 2024-09-02 164953](https://github.com/user-attachments/assets/23203f27-09bb-43fd-bb84-6f0b89d651e7)

   - Description: This page shows the movie recommendations generated based on user inputs.

.

## Notes

- Ensure that the `movie_hindi.pkl` file is in the same directory as `app.py` for the application to function correctly.
- If you encounter issues, make sure all dependencies are installed and your virtual environment is properly activated.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Bollywood movie dataset for providing the data necessary for training the recommendation model.
- Streamlit for offering a framework to create interactive web applications.
