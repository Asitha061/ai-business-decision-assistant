import streamlit as st

st.title("AI Business Decision Assistant")

st.write("Enter your business details:")

revenue = st.number_input("Revenue", min_value=0.0, value=0.0)
cost = st.number_input("Cost", min_value=0.0, value=0.0)

if st.button("Analyze"):

    profit = revenue - cost
    st.write("### Profit:", profit)

    # avoid divide issues + make logic clearer
    if revenue == 0:
        st.warning("Enter revenue greater than 0")
    else:
        profit_margin = (profit / revenue) * 100
        st.write("Profit Margin (%):", profit_margin)

        if cost > revenue:
            st.error("⚠️ High Risk: You are making a loss!")
        elif cost > 0.8 * revenue:
            st.warning("⚠️ Medium Risk: Low profit margin")
        else:
            st.success("✅ Low Risk: Business is healthy")