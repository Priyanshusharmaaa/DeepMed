# DeepMed AI

[![License](https://img.shields.io/github/license/Priyanshusharmaaa/DeepMed)](LICENSE)

DeepMed AI is a **state-of-the-art medical imaging platform** that generates context-aware medical reports from chest X-ray images. By combining **advanced vision-language models** like BioViLT and BioGPT, DeepMed AI aims to assist healthcare professionals in automating the interpretation of radiological images, reducing manual effort, and improving report consistency.

You can access the live demo here: [DeepMed AI Streamlit App](https://xyz.link)

---

## 🌟 Project Highlights

- **Automated Medical Report Generation**: Converts chest X-ray images into detailed, clinically relevant reports.  
- **Vision-Language Integration**: Uses BioViLT to extract image features and aligns them with textual data for accurate reporting.  
- **AI-Powered Chatbot**: Interactive chatbot for querying medical findings and explanations.  
- **End-to-End Pipeline**: Includes preprocessing, feature extraction, alignment, report generation, and post-processing.  
- **Demo Video**: [DeepMedAI.mp4](DeepMedAI.mp4) demonstrates the full workflow.

---

## 🏗 Architecture Overview

The project is divided into several modular components:

1. **Image Feature Extraction (`phrase_ground.py`)**  
   - Extracts meaningful visual features from chest X-ray images using BioViLT.  
   - Handles localization of findings and feature grounding for accurate report generation.

2. **Report Generation (`report_gen.py`)**  
   - Fine-tunes BioGPT on medical text data to generate structured and coherent reports.  
   - Produces clinically relevant observations in a human-readable format.

3. **Interactive Chatbot (`chatbotBackend.py`, `app.py`)**  
   - Backend processes user queries and generates AI-based explanations.  
   - Frontend uses Streamlit for an intuitive interface to query findings, generate reports, and review results.

4. **Deployment (`main.py`)**  
   - Integrates all modules for seamless execution.  
   - Provides an interactive interface for medical professionals or users to upload images and obtain reports.

---

## 📁 Repository Structure

```plaintext
DeepMed/
├── app.py               # Streamlit app frontend
├── main.py              # Main script integrating all modules
├── report_gen.py        # Medical report generation
├── chatbotBackend.py    # Chatbot backend logic
├── phrase_ground.py     # Image feature extraction and grounding
├── requirements.txt     # Python dependencies
├── DeepMedAI.mp4        # Demo video
├── LICENSE              # MIT License
└── .gitignore

