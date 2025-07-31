# Resume Chatbot 🤖

An intelligent AI-powered chatbot that acts as a personal assistant for your resume, allowing users to have natural conversations about your background, skills, and experience.

## ✨ Features

- **Natural Conversation**: Chat with an AI that responds as if it's you (Vishak) having a personal conversation
- **Resume Integration**: Loads your resume data from a JSON file and uses it to provide accurate responses
- **Interactive Web Interface**: Beautiful Gradio-based web interface for easy interaction
- **OpenAI Integration**: Powered by GPT-4o-mini for intelligent and contextual responses
- **Conversation Memory**: Maintains chat history for contextual conversations
- **Error Handling**: Robust error handling for API limits and network issues

## 🚀 Demo

The chatbot provides a conversational interface where users can ask questions like:
- "Tell me about your experience"
- "What are your technical skills?"
- "What projects have you worked on?"
- "Why should I hire you?"

And the AI responds naturally as if it's you having a conversation about your background.

## 🛠️ Technology Stack

- **Python 3.10+**
- **Gradio** - Web interface framework
- **OpenAI API** - GPT-4o-mini for natural language processing
- **FastAPI** - Backend framework (used by Gradio)
- **python-dotenv** - Environment variable management

## 📋 Prerequisites

- Python 3.10 or higher
- OpenAI API key
- Git

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd my_resume_chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Prepare your resume data**
   - Update the `resume.json` file with your personal information
   - Include your experience, skills, projects, and other relevant details

## 🎯 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Access the web interface**
   - Open your browser and go to `http://localhost:7860`
   - The chatbot interface will load automatically

3. **Start chatting**
   - Type your questions in the text box
   - Press Enter or click "Send" to get responses
   - The AI will respond as if it's you having a conversation

## 📁 Project Structure

```
my_resume_chatbot/
├── main.py              # Main application file
├── requirements.txt     # Python dependencies
├── resume.json         # Your resume data
├── .env               # Environment variables (create this)
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔧 Configuration

### Resume Data Format

The `resume.json` file should contain your personal information in a structured format:

```json
{
  "name": "Your Name",
  "title": "Your Title",
  "summary": "Professional summary",
  "experience": [
    {
      "company": "Company Name",
      "role": "Job Title",
      "duration": "Time Period",
      "responsibilities": ["Responsibility 1", "Responsibility 2"]
    }
  ],
  "skills": {
    "languages": ["Python", "JavaScript"],
    "frameworks": ["React", "FastAPI"]
  }
}
```

### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

## 🎨 Customization

### Modifying the AI Personality

You can customize how the AI responds by modifying the `system_prompt` in `main.py`. The current prompt makes the AI respond as if it's you having a natural conversation.

### Adding New Features

- **File Upload**: Add resume file upload functionality
- **Voice Chat**: Integrate speech-to-text and text-to-speech
- **Multi-language Support**: Add support for different languages
- **Analytics**: Track conversation metrics and user interactions

## 🐛 Troubleshooting

### Common Issues

1. **"No module named 'gradio'"**
   - Make sure you've activated your virtual environment
   - Run `pip install -r requirements.txt`

2. **"OpenAI API key not found"**
   - Check that your `.env` file exists and contains the correct API key
   - Ensure the key is valid and has sufficient credits

3. **"Pydantic schema generation error"**
   - This is a known compatibility issue with certain package versions
   - The current `requirements.txt` uses compatible versions

4. **Port already in use**
   - The default port is 7860
   - You can modify the port in the `demo.launch()` call

### Error Messages

- **"Open AI limit exceeded"**: Your OpenAI API quota has been reached
- **"Invalid Text"**: The input text couldn't be processed
- **"An Error Occurred"**: General error, check the console for details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- OpenAI for providing the GPT API
- Gradio team for the excellent web interface framework
- The open-source community for various Python packages

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the error messages in the console
3. Ensure all dependencies are properly installed
4. Verify your OpenAI API key is valid

---

**Happy Chatting! 🎉**

*This chatbot brings your resume to life through natural conversation, making it easier for potential employers and collaborators to learn about your background and experience.* 