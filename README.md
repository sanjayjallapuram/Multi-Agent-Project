# 🔬 Multi-Agent Research System

An AI-powered **multi-agent research assistant** that automatically searches the web, extracts detailed information from relevant sources, generates a structured research report, and evaluates the report using a dedicated critic agent.

## 🚀 Key Features

- **Search Agent** — Searches the web for recent and reliable information using Tavily.
- **Reader Agent** — Selects a relevant URL from the search results and extracts deeper webpage content.
- **Writer Agent** — Converts the collected research into a structured professional report.
- **Critic Agent** — Reviews the generated report and provides a score, strengths, areas for improvement, and an overall verdict.
- **Streamlit UI** — Provides an interactive interface for entering research topics and viewing each pipeline stage.
- **Report Download** — Allows the generated research report to be downloaded as a text file.

## 🏗️ Architecture

```text
                    ┌─────────────────────┐
                    │    User / Topic     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Search Agent     │
                    │   Tavily Web Search │
                    └──────────┬──────────┘
                               │
                         Search Results
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Reader Agent     │
                    │   URL Web Scraper   │
                    └──────────┬──────────┘
                               │
                        Scraped Content
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Writer Chain     │
                    │  Research Report    │
                    └──────────┬──────────┘
                               │
                         Generated Report
                               │
                               ▼
                    ┌─────────────────────┐
                    │    Critic Chain     │
                    │ Report Evaluation   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Final Report +      │
                    │ Critic Feedback     │
                    └─────────────────────┘
```

The pipeline executes the four stages sequentially and stores intermediate outputs in a shared state dictionary. 

## 🧠 Agent Responsibilities

### 1. Search Agent 🔎

The Search Agent is responsible only for web research. It uses the `web_search` tool and returns search results containing titles, URLs, and snippets.

### 2. Reader Agent 📖

The Reader Agent receives the search results, identifies the most relevant URL, and uses the `scrape_url` tool to extract deeper webpage content.

### 3. Writer Agent ✍️

The Writer Chain combines the search results and scraped content to generate a structured research report containing:

- Introduction
- Key Findings
- Conclusion
- Sources



### 4. Critic Agent 🧐

The Critic Chain evaluates the generated report and returns:

- Score out of 10
- Strengths
- Areas to improve
- One-line verdict



## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangChain Agents**
- **Groq LLM**
- **Tavily Search API**
- **BeautifulSoup**
- **Requests**
- **Streamlit**
- **python-dotenv**
- **Rich**

The project dependencies are defined in `requirements.txt`.

The pipeline passes the search results and scraped content into the writer, then sends the generated report to the critic for evaluation.

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

The Tavily client reads the API key from the environment, while the LLM is configured through `ChatGroq`. 

## ▶️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd multi-agent-research
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure API keys

Create `.env` and add your Tavily and Groq API keys.

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

Then open the Streamlit URL displayed in the terminal.

## 💻 Example

Enter a topic such as:

```text
Impact of AI on software engineering jobs
```

The system will automatically:

1. Search for relevant information.
2. Select and scrape a relevant source.
3. Generate a structured research report.
4. Evaluate the report using the critic.
5. Display the results in the Streamlit interface.
6. Allow the report to be downloaded.


