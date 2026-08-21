"""
About page - Information about MindBridge.
Displays project overview, technology stack, architecture, and disclaimers.
"""

import streamlit as st

from components.common import render_header, render_disclaimer
from components.sidebar import render_sidebar
from utils.session import SessionManager


# Page configuration
st.set_page_config(
    page_title="MindBridge - About",
    page_icon="ℹ️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session
SessionManager.initialize_session()

# Render sidebar
render_sidebar()


def main():
    """Main function for the About page."""
    render_header("ℹ️ About MindBridge", "Learn more about this project")
    
    # Introduction section
    st.markdown("""
    ## What is MindBridge?
    
    MindBridge is an intent-based conversational support application designed to help you 
    explore and understand your thoughts and feelings through supportive conversation.
    
    ### 🎯 Mission
    
    To provide a safe, judgment-free space where you can express yourself and gain clarity 
    through supportive conversation, powered by explainable, rule-based intelligence.
    """)
    
    st.divider()
    
    # How it works
    st.markdown("""
    ## 🔍 How Does It Work?
    
    MindBridge uses a rule-based conversation system that:
    
    1. **Analyzes** your messages for intent and emotional content
    2. **Detects** patterns and triggers in your conversation
    3. **Provides** supportive and relevant responses
    4. **Generates** insights and personalized recommendations
    
    ### 🧠 The Process
    
    When you send a message, it goes through several stages:
    
    1. **Preprocessing** - Clean and normalize your message
    2. **Safety Check** - Ensure the conversation is safe and appropriate
    3. **Intent Detection** - Identify what you're expressing (stress, anxiety, etc.)
    4. **Entity Extraction** - Find key topics and triggers
    5. **Context Analysis** - Understand the conversation history
    6. **Response Generation** - Create a supportive, relevant response
    7. **Recommendation Engine** - Suggest actionable steps
    """)
    
    st.divider()
    
    # Technology stack
    st.markdown("""
    ## 🛠️ Technology Stack
    
    MindBridge is built with a modern, lightweight architecture:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 📱 Frontend (Streamlit)
        - **Python 3.11+**
        - **Streamlit** - UI framework
        - **Requests** - API communication
        - **Session State** - Temporary data storage
        - **Mobile-responsive** - Works in Android WebView
        - **No databases** - Privacy-first approach
        
        ### ⚡ Key Frontend Features
        - Clean, calming interface
        - Real-time chat
        - Quick action buttons
        - Explainable AI responses
        - Mood visualization
        - Personal insights
        - Actionable recommendations
        """)
    
    with col2:
        st.markdown("""
        ### 🚀 Backend (FastAPI)
        - **Python 3.11+**
        - **FastAPI** - High-performance API
        - **Pydantic** - Data validation
        - **Rule-based engines** - No ML/LLM required
        - **Session management** - Context tracking
        - **CORS enabled** - Cross-origin support
        
        ### 🧩 Backend Components
        - Preprocessing engine
        - Safety detection
        - Intent detection
        - Entity extraction
        - Context management
        - Response generation
        - Recommendation system
        """)
    
    st.divider()
    
    # Architecture diagram
    st.markdown("""
    ## 🏗️ Architecture Overview
    
    MindBridge follows a clean, scalable architecture:
    """)
    
    # ASCII art architecture in markdown
    st.markdown("""
    ANDROID APP
│
▼
WEBVIEW
│
▼
┌─────────────────┐
│ STREAMLIT │
│ FRONTEND │
└─────────────────┘
│
┌──────────────────┼──────────────────┐
▼ ▼ ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│ CHAT │ │ MOOD │ │ INSIGHTS │
└──────────┘ └──────────┘ └──────────┘
│ │ │
└──────────────────┼──────────────────┘
│
▼
┌─────────────────┐
│ FASTAPI │
│ BACKEND │
└─────────────────┘
│
▼
┌─────────────────┐
│ MIND BRIDGE │
│ ENGINES │
├─────────────────┤
│ Preprocessing │
│ Safety │
│ Intent │
│ Entity │
│ Context │
│ Response │
│ Recommendation │
└─────────────────┘
""")

st.divider()

# Key features
st.markdown("""
## 🚀 Key Features & Benefits

### 🤖 No LLM Required
MindBridge operates entirely on **rule-based systems**, making it:
- **Fast** - Responses in milliseconds
- **Privacy-focused** - No data sent to external AI services
- **Explainable** - Every response includes the reasoning behind it
- **Lightweight** - Minimal computational requirements
- **Cost-effective** - No expensive API calls

### 🔍 Explainable AI
Every response includes a detailed explanation:
- **Detected Intent** - What we understood from your message
- **Confidence Level** - How confident we are in the detection
- **Matched Signals** - Keywords and phrases that triggered the response
- **Safety Assessment** - How we're handling your conversation

### 🔒 Privacy-Focused
- **No Database Storage** - Your conversations are never saved
- **Session-Based** - Data exists only for your current session
- **No Tracking** - No analytics, no cookies, no tracking pixels
- **Temporary Processing** - All analysis is done in real-time

### 📊 Comprehensive Analysis
- **Mood Tracking** - Visualize your emotional patterns
- **Pattern Recognition** - Understand recurring themes
- **Trigger Detection** - Identify what's affecting you
- **Progress Monitoring** - See how your conversations evolve

### 💡 Actionable Insights
- **Personalized Recommendations** - Tailored to your situation
- **Practical Suggestions** - Real steps you can take
- **Supportive Guidance** - Encouragement and understanding
- **Coping Strategies** - Tools for managing difficult emotions
""")

st.divider()

# Project philosophy
st.markdown("""
## 💭 Project Philosophy

### Why "MindBridge"?

The name reflects our core purpose: **bridging the gap between your thoughts and clarity**.

- **Mind** represents your thoughts, feelings, and experiences
- **Bridge** represents the connection to understanding and support

### Our Approach

1. **Conversation-First** - Natural, supportive dialogue
2. **Explainable** - Transparent and understandable
3. **Accessible** - Available on any device
4. **Privacy-Respecting** - Your data stays yours
5. **Supportive** - Encouraging, non-judgmental
6. **Practical** - Actionable insights and recommendations

### What We're Not

MindBridge is **not**:
- ❌ A medical diagnosis tool
- ❌ A crisis intervention service
- ❌ A replacement for professional therapy
- ❌ A clinical mental health application
- ❌ An emergency response system
- ❌ A substitute for human connection

### What We Are

MindBridge is:
- ✅ A supportive conversation partner
- ✅ A tool for self-reflection
- ✅ A way to explore your thoughts
- ✅ A bridge to greater self-understanding
- ✅ A prototype for accessible support
""")

st.divider()

# Statistics and impact
st.markdown("""
## 📈 Hackathon Project

This project was built as part of a hackathon with the following goals:

### 🎯 Objectives

1. **Build a functional conversational AI** without using LLMs
2. **Create an explainable system** where users understand responses
3. **Design for mobile** through Android WebView integration
4. **Demonstrate rule-based intelligence** in a support context
5. **Showcase modular architecture** with separation of concerns

### 🔧 Technical Achievements

- **Zero external AI dependencies** - All intelligence is rule-based
- **Complete separation** - Frontend and backend are independent
- **Mobile-first design** - Works flawlessly on Android
- **Session-based architecture** - No database required
- **Explainable responses** - Users see the reasoning behind answers
- **Modular components** - Clean, maintainable code structure
- **Real-time processing** - Instant, responsive interactions

### 🏆 Key Innovations

- **Intent Detection Engine** - Rule-based classification system
- **Safety Layer** - Protective filtering for sensitive content
- **Context Management** - Session-aware conversation tracking
- **Recommendation System** - Contextual, personalized suggestions
- **Mood Analysis** - Rule-based emotional estimation
- **Mobile Integration** - Native Android WebView support
""")

st.divider()

# Future vision
st.markdown("""
## 🚀 Future Vision

### Short-term Improvements

- Enhanced intent detection with more patterns
- Expanded emotional vocabulary
- More personalized recommendations
- Additional quick action options
- Improved mobile responsiveness

### Long-term Goals

- Integration with mental health resources
- Optional, encrypted user accounts
- Longitudinal conversation tracking
- Advanced mood visualization
- Community support features
- Multi-language support

### Technical Roadmap

- **API Versioning** - Support multiple API versions
- **WebSocket Support** - Real-time bidirectional communication
- **Enhanced Caching** - Optimize performance
- **Progressive Web App** - Installable mobile experience
- **Voice Interface** - Speech-to-text capabilities
- **Accessibility Features** - Screen reader support
""")

st.divider()

# Team and credits
st.markdown("""
## 👨‍💻 Project Credits

### Architecture & Development

This project was designed and built with:

- **Clean Architecture** - Separation of concerns
- **Test-Driven Design** - Reliability and robustness
- **User-Centered Design** - Focus on the user experience
- **Privacy-First Approach** - Data protection is paramount

### Technology Partners

- **Streamlit** - For the amazing frontend framework
- **FastAPI** - For the high-performance backend
- **Python** - For the powerful programming language

### Special Thanks

This project was created for a hackathon to demonstrate:
- Innovative use of rule-based systems
- Integration of multiple technologies
- Focus on user experience and accessibility
- Commitment to privacy and explainability
""")

st.divider()

# Resources and links
st.markdown("""
## 📚 Resources

### Documentation

- **Frontend** - Built with Streamlit
- **Backend** - Built with FastAPI  
- **API** - RESTful endpoints with JSON
- **Mobile** - Android WebView integration

### Source Code

The complete source code is available for review:
- Clean, modular architecture
- Comprehensive documentation
- Example configurations
- Deployment instructions

### Contact & Support

For questions, feedback, or support:
- Please reach out through the hackathon platform
- Check the project documentation
- Review the troubleshooting guide
""")

st.divider()

# Disclaimer
st.markdown("## ⚠️ Important Information")
render_disclaimer(compact=False)

# Footer
st.divider()
st.caption("🧠 MindBridge v1.0 | Made with ❤️ for Hackathon")
st.caption("📅 2024 | All Rights Reserved")
st.caption("🔒 Privacy First | No Data Storage | Transparent AI")


if __name__ == "__main__":
    main()