import streamlit as st

# Clean, minimalist, modernist design constraint
st.set_page_config(page_title="Eat Creative Psychoanalyst", page_icon="🧠", layout="centered")

st.title("🏛️ The Eat Creative Psychoanalyst")
st.markdown("""
*Welcome back to the clinic.* This operational tool applies psychodynamic psychotherapy frameworks 
to everyday dynamics within the **Eat Creative team**. Use it to look beneath the surface of project friction 
and respond from a place of grounded, secure ego functioning.
""")

st.markdown("---")

# Input 1: Tailored Corporate Manifest Behaviors
st.subheader("1. Diagnose the Manifest Behavior")
behavior_type = st.selectbox(
    "What core defensive pattern is your stakeholder or colleague projecting right now?",
    options=[
        "Select a dynamic...",
        "The Ghost Brief / Shocking Input (Avoidant Attachment / Passive Aggression)",
        "The 11th-Hour Panic / Reactive Chaos (Ego Regression)",
        "The Decision-Making Paralysis (Splitting & Castration Anxiety)",
        "The Hyper-Critical Nitpicker (Narcissistic Defense / Control Need)"
    ]
)

# Input 2: Tailored Arenas (Monday.com, Figma, DAM, etc.)
st.subheader("2. Identify the Ocado Arena")
work_context = st.selectbox(
    "Where is this dynamic bottlenecking our workflow?",
    options=[
        "Creative Briefing Request Form / Scope Definition",
        "Figma Live Link / Interactive Proofing Stage",
        "The Creative Project Hub (Comments, Tagging, and Asset Chasing)",
        "Media Deadlines & Production Timelines (e.g., Trade & Brand Campaign Processes)"
    ]
)

# Psychodynamic Engine & Interventions tailored for Ocado Retail
ANALYSIS_ENGINE = {
    "The Ghost Brief / Shocking Input (Avoidant Attachment / Passive Aggression)": {
        "insight": "Dropping a blank Word doc or an incomplete, vague creative brief is a classic **Avoidant Attachment** response to a structured operational system. Submitting a 'ghost brief' allows the stakeholder to maintain a sense of control while unconsciously avoiding accountability for defining specific parameters.",
        "counter_transference": "Watch out for *operational over-functioning*. Do not spend your valuable 8am-6pm window chasing them across Slack channels or attempting to read their mind to fix the brief for them.",
        "intervention": "Enforce clear, firm boundaries. Do not process the request into active projects on the board until it is fully completed. Gently but strictly guide them back to the formal briefing request form as a supportive holding environment."
    },
    "The 11th-Hour Panic / Reactive Chaos (Ego Regression)": {
        "insight": "When a stakeholder bypasses the standard 12-week brand or trade pipeline and demands immediate, reactive turnarounds, they are experiencing **Ego Regression**. Faced with external media deadlines, their capacity for logical planning collapses, and they regress into an infant-like state of immediate gratification ('I need this asset right now').",
        "counter_transference": "Avoid absorbing their panic via **Projective Identification**. If you let their emergency disrupt the entire studio's planned timeline, you validate their chaotic internal state.",
        "intervention": "Act as a stabilizing psychological container. Bring operational structure back into the room. Remind them calmly of the agreed workflow, assess the actual urgency with Creative Ops, and map out a realistic, step-by-step production plan to anchor their anxiety."
    },
    "The Decision-Making Paralysis (Splitting & Castration Anxiety)": {
        "insight": "A stakeholder who refuses to sign off on a Figma proof or finalize copy is frozen by **Splitting** (the fear that a choice will be entirely 'wrong' or 'bad'). In psychoanalytic terms, this decision-making block is a form of performance anxiety; making a definitive choice exposes them to potential judgment or failure, so they choose paralyzing safety instead.",
        "counter_transference": "Be careful not to take over the decision-making entirely out of operational frustration. If you do, you breed further dependency.",
        "intervention": "Reduce choice complexity. Instead of asking broad questions, give them two distinct, highly contained binary options to choose from. Frame the sign-off as a collaborative, step-by-step iteration rather than a high-stakes, unchangeable finality."
    },
    "The Hyper-Critical Nitpicker (Narcissistic Defense / Control Need)": {
        "insight": "Leaving endless, trivial comments on a Figma link or a brief amendment document often stems from a **Narcissistic Defense Mechanism**. The critic projects their own inner insecurity by micromanaging creative nuances, attempting to prove their own value by finding fault in the work of others.",
        "counter_transference": "Avoid getting defensive or taking the critique as a personal attack on Tom, Olivia, or the wider design function.",
        "intervention": "Utilize strategic validation. Acknowledge their keen eye and attention to detail first to soothe their fragile ego. Once validated, smoothly steer the focus back to the core objectives of the initial creative brief to separate personal opinion from strategic goals."
    }
}

# Output Generation
if st.button("Run Psychoanalytic Audit"):
    if behavior_type == "Select a dynamic...":
        st.warning("Please select a manifest behavior to run the analysis.")
    else:
        profile = ANALYSIS_ENGINE[behavior_type]
        
        st.markdown("---")
        st.subheader("🕵️‍♂️ The Psychoanalytic Breakdown")
        st.info(f"**Underlying Unconscious Dynamic:**\n{profile['insight']}")
        
        st.subheader("⚠️ Counter-Transference Warning")
        st.warning(f"**Your Instinctive (But Counter-Productive) Reaction:**\n{profile['counter_transference']}")
        
        st.subheader("🛠️ Tactical Operational Intervention")
        st.success(f"**How to handle this within our *{work_context}* workflow:**\n{profile['intervention']}")
        
        st.markdown("---")
        st.caption("Disclaimer: This tool is intended for operational team alignment and educational lightheartedness. Please do not drop an official Freud diagnosis directly into the Monday.com job comments.")
