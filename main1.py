import tkinter as tk
import joblib
import scipy.sparse



# Load the trained model and vectorizer
model = joblib.load("rf_sentiment_model.pkl")  # Ensure this file exists
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")  # Ensure this file exists

# Create Tkinter window
root = tk.Tk()
root.title("Tamil Sentiment Analysis")
root.geometry("400x300")

# Create input field
entry_label = tk.Label(root, text="Enter Tamil Text:")
entry_label.pack()

entry = tk.Entry(root, width=40)
entry.pack()

# Result Label
result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

# Function to predict sentiment
def predict_sentiment():
    user_text = entry.get().strip()

    if not user_text:
        result_label.config(text="Please enter text!", fg="red")
        return

    try:
        print(f"User Input: {user_text}")

        processed_text = user_text.lower()  
        print(f"Processed Text: {processed_text}")

        prediction = model.predict([processed_text])[0]  
        print(f"Raw Model Prediction: {prediction}")  # 🔍 Debugging log

        # ✅ Check if labels are correctly mapped
        if isinstance(prediction, str):
            sentiment = prediction  # If the model returns text labels like "Happy"
        else:
            # If the model returns numerical values (e.g., 1, 0), map them manually
            sentiment_mapping = {1: "Positive", 0: "Negative"}
            sentiment = sentiment_mapping.get(prediction, "Unknown")

        print(f"Final Sentiment for GUI: {sentiment}")
        result_label.config(text=f"Predicted Sentiment: {sentiment}", fg="green")
        
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")
        print(f"Error: {e}")




# Create Predict Button
predict_button = tk.Button(root, text="Predict", command=predict_sentiment)
predict_button.pack()

# Run Tkinter event loop
root.mainloop()
