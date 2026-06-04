import streamlit as st

# Page config utilizing clean, modernist design constraints
st.set_page_config(page_title="Workplace Psychoanalyst", page_icon="🧠", layout="centered")

st.title("🏛️ The Workplace Psychoanalyst")
st.markdown("""
*Welcome to the clinic.* This interactive tool applies traditional and modern psychodynamic psychotherapy 
theory to everyday office dynamics. Use it to look beneath the surface of challenging interactions and 
decide how to respond from a place of secure ego functioning.
""")

st.markdown("---")

# Input 1: Diagnostic Profiling
st.subheader("1. Diagnose the Manifest Behavior")
behavior_type = st.selectbox(
    "What core pattern is your colleague or stakeholder projecting right now?",
    options=[
        "Select a dynamic...",
        "The Control Freaking (Classic Perfectionism / Ego Defense)",
        "The Silent Ghosting (Avoidant Attachment / Passive Aggression)",
        "The Immediate Panic (High-Anxiety / Regression)",
        "The Constant Validation Seeker (Narcissistic Injury / Mirroring Need)"
    ]
)

# Input 2: Environmental Context
st.subheader("2. Identify the Corporate Arena")
work_context = st.selectbox(
    "Where is this dynamic manifesting itself?",
    options=[
        "Creative Briefing or Scope Adjustments",
        "Feedback, Proofing, and Sign-off Stages",
        "Day-to-day Slack Chats and Asynchronous Comm",
        "Resource Allocation and Deadlines"
    ]
)

# Psychodynamic Engine & Interventions
ANALYSIS_ENGINE = {
    "The Control Freaking (Classic Perfectionism / Ego Defense)": {
        "insight": "This individual is likely utilizing **Reaction Formation** or **Splitting**. Underneath the rigid exterior and micromanagement lies a profound, unconscious fear of chaos, failure, or losing structural control. They cope by over-functioning.",
        "counter_transference": "Be careful not to regress into an *anxious child* or *rebellious teenager* role. Avoid the urge to push back aggressively or disengage completely.",
        "intervention": "Provide extreme structural containment. Over-communicate updates clearly to soothe their hyper-vigilant ego defenses. Acknowledge their high standards explicitly to disarm their anxiety."
    },
    "The Silent Ghosting (Avoidant Attachment / Passive Aggression)": {
        "insight": "This pattern points heavily toward an **Avoidant Attachment Style**. When confronted with professional conflict, heavy volume, or vulnerability, their defense mechanism is psychological withdrawal to preserve autonomy and safety.",
        "counter_transference": "Watch out for *chaser behavior*—sending compounding follow-ups out of anxiety, which will only drive them further into their defensive shell.",
        "intervention": "Lower the emotional stakes of the interaction. Move the conversation away from high-pressure channels into a low-friction setup. Offer clear, bite-sized next steps rather than overwhelming demands."
    },
    "The Immediate Panic (High-Anxiety / Regression)": {
        "insight": "The individual is experiencing **Ego Regression**. Faced with stress or tight deadlines, their capacity for mature adult functioning temporarily collapses, reverting them to a frantic, overwhelmed state where everything feels catastrophic.",
        "counter_transference": "Avoid absorbing their anxiety (**Projective Identification**). If you panic alongside them, you validate their internal belief that the sky is falling.",
        "intervention": "Act as a **Psychological Container** (Donald Winnicott's holding environment). Speak with deliberate calm, break the overwhelming chaos down into highly structured micro-tasks, and offer strong, grounded boundaries."
    },
    "The Constant Validation Seeker (Narcissistic Injury / Mirroring Need)": {
        "insight": "This person is searching for a **Mirroring Selfobject** (Heinz Kohut's Self Psychology). Their constant need for praise masks a fragile underlying self-esteem. A simple rejection of their idea feels to them like a deep personal attack.",
        "counter_transference": "Ensure you don't respond with irritation, cold dismissal, or competitive ego-checking.",
        "intervention": "Utilize the **Feedback Sandwich with Empathy**. Explicitly validate their intent and value first to secure their self-esteem, deliver the operational reality smoothly, and conclude with a collaborative path forward."
    }
}

# Output Generation
if st.button("Analyze Dynamics & Get Intervention"):
    if behavior_type == "Select a dynamic...":
        st.warning("Please select a manifest behavior to run the analysis.")
    else:
        profile = ANALYSIS_ENGINE[behavior_type]
        
        st.markdown("---")
        st.subheader("🕵️‍♂️ The Psychoanalytic Breakdown")
        st.info(f"**Underlying Unconscious Dynamic:**\n{profile['insight']}")
        
        st.subheader("⚠️ Counter-Transference Warning")
        st.warning(f"**How *You* Might Instinctively (But Incorrectly) React:**\n{profile['counter_transference']}")
        
        st.subheader("🛠️ Tactical Clinical Intervention")
        st.success(f"**How to handle them in the context of *{work_context}*:**\n{profile['intervention']}")
        
        # Lighthearted closing note 
        st.markdown("---")
        st.caption("Disclaimer: This tool is based on psychodynamic frameworks for educational and team-building amusement. Please do not hand-deliver an official psychiatric diagnosis to your stakeholders over Slack.")
