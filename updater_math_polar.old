import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Optionally read CSS from a separate file to style the app
try:
    with open("styles.css") as f:
        css_code = f.read()
    st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass  # If you don't have a styles.css, it's okay

st.title("Grade 8 Math Visualization — cbcelimuportal.org")

# Intro text
st.markdown("""
**With the incisive clarity of an alien intelligence, and the elegance and wisdom of a master teacher**, 
we explore Radians, Degree, Functions, Parametric, Polar, and Sequence.
""")

# Sidebar selection
topic = st.sidebar.radio(
    "Select a topic:",
    ["Radians", "Degree", "Function", "Parametric", "Polar", "Sequence"]
)

# -- RADIANS -------------------------------------------------
if topic == "Radians":
    st.subheader("Radians")
    st.markdown("1 radian is the angle subtended by an arc of length 1 on a unit circle.")
    st.markdown(r"**Relationship**: $\pi$ radians = 180°, hence 1 rad ≈ 57.2958°.")

    # Simple interactive demonstration:
    deg = st.slider("Degrees → Radians", 0, 360, 90)
    rad = deg * np.pi / 180
    st.write(f"**{deg}°** is ~ **{rad:.4f} radians**")

# -- DEGREE --------------------------------------------------
elif topic == "Degree":
    st.subheader("Degree")
    st.markdown("A full revolution is 360°. Common angles include 90°, 180°, etc.")
    st.markdown(r"Use the slider below to see how degrees convert to radians.")
    deg_input = st.slider("Degrees → Radians", min_value=0, max_value=360, value=45)
    rad_conv = deg_input * np.pi / 180
    st.write(f"**{deg_input}°** = ~ **{rad_conv:.4f} rad**")

# -- FUNCTION -----------------------------------------------
elif topic == "Function":
    st.subheader("Function: y = 2x + 3")
    x = np.linspace(-10, 10, 100)
    y = 2 * x + 3
    fig, ax = plt.subplots()
    ax.plot(x, y, label="y = 2x + 3", color="blue")
    ax.set_title("Linear Function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)

# -- PARAMETRIC ---------------------------------------------
elif topic == "Parametric":
    st.subheader("Parametric Equations: x(t)=sin(t), y(t)=cos(t)")
    t = np.linspace(0, 2 * np.pi, 100)
    x = np.sin(t)
    y = np.cos(t)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Circle Parametric", color="green")
    ax.set_aspect("equal", "box")
    ax.set_title("x(t) = sin(t), y(t) = cos(t)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)

# -- POLAR --------------------------------------------------
elif topic == "Polar":
    st.subheader("Polar Coordinates: r = 2θ")
    theta = np.linspace(0, 2*np.pi, 100)
    r = 2 * theta
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(theta, r, label="r=2θ", color="red")
    ax.set_title("Polar Spiral")
    ax.legend()
    st.pyplot(fig)

# -- SEQUENCE -----------------------------------------------
elif topic == "Sequence":
    st.subheader("Sequence: u(n) = 2n + 1")
    n = np.arange(1, 10)
    u = 2 * n + 1
    fig, ax = plt.subplots()
    markerline, stemlines, baseline = ax.stem(n, u)
    # Customize the plot
    plt.setp(markerline, marker='o', markersize=5, markerfacecolor='red')
    plt.setp(stemlines, color='gray', linewidth=1)
    plt.setp(baseline, color='black', linewidth=0.5)
    ax.set_title("Arithmetic Sequence")
    ax.set_xlabel("n")
    ax.set_ylabel("u(n)")
    st.pyplot(fig)
