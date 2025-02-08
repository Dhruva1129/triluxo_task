import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load the FAISS index and model
model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.read_index('app/models/course_embeddings.index')

class Chatbot:
    def get_response(self, user_input):
        # Create embedding for user input
        user_embedding = model.encode([user_input])

        # Search for similar courses
        distances, indices = index.search(np.array(user_embedding), k=3)

        # Return the top 3 similar courses
        results = []
        for idx in indices[0]:
            results.append(courses[idx])

        return results
