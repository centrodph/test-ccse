# Questions Nationality - CCSE Exam Practice

This project is a comprehensive toolset for practicing and studying questions for the Spanish nationality exam (CCSE). It combines automated data processing with an interactive web interface.

## 🚀 Project Overview

The project is divided into two main parts:
1.  **Data Processing Tools**: Python scripts used to clean and format audio transcriptions into a usable JSON format.
2.  **Web Application**: A modern React-based dashboard that allows users to browse questions, listen to audio, and verify answers.

---

## 📁 Project Structure

```text
.
├── AUDIOS_CCSE_2026/      # Raw audio source files
├── scripts/                # Python scripts for data management
│   ├── convert_transcriptions.py  # Cleans and splits raw transcriptions
│   └── audio_transcriptions.json  # Raw/Processed data source
│
└── web-app/                # React + TypeScript + Vite Application
    ├── public/             # Static assets
    │   └── audios/         # MP3 files for the questions
    ├── src/
    │   ├── components/     # UI Components (QuestionCard, etc.)
    │   ├── data/           # Application data (questions.json)
    │   └── App.tsx         # Main application logic
    └── package.json        # Web app dependencies and scripts
```

---

## 🛠️ Local Development Setup

Follow these steps to set up and run the project on your local machine.

### 1. Prerequisites
- **Node.js** (v18 or higher)
- **Python** (v3.10 or higher)

### 2. Python Environment & Data Processing
The data processing scripts require specific Python libraries. It is recommended to use a virtual environment.

```bash
# From the project root
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install faster-whisper tqdm
```

#### Running the Scripts:
- **Transcription**: To transcribe the raw audios in `AUDIOS_CCSE_2026/` to text:
  ```bash
  python3 scripts/transcribe_audios.py
  ```
- **Conversion/Cleaning**: To split the text into structured questions and answers:
  ```bash
  python3 scripts/convert_transcriptions.py
  ```

### 3. Web Application
The frontend is built with Vite and React.

```bash
# Navigate to the web-app directory
cd web-app

# Install dependencies
npm install

# Start the development server
npm run dev
```
Once the server is running, open [http://localhost:5173/test-ccse/](http://localhost:5173/test-ccse/) in your browser.

---

## 🚀 Deployment

This project is configured for automated deployment to **GitHub Pages** via GitHub Actions.

- **Vite Configuration**: The `base` path is set to `/test-ccse/` in `vite.config.ts`.
- **Workflow**: Any push to the `main` branch triggers the `.github/workflows/deploy.yml` action, which builds the app and deploys it.

The live version can be accessed at: `https://centrodph.github.io/test-ccse/`

---

## ✨ Features

-   **Interactive Question Cards**: Browse through the complete list of CCSE questions.
-   **Audio Integration**: Listen to the actual audio recordings for each question.
-   **Structured Data**: Cleaned and formatted data for better readability.
-   **Modern Tech Stack**: Built with React 19, TypeScript, and Vite for a fast and reliable experience.

---

## 📝 License
This project is for educational and study purposes.
