CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;800&display=swap');

:root {
  --bg: #05050B;
  --text: #F5F5FA;
  --muted: #9CA0B8;
  --indigo: #5B3DF5;
  --accent: #7C83FF;
}

@keyframes drift {
  0%   { transform: translate3d(-3%, -2%, 0) scale(1); }
  100% { transform: translate3d(3%, 3%, 0) scale(1.1); }
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: .35; }
}
@keyframes rise {
  from { opacity: 0; transform: translateY(8px); }
  to   { opacity: 1; transform: none; }
}

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stHeaderActionElements"] { display: none; }

html, body, .stApp, [data-testid="stMarkdownContainer"], input, button, textarea {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
}

.stApp { background: var(--bg); color: var(--text); }
.stApp::before {
  content: ""; position: fixed; inset: -15%; pointer-events: none;
  background:
    radial-gradient(28% 32% at 18% 62%, rgba(79,91,213,.75), transparent 70%),
    radial-gradient(26% 30% at 45% 18%, rgba(168,85,190,.55), transparent 70%),
    radial-gradient(24% 28% at 88% 20%, rgba(190,50,120,.50), transparent 70%);
  filter: blur(40px);
  animation: drift 22s ease-in-out infinite alternate;
}
.block-container, [data-testid="stBottom"] { position: relative; z-index: 1; }
.block-container { max-width: 760px; padding-top: 3.5rem; }

/* Hero */
.hero { text-align: center; margin-bottom: 2rem; }
.hero .pill {
  display: inline-flex; align-items: center; gap: .5rem;
  padding: .35rem .9rem; border-radius: 999px;
  border: 1px solid rgba(124,131,255,.4); background: rgba(91,61,245,.14);
  color: #8C93FF; font-size: .72rem; font-weight: 600;
  letter-spacing: .06em; text-transform: uppercase;
}
.hero .pill::before {
  content: ""; width: 7px; height: 7px; border-radius: 50%;
  background: var(--accent); animation: pulse 2s ease-in-out infinite;
}
.stApp .hero h1 {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 3.1rem !important; font-weight: 800 !important;
  line-height: 1.12 !important; letter-spacing: -0.02em;
  color: #FFFFFF !important; margin: 1.3rem 0 1rem; padding: 0;
}
.stApp h1.brand {
  font-family: 'Plus Jakarta Sans', sans-serif !important;
  font-size: 1.9rem !important; font-weight: 800 !important;
  letter-spacing: -0.02em; color: #FFFFFF !important; margin: 0; padding: 0;
}
.stApp .hero .accent, .stApp h1.brand .accent { color: #7C83FF !important; }
[data-testid="stCaptionContainer"] { color: var(--muted); }

/* Form */
[data-testid="stForm"] {
  max-width: 520px; margin: 0 auto;
  background: rgba(255,255,255,.04); backdrop-filter: blur(14px);
  border: 1px solid rgba(255,255,255,.10); border-radius: 22px; padding: 1.8rem;
  box-shadow: 0 20px 60px rgba(0,0,0,.45);
}
.stTextInput label p { color: var(--muted); font-size: .9rem; }

/* Buttons */
div.stButton > button, div[data-testid="stFormSubmitButton"] > button {
  background: var(--indigo); color: #fff !important; border: none;
  border-radius: 999px; font-weight: 600; padding: .6rem 1.6rem;
  box-shadow: 0 8px 24px rgba(91,61,245,.4);
  transition: transform .2s ease, box-shadow .2s ease, background .2s;
}
div.stButton > button p, div[data-testid="stFormSubmitButton"] > button p { color: #fff !important; }
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
  background: #6C50FF; transform: translateY(-2px); box-shadow: 0 12px 32px rgba(91,61,245,.6);
}
div.stButton > button:disabled { opacity: .35; transform: none; box-shadow: none; }
[data-testid="stLinkButton"] a {
  background: rgba(0,0,0,.4); color: #fff; border: 1px solid rgba(255,255,255,.18);
  border-radius: 999px; font-weight: 600; transition: border-color .2s;
}
[data-testid="stLinkButton"] a:hover { border-color: var(--accent); }

/* Chat */
[data-testid="stChatMessage"] {
  background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.09);
  border-radius: 18px; padding: 1rem 1.2rem; margin-bottom: .8rem;
  backdrop-filter: blur(10px); animation: rise .45s ease both;
}
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
  background: transparent; border-color: rgba(124,131,255,.5);
}
[data-testid="stImage"] img { border-radius: 14px; }
[data-testid="stBottom"] > div { background: transparent; }
[data-testid="stChatInput"] {
  background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.14);
  border-radius: 999px; transition: box-shadow .2s, border-color .2s;
}
[data-testid="stChatInput"]:focus-within {
  border-color: var(--accent); box-shadow: 0 0 0 3px rgba(91,61,245,.3);
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after { animation: none !important; transition: none !important; }
}

/* Input boxes (keep at the end) */
.stTextInput [data-baseweb="input"] {
  background-color: rgba(255,255,255,.08) !important;
  border: 1px solid rgba(255,255,255,.22) !important;
  border-radius: 12px !important;
  transition: border-color .2s, box-shadow .2s, background-color .2s;
}
.stTextInput [data-baseweb="base-input"],
.stTextInput input {
  background-color: transparent !important; color: #F5F5FA !important;
}
.stTextInput input::placeholder { color: #8B8FA8 !important; }
.stTextInput [data-baseweb="input"]:focus-within {
  background-color: rgba(255,255,255,.12) !important;
  border-color: #7C83FF !important;
  box-shadow: 0 0 0 3px rgba(91,61,245,.3);
}
</style>
"""