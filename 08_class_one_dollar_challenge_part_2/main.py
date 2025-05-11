import streamlit as st
from modules.pdf_summarizer import PDFSummarizer
from modules.flashcard_generator import FlashcardGenerator
from modules.pomodoro_timer import PomodoroTimer
from modules.schedule_planner import StudyScheduleGenerator
import tempfile

st.set_page_config(page_title="Smart Study Companion", layout="centered")

st.title("🧠 Smart Study Companion")

# Tabs for Navigation
tab1, tab2, tab3, tab4 = st.tabs([
    "📚 PDF Summarizer",
    "🧠 Flashcard Generator",
    "⏳ Pomodoro Timer",
    "📅 Study Schedule Generator"
])

# --- PDF Summarizer Tab ---
with tab1:
    st.header("📚 PDF Summarizer")
    uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name

        summarizer = PDFSummarizer(temp_path)

        if st.button("Extract & Summarize"):
            try:
                text = summarizer.extract_text()
                summary = summarizer.basic_summarize()
                st.subheader("📄 Summary:")
                st.write(summary)
                with st.expander("📘 Full Extracted Text"):
                    st.write(text)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

# --- Flashcard Generator Tab ---
with tab2:
    st.header("🧠 Flashcard Generator")
    input_text = st.text_area("Paste or write study material here:", height=200)
    if st.button("Generate Flashcards"):
        if input_text.strip():
            generator = FlashcardGenerator(input_text)
            cards = generator.generate_flashcards()
            if cards:
                st.success("Flashcards Generated:")
                for i, card in enumerate(cards):
                    st.markdown(f"**Q{i+1}:** {card['question']}")
                    st.markdown(f"*A{i+1}:* {card['answer']}")
            else:
                st.warning("No valid flashcards found. Try different input.")
        else:
            st.error("Please paste some content first.")

# --- Pomodoro Timer Tab ---
with tab3:
    st.header("⏲️ Pomodoro Timer")

    work_duration = st.number_input("Work duration (minutes):", min_value=1, max_value=60, value=25)
    break_duration = st.number_input("Break duration (minutes):", min_value=1, max_value=30, value=5)

    timer = PomodoroTimer(work_duration, break_duration)

    if st.button("Start Work Session"):
        session = timer.start_session(is_break=False)
        st.success("✅ Work session completed!")
        st.write(f"📈 Sessions Completed: {timer.sessions_completed}")
        st.write(f"🕒 Total Time Spent: {int(timer.total_time // 60)} minutes")

    if st.button("Start Break Session"):
        session = timer.start_session(is_break=True)
        st.info("☕ Break session completed!")
        st.write(f"📈 Sessions Completed: {timer.sessions_completed}")
        st.write(f"🕒 Total Time Spent: {int(timer.total_time // 60)} minutes")

# --- Study Schedule Generator Tab ---
with tab4:
    st.header("📅 Study Schedule Generator")

    subjects_input = st.text_input("Enter subjects (comma-separated)", placeholder="Math, Science, History")
    total_hours = st.number_input("Total Available Study Hours Today", min_value=1.0, step=0.5)

    subjects = [s.strip() for s in subjects_input.split(",") if s.strip()]

    use_custom_priority = st.checkbox("Use custom priority for each subject")

    if use_custom_priority and subjects:
        st.subheader("🎯 Set Priority (Higher = More Important)")
        priorities = {}
        for subject in subjects:
            weight = st.slider(f"Priority for {subject}", min_value=1, max_value=10, value=5)
            priorities[subject] = weight

    if st.button("Generate Study Schedule"):
        if not subjects:
            st.error("Please enter at least one subject.")
        elif total_hours <= 0:
            st.error("Total study hours must be greater than 0.")
        else:
            generator = StudyScheduleGenerator(subjects, total_hours)

            if use_custom_priority:
                schedule = generator.generate_custom_schedule(priorities)
            else:
                schedule = generator.generate_equal_schedule()

            st.subheader("📆 Your Study Schedule:")
            for item in schedule:
                st.write(f"📘 {item['subject']}: {item['hours']} hours")
