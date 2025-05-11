import streamlit as st
import time

class PomodoroTimer:
    def __init__(self, work_duration=25, break_duration=5):
        self.work_duration = work_duration * 60  # minutes → seconds
        self.break_duration = break_duration * 60
        self.sessions_completed = 0
        self.total_time = 0

    def start_session(self, is_break=False):
        duration = self.break_duration if is_break else self.work_duration
        label = "Break" if is_break else "Work"

        # Visual countdown
        countdown_placeholder = st.empty()
        for remaining in range(duration, 0, -1):
            mins, secs = divmod(remaining, 60)
            countdown_placeholder.markdown(
                f"### ⏳ {label} Timer: {mins:02d}:{secs:02d}"
            )
            time.sleep(1)

        self.total_time += duration
        if not is_break:
            self.sessions_completed += 1

        return {
            "type": label,
            "duration": duration,
            "completed_sessions": self.sessions_completed,
            "total_time": self.total_time,
        }