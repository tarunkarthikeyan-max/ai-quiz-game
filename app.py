import streamlit as st
import random
import time
import pandas as pd
from questions import QUESTION_BANK

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Command Center | Interactive Quiz Game",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CYBERPUNK / GLASSMORPHISM CUSTOM CSS ---
st.markdown("""
<style>
    /* Dark Theme Core */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #020617 100%);
        color: #f8fafc;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Header Banner Styling */
    .hero-container {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 24px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    }
    
    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }
    
    /* Question Card Styling */
    .quiz-card {
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(99, 102, 241, 0.25);
        border-radius: 16px;
        padding: 24px;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    }
    
    /* Custom Badges */
    .badge-topic {
        background: linear-gradient(90deg, #3b82f6, #1d4ed8);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
        margin-right: 8px;
    }
    
    .badge-module {
        background: linear-gradient(90deg, #8b5cf6, #6d28d9);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Gamification Metric Boxes */
    .metric-card {
        background: rgba(30, 41, 59, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
    }
    
    .metric-value {
        font-size: 1.8rem;
        font-weight: 800;
        color: #38bdf8;
    }
    
    .metric-label {
        font-size: 0.85rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
</style>
""", unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "max_streak" not in st.session_state:
    st.session_state.max_streak = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "show_hint" not in st.session_state:
    st.session_state.show_hint = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "selected_module" not in st.session_state:
    st.session_state.selected_module = "All Modules"

# --- HERO BANNER ---
st.markdown("""
<div class="hero-container">
    <div class="hero-title">⚡ DSC401-6: Artificial Intelligence Quiz Arena</div>
    <div style="color: #94a3b8; font-size: 1rem;">
        Units I & II Interactive Assessment | Search Strategies, Agents, CSP, Logic & Games
    </div>
</div>
""", unsafe_allow_html=True)

# --- SIDEBAR CONTROLS ---
with st.sidebar:
    st.header("⚙️ Game Settings")
    
    if not st.session_state.quiz_started:
        module_filter = st.selectbox("Select Module / Unit:", ["All Modules", "Module 1", "Module 2", "Module 3"])
        
        num_q = st.slider("Number of Questions:", min_value=5, max_value=50, value=10, step=5)
        
        st.markdown("---")
        st.subheader("💡 Features")
        st.markdown("""
        * **Streak Multiplier 🔥**
        * **Instant Explanations 📖**
        * **Timed Performance ⏳**
        * **Detailed Review Matrix 📊**
        """)
        
        if st.button("🚀 Start Challenge", use_container_width=True, type="primary"):
            if module_filter == "All Modules":
                pool = QUESTION_BANK.copy()
            else:
                pool = [q for q in QUESTION_BANK if q["module"] == module_filter]
                
            random.shuffle(pool)
            st.session_state.questions = pool[:num_q]
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.streak = 0
            st.session_state.max_streak = 0
            st.session_state.user_answers = {}
            st.session_state.show_hint = False
            st.session_state.start_time = time.time()
            st.session_state.quiz_started = True
            st.rerun()
    else:
        st.markdown("### 📊 Live Stats")
        st.metric("Current Score", f"{st.session_state.score} / {len(st.session_state.questions)}")
        st.metric("Streak 🔥", f"{st.session_state.streak} (Max: {st.session_state.max_streak})")
        
        elapsed = int(time.time() - st.session_state.start_time)
        st.metric("Time Elapsed ⏳", f"{elapsed // 60}m {elapsed % 60}s")
        
        st.markdown("---")
        if st.button("🔄 Abandon & Restart", use_container_width=True):
            st.session_state.quiz_started = False
            st.rerun()

# --- MAIN DISPLAY CONTENT ---
if not st.session_state.quiz_started:
    # LANDING PAGE
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">50</div>
            <div class="metric-label">Total Questions</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">3</div>
            <div class="metric-label">Modules Covered</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">100%</div>
            <div class="metric-label">Concept Coverage</div>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.subheader("📌 What to Expect")
    st.markdown("""
    * **Topics Included:** Foundations, PEAS, Agents & Environments, BFS/DFS, Hill Climbing, Simulated Annealing, A* Consistency, CSP (AC-3, MRV, LCV), Means-End Analysis, Game Theory.
    * **Diverse Formats:** Scenario-Based, Assertion-Reason, Problem-Solving / Numerical, Match the Following, and Conceptual MCQs.
    * *Select options in the sidebar and click **Start Challenge** to test your knowledge!*
    """)

else:
    # QUIZ IN PROGRESS
    q_idx = st.session_state.current_index
    total_q = len(st.session_state.questions)
    
    if q_idx < total_q:
        current_q = st.session_state.questions[q_idx]
        
        # Progress Bar & Metainfo
        progress = (q_idx) / total_q
        st.progress(progress)
        
        st.markdown(f"""
        <div>
            <span class="badge-module">{current_q['module']}</span>
            <span class="badge-topic">{current_q['topic']}</span>
            <span style="color: #94a3b8; font-size: 0.9rem;">Type: {current_q['type']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Question Display
        st.markdown(f"""
        <div class="quiz-card">
            <h3 style="margin-top:0; color: #f8fafc;">Q{q_idx + 1}: {current_q['question']}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Hint Button
        if st.button("💡 Reveal Lifeline / Hint"):
            st.session_state.show_hint = not st.session_state.show_hint
            
        if st.session_state.show_hint:
            st.info(f"**Hint:** {current_q['hint']}")
            
        # Form
        with st.form(key=f"q_form_{q_idx}"):
            user_choice = st.radio("Select your answer:", current_q["options"], key=f"radio_{q_idx}")
            submit_btn = st.form_submit_button("Submit Answer 🎯")
            
        if submit_btn:
            st.session_state.user_answers[q_idx] = user_choice
            
            if user_choice == current_q["answer"]:
                st.session_state.score += 1
                st.session_state.streak += 1
                if st.session_state.streak > st.session_state.max_streak:
                    st.session_state.max_streak = st.session_state.streak
                st.success(f"✅ **Correct!** Streak: {st.session_state.streak} 🔥")
            else:
                st.session_state.streak = 0
                st.error(f"❌ **Incorrect!** Correct Answer: **{current_q['answer']}**")
                
            st.markdown(f"**📖 Detailed Explanation:**\n{current_q['explanation']}")
            time.sleep(2.0)
            st.session_state.current_index += 1
            st.session_state.show_hint = False
            st.rerun()

    else:
        # QUIZ COMPLETED / RESULTS DASHBOARD
        st.balloons()
        st.markdown("## 🏆 Assessment Complete!")
        
        final_score = st.session_state.score
        pct = (final_score / total_q) * 100
        total_time = int(time.time() - st.session_state.start_time)
        
        # Rank Calculation
        if pct >= 90:
            rank_badge = "🥇 S-Rank (Master)"
        elif pct >= 75:
            rank_badge = "🥈 A-Rank (Proficient)"
        elif pct >= 50:
            rank_badge = "🥉 B-Rank (Apprentice)"
        else:
            rank_badge = "⚠️ C-Rank (Needs Revision)"
            
        col_a, col_b, col_c, col_d = st.columns(4)
        col_a.metric("Final Score", f"{final_score} / {total_q}")
        col_b.metric("Accuracy", f"{pct:.1f}%")
        col_c.metric("Max Streak", f"{st.session_state.max_streak} 🔥")
        col_d.metric("Rank", rank_badge)
        
        st.markdown("---")
        st.subheader("📝 Question-by-Question Review Matrix")
        
        for idx, q in enumerate(st.session_state.questions):
            user_ans = st.session_state.user_answers.get(idx, "No Answer")
            is_correct = user_ans == q["answer"]
            status = "✅ Correct" if is_correct else "❌ Incorrect"
            
            with st.expander(f"Q{idx+1}: {q['topic']} ({status})"):
                st.write(f"**Question:** {q['question']}")
                st.write(f"**Your Choice:** {user_ans}")
                st.write(f"**Correct Choice:** {q['answer']}")
                st.info(f"**Explanation:** {q['explanation']}")
                
        if st.button("Play Again 🔄", type="primary"):
            st.session_state.quiz_started = False
            st.rerun()