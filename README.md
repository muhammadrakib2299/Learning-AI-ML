# Learning AI / ML

Notes, notebooks and small projects from my AI/ML learning path — from Python foundations to Streamlit apps and the Gemini API. Most of the notebook work follows Phitron's *AI Programming with Python* track.

## What's inside

| Folder | Contents |
|---|---|
| `Pre-Python for ML/` | Warm-up notebooks: variables, operators, conditionals, logical operators, digit summation |
| `Pythons foundations for Ml/` | Functions, return types, iterators, and OOP (encapsulation, inheritance, abstraction) |
| `Assignments/` | Course assignment notebooks |
| `Streamlit/` | Streamlit basics — text input, options, images and media elements |
| `Simple projects/Note Summery/` | Streamlit app: upload up to 3 note images to generate summaries and quizzes |
| `Googel gemini AI/` | First call to Google Gemini (`gemini-2.0-flash`) with the `google-genai` SDK |

## Run the examples

```bash
python -m venv .venv && source .venv/bin/activate
pip install jupyter streamlit google-genai python-dotenv

jupyter notebook                                   # open any .ipynb
streamlit run "Simple projects/Note Summery/app.py"

cp "Googel gemini AI/.env.example" "Googel gemini AI/.env"   # add your GEMINI_API_KEY
python "Googel gemini AI/app.py"
```

## Where this led

The fundamentals here fed into my applied ML projects — [PneumoScan](https://github.com/muhammadrakib2299/PneumoScan), [BanglaHealth-AI](https://github.com/muhammadrakib2299/BanglaHealth-AI), [VerifyAI](https://github.com/muhammadrakib2299/VerifyAI-fake-news-detector) and [MalVis](https://github.com/muhammadrakib2299/MalVis).

## License

[MIT](LICENSE) © Md. Rakib
