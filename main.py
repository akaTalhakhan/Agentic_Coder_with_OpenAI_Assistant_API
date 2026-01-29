import streamlit as st
import time
from datetime import datetime
from helper_ai import get_ai_response


def initialize_session_state():
    """Initialize session state variables"""
    if "api_key" not in st.session_state:
        st.session_state.api_key = ""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "code_history" not in st.session_state:
        st.session_state.code_history = []
    if "current_code" not in st.session_state:
        st.session_state.current_code = ""
    if "selected_ai_model" not in st.session_state:
        st.session_state.selected_ai_model = "ChatGPT-4o"


def create_code_chat():
    """Create a compact AI chat interface for right sidebar"""
    # Add visual container with border
    with st.container():
        # st.markdown(
        #     """
        # <div style="border: 2px solid #4CAF50; border-radius: 10px; padding: 15px; background-color: #f8f9fa;">
        # """,
        #     unsafe_allow_html=True,
        # )

        st.markdown(
            """
        <h3 style="text-align:center;">AI Assistant</h3>
        """,
            unsafe_allow_html=True,
        )

        # Compact chat info
        if st.session_state.current_code:
            st.success(
                f"📝 Code loaded ({len(st.session_state.current_code.split())} words)"
            )
        else:
            st.warning("📝 No code loaded")

        st.divider()

        # Chat history display with proper chat messages
        st.write("**💬 Chat History:**")

        # Create a container for chat history
        chat_container = st.container()
        with chat_container:
            if not st.session_state.chat_history:
                st.info("💡 Ask me anything about your code!")

            # Show all messages with proper chat formatting
            for message in st.session_state.chat_history:
                if message["role"] == "user":
                    with st.chat_message("user"):
                        st.write(message["content"])
                else:
                    with st.chat_message("assistant"):
                        st.write(message["content"])

        st.divider()

        # Quick question buttons
        st.write("**⚡ Quick Actions:**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Find Bugs", use_container_width=True, key="find_bugs"):
                if st.session_state.current_code:
                    auto_prompt = (
                        "Review this code and find any potential bugs or issues."
                    )
                    st.session_state.chat_history.append(
                        {"role": "user", "content": auto_prompt}
                    )
                    with st.spinner("Finding bugs..."):
                        context = f"Code to review: {st.session_state.current_code}"
                        selected_model = getattr(
                            st.session_state, "selected_ai_model", "ChatGPT-4o"
                        )
                        response = get_ai_response(
                            context + "\n\n" + auto_prompt,
                            st.session_state.api_key,
                            selected_model,
                        )
                        st.session_state.chat_history.append(
                            {"role": "assistant", "content": response}
                        )
                    st.rerun()
                else:
                    st.error("Please add some code first!")

        with col2:
            if st.button("Explain Code", use_container_width=True, key="explain_code"):
                if st.session_state.current_code:
                    auto_prompt = "Explain what this code does in simple terms."
                    st.session_state.chat_history.append(
                        {"role": "user", "content": auto_prompt}
                    )
                    with st.spinner("Explaining code..."):
                        context = f"Code to explain: {st.session_state.current_code}"
                        selected_model = getattr(
                            st.session_state, "selected_ai_model", "ChatGPT-4o"
                        )
                        response = get_ai_response(
                            context + "\n\n" + auto_prompt,
                            st.session_state.api_key,
                            selected_model,
                        )
                        st.session_state.chat_history.append(
                            {"role": "assistant", "content": response}
                        )
                    st.rerun()
                else:
                    st.error("Please add some code first!")

        # Manual chat input
        if prompt := st.chat_input("Type your question...", key="chat_input"):
            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            # Generate AI response
            with st.spinner("AI thinking..."):
                context = (
                    f"Current code: {st.session_state.current_code[:1000]}..."
                    if st.session_state.current_code
                    else "No code provided yet."
                )
                full_prompt = f"Context: {context}\n\nUser question: {prompt}"

                # Use the selected AI model from session state
                selected_model = getattr(
                    st.session_state, "selected_ai_model", "ChatGPT-4o"
                )
                response = get_ai_response(
                    full_prompt, st.session_state.api_key, selected_model
                )

            # Add AI response to chat history
            st.session_state.chat_history.append(
                {"role": "assistant", "content": response}
            )

            # Rerun to show new messages
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)


