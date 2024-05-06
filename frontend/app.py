import streamlit as st
import json
import requests as re

st.title("Hệ thống phát hiện gian lận thẻ tín dụng thời gian thực")

st.image("image.png")

st.write("""

**Thành viên - MSSV** 
- **Võ Quốc Huy - 20081001**
- **Ngô Hoàng Nhật Huy - 20079071**
- **Nguyễn Quang Bảo -  20083601**
- **Nguyễn Xuân Giang - 20079601**
""")

st.sidebar.header('Input Features of The Transaction')
time = st.sidebar.number_input("Time")
V1 = st.sidebar.number_input("V1")
V2 = st.sidebar.number_input("V2")
V3 = st.sidebar.number_input("V3")
V4 = st.sidebar.number_input("V4")
V5 = st.sidebar.number_input("V5")
V6 = st.sidebar.number_input("V6")
V7 = st.sidebar.number_input("V7")
V8 = st.sidebar.number_input("V8")
V9 = st.sidebar.number_input("V9")
V10 = st.sidebar.number_input("V10")
V11 = st.sidebar.number_input("V11")
V12 = st.sidebar.number_input("V12")
V13 = st.sidebar.number_input("V13")
V14 = st.sidebar.number_input("V14")
V15 = st.sidebar.number_input("V15")
V16 = st.sidebar.number_input("V16")
V17 = st.sidebar.number_input("V17")
V18 = st.sidebar.number_input("V18")
V19 = st.sidebar.number_input("V19")
V20 = st.sidebar.number_input("V20")
V21 = st.sidebar.number_input("V21")
V22 = st.sidebar.number_input("V22")
V23 = st.sidebar.number_input("V23")
V24 = st.sidebar.number_input("V24")
V25 = st.sidebar.number_input("V25")
V26 = st.sidebar.number_input("V26")
V27 = st.sidebar.number_input("V27")
V28 = st.sidebar.number_input("V28")
Amount = st.sidebar.number_input("Amount")


if st.button("Detection Result"):
    values = {
        "time": float(time),
        "V1": float(V1),
        "V2": float(V2),
        "V3": float(V3),
        "V4": float(V4),
        "V5": float(V5),
        "V6": float(V6),
        "V7": float(V7),
        "V8": float(V8),
        "V9": float(V9),
        "V10": float(V10),
        "V11": float(V11),
        "V12": float(V12),
        "V13": float(V13),
        "V14": float(V14),
        "V15": float(V15),
        "V16": float(V16),
        "V17": float(V17),
        "V18": float(V18),
        "V19": float(V19),
        "V20": float(V20),
        "V21": float(V21),
        "V22": float(V22),
        "V23": float(V23),
        "V24": float(V24),
        "V25": float(V25),
        "V26": float(V26),
        "V27": float(V27),
        "V28": float(V28),
        "Amount": float(Amount)
    }

    st.write(f"""### These are the transaction details:\n
    Time: {time} \n 
    V1:{V1} \t V2:{V2} \t V3:{V3} \t V4:{V4} \t V5:{V5} \t V6:{V6} \t V7:{V7} \n
    V8:{V8} \t V9:{V9} \t V10:{V10} \t V11:{V11} \t V12:{V12} \t V13:{V13} \t V14:{V14} \n 
    V15:{V15} \t V16:{V16} \t V17:{V17} \t V18:{V18} \t V19:{V19} \t V20:{V20} \t V21:{V21} \n 
    V22:{V22} \t V23:{V23} \t V24:{V24} \t V25:{V25} \t V26:{V26} \t V27:{V27} \t V28:{V28} \n
    Amount:{Amount}""")

    st.subheader("Prediction:")
    response = re.post("http://backend.docker:8000/predict", json=values)
    if response.status_code == 200:
        result = response.json()
        if result is not None:
            st.write(f"{result[0]}")
        else:
            st.write("Invalid response from prediction API.")
    else:
        st.write(f"Error: {response.status_code} - {response.text}")
