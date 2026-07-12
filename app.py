import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import math
import os

# --- BRANDING FILE CONFIGURATION ---
logo_filename = "logo.png"

# --- SYSTEM WIDE CONFIGURATION ---
st.set_page_config(
    page_title="LHBL Value Optimization Portal",
    page_icon="🏗️",
    layout="centered"
)

# --- GLOBAL DESIGN SYSTEM & MOBILE RESPONSIVE STYLES ---
st.markdown("""
    <style>
    html, body, [data-testid="stAppViewContainer"] {
        padding: 4px !important;
    }
    .company-header { 
        font-size: 24px !important; 
        font-weight: 800; 
        color: #DC2626; 
        margin-bottom: 2px;
        line-height: 1.2;
    }
    .app-title {
        font-size: 16px !important;
        font-weight: 600;
        color: #4B5563;
        margin-bottom: 15px;
        line-height: 1.3;
    }
    .stNumberInput input, .stSelectbox div {
        font-size: 16px !important; 
        padding: 8px !important;
    }
    .tco-card {
        padding: 14px;
        border-radius: 8px;
        margin-bottom: 10px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .card-title { font-size: 11px; font-weight: 700; letter-spacing: 0.5px; margin-bottom: 4px; }
    .card-value { font-size: 20px; font-weight: 800; }
    .card-sub { font-size: 11px; color: #4B5563; margin-top: 2px; }
    
    .mobile-metric-card {
        background-color: #F9FAFB;
        padding: 16px;
        border-radius: 8px;
        border-left: 5px solid #2563EB;
        margin-top: 15px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .metric-label { font-size: 12px; color: #6B7280; font-weight: bold; letter-spacing: 0.5px; }
    .metric-value { font-size: 22px; font-weight: 800; color: #111827; }

    .dev-footer {
        background-color: #F3F4F6; 
        padding: 14px; 
        border-radius: 6px; 
        border-left: 4px solid #DC2626;
        margin-top: 30px;
    }
    .signature-box { font-size: 13px; color: #6B7280; line-height: 1.4; border-top: 1px solid #E5E7EB; padding-top: 10px; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- CORE SESSION DATA HANDLERS ---
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = "Dashboard"

# --- AUTHENTICATION LAYER PORTAL ---
if not st.session_state['authenticated']:
    st.markdown("<br>", unsafe_allow_html=True)
    col_l, col_login, col_r = st.columns([0.1, 1.0, 0.1])
    
    with col_login:
        if os.path.exists(logo_filename):
            st.image(logo_filename, use_container_width=True)
            st.markdown("<br>", unsafe_allow_html=True)
            
        st.header("Port Login")
        st.subheader("LafargeHolcim Bangladesh PLC")
        
        user_id = st.text_input("User ID (TSE01 to TSE10)", key="sys_uid").strip().upper()
        password = st.text_input("Password", type="password", key="sys_pwd")
        
        valid_users = [f"TSE{str(i).zfill(2)}" for i in range(1, 11)]
        
        if st.button("Access Dashboard", use_container_width=True):
            if user_id in valid_users and password == "12121":
                st.session_state['authenticated'] = True
                st.session_state['user_id'] = user_id
                st.session_state['current_page'] = "Dashboard"
                st.rerun()
            else:
                st.error("Invalid User ID or Password. Please try again.")
        
        st.markdown("""
            <div class="signature-box">
                <b>🔑 Admin Support & Maintenance:</b><br>
                MD Abdullah Al Naim<br>
                Assistant Engineer, FrontDesk Bangladesh Ltd.
            </div>
        """, unsafe_allow_html=True)
    st.stop()

# --- APP NAVIGATION MENU UTILITIES ---
def go_to_page(page_name):
    st.session_state['current_page'] = page_name
    st.rerun()

# --- BRANDING BAR TOP LAYER ---
if os.path.exists(logo_filename):
    st.image(logo_filename, width=160)

st.markdown('<div class="company-header">LafargeHolcim Bangladesh PLC</div>', unsafe_allow_html=True)

# --- MAIN ENGINE DISTRIBUTION CENTRE ---

# PAGE A: CENTRAL NAVIGATION PANEL
if st.session_state['current_page'] == "Dashboard":
    st.markdown(f'<div class="app-title">Commercial Execution Suite | Session: {st.session_state["user_id"]}</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("🚀 Select Analytical Engine Tool")
    
    if st.button("📊 Total Cost of Ownership (TCO) Analyzer", use_container_width=True):
        go_to_page("TCO")
        
    if st.button("🧱 Wall & Roof Plaster Calculator", use_container_width=True):
        go_to_page("Plaster")
        
    if st.button("🏗️ Structural Elements (Slab / Column) Estimator", use_container_width=True):
        go_to_page("SlabColumn")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 System Log Out", use_container_width=True):
        st.session_state['authenticated'] = False
        st.rerun()

# PAGE B: TOTAL COST OF OWNERSHIP LCC ENGINE
elif st.session_state['current_page'] == "TCO":
    st.markdown('<div class="app-title">Total Cost of Ownership (TCO) & Value Analyzer</div>', unsafe_allow_html=True)
    
    # Navigation Action Bar
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    st.subheader("🏢 Structural Scope Parameters")
    floor_size = st.number_input("Floor Area per Story (Sq. Ft.)", min_value=100, value=2000, step=100, key="tco_f_sz")
    stories = st.number_input("Number of Stories", min_value=1, value=5, step=1, key="tco_st_n")
    
    st.subheader("💰 Pricing Adjustments (BDT)")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        local_brand_price = st.number_input("Local Brand Price (per Bag)", min_value=300, value=560, step=10, key="tco_l_pr")
        lh_premium_price = st.number_input("Holcim Premium Price (per Bag)", min_value=400, value=680, step=10, key="tco_p_pr")
    with col_t2:
        paint_price_sqft = st.number_input("Paint & Putty Cost (per Sq. Ft.)", min_value=5, value=35, step=5, key="tco_p_sq")
        repair_labor_sqft = st.number_input("Scraping Labor Cost (per Sq. Ft.)", min_value=5, value=5, step=5, key="tco_l_sq")
        
    failure_years = st.slider("Projected Dampness Failure Event Horizon (Years)", min_value=2, max_value=10, value=5, key="tco_fail_y")
    
    # Process Math Logic (Isolated strictly to wall surface protections per corporate alignment)
    ext_area = floor_size * stories * 0.7
    int_area = floor_size * stories * 2.8
    total_wall_area = ext_area + int_area
    roof_screed = floor_size
    
    def calc_bags(area, thick):
        return (area * (thick / 12.0) * 1.33 * 0.2) / 1.25
    
    t_bags = round(calc_bags(int_area, 0.5) + calc_bags(ext_area, 0.75) + calc_bags(roof_screed, 0.75))
    
    init_std = t_bags * local_brand_price
    init_hwp = t_bags * lh_premium_price
    upfront_delta = init_hwp - init_std
    
    f_paint = total_wall_area * paint_price_sqft
    f_labor = total_wall_area * repair_labor_sqft
    total_liabilities = f_paint + f_labor
    net_value_saved = total_liabilities - upfront_delta
    
    # Financial Output Display Panel
    st.markdown(f"""
        <div class="tco-card" style="background-color: #FEF2F2; border-left: 5px solid #EF4444;">
            <div class="card-title" style="color: #991B1B;">LOCAL BRAND INITIAL BUDGET</div>
            <div class="card-value" style="color: #B91C1C;">BDT {init_std:,.0f}</div>
            <div class="card-sub">For {t_bags:,} bags @ BDT {local_brand_price}/bag</div>
        </div>
        <div class="tco-card" style="background-color: #EFF6FF; border-left: 5px solid #2563EB;">
            <div class="card-title" style="color: #1E3A8A;">HOLCIM PREMIUM BUDGET</div>
            <div class="card-value" style="color: #1D4ED8;">BDT {init_hwp:,.0f}</div>
            <div class="card-sub">Upfront Investment Delta: <b>BDT {upfront_delta:,.0f}</b></div>
        </div>
        <div class="tco-card" style="background-color: #ECFDF5; border-left: 5px solid #10B981;">
            <div class="card-title" style="color: #065F46;">NET FINISHES SAVED (YEAR {failure_years})</div>
            <div class="card-value" style="color: #047857;">BDT {max(0, net_value_saved):,.0f}</div>
            <div class="card-sub">Avoided wall peeling and cosmetic maintenance bills</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Graphical Analytics Panel (Using explicit tickfont configs)
    fig = go.Figure()
    fig.add_trace(go.Bar(y=['Traditional Plan', 'Premium Plan'], x=[init_std, init_hwp], name='Initial Cement Cost', orientation='h', marker=dict(color='#3B82F6')))
    fig.add_trace(go.Bar(y=['Traditional Plan', 'Premium Plan'], x=[total_liabilities, 0], name=f'Wall Dampness Repair (Year {failure_years})', orientation='h', marker=dict(color='#EF4444')))
    fig.update_layout(barmode='stack', height=220, margin=dict(l=10, r=10, t=10, b=10), legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5, font=dict(size=9)), xaxis=dict(title="Total Outflow (BDT)", tickformat=",.0f", tickfont=dict(size=9)), yaxis=dict(tickfont=dict(size=9)))
    st.plotly_chart(fig, use_container_width=True)

