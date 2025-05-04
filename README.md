# 🛡️ Sentinel AI
<p align="left">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python Version">
  <img src="https://img.shields.io/badge/Streamlit-1.33.0-ff4b4b?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/MySQL-8.0-blue?logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Ollama-LLM-green?logo=openai&logoColor=white" alt="Ollama">
  <img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="License">
</p>

**The Future of Intelligent Criminal Search Systems**

---

## 🚀 Overview

**Sentinel AI** is an advanced AI-powered intelligence tool designed to **rapidly search and retrieve criminal data** using **state-of-the-art Retrieval-Augmented Generation (RAG)** techniques. Built with the synergy of modern Python frameworks and AI tools, Sentinel AI blends **Streamlit**, **Tortoise ORM**, **Aerich**, **Ollama**, and **MySQL** to deliver lightning-fast, contextual search and analysis across criminal records databases.

---

## 🧠 Core Features

- 🔍 **RAG-Powered Search**: Combines information retrieval with generative AI for deep, context-aware querying.
- 🖥️ **Interactive UI**: Built with Streamlit for a sleek and responsive front-end experience.
- 🐢 **Tortoise ORM + Aerich**: Modern, async-ready database modeling and migrations.
- 🐬 **MySQL Backend**: Robust and scalable relational data storage.
- 🤖 **Ollama Integration**: Harness the power of local LLMs for blazing-fast, secure language generation.
- ⚡ **Asynchronous Performance**: Built with performance and scalability in mind using Python’s async ecosystem.

---

## 🏗️ Tech Stack

| Component      | Technology         |
|----------------|--------------------|
| 🧠 AI Engine    | Ollama (LLMs)       |
| 🧪 Retrieval    | RAG (Retrieval-Augmented Generation) |
| 🌐 UI          | Streamlit          |
| 🐢 ORM         | Tortoise ORM       |
| 🔄 Migrations  | Aerich             |
| 🗄️ Database     | MySQL              |
| 🐍 Language    | Python 3.10+        |

---

## 📦 Installation

```bash
git clone https://github.com/your-username/sentinel-ai.git
cd sentinel-ai
pip install -r requirements.txt

# Run database migrations
aerich upgrade

# Launch the app
streamlit run app.py