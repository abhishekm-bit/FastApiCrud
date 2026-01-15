# import faiss
# import numpy as np

# dimension = 384
# index = faiss.IndexFlatL2(dimension)
# texts = []


# # vectors means here embedded data 

# def store_vectors(vectors, data):
#     # Saved vector with text
#     index.add(np.array(vectors))
#     # below saves matching text
#     texts.extend(data)

# def search(vector):
#     D, I = index.search(np.array(vector), 5)
#     return [texts[i] for i in I[0]]



import faiss
import numpy as np

dimension = 384

# index means vector db that store multiple vecotrs t

# Use Inner Product got there index theres
# Dot product done in the abvoe 
index = faiss.IndexFlatIP(dimension)

texts = []

# normalize makes each vector length 1 
# 

def normalize(vectors):
    vectors = np.array(vectors).astype("float32")
    faiss.normalize_L2(vectors) 
    # Divide by length above 
    # Divides each vector by its own length
    return vectors

def store_vectors(vectors, data):
    vectors = normalize(vectors)
    index.add(vectors)
    texts.extend(data)

def search(vector):
    vector = normalize(vector)
    # D → similarity scores
    # I → index positions
    D, I = index.search(vector, 5)
    return [texts[i] for i in I[0]]
