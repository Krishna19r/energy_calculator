import streamlit as st

# Page configuration
st.set_page_config(
    page_title="🏡 Energy Calculator",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize session state variables
def init_session_state():
    if 'step' not in st.session_state:
        st.session_state.step = 1
    if 'user_data' not in st.session_state:
        st.session_state.user_data = {}
    if 'cal_energy' not in st.session_state:
        st.session_state.cal_energy = 0.0

# Custom CSS
st.markdown("""
<style>
    .main > div {
        padding-top: 1rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    .main-header {
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
    }
    
    .step-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    .step-header {
        color: #4facfe;
        font-size: 1.3rem;
        font-weight: bold;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .step-number {
        background: linear-gradient(45deg, #4facfe, #00f2fe);
        color: white;
        border-radius: 50%;
        width: 35px;
        height: 35px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1rem;
    }
    
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
        margin: 1rem 0;
    }
    
    .energy-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FFD700;
        margin: 1rem 0;
    }
    
    .summary-item {
        background: rgba(255, 255, 255, 0.1);
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        color: white;
    }
    
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
init_session_state()

# Header
st.markdown('<h1 class="main-header">⚡ Smart Energy Calculator</h1>', unsafe_allow_html=True)

# Progress indicator
progress_percentage = min(((st.session_state.step - 1) / 7) * 100, 100)
st.progress(progress_percentage / 100)
st.markdown(f"<p style='text-align: center; color: white; margin-bottom: 2rem;'>Step {st.session_state.step} of 8</p>", unsafe_allow_html=True)

# Navigation functions
def next_step():
    if st.session_state.step < 8:
        st.session_state.step += 1

def prev_step():
    if st.session_state.step > 1:
        st.session_state.step -= 1

def calculate_energy():
    """Calculate energy based on user selections"""
    energy = 0.0
    
    # Base energy calculation
    facility = st.session_state.user_data.get('facility', '')
    if facility == '1bhk':
        energy += 2 * 0.4 + 2 * 0.8  # 2.4
    elif facility == '2bhk':
        energy += 3 * 0.4 + 3 * 0.8  # 3.6
    elif facility == '3bhk':
        energy += 4 * 0.4 + 4 * 0.8  # 4.8
    
    # Appliances
    if st.session_state.user_data.get('ac') == 'yes':
        energy += 3
    if st.session_state.user_data.get('fridge') == 'yes':
        energy += 3
    if st.session_state.user_data.get('washing_machine') == 'yes':
        energy += 3
    
    st.session_state.cal_energy = energy
    return energy

# Step 1: Personal Information
if st.session_state.step == 1:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">1</div>
            <span>👋 Personal Information</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("personal_info_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("🧑 Your Name", placeholder="Enter your full name")
        
        with col2:
            age = st.number_input("🎂 Your Age", min_value=1, max_value=120, value=25)
        
        submitted = st.form_submit_button("Next Step →", use_container_width=True)
        
        if submitted:
            if name.strip():
                st.session_state.user_data['name'] = name.strip()
                st.session_state.user_data['age'] = age
                next_step()
                st.rerun()
            else:
                st.error("Please enter your name to continue.")

# Step 2: Location Information
elif st.session_state.step == 2:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">2</div>
            <span>📍 Location Details</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("location_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            city = st.text_input("🏙️ City", placeholder="Enter your city")
        
        with col2:
            area = st.text_input("🏘️ Area", placeholder="Enter your area")
        
        col1, col2 = st.columns(2)
        with col1:
            prev_btn = st.form_submit_button("← Previous", use_container_width=True)
        with col2:
            next_btn = st.form_submit_button("Next Step →", use_container_width=True)
        
        if prev_btn:
            prev_step()
            st.rerun()
        elif next_btn:
            if city.strip() and area.strip():
                st.session_state.user_data['city'] = city.strip()
                st.session_state.user_data['area'] = area.strip()
                next_step()
                st.rerun()
            else:
                st.error("Please fill in both city and area.")

# Step 3: Housing Type
elif st.session_state.step == 3:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">3</div>
            <span>🏠 Housing Type</span>
        </div>
        <p style="margin-bottom: 1rem;">Select your housing type:</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏢 Flat", key="flat_btn", use_container_width=True):
            st.session_state.user_data['housing_type'] = 'Flat'
            next_step()
            st.rerun()
    
    with col2:
        if st.button("🏘️ Tenament", key="tenament_btn", use_container_width=True):
            st.session_state.user_data['housing_type'] = 'Tenament'
            next_step()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Previous", key="prev_3", use_container_width=True):
        prev_step()
        st.rerun()

# Step 4: Room Configuration
elif st.session_state.step == 4:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">4</div>
            <span>🛏️ Room Configuration</span>
        </div>
        <p style="margin-bottom: 1rem;">How many bedrooms does your home have?</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("1️⃣ 1 BHK", key="1bhk_btn", use_container_width=True):
            st.session_state.user_data['facility'] = '1bhk'
            next_step()
            st.rerun()
    
    with col2:
        if st.button("2️⃣ 2 BHK", key="2bhk_btn", use_container_width=True):
            st.session_state.user_data['facility'] = '2bhk'
            next_step()
            st.rerun()
    
    with col3:
        if st.button("3️⃣ 3 BHK", key="3bhk_btn", use_container_width=True):
            st.session_state.user_data['facility'] = '3bhk'
            next_step()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Previous", key="prev_4", use_container_width=True):
        prev_step()
        st.rerun()

# Step 5: Air Conditioning
elif st.session_state.step == 5:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">5</div>
            <span>❄️ Air Conditioning</span>
        </div>
        <p style="margin-bottom: 1rem;">Do you use air conditioning?</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Yes", key="ac_yes", use_container_width=True):
            st.session_state.user_data['ac'] = 'yes'
            next_step()
            st.rerun()
    
    with col2:
        if st.button("❌ No", key="ac_no", use_container_width=True):
            st.session_state.user_data['ac'] = 'no'
            next_step()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Previous", key="prev_5", use_container_width=True):
        prev_step()
        st.rerun()

# Step 6: Refrigerator
elif st.session_state.step == 6:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">6</div>
            <span>🧊 Refrigerator</span>
        </div>
        <p style="margin-bottom: 1rem;">Do you have a refrigerator?</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Yes", key="fridge_yes", use_container_width=True):
            st.session_state.user_data['fridge'] = 'yes'
            next_step()
            st.rerun()
    
    with col2:
        if st.button("❌ No", key="fridge_no", use_container_width=True):
            st.session_state.user_data['fridge'] = 'no'
            next_step()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Previous", key="prev_6", use_container_width=True):
        prev_step()
        st.rerun()

# Step 7: Washing Machine
elif st.session_state.step == 7:
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">7</div>
            <span>🧺 Washing Machine</span>
        </div>
        <p style="margin-bottom: 1rem;">Do you have a washing machine?</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("✅ Yes", key="wm_yes", use_container_width=True):
            st.session_state.user_data['washing_machine'] = 'yes'
            next_step()
            st.rerun()
    
    with col2:
        if st.button("❌ No", key="wm_no", use_container_width=True):
            st.session_state.user_data['washing_machine'] = 'no'
            next_step()
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Previous", key="prev_7", use_container_width=True):
        prev_step()
        st.rerun()

# Step 8: Results
elif st.session_state.step == 8:
    # Calculate final energy
    total_energy = calculate_energy()
    
    # Results display
    st.markdown(f"""
    <div class="result-card">
        <h2>🎉 Calculation Complete!</h2>
        <div class="energy-value">{total_energy:.2f} kWh</div>
        <p style="font-size: 1.2rem;">Your Daily Energy Consumption</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Summary
    st.markdown("""
    <div class="step-card">
        <div class="step-header">
            <div class="step-number">✓</div>
            <span>📊 Summary</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="summary-item">
            <strong>👤 Name:</strong> {st.session_state.user_data.get('name', 'N/A')}
        </div>
        <div class="summary-item">
            <strong>🎂 Age:</strong> {st.session_state.user_data.get('age', 'N/A')} years
        </div>
        <div class="summary-item">
            <strong>📍 Location:</strong> {st.session_state.user_data.get('area', 'N/A')}, {st.session_state.user_data.get('city', 'N/A')}
        </div>
        <div class="summary-item">
            <strong>🏠 Housing:</strong> {st.session_state.user_data.get('housing_type', 'N/A')}
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="summary-item">
            <strong>🛏️ Configuration:</strong> {st.session_state.user_data.get('facility', 'N/A').upper()}
        </div>
        <div class="summary-item">
            <strong>❄️ Air Conditioning:</strong> {'✅ Yes' if st.session_state.user_data.get('ac') == 'yes' else '❌ No'}
        </div>
        <div class="summary-item">
            <strong>🧊 Refrigerator:</strong> {'✅ Yes' if st.session_state.user_data.get('fridge') == 'yes' else '❌ No'}
        </div>
        <div class="summary-item">
            <strong>🧺 Washing Machine:</strong> {'✅ Yes' if st.session_state.user_data.get('washing_machine') == 'yes' else '❌ No'}
        </div>
        """, unsafe_allow_html=True)
    
    # Energy breakdown
    st.markdown("### Energy Breakdown")
    
    # Calculate individual components
    base_energy = 0
    facility = st.session_state.user_data.get('facility', '')
    if facility == '1bhk':
        base_energy = 2.4
    elif facility == '2bhk':
        base_energy = 3.6
    elif facility == '3bhk':
        base_energy = 4.8
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("🏠 Base", f"{base_energy:.1f} kWh")
    
    with col2:
        ac_energy = 3 if st.session_state.user_data.get('ac') == 'yes' else 0
        st.metric("❄️ AC", f"{ac_energy:.1f} kWh")
    
    with col3:
        fridge_energy = 3 if st.session_state.user_data.get('fridge') == 'yes' else 0
        st.metric("🧊 Fridge", f"{fridge_energy:.1f} kWh")
    
    with col4:
        wm_energy = 3 if st.session_state.user_data.get('washing_machine') == 'yes' else 0
        st.metric("🧺 Washing", f"{wm_energy:.1f} kWh")
    
    # Action buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Start Over", key="restart", use_container_width=True):
            # Reset all session state
            st.session_state.step = 1
            st.session_state.user_data = {}
            st.session_state.cal_energy = 0.0
            st.rerun()
    
    with col2:
        if st.button("← Previous", key="prev_final", use_container_width=True):
            prev_step()
            st.rerun()

# Debug info (remove in production)
if st.sidebar.checkbox("Debug Info", value=False):
    st.sidebar.write("Current Step:", st.session_state.step)
    st.sidebar.write("User Data:", st.session_state.user_data)
    st.sidebar.write("Energy:", st.session_state.cal_energy)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255, 255, 255, 0.8); padding: 1rem;">
    <p>⚡ Smart Energy Calculator | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)