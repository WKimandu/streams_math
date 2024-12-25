import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Attempt to read a custom CSS file for extra styling (optional)
try:
    with open("styles.css") as f:
        css_code = f.read()
    st.markdown(f"<style>{css_code}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    pass

st.title("Grade 8 Math Interactive App — cbcelimuportal.org")

st.markdown("""
With the incisive clarity,elegance and wisdom of a master teacher, 
let's explore Radians, Degree, Functions, Parametric Equations, Polar Coordinates, and Sequences in an interactive way.
""")

topic = st.sidebar.radio(
    "Select a topic:",
    ["Radians", "Degree", "Function", "Parametric", "Polar", "Sequence"]
)

# -------------------------------------------------------------------
# 1. RADIANS
# -------------------------------------------------------------------
if topic == "Radians":
    st.subheader("Radians")

    st.markdown("""
    A radian measures the angle based on the arc length on a unit circle.
    - 1 radian = length of arc = 1 (on a unit circle).
    - π radians = 180°, so 1 rad ≈ 57.2958°.
    """)

    st.markdown("Interactive Conversion: Move the slider to convert degrees to radians.")
    deg_slider = st.slider("Degrees", min_value=0, max_value=360, value=90, step=5)
    radians_value = deg_slider  np.pi / 180
    st.write(f"{deg_slider}° is about {radians_value:.3f} radians.")

    st.markdown("Now try converting radians back to degrees.")
    #rad_slider = st.slider("Radians", min_value=0.0, max_value=2np.pi, value=np.pi/2, step=0.1)
    rad_slider = st.slider("Radians", min_value=0.0, max_value=2*np.pi, value=np.pi/2, step=0.1) 
    degrees_value = rad_slider  180 / np.pi
    st.write(f"{rad_slider:.2f} radians is about {degrees_value:.2f}°.")

# -------------------------------------------------------------------
# 2. DEGREE
# -------------------------------------------------------------------
elif topic == "Degree":
    st.subheader("Degree")

    st.markdown("""
    A degree is a measure of plane angles, with a full circle being 360°.
    Common angles: 90° (right angle), 180° (straight angle), 360° (full turn).
    """)

    st.markdown("Activity: Let's break down a circle into degrees.")
    circle_degrees = st.slider("Divide the circle?", 1, 360, 6, step=1)
    st.write(f"A full circle is split into slices of {360/circle_degrees:.2f}° each.")
    
    # (Optional) Visual representation: a pie chart
    fig, ax = plt.subplots()
    ax.pie([1]circle_degrees, startangle=90, labels=None)
    ax.set_title(f"{circle_degrees} slices in a circle (each is {360/circle_degrees:.1f}°).")
    st.pyplot(fig)

# -------------------------------------------------------------------
# 3. FUNCTION
# -------------------------------------------------------------------
elif topic == "Function":
    st.subheader("Linear Function")

    st.markdown("""
    A linear function follows the form y = mx + b, where:
    - m = slope
    - b = y-intercept
    Move the sliders below to change the slope and intercept.
    """)

    slope = st.slider("Slope (m)", min_value=-5.0, max_value=5.0, value=2.0, step=0.5)
    intercept = st.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=3.0, step=1.0)

    x_vals = np.linspace(-10, 10, 200)
    y_vals = slope  x_vals + intercept

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f"y = {slope}x + {intercept}", color="blue")
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_title("Interactive Linear Function")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)

# -------------------------------------------------------------------
# 4. PARAMETRIC
# -------------------------------------------------------------------
elif topic == "Parametric":
    st.subheader("Parametric Equations")

    st.markdown("""
    We define both x(t) and y(t) in terms of a third variable, t.
    Here, let's explore a circle or an ellipse by adjusting its parameters.
    """)

    radius_a = st.slider("Radius A (along x direction)", 0.5, 5.0, 1.0, step=0.5)
    radius_b = st.slider("Radius B (along y direction)", 0.5, 5.0, 1.0, step=0.5)

    t = np.linspace(0, 2np.pi, 200)
    x = radius_a  np.cos(t)
    y = radius_b  np.sin(t)

    fig, ax = plt.subplots()
    ax.plot(x, y, color="green", label=f"x(t)={radius_a}cos(t), y(t)={radius_b}sin(t)")
    ax.set_aspect("equal", "box")
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_title("Parametric Ellipse/Circle")
    ax.legend()
    st.pyplot(fig)

# -------------------------------------------------------------------
# 5. POLAR
# -------------------------------------------------------------------
elif topic == "Polar":
    st.subheader("Polar Coordinates")

    st.markdown("""
    In polar coordinates, a point is represented as (r, θ), where:
    - r is the distance from the origin
    - θ is the angle from the positive x-axis
    Let's visualize a spiral: r = a  θ. Move the slider to change a.
    """)

    a_value = st.slider("Spiral constant (a)", 0.1, 2.0, 1.0, step=0.1)

    theta = np.linspace(0, 4np.pi, 300)
    r = a_value  theta  # Spiral equation
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(theta, r, color="red", label=f"r = {a_value}  θ")
    ax.set_title("Polar Spiral")
    ax.legend()
    st.pyplot(fig)

# -------------------------------------------------------------------
# 6. SEQUENCE
# -------------------------------------------------------------------
elif topic == "Sequence":
    st.subheader("Arithmetic Sequence")

    st.markdown("""
    An arithmetic sequence is given by: 
    \[
      a_n = a_1 + (n-1)d
    \]
    where:
    - \( a_1 \) is the first term
    - \( d \) is the common difference
    """)

    first_term = st.number_input("First term (a₁)", value=3)
    common_diff = st.number_input("Common difference (d)", value=2)
    length = st.slider("How many terms?", min_value=5, max_value=20, value=10)

    n_values = np.arange(1, length+1)
    seq = [first_term + (n-1)common_diff for n in n_values]

    fig, ax = plt.subplots()
    markerline, stemlines, baseline = ax.stem(n_values, seq)
    # Optional styling
    plt.setp(markerline, marker='o', markersize=5, markerfacecolor='red')
    plt.setp(stemlines, color='gray', linewidth=1)
    plt.setp(baseline, color='black', linewidth=0.5)

    ax.set_title(f"Arithmetic Sequence (a₁={first_term}, d={common_diff})")
    ax.set_xlabel("Term index (n)")
    ax.set_ylabel("Value")
    st.pyplot(fig)

    st.write("Sequence values:", seq)
