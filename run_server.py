#!/usr/bin/env python
import sys
import traceback

try:
    from flask import Flask, render_template, request
    import pickle
    import numpy as np

    print("Loading pickle files...")
    popular_df = pickle.load(open('popular.pkl', 'rb'))
    print(f"✓ popular.pkl loaded - shape: {popular_df.shape}")
    
    pt = pickle.load(open('pt.pkl', 'rb'))
    print(f"✓ pt.pkl loaded - shape: {pt.shape}")
    
    books = pickle.load(open('books.pkl', 'rb'))
    print(f"✓ books.pkl loaded - shape: {books.shape}")
    
    similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
    print(f"✓ similarity_score.pkl loaded - shape: {similarity_score.shape}")

    print("\nCreating Flask app...")
    app = Flask(__name__)

    @app.route('/')
    def index():
        print("Index route called")
        return render_template('index.html',
                               book_name=list(popular_df['Book-Title'].values),
                               author=list(popular_df['Book-Author'].values),
                               image=list(popular_df['Image-URL-M'].values),
                               votes=list(popular_df['num_ratings'].values),
                               rating=list(popular_df['avg_rating'].values)
                               )

    @app.route('/recommend')
    def recommend_ui():
        return render_template('recommend.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/recommend_books', methods=['POST'])
    def recommend_books():
        user_input = request.form.get('user-input', '').strip()

        if not user_input:
            return render_template(
                'recommend.html',
                data=None,
                user_input='',
                error="Please enter a book name."
            )

        matches = np.where(pt.index.str.lower() == user_input.lower())[0]

        if len(matches) == 0:
            error_msg = f"No book found named '{user_input}'. Please check the spelling."
            return render_template(
                'recommend.html',
                data=None,
                user_input=user_input,
                error=error_msg
            )

        index_no = matches[0]
        similar_items = sorted(list(enumerate(similarity_score[index_no])), key=lambda x: x[1], reverse=True)[1:6]

        data = []
        for i in similar_items:
            item = []
            temp_df = books[books['Book-Title'] == pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)

        print("User input:", user_input)
        print("Recommendations:", data)

        return render_template(
            'recommend.html',
            data=data,
            user_input=user_input,
            error=None
        )

    print("\n✓ Flask app created successfully!")
    print("Starting server on http://127.0.0.1:5000")
    print("=" * 50)
    app.run(debug=True, host='127.0.0.1', port=5000)

except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    print("\nFull traceback:")
    traceback.print_exc()
    sys.exit(1)
