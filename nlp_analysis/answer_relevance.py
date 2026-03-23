from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read your transcript
with open("transcript.txt", "r") as f:
    candidate_answer = f.read()

# Define ideal answer (you can change this)
ideal_answer = "Explain your project and experience in AI and machine learning"

# Convert to embeddings
emb1 = model.encode(candidate_answer, convert_to_tensor=True)
emb2 = model.encode(ideal_answer, convert_to_tensor=True)

# Calculate similarity
score = util.cos_sim(emb1, emb2)

print("Answer Relevance Score:", float(score[0][0]) * 100)