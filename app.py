import streamlit as st
import ast
import pandas as pd
import openai
import matplotlib
from openai.embeddings_utils import cosine_similarity

openai.api_key =  st.secrets["mykey"]
df = pd.read_csv("qa_dataset_with_embeddings.csv")

# Convert the string embeddings back to lists
df['Question_Embedding'] = df['Question_Embedding'].apply(ast.literal_eval)

def find_best_answer(user_question):
   # Get embedding for the user's question
   user_question_embedding = get_embedding(user_question)

   # Calculate cosine similarities for all questions in the dataset
   df['Similarity'] = df['Question_Embedding'].apply(lambda x: cosine_similarity(x, user_question_embedding))

   # Find the most similar question and get its corresponding answer
   most_similar_index = df['Similarity'].idxmax()
   max_similarity = df['Similarity'].max()

   # Set a similarity threshold to determine if a question is relevant enough
   similarity_threshold = 0.6  # You can adjust this value

   if max_similarity >= similarity_threshold:
      best_answer = df.loc[most_similar_index, 'Answer']
      return best_answer
   else:
      return "I apologize, but I don't have information on that topic yet. Could you please ask other questions?"




st.text_input("First name")

# Streamlit UI
st.title("Smart FAQ Assistant ")
question = st.text_input("Question")


if st.button("Trigger the answer"):
    caption, image_description = generate_copy(product_name, selected_features, selected_benefits, selected_audience, selected_pain_points, selected_desires, selected_channel, selected_tone)
    st.subheader("Answer:")
    st.text_area(st.write(generate_copy(question)))
    

def generate_copy(question):
    prompt = f"""
    **Your question:** {question}

    **Your answer:** find_best_answer(question)
    """
   
    return prompt




