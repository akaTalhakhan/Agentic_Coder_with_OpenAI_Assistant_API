# 🚀 Agentic Coder with OpenAI Assistant API

<div align="center">

![AI Coding Companion](https://img.shields.io/badge/AI-Coding%20Companion-blue?style=for-the-badge&logo=openai)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green.svg?style=for-the-badge&logo=openai)
![Google](https://img.shields.io/badge/Google-Gemini_Pro-orange.svg?style=for-the-badge&logo=google)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**A powerful, intelligent AI-powered coding assistant that transforms your development workflow with advanced code analysis, optimization, and multi-model AI integration.**

[🚀 Quick Start](#-quick-start) • [✨ Features](#-features) • [📖 Documentation](#-usage) • [🤝 Contributing](#-contributing)

</div>

---

## 🌟 Overview

The **Agentic Coder** is a sophisticated AI-powered programming assistant built with Streamlit that leverages multiple state-of-the-art language models including **OpenAI GPT-4o**, **GPT-3.5 Turbo**, and **Google Gemini Pro**. This tool provides intelligent code analysis, bug detection, optimization suggestions, and real-time programming assistance through an intuitive web interface.

### 🎯 Key Highlights

- **🤖 Multi-Model AI Integration** - Seamlessly switch between OpenAI and Google Gemini models
- **🔍 Advanced Code Analysis** - Deep code inspection with security scanning and performance optimization
- **💬 Real-time AI Chat** - Interactive coding assistant with contextual understanding
- **🧪 Automated Testing** - Generate comprehensive unit tests and documentation
- **📊 Visual Analytics** - Code complexity analysis and performance metrics
- **🔒 Security-First** - Built-in security scanning and best practices enforcement

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🧠 **Intelligent Code Analysis**
- **Code Quality Assessment** - Comprehensive code review and quality scoring
- **Bug Detection** - Automated identification of potential issues and vulnerabilities
- **Performance Optimization** - Suggestions for improving code efficiency
- **Security Scanning** - Detection of security vulnerabilities and best practices

</td>
<td width="50%">

### 🔄 **Multi-Model AI Support**
- **OpenAI GPT-4o** - Advanced reasoning and code generation
- **GPT-3.5 Turbo** - Fast and efficient for most coding tasks
- **Google Gemini Pro** - Multimodal AI with advanced capabilities
- **Smart Model Routing** - Automatic selection based on task complexity

</td>
</tr>
<tr>
<td width="50%">

### 💻 **Developer Experience**
- **Interactive Code Editor** - Syntax highlighting and real-time editing
- **File Upload Support** - Direct upload of code files for analysis
- **Export Capabilities** - Save results in multiple formats (PDF, JSON, Markdown)
- **Project History** - Track analysis results and code changes

</td>
<td width="50%">

### 🧪 **Testing & Documentation**
- **Automated Test Generation** - Create comprehensive unit tests
- **Documentation Generation** - Auto-generate code documentation
- **Code Conversion** - Convert between different programming languages
- **Best Practices** - Enforce coding standards and conventions

</td>
</tr>
</table>

---

## 🚀 Quick Start

### 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.9+** - [Download Python](https://python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **API Keys**:
  - OpenAI API Key - [Get here](https://platform.openai.com/account/api-keys)
  - Google Gemini API Key - [Get here](https://makersuite.google.com/app/apikey)

### ⚡ Installation

```bash
# 1. Clone the repository
git clone https://github.com/akaTalhakhan/Agentic_Coder_with_OpenAI_Assistant_API.git
cd Agentic_Coder_with_OpenAI_Assistant_API

# 2. Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the application
streamlit run main.py
```

### 🌐 Access the Application

Once the installation is complete, open your browser and navigate to:
```
http://localhost:8501
```

---

## 🧠 Supported AI Models

<div align="center">

| Model | Provider | Capabilities | Best For | Cost |
|-------|----------|-------------|----------|------|
| **GPT-4o** | OpenAI | Advanced reasoning, multimodal | Complex analysis, architecture design | $$$ |
| **GPT-3.5 Turbo** | OpenAI | Fast processing, good quality | General coding tasks, quick fixes | $ |
| **Gemini Pro** | Google | Multimodal, efficient | Code review, documentation | $$ |

</div>

---

## 📖 Usage

### 🎮 Getting Started with the Interface

1. **Configure API Keys** 📝
   - Select your preferred AI model from the sidebar
   - Enter your API key for the chosen model
   - Click "Validate API Key" to confirm

2. **Upload or Write Code** 💻
   - Use the file uploader to import existing code files
   - Or write/paste code directly in the editor
   - Supports multiple programming languages

3. **Choose Analysis Options** ⚙️
   - Select desired analysis features (complexity, security, optimization)
   - Choose target language for code conversion
   - Enable additional features like test generation

4. **Get AI Insights** 🤖
   - Click "Process Code" to run comprehensive analysis
   - Use the AI chat for specific questions
   - Export results for future reference

### 🔧 Advanced Features

#### Security Analysis
```python
# The tool automatically detects security issues like:
password = "hardcoded_password"  # ❌ Security risk detected
eval(user_input)                 # ❌ Dangerous eval usage
```

#### Performance Optimization
```python
# Before (inefficient)
for i in range(len(items)):
    print(items[i])

# After (optimized suggestion)
for item in items:
    print(item)
```

#### Code Quality Metrics
- **Cyclomatic Complexity** - Measure code complexity
- **Maintainability Index** - Assess code maintainability
- **Technical Debt** - Identify areas needing refactoring

---

## 📁 Project Structure

```
agentic-coder/
├── 📄 main.py              # Main Streamlit application
├── 🤖 helper_ai.py         # AI model integration and response handling
├── ⚙️ config.py            # Configuration settings and constants
├── 📋 requirements.txt     # Python dependencies
├── 📖 README.md           # Project documentation
├── 🔒 .gitignore          # Git ignore rules
└── 📁 .git/               # Git repository data
```

### 📄 File Descriptions

- **`main.py`** - Core Streamlit application with UI components and user interaction logic
- **`helper_ai.py`** - Handles communication with OpenAI and Google Gemini APIs
- **`config.py`** - Centralized configuration management for all application settings
- **`requirements.txt`** - Complete list of Python package dependencies

---

## 🛠️ Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Google Gemini Configuration
GOOGLE_API_KEY=your_google_api_key_here

# Application Settings
DEBUG=False
LOG_LEVEL=INFO
```

### Custom Configuration

Modify `config.py` to customize:

- **AI Model Settings** - Temperature, max tokens, model preferences
- **UI Customization** - Themes, layouts, component settings
- **Analysis Features** - Enable/disable specific analysis tools
- **Security Settings** - Configure security scanning patterns

---

## 🎨 Screenshots






## 🚀 Deployment

### Local Development
```bash
streamlit run main.py --server.port 8501
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address", "0.0.0.0"]
```

### Cloud Deployment
- **Streamlit Cloud** - Direct GitHub integration
- **Heroku** - Easy deployment with Procfile
- **AWS/GCP** - Scalable cloud deployment options

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🐛 Bug Reports
- Use the [issue tracker](https://github.com/akaTalhakhan/Agentic_Coder_with_OpenAI_Assistant_API/issues)
- Include detailed reproduction steps
- Provide system information and error logs

### 💡 Feature Requests
- Describe the feature and its benefits
- Provide use cases and examples
- Consider implementation complexity

### 🔧 Pull Requests
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### 📝 Development Setup
```bash
# Clone your fork
git clone https://github.com/your-username/Agentic_Coder_with_OpenAI_Assistant_API.git

# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests before committing
pytest tests/
```

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Agentic Coder Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 🙏 Acknowledgments

- **OpenAI** for providing the GPT models and API
- **Google** for the Gemini AI platform
- **Streamlit** for the amazing web framework
- **Python Community** for the excellent libraries and tools
- **Contributors** who help improve this project


<div align="center">


*Empowering developers with AI-driven coding assistance*

