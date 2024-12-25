import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# 1. Read CSS from a separate file (if you want custom styles)
with open("styles.css") as f:
    css_code = f.read()
st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)

st.title("Grade 8 Math Visualization - cbcelimuportal.org")
st.sidebar.title("Topics")

# Add a descriptive header:
st.markdown("""
**With the incisive clarity of an alien intelligence, and the elegance and wisdom of a master teacher**, 
explore Radian & Degree, Functions, Parametric Equations, Polar Coordinates, and Sequences.
""")

topic = st.sidebar.radio(
    "Select a topic:",
    ["Radian & Degree", "Function", "Parametric", "Polar", "Sequence"]
)

if topic == "Radian & Degree":
    st.subheader("Radians vs Degrees")
    st.markdown("""
    1 radian = 180/π degrees. 
    Use the sliders below to convert between radians and degrees.
    """)
    # Interactive demonstration:
    deg = st.slider("Degrees", min_value=0, max_value=360, value=90)
    rad = deg * np.pi / 180
    st.write(f"**Radians:** {rad:.3f}")

    st.write("Or try converting radians to degrees:")
    rad_input = st.slider("Radians", min_value=0.0, max_value=2*np.pi, value=np.pi/2)
    deg_converted = rad_input * 180 / np.pi
    st.write(f"**Degrees:** {deg_converted:.2f}")

elif topic == "Function":
    x = np.linspace(-10, 10, 100)
    y = 2 * x + 3
    fig, ax = plt.subplots()
    ax.plot(x, y, label="y = 2x + 3")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Linear Function: y = 2x + 3")
    ax.legend()
    st.pyplot(fig)

elif topic == "Parametric":
    t = np.linspace(0, 2 * np.pi, 100)
    x = np.sin(t)
    y = np.cos(t)
    fig, ax = plt.subplots()
    ax.plot(x, y, label="x=sin(t), y=cos(t)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Parametric Circle")
    ax.legend()
    ax.set_aspect("equal", "box")  # Make it a perfect circle
    st.pyplot(fig)

elif topic == "Polar":
    theta = np.linspace(0, 2 * np.pi, 100)
    r = 2 * theta  # Spiral
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(theta, r, label="r = 2θ")
    ax.set_title("Polar Spiral: r = 2θ")
    ax.legend()
    st.pyplot(fig)

elif topic == "Sequence":
    # Arithmetic sequence: u(n) = 2n + 1
    n = np.arange(1, 10)
    u = 2 * n + 1
    fig, ax = plt.subplots()
    # For older Matplotlib, remove use_line_collection=True
    markerline, stemlines, baseline = ax.stem(n, u)
    # Optional customization:
    import matplotlib
    plt.setp(markerline, marker='o', markersize=5, markerfacecolor='red')
    plt.setp(stemlines, color='gray', linewidth=1)
    plt.setp(baseline, color='black', linewidth=0.5)

    ax.set_title("Sequence: u = 2n + 1")
    ax.set_xlabel("n")
    ax.set_ylabel("u")
    st.pyplot(fig)