# PAGE C: WALL & ROOF PLASTER MATERIAL QUANTIFICATION
elif st.session_state['current_page'] == "Plaster":
    st.markdown('<div class="app-title">Wall & Roof Plaster Calculator Engine</div>', unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    st.subheader("📋 Design Dimensions")
    f_size = st.number_input("Floor Footprint Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="pl_f_sz")
    f_stories = st.number_input("Number of Stories", min_value=1, value=5, step=1, key="pl_st_n")
    s_ratio = st.number_input("Sand Proportion Ratio (1:X)", min_value=1.0, value=4.0, step=0.5, key="pl_s_rt")
    c_price = st.number_input("Cement Bag Price (BDT) - Optional", min_value=0, value=650, step=10, key="pl_c_pr")
    
    # Plaster Volumetric Matrix Layer
    b_up_area = f_size * f_stories
    a_out = b_up_area * 0.7
    a_in = b_up_area * 2.8
    a_rf = f_size
    
    def run_plaster_math(area, thick, sand):
        return (((area * (thick / 12.0)) * 1.33) * (1.0 / (1.0 + sand))) / 1.25
        
    b_out = run_plaster_math(a_out, 0.75, s_ratio)
    b_in = run_plaster_math(a_in, 0.5, s_ratio)
    b_rf = run_plaster_math(a_rf, 0.5, s_ratio)
    
    total_plaster_bags = math.ceil(b_out + b_in + b_rf)
    
    st.markdown(f"""
        <div class="mobile-metric-card" style="border-left-color: #DC2626;">
            <div class="metric-label">TOTAL PLASTER CEMENT REQUIRED</div>
            <div class="metric-value">{total_plaster_bags:,} Bags</div>
        </div>
    """, unsafe_allow_html=True)
    if c_price > 0:
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #10B981;">
                <div class="metric-label">TOTAL ESTIMATED CEMENT BUDGET</div>
                <div class="metric-value">BDT {total_plaster_bags * c_price:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)

# PAGE D: STRUCTURAL ELEMENTS STRUCTURAL COMPUTATION
elif st.session_state['current_page'] == "SlabColumn":
    st.markdown('<div class="app-title">Structural Elements Concrete Estimator</div>', unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    el_choice = st.radio("Select Structural Variant Target:", ["Column", "Slab & Beam"], horizontal=True)
    st.markdown("---")
    
    if el_choice == "Column":
        st.subheader("🏛️ Column Engineering Scope")
        cw = st.number_input("Column Width (Inches)", min_value=1.0, value=10.0, step=1.0, key="col_w")
        cl = st.number_input("Column Length (Inches)", min_value=1.0, value=12.0, step=1.0, key="col_l")
        ch = st.number_input("Height of Column (Feet)", min_value=1.0, value=10.0, step=0.5, key="col_h")
        c_num = st.number_input("Number of Columns", min_value=1, value=15, step=1, key="col_n")
        
        st.subheader("🧪 Concrete Volumetric Aggregates Mix")
        csand = st.number_input("Sand Ratio Component", min_value=0.5, value=1.5, step=0.5, key="col_sd_r")
        cagg = st.number_input("Stone/Khoa Ratio Component", min_value=0.5, value=3.0, step=0.5, key="col_ag_r")
        
        c_wet = ((cw / 12.0) * (cl / 12.0) * ch) * c_num
        c_dry = c_wet * 1.54
        c_bags = math.ceil((c_dry * (1.0 / (1.0 + csand + cagg))) / 1.25)
        
        st.markdown(f"""
            <div class="mobile-metric-card">
                <div class="metric-label">TOTAL COLUMN CEMENT REQUIRED</div>
                <div class="metric-value">{c_bags:,} Bags</div>
            </div>
        """, unsafe_allow_html=True)

    elif el_choice == "Slab & Beam":
        st.subheader("📐 Horizontal Slab Footprint")
        s_area = st.number_input("Floor Footprint Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="sb_a")
        s_thick = st.number_input("Slab Core Thickness (Inches)", min_value=1.0, value=5.0, step=0.5, key="sb_t")
        
        b_profile = st.radio("Select Beam Profile Style:", ["Concealed Beam", "Normal Hanging Beam"], horizontal=True)
        eff_thick = s_thick + 0.5 if b_profile == "Normal Hanging Beam" else s_thick
        if b_profile == "Normal Hanging Beam":
            st.info("💡 Added 0.5 inches thickness parameters globally to encompass physical beams allowances.")
            
        st.subheader("🧪 Concrete Volumetric Aggregates Mix")
        ssand = st.number_input("Sand Ratio Component", min_value=0.5, value=2.0, step=0.5, key="sb_sd_r")
        sagg = st.number_input("Stone/Khoa Ratio Component", min_value=0.5, value=4.0, step=0.5, key="sb_ag_r")
        
        s_wet = s_area * (eff_thick / 12.0)
        s_dry = s_wet * 1.54
        s_bags = math.ceil((s_dry * (1.0 / (1.0 + ssand + sagg))) / 1.25)
        
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #10B981;">
                <div class="metric-label">TOTAL SLAB & BEAM CEMENT REQUIRED</div>
                <div class="metric-value">{s_bags:,} Bags</div>
            </div>
        """, unsafe_allow_html=True)

# --- GLOBAL SYSTEM FOOTER BANNER ---
st.markdown(f"""
    <div class="dev-footer">
        <span style="font-size: 10px; color: #6B7280; font-weight: bold; letter-spacing: 0.5px;">SYSTEM DEVELOPER & MAINTENANCE</span><br>
        <span style="font-size: 14px; font-weight: 700; color: #111827;">MD Abdullah Al Naim</span><br>
        <span style="font-size: 11px; color: #4B5563;">Assistant Engineer</span><br>
        <span style="font-size: 11px; color: #4B5563; font-style: italic;">LafargeHolcim Bangladesh PLC</span>
    </div>
""", unsafe_allow_html=True)
