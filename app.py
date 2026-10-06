import streamlit as st
from pipeline import run_research_pipeline


# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔬",
    layout="wide"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

.main-title {
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #777;
    font-size: 18px;
    margin-bottom: 30px;
}

.stage {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">🔬 Multi-Agent Research System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Search → Read → Write → Critic'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------
with st.sidebar:

    st.header("⚙️ Research Settings")

    topic = st.text_area(
        "Enter Research Topic",
        placeholder="Example: Impact of AI on software engineering jobs",
        height=120
    )

    run_button = st.button(
        "🚀 Start Research",
        type="primary",
        use_container_width=True
    )

    st.divider()

    st.markdown("""
    ### How it works

    **1. Search Agent 🔎**

    Searches the web for recent and reliable information.

    **2. Reader Agent 📖**

    Selects relevant sources and scrapes deeper content.

    **3. Writer Agent ✍️**

    Converts the research into a structured report.

    **4. Critic Agent 🧐**

    Reviews the generated report and provides feedback.
    """)


# ---------------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------------

if run_button:

    if not topic.strip():
        st.warning("⚠️ Please enter a research topic first.")

    else:

        st.info(f"🔍 Starting research on: **{topic}**")

        # -------------------------------------------------
        # PROGRESS
        # -------------------------------------------------

        progress = st.progress(0)

        status = st.empty()

        # -------------------------------------------------
        # STAGE 1
        # -------------------------------------------------

        with st.expander("🔎 Step 1 — Search Agent", expanded=True):

            status.write("🔎 Search Agent is searching the web...")

            search_placeholder = st.empty()

        # -------------------------------------------------
        # RUN PIPELINE
        # -------------------------------------------------

        try:

            result = run_research_pipeline(topic)

            progress.progress(100)

            status.success("✅ Research pipeline completed!")

            # -------------------------------------------------
            # SEARCH RESULTS
            # -------------------------------------------------

            with st.expander(
                "🔎 Step 1 — Search Results",
                expanded=False
            ):

                st.markdown("### Web Search Results")

                st.text_area(
                    "Search Agent Output",
                    result.get("search_results", ""),
                    height=400
                )

            # -------------------------------------------------
            # READER
            # -------------------------------------------------

            with st.expander(
                "📖 Step 2 — Reader Agent",
                expanded=False
            ):

                st.markdown("### Scraped Content")

                st.text_area(
                    "Reader Agent Output",
                    result.get("scraped_content", ""),
                    height=500
                )

            # -------------------------------------------------
            # WRITER
            # -------------------------------------------------

            with st.expander(
                "✍️ Step 3 — Writer Agent",
                expanded=True
            ):

                st.markdown("### 📄 Research Report")

                st.markdown(
                    result.get("report", "")
                )

                st.download_button(
                    label="⬇️ Download Research Report",
                    data=result.get("report", ""),
                    file_name="research_report.txt",
                    mime="text/plain"
                )

            # -------------------------------------------------
            # CRITIC
            # -------------------------------------------------

            with st.expander(
                "🧐 Step 4 — Critic Agent",
                expanded=True
            ):

                st.markdown("### Critic Feedback")

                st.markdown(
                    result.get("feedback", "")
                )

        except Exception as e:

            st.error("❌ An error occurred while running the research pipeline.")

            st.exception(e)