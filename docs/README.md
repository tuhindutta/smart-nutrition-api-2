# 🍏 NutriGuide API

### [🔗 Nutrition guide API documentation link](https://tuhindutta.github.io/nutriguide/api_doc.html)
### [🔗 Docker Hub image and user guide](https://hub.docker.com/r/tkdutta/nutriguide-api)

NutriGuide is a lightweight **nutrition and health assistant** powered by LLMs.  
It provides personalized food recommendations based on a user’s **health status** and **nutrition values** of products.  
The project is built with **FastAPI** and can be deployed using **Docker**.

---

## ✨ Features
- Set **health profile** (dietary conditions, goals, etc.)
- Register **food products** with nutrition values
- Query the assistant for **personalized nutrition guidance**
- REST API powered by **FastAPI** (`/docs` for Swagger UI)
- Containerized deployment with **Docker**

---

## 📂 Code Structure
```bash
nutriguide/
├── utils.py       # JSONL helpers + LLM class (Groq API wrapper)
├── main.py        # FastAPI app with endpoints
├── Dockerfile     # Container configuration
├── requirements.txt
└── README.md
```

---

## 🚀 Usage Notes
1. Uses Groq API with meta-llama/llama-4-scout-17b-16e-instruct model
2. Conversation history is maintained in-session
3. Designed for concise nutrition suggestions only

---

## 📈 [Future Prospects](https://tuhindutta.github.io/nutriguide/future-prospect)

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes. For more details and updates, visit the [GitHub Repository](https://github.com/tuhindutta/nutriguide).
