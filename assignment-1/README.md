# ✅ FIXED VERSION of metadata_extraction.ipynb
```
# Assignment 1 - Metadata Extraction from Legal Agreements

## 🧠 Problem Statement
Extract structured metadata fields from legal agreement documents (DOCX/PNG) using AI techniques — without using regex or template-based logic.

## 📁 Folder Structure
```
assignment-1/
├── metadata_extraction.ipynb       # Main solution notebook
├── api_service.py                  # (Optional) REST API service
├── data/
│   ├── train/                      # Train documents
│   ├── test/                       # Test documents
│   ├── train.csv                   # Ground truth metadata
│   └── test.csv                    # File names only
├── output/
│   ├── train_predictions.csv       # Your model’s output on train set
│   └── test_predictions.csv        # Your model’s output on test set
└── README.md
```

## ⚙️ Approach Summary
- Used **Cohere's `command-r-plus`** large language model to extract metadata from text.
- Processed `.docx`, `.pdf`, and `.png` files using Python libraries:
  - `python-docx`, `pdfplumber`, `pytesseract`
- Created prompts to extract:
  - `agreement_value`, `start_date`, `end_date`, `renewal_notice_days`, `party_one`, `party_two`
- Used a **zero-shot approach** — no training data required.

## 📊 Evaluation: Field-wise Recall on Train Set
| Field                  | Recall     |
|------------------------|------------|
| agreement_value        | 37.50%     |
| start_date             | 37.50%     |
| end_date               | 12.50%     |
| renewal_notice_days    | 0.00%      |
| party_one              | 0.00%      |
| party_two              | 12.50%     |

## ▶️ How to Run Notebook
1. Install dependencies:
```bash
pip install pandas cohere pdfplumber pytesseract python-docx tqdm
```

2. Add your **Cohere API key** in the notebook:
```python
COHERE_API_KEY = "your-api-key-here"
```

3. Run all cells in the notebook:
- Predictions will be saved to `output/` folder
- Recall on the train set will be printed

---

## 🔌 Optional: Run as a REST API (Extra Credit)
You can wrap the metadata extractor as an API using FastAPI.

### 📄 File: `api_service.py`
```bash
pip install fastapi uvicorn cohere
uvicorn api_service:app --reload
```

### 🚀 API Usage
- Run the server using the command above
- Then go to:
```
http://127.0.0.1:8000/docs
```
This opens the Swagger UI

### ✉️ POST /extract
**Input (JSON):**
```json
{
  "text": "This agreement is made on 1 Jan 2024 between John Doe and Jane Smith. The rent is $5000. It starts on 01.01.2024 and ends on 31.12.2024. Renewal notice is 60 days."
}
```

**Output (JSON):**
```json
{
  "metadata": {
    "agreement_value": "5000",
    "start_date": "01.01.2024",
    "end_date": "31.12.2024",
    "renewal_notice_days": "60",
    "party_one": "John Doe",
    "party_two": "Jane Smith"
  }
}
```

📍 You can also use tools like **Postman** or `curl`:
```bash
curl -X POST http://127.0.0.1:8000/extract -H "Content-Type: application/json" -d '{"text": "your agreement content here"}'
```

---

## 🚫 Limitations
- OCR-based PNG extraction may miss fields due to image noise
- Entity extraction (party names) shows lower accuracy in zero-shot mode

## 🙌 Author
Saurabh Kumar  
RV College of Engineering  
B.E in Computer Science & Engineering (Graduating 2025)
```