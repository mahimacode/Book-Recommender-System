# Book-Recommender-System
A collaborative filtering based Book Recommender System built on the Book-Crossing dataset. Includes preprocessing, EDA, popularity-based filtering, and item similarity using cosine/Pearson correlation. Implemented in Python with Pandas, NumPy, Scikit-learn, and Jupyter for analysis and recommendations, and is deployed as a Flask web application styled with Bootstrap CSS.


Features-:

Data Preprocessing: Cleaning, merging, and preparing Books, Users, and Ratings datasets.

Exploratory Data Analysis (EDA): Popularity metrics (num_ratings, avg_rating), threshold filtering, top-N books.

Popularity-Based Filtering: Recommends books with high rating counts and averages.

Collaborative Filtering: Item-based recommendations using similarity metrics (Cosine, Pearson).

Model Serialization: Trained recommender saved as .pkl using Pickle for fast loading in production.

Web Deployment: Flask backend + Bootstrap CSS frontend. Users can enter a book name and receive top recommended books via the web interface.


Tech Stack-:

Python: Pandas, NumPy, Scikit-learn

Flask: Web framework for deployment

Pickle: Model persistence

Bootstrap CSS: Responsive UI styling

Jupyter Notebook: For analysis and prototyping

Usage-:

Enter a book title in the search bar.

The system fetches recommendations using the collaborative filtering model.

Results are displayed with Bootstrap-styled cards on the webpage.
