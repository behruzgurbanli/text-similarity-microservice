import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similars(file_path: str) -> dict:
    """
    Finds similar documents based on cosine similarity.

    Args:
        file_path (str): Path to the CSV file containing documents.

    Returns:
        dict: Dictionary containing similarity results.
    """
    try:
        # Load CSV
        df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip', delimiter=';')
        
        docs = df[['Content', 'Date']].dropna().copy()
        docs['Date'] = pd.to_datetime(docs['Date'])
        
        docs.sort_values(by='Date', inplace=True)

        tfidf = TfidfVectorizer()
        response = tfidf.fit_transform(docs['Content'])
        cosine_similarities = cosine_similarity(response)

        similar_dict = {}
        processed_docs = set()

        for i in range(len(docs)):
            if i in processed_docs:
                continue

            main_doc = docs.iloc[i]
            similar_dict[i] = []
            
            for j in range(i + 1, len(docs)):
                if j in processed_docs:
                    continue

                later_doc = docs.iloc[j]
                if later_doc['Date'] > main_doc['Date']:
                    similarity_score = cosine_similarities[i, j]
                    if similarity_score > 0.5:
                        similar_dict[i].append((j, similarity_score))
                        processed_docs.add(j)
        
        return similar_dict
    except Exception as e:
        return {"status": "error", "message": str(e)}