def main():
    st.set_page_config(
        page_title="AI Coding Companion",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_session_state()

    # Main header
    st.markdown(
        """
        <h1 style="text-align:center;">AI Coding Companion</h1>
        """,
        unsafe_allow_html=True,
    )
    st.divider()

    # Sidebar configuration with better visual design
    with st.sidebar:
        # Add visual container with border
        # st.markdown(
        #     """
        # <div style="border: 2px solid #9C27B0; border-radius: 10px; padding: 15px; background-color: #f3e5f5; margin-bottom: 15px;">
        # """,
        #     unsafe_allow_html=True,
        # )

        st.header("⚙️ Configuration")

        # AI Model selection
        ai_model = st.selectbox(
            "🤖 AI Model",
            ["ChatGPT-4o", "GPT-3.5-Turbo", "Gemini Pro"],
            help="Select your preferred AI model for code assistance",
        )

        # Store selected model in session state for chat function
        st.session_state.selected_ai_model = ai_model

        # API Key input with validation
        api_key = st.text_input(
            f"🔑 {ai_model} API Key",
            type="password",
            value=st.session_state.api_key,
            help="Enter your API key for the selected model",
        )

        if st.button("🔒 Validate API Key", use_container_width=True):
            if api_key:
                st.session_state.api_key = api_key
                st.success("✅ API Key saved!")
            else:
                st.error("❌ Please enter a valid API key")

        st.markdown("</div>", unsafe_allow_html=True)

        # Quick actions section
        # st.markdown(
        #     """
        # <div style="border: 2px solid #795548; border-radius: 10px; padding: 15px; background-color: #efebe9;">
        # """,
        #     unsafe_allow_html=True,
        # )

        st.header("⚡ Quick Actions")

        if st.button("🧹 Clear Chat History", use_container_width=True):
            st.session_state.chat_history = []
            st.success("Chat history cleared!")

        st.markdown("</div>", unsafe_allow_html=True)

    # Main content layout with columns and spacer
    # Create three columns: code editor, spacer, AI chat
    main_col, spacer_col, chat_col = st.columns([2.2, 0.1, 1.2])

    # Left column - Code Editor with visual container
    with main_col:
        # Add visual container with border
        # st.markdown(
        #     """
        # <div style="border: 2px solid #2196F3; border-radius: 10px; padding: 15px; background-color: #f5f5f5; margin-bottom: 10px;">
        # """,
        #     unsafe_allow_html=True,
        # )

        st.subheader("Code Editor")

        # File upload option
        uploaded_file = st.file_uploader(
            "📁 Upload Code File",
            type=["py", "js", "java", "cpp", "c", "rb", "go", "rs"],
            help="Upload a code file for analysis",
        )

        if uploaded_file:
            st.session_state.current_code = str(uploaded_file.read(), "utf-8")
            st.success(f"✅ Loaded {uploaded_file.name}")

        # Code input area
        code_input = st.text_area(
            "✨ Enter your code here:",
            value=st.session_state.current_code,
            height=400,
            help="Type or paste your code here for analysis and enhancement",
        )

        if code_input != st.session_state.current_code:
            st.session_state.current_code = code_input

        st.markdown("</div>", unsafe_allow_html=True)

        # Options section with separate container
        # st.markdown(
        #     """
        # <div style="border: 2px solid #FF9800; border-radius: 10px; padding: 15px; background-color: #fff8e1; margin-bottom: 10px;">
        # """,
        #     unsafe_allow_html=True,
        # )

        st.markdown(
            """
        <h3 style="text-align:center;">⚙️ Advanced Filters</h3>
        """,
            unsafe_allow_html=True,
        )
        st.divider()

        # Simplified customization options
        col1, col2 = st.columns(2)

        with col1:
            st.write("**🎯 Analysis Options**")
            time_complexity = st.checkbox("⏱️ Time Complexity Analysis")
            space_complexity = st.checkbox("💾 Space Complexity Analysis")
            generate_tests = st.checkbox("🧪 Generate Unit Tests")
            generate_docs = st.checkbox("📚 Generate Documentation")

        with col2:
            st.write("**🛠️ Code Enhancement**")
            target_language = st.selectbox(
                "Convert to Language",
                [
                    "Keep Original",
                    "Python",
                    "JavaScript",
                    "Java",
                    "C++",
                    "Go",
                    "TypeScript",
                    "Ruby",
                    "Rust",
                    "C#",
                    "PHP",
                    "Swift",
                    "Kotlin",
                    "Dart",
                ],
            )
            add_comments = st.checkbox("💬 Add Comments")
            optimize_code = st.checkbox("🚀 Optimize Performance")

        # Process button
        if st.button("🎯 Process Code", type="primary", use_container_width=True):
            if not st.session_state.current_code:
                st.error("❌ Please provide some code first!")
            elif not st.session_state.api_key:
                st.error("❌ Please configure your API key first!")
            else:
                with st.spinner("🤖 AI is processing your code..."):
                    # Build comprehensive prompt
                    prompt_parts = ["Analyze and enhance the following code:"]

                    if time_complexity:
                        prompt_parts.append("- Calculate time complexity")
                    if space_complexity:
                        prompt_parts.append("- Calculate space complexity")
                    # if security_scan:
                    #     prompt_parts.append("- Perform security analysis")
                    if target_language != "Keep Original":
                        prompt_parts.append(f"- Convert to {target_language}")
                    if generate_docs:
                        prompt_parts.append("- Generate comprehensive documentation")
                    if generate_tests:
                        prompt_parts.append("- Create unit tests")
                    if add_comments:
                        prompt_parts.append("- Add detailed comments")
                    if optimize_code:
                        prompt_parts.append("- Optimize for better performance")

                    full_prompt = (
                        "\n".join(prompt_parts)
                        + f"\n\nCode:\n{st.session_state.current_code}"
                    )

                    # Get AI response
                    response = get_ai_response(
                        full_prompt, st.session_state.api_key, ai_model
                    )

                    # Display results
                    st.success("✅ Analysis completed!")

                    with st.expander("📋 AI Analysis Results", expanded=True):
                        st.markdown(response)

                    # Save to history
                    st.session_state.code_history.append(
                        {
                            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                            "code": st.session_state.current_code[:200] + "...",
                            "analysis": response[:500] + "...",
                        }
                    )

        st.markdown("</div>", unsafe_allow_html=True)
    # Right column - AI Chat
    with chat_col:
        create_code_chat()

    # Footer with better visual design
    st.divider()
    # st.markdown(
    #     """
    # <div style="border: 1px solid #607D8B; border-radius: 5px; padding: 10px; background-color: #eceff1; margin-top: 20px;">
    # """,
    #     unsafe_allow_html=True,
    # )

    col1, col2 = st.columns(2)
    with col1:
        st.info("💡 **Tip**: Upload a file or paste code to get started!")
    with col2:
        st.info("💬 **Chat**: Ask the AI about your code in real-time!")

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
