import streamlit as st

# Ensure 'streamlit' is installed in the environment before running
try:
    import streamlit as st
except ModuleNotFoundError:
    raise ModuleNotFoundError("Streamlit is not installed. Install it using 'pip install streamlit'")

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * (conversion_dict[to_unit] / conversion_dict[from_unit])
    return None

# Conversion factors (relative to SI units)
unit_conversions = {
    "Energy": {"J": 1, "eV": 1.60218e-19, "Ha": 4.35974e-18},
    "Length": {"m": 1, "nm": 1e-9, "Å": 1e-10, "feet": 3.28084},
    "Time": {"s": 1, "fs": 1e-15, "day": 86400},
    "Frequency": {"Hz": 1, "THz": 1e12},
    "Mass": {"kg": 1, "amu": 1.66054e-27, "pounds": 2.20462},
    "Speed": {"mph": 1, "km/h": 1.60934},
    "Temperature": {"C": 1, "F": (lambda x: x * 9/5 + 32, lambda x: (x - 32) * 5/9)}
}

st.title("🔬 Quantum Unit Converter")

st.sidebar.header("🌟 Popular Conversions")
st.sidebar.text("Length: 1 meter = 3.28084 feet")
st.sidebar.text("Weight: 1 kilogram = 2.20462 pounds")
st.sidebar.text("Temperature: 0°C = 32°F")
st.sidebar.text("Speed: 1 mph = 1.60934 km/h")
st.sidebar.text("Time: 1 day = 86400 seconds")

# Sidebar selection for unit type
unit_type = st.sidebar.selectbox("Select Quantity Type", list(unit_conversions.keys()))

# Get available units for the selected type
available_units = list(unit_conversions[unit_type].keys())

# User input fields
value = st.number_input("Enter value:", min_value=0.0, format="%.6f")
from_unit = st.selectbox("From", available_units)
to_unit = st.selectbox("To", available_units)

if st.button("Convert"):
    if unit_type == "Temperature":
        to_func, from_func = unit_conversions[unit_type]["F"]
        if from_unit == "C" and to_unit == "F":
            result = to_func(value)
        elif from_unit == "F" and to_unit == "C":
            result = from_func(value)
        else:
            result = None
    else:
        result = convert_units(value, from_unit, to_unit, unit_conversions[unit_type])
    
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.6e} {to_unit}")
    else:
        st.error("Invalid conversion!")
