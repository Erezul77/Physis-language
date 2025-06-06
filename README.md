# Physis Reflector API

🌱 **Physis** is a recursive symbolic language inspired by Nature. This API lets you reflect on Physis expressions using a custom parser and symbolic meaning engine.

## 🔁 Example

POST to `/reflect` with:
```json
{ "code": "(🌱☯)" }
```

Response:
```json
{
  "reflection": [
    {
      "group": [
        { "symbol": "🌱", "meaning": "growth, potential, emergence" },
        { "symbol": "☯", "meaning": "duality, harmony, balance" }
      ]
    }
  ]
}
```

## 🚀 How to run
```bash
pip install flask
python app.py
```

## 🌐 Deploy to Hugging Face
Just upload this folder as a new Space (Python + Flask template).
