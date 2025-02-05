**Building a Smart FAQ Assistant with Streamlit & Embedding**

**Goal:**

Create a Streamlit web application that allows users to ask questions about heart, lung, and blood-related health topics. The app will use the provided [`qa_dataset_with_embeddings.csv`](https://drive.google.com/file/d/1g6DaU_WcdlHFYlSoeVqEzyFVq05IiKQq/view?usp=drive_link) dataset, its corresponding embeddings (`Question_Embedding` column), and an appropriate embedding model to find the most relevant answer.

**Dataset:**
  * `qa_dataset_with_embeddings.csv` :
  * `Question`: Contains user questions.
  * `Answer`: Provides corresponding answers.
  * `Question_Embedding`: Stores vector representations (embeddings) of the questions.

**Tasks:**

1. Load Data & Embeddings:
  * Read the CSV file into a Pandas DataFrame.
  * Load the pre-calculated question embeddings (you can use libraries like numpy to load them as arrays).

2. Choose an Embedding Model:
  * Select a suitable embedding model that can generate embeddings for new user questions.
3. Build the Streamlit Interface:
  * Create a text input field for users to enter their questions.
  * Add a button to trigger the answer search.
  * Design an output area to display the answer.
4. Implement the Question Answering Logic:
  * When the button is clicked:
    * Get the user's question.
    * Generate an embedding for the user's question using the selected model.
    * Calculate the cosine similarity between the user's question embedding and all the question embeddings in the dataset.
    * Find the question with the highest similarity score.
    * If the similarity score is above a certain threshold (experiment to find a good value), display the corresponding answer.
    * If no relevant answer is found (below the threshold), display the message: "I apologize, but I don't have information on that topic yet. Could you please ask other questions?"
5. Additional Features (Optional):
  * Add a "Clear" button to reset the input field.
  * Display the similarity score next to the answer.
  * Allow users to rate the answer's helpfulness.
  * Include a section to display common FAQs or a search bar to filter questions.
