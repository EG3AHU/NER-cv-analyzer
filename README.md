# CV NLP Analysis System 📄🔍

An intelligent Resume Parsing and Analysis tool built with Python, Streamlit, and spaCy. This project demonstrates the practical application of Natural Language Processing (NLP) in human resources and administrative systems. 

Developed as an academic project for the Management Information Systems (MIS) department at Bilecik Şeyh Edebali University, the system is designed to efficiently extract, structure, and analyze unstructured resume data.

## ✨ Key Features

* **PDF Text Extraction:** Reads and extracts plain text from uploaded CVs using `pdfplumber`.
* **Named Entity Recognition (NER):** Utilizes `spaCy` to identify and categorize key entities such as Organizations, Dates, Persons, and Locations.
* **Linguistic Analysis & POS Tagging:** Breaks down the document structure to extract Top Nouns, Verbs, and Adjectives, providing insights into the candidate's action-oriented language.
* **Smart Contact Extraction:** Automatically identifies and extracts Emails and Phone Numbers using Regex.
* **Targeted Skills Detection:** Includes a rule-based matching system tailored for IT, Network Engineering, and System Administration roles (e.g., CCNA, MCSA, Windows Server, Linux, Firewalls).
* **Interactive UI:** Built with `Streamlit` to provide a user-friendly, web-based dashboard for instant resume analysis.

## 🛠️ Tech Stack

* **Python 3.x**
* **Streamlit** (Web Interface)
* **spaCy** (NLP & Linguistic Features)
* **pdfplumber** (PDF Parsing)

## 🚀 Live Demo
*(You can place your Streamlit Cloud link here later)*

## 💡 Academic Context
This project serves as a proof-of-concept for automating recruitment workflows. By highlighting the limitations of pre-trained generic NER models in specialized domains (like IT/Networking), it lays the groundwork for developing custom, domain-specific NER pipelines for HR systems.
