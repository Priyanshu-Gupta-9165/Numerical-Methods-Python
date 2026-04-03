import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Configure Streamlit page
st.set_page_config(
    page_title="Polynomial Regression Dashboard",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper Functions
@st.cache_data
def generate_sample_data():
    """Generates some sample non-linear data."""
    np.random.seed(42)
    x = np.linspace(-5, 5, 30)
    y = 0.5 * x**3 - 2 * x**2 + x + 10 + np.random.normal(0, 15, 30)
    return pd.DataFrame({"X": x, "Y": y})

def train_poly_model(X, y, degree):
    """Fits a polynomial regression model."""
    poly = PolynomialFeatures(degree=degree)
    X_poly = poly.fit_transform(X)
    
    model = LinearRegression()
    model.fit(X_poly, y)
    
    return model, poly

def calculate_errors(y_true, y_pred):
    """Calculates Mean Squared Error and Root Mean Squared Error."""
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    return mse, rmse

def predict_value(model, poly, x_val):
    """Predicts y for a given x using the trained model."""
    x_val_poly = poly.transform([[x_val]])
    return model.predict(x_val_poly)[0]

# UI Layout
st.title("📈 Polynomial Regression Dashboard")

st.markdown("""
This application allows you to explore **Polynomial Regression**. You can upload your own dataset or use manual inputs to see how changing the degree of the polynomial affects the model's fit to the data.
""")

# Sidebar settings
st.sidebar.header("1. Data Input")
data_source = st.sidebar.radio("Choose Data Source:", ("Use Sample Data", "Upload CSV", "Manual Input"))

df = None

if data_source == "Use Sample Data":
    df = generate_sample_data()
    st.sidebar.markdown("Using generated sample data for demonstration.")

elif data_source == "Upload CSV":
    uploaded_file = st.sidebar.file_uploader("Upload CSV file (must have 'X' and 'Y' columns)", type=["csv"])
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            if 'X' not in df.columns or 'Y' not in df.columns:
                st.sidebar.error("CSV must contain 'X' and 'Y' columns (case-sensitive).")
                df = None
        except Exception as e:
            st.sidebar.error(f"Error reading file: {e}")

elif data_source == "Manual Input":
    st.sidebar.markdown("Enter comma-separated numerical values:")
    x_input = st.sidebar.text_input("X values", "1, 2, 3, 4, 5, 6, 7")
    y_input = st.sidebar.text_input("Y values", "2.1, 3.9, 10.2, 15.5, 26.0, 35.1, 50.9")
    try:
        x_vals = [float(i.strip()) for i in x_input.split(",")]
        y_vals = [float(i.strip()) for i in y_input.split(",")]
        if len(x_vals) == len(y_vals) and len(x_vals) > 0:
            df = pd.DataFrame({"X": x_vals, "Y": y_vals})
        else:
            st.sidebar.error("X and Y must have the exact same number of values.")
    except ValueError:
        st.sidebar.error("Please enter valid numeric values separated by commas.")

# Main Application Logic
if df is not None and not df.empty:
    X = df[['X']].values
    y = df['Y'].values
    
    st.header("1. Dataset Overview")
    colA, colB = st.columns([1, 2])
    with colA:
        st.dataframe(df, use_container_width=True)
    
    st.sidebar.header("2. Model Settings")
    degree = st.sidebar.slider("Select Polynomial Degree", min_value=1, max_value=15, value=2, step=1)
    
    # Train model
    model, poly = train_poly_model(X, y, degree)
    
    # Range for plotting a smooth fitted curve instead of discrete points
    x_range = np.linspace(X.min() - (X.max()-X.min())*0.1, X.max() + (X.max()-X.min())*0.1, 300).reshape(-1, 1)
    y_range_pred = model.predict(poly.transform(x_range))
    
    y_pred = model.predict(poly.transform(X))
    mse, rmse = calculate_errors(y, y_pred)
    
    # Visualization
    st.header("2. Interactive Visualization")
    fig = go.Figure()
    
    # Plot original data points
    fig.add_trace(go.Scatter(x=df['X'], y=df['Y'], mode='markers', name='Actual Data',
                             marker=dict(size=10, color='#1f77b4', opacity=0.8)))
    
    # Plot fitted curve
    fig.add_trace(go.Scatter(x=x_range.flatten(), y=y_range_pred, mode='lines', name=f'Fitted Curve (Degree {degree})',
                             line=dict(color='#ff7f0e', width=3)))
    
    fig.update_layout(
        title=f"<b>Polynomial Regression Fit (Degree {degree})</b>",
        xaxis_title="X values",
        yaxis_title="Y values",
        template="plotly_white",
        hovermode="x unified",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Model details
    st.header("3. Model Details & Error Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Mean Squared Error (MSE)", value=f"{mse:.4f}")
    with col2:
        st.metric(label="Root Mean Squared Error (RMSE)", value=f"{rmse:.4f}")
        
    st.info("💡 **Error Insight**: Lower MSE and RMSE values indicate a better fit on the training data. Beware of **overfitting** when choosing a very high degree—the line may pass through clearly every point but fail dramatically on unseen data!")

    # Mathematical Formula Display Setup
    coefficients = model.coef_
    intercept = model.intercept_
    
    equation_parts = [f"{intercept:.4f}"]
    for i in range(1, len(coefficients)):
        coef = coefficients[i]
        if coef != 0:
            equation_parts.append(f"({coef:.4f}) X^{i}")
            
    equation_str = " + ".join(equation_parts).replace("+ -", "- ")
    
    st.markdown("### Generated Polynomial Equation:")
    if degree <= 5: # Render latex only for reasonable width
        st.latex(f"Y = {equation_str}")
    else:
        st.code(f"Y = {equation_str}", language="text")
    
    # Prediction
    st.sidebar.header("3. Make a Prediction")
    pred_input = st.sidebar.number_input("Enter a new X value to predict corresponding Y", value=0.0)
    pred_y = predict_value(model, poly, pred_input)
    st.sidebar.success(f"**Predicted Y:** {pred_y:.4f}")
    
    # Download
    st.sidebar.header("4. Export Results")
    df_results = df.copy()
    df_results['Predicted Y'] = y_pred
    df_results['Error (Y - Pred Y)'] = df_results['Y'] - df_results['Predicted Y']
    
    csv_results = df_results.to_csv(index=False)
    st.sidebar.download_button(
        label="Download Results (CSV)",
        data=csv_results,
        file_name=f'poly_regression_results_deg{degree}.csv',
        mime='text/csv'
    )
        
    # Bonus section
    st.markdown("---")
    with st.expander("📚 How Polynomial Regression Works & Overfitting Explained"):
        st.markdown("""
        **Polynomial Regression** is a form of regression analysis modeling the relationship between the independent variable $x$ and the dependent variable $y$ as an $n$th degree polynomial.
        
        The standard equation looks like this:
        $$ y = \\beta_0 + \\beta_1 x + \\beta_2 x^2 + \\dots + \\beta_n x^n + \\epsilon $$
        
        **The Effect of the Polynomial Degree ($n$):**
        - **Degree 1 (Underfitting):** Forms a simple straight line. Often fails to capture complexities or curves in the data trend.
        - **Optimal Degree:** Balances bias and variance flexibly following the true underlying data trend.
        - **High Degree (Overfitting):** The curve starts wiggling violently to pass perfectly through every single training point, capturing arbitrary *noise* instead of the actual pattern. It performs terribly when extrapolating or on new, unseen data, despite near-zero error on training data!
        """)
        
else:
    st.warning("Please provide valid data to proceed.")
