import streamlit as st

st.set_page_config(page_title="NexusLM: Autoregressive Language Model", page_icon="🤖", layout="centered")

st.title("🤖 NexusLM: Custom Autoregressive Language Model")
st.subheader("Deep Learning Infrastructure Project")

st.info("🚀 **Deployment Status:** The core neural network architecture files and training scripts are currently being finalized and optimized for local consumer GPU training runs. Checkpoint weights and the interactive Streamlit inference interface will be pushed to this main branch shortly.", icon="ℹ️")

st.markdown("""
### Technical Overview of the Architecture:
* **Core Framework:** PyTorch implementation of a vanilla Transformer architecture (Decoder-only configuration).
* **Tokenization & Embeddings:** Custom character-level tokenization mapping to trainable positional embedding vectors.
* **Attention Mechanism:** Multi-Head Scaled Dot-Product Self-Attention blocks to capture long-range contextual relationships.
* **Optimization & Loss:** Optimised via the AdamW optimizer and evaluated through cross-entropy loss functions.

*Check back soon to interact with the trained checkpoint weights directly from this dashboard!*
""")
