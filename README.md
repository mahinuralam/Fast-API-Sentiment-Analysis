# Fast-API-Sentiment-Analysis

In this project, A RESTful API is created along with Machine Learning. Where base on a Text the
The machine learning model will provide a Sentiment Analysis of that Text as a response.

## Installation

To run this project locally following things need to be installed.

1. Python (3.9~)

## Follow these steps to set up the project:

1. Clone the repository:

```
git clone https://github.com/mahinuralam/Fast-API-Sentiment-Analysis
```

2. Navigate to the project directory:

```
cd Fast-API-Sentiment-Analysis
```

3. Install the dependencies:

```
pip install -r requirement.txt
```

4. StatsGary/setfit-ft-sentinent-eval
   This is a SetFit model that can be used for text classification.
   The model has been trained using an efficient few-shot learning technique that involves:

- Fine-tuning a Sentence Transformer with contrastive learning.
- Training a classification head with features from the fine-tuned Sentence Transformer.

```
python -m pip install setfit
```

5. Start the server:

```
uvicorn main:app --reload
```

- By default, the server will start on port 8000. You can access the APIs at http://localhost:8000/docs with Swagger.

## API Routes

The following routes are available in the API:

- POST /analyze - Create a new text.
- GET /analyze - Get all text with sentiment response.
- GET /analyze/:id - Get a specific post by ID with a sentiment response.
- PUT /analyze/:id - Update a post.
- DELETE /analyze/:id - Delete a post.

Please refer to the source code and documentation for more details on the API routes and request/response formats.

## License

MIT
