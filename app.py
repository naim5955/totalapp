import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import math
import os

# --- BRANDING FILE CONFIGURATION ---
logo_filename = "logo.png"

# --- SYSTEM WIDE CONFIGURATION ---
st.set_page_config(
    page_title="Techno Commercial Suite | LafargeHolcim",
    page_icon="🏗️",
    layout="centered"
)

# --- ADVANCED EXECUTIVE DESIGN SYSTEM & STYLES ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #F8FAFC !important;
        padding: 4px !important;
    }
    
    /* Centered Header Container */
    .hero-header-box {
        text-align: center !important;
        background: #FFFFFF;
        padding: 20px 15px 15px 15px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        margin-bottom: 20px;
    }
    
    .company-header-centered { 
        font-size: 26px !important; 
        font-weight: 800; 
        color: #DC2626; 
        letter-spacing: -0.5px;
        margin-top: 10px;
        margin-bottom: 2px;
        line-height: 1.2;
        text-align: center !important;
    }
    .app-title-centered {
        font-size: 14px !important;
        font-weight: 600;
        color: #64748B;
        text-align: center !important;
        margin-bottom: 5px;
        line-height: 1.3;
    }

    /* Executive Cards with Lift & Gradient Accents */
    .tco-card {
        padding: 18px;
        border-radius: 14px;
        margin-bottom: 14px;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04), 0 2px 4px -1px rgba(0, 0, 0, 0.02);
        transition: all 0.25s ease-in-out;
    }
    .tco-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 20px -4px rgba(0, 0, 0, 0.08);
    }
    .card-title { font-size: 11px; font-weight: 800; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 6px; }
    .card-value { font-size: 22px; font-weight: 800; }
    .card-sub { font-size: 12px; color: #64748B; margin-top: 4px; line-height: 1.4; }
    
    /* Grid KPI Cards */
    .mobile-metric-card {
        background-color: #FFFFFF;
        padding: 18px;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        border-left: 6px solid #2563EB;
        margin-top: 8px;
        margin-bottom: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        transition: transform 0.2s ease;
    }
    .mobile-metric-card:hover { transform: translateY(-2px); }
    .metric-label { font-size: 11px; color: #64748B; font-weight: 700; letter-spacing: 0.5px; text-transform: uppercase; }
    .metric-value { font-size: 22px; font-weight: 800; color: #0F172A; margin-top: 2px; }

    /* Custom Tables */
    .custom-tco-table {
        width: 100% !important;
        table-layout: fixed !important;
        border-collapse: separate !important;
        border-spacing: 0 !important;
        border-radius: 12px !important;
        overflow: hidden !important;
        border: 1px solid #E2E8F0 !important;
        margin-bottom: 12px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02) !important;
    }
    .custom-tco-table th {
        text-align: center !important;
        vertical-align: middle !important;
        font-weight: 700 !important;
        padding: 12px 10px !important;
        background-color: #F1F5F9 !important;
        color: #334155 !important;
        border-bottom: 1px solid #E2E8F0 !important;
        font-size: 12px !important;
    }
    .custom-tco-table td {
        text-align: right !important;
        vertical-align: middle !important;
        padding: 12px 10px !important;
        border-bottom: 1px solid #F1F5F9 !important;
        background-color: #FFFFFF !important;
        font-size: 13px !important;
        color: #1E293B !important;
    }
    .custom-tco-table tr:hover td {
        background-color: #F8FAFC !important;
    }
    .custom-tco-table td:first-child {
        text-align: left !important;
        font-weight: 600 !important;
    }

    /* Buttons */
    div.stButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 10px 16px !important;
        transition: all 0.2s ease !important;
    }

    /* Footer */
    .dev-footer {
        background: linear-gradient(135deg, #FFFFFF 0%, #F8FAFC 100%);
        padding: 18px; 
        border-radius: 14px; 
        border: 1px solid #E2E8F0;
        border-left: 6px solid #DC2626;
        margin-top: 35px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .signature-box { font-size: 13px; color: #64748B; line-height: 1.5; border-top: 1px solid #E2E8F0; padding-top: 12px; margin-top: 20px; }
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
        st.markdown('<div class="hero-header-box">', unsafe_allow_html=True)
        if os.path.exists(logo_filename):
            col_l_img, col_m_img, col_r_img = st.columns([1, 2, 1])
            with col_m_img:
                st.image(logo_filename, use_container_width=True)
        st.markdown('<div class="company-header-centered">LafargeHolcim Bangladesh PLC</div>', unsafe_allow_html=True)
        st.markdown('<div class="app-title-centered">আমার বাড়ি Techno-Commercial Suite</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<p style='font-size: 14px; color: #475569; font-weight: 600; text-align: center;'>Developed By MD. Abdullah Al Naim, AE (Noakhali Area)</p>", unsafe_allow_html=True)
        user_id = st.text_input("User ID (TSE01 to TSE10)", key="sys_uid").strip().upper()
        password = st.text_input("Password", type="password", key="sys_pwd")
        
        valid_users = [f"TSE{str(i).zfill(2)}" for i in range(1, 11)]
        
        if st.button("Access Portal Dashboard", use_container_width=True, type="primary"):
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
                Assistant Engineer, LHB
            </div>
        """, unsafe_allow_html=True)
    st.stop()

# --- APP NAVIGATION MENU UTILITIES ---
def go_to_page(page_name):
    st.session_state['current_page'] = page_name
    st.rerun()

# --- BRANDING BAR TOP LAYER (CENTERED HERO BOX) ---
st.markdown('<div class="hero-header-box">', unsafe_allow_html=True)
if os.path.exists(logo_filename):
    c_l, c_m, c_r = st.columns([1.2, 1, 1.2])
    with c_m:
        st.image(logo_filename, width=150)
st.markdown('<div class="company-header-centered">LafargeHolcim Bangladesh PLC</div>', unsafe_allow_html=True)
st.markdown(f'<div class="app-title-centered">আমার বাড়ি Techno-Commercial Suite | Session: <b>{st.session_state.get("user_id", "Guest")}</b></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- MAIN ENGINE DISTRIBUTION CENTRE ---

# PAGE A: CENTRAL NAVIGATION PANEL
if st.session_state['current_page'] == "Dashboard":
    st.subheader("Select Commercial Suite Calculator")
    st.markdown("---")
    
    if st.button("📊 Cost Estimation Calculator (Dampproof Wall)", use_container_width=True):
        go_to_page("TCO")
        
    if st.button("🧱 Wall & Ceiling Plaster Calculator", use_container_width=True):
        go_to_page("Plaster")
        
    if st.button("🏗️ Slab / Column Material Volume Estimator", use_container_width=True):
        go_to_page("SlabColumn")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 System Log Out", use_container_width=True):
        st.session_state['authenticated'] = False
        st.rerun()

# PAGE B: COST ESTIMATION CALCULATOR (DAMPPROOF WALL)
elif st.session_state['current_page'] == "TCO":
    st.markdown("<h4 style='text-align: center; color: #1E293B;'>Cost Estimation Calculator (Dampproof Wall)</h4>", unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    st.subheader("🏢 Building Details")
    floor_size = st.number_input("Floor Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="tco_f_sz")
    stories = st.number_input("Number of Stories", min_value=1, value=5, step=1, key="tco_st_n")
    
    st.subheader("Enter Unit Pricing (BDT)")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        local_brand_price = st.number_input("Local Cement Price (per Bag)", min_value=300, value=530, step=5, key="tco_l_pr")
        lh_premium_price = st.number_input("Holcim Premium Price (per Bag)", min_value=400, value=680, step=10, key="tco_p_pr")
        sand_price_cft = st.number_input("Sand Price (per CFT)", min_value=10, value=40, step=5, key="tco_s_pr")
    with col_t2:
        initial_paint_sqft = st.number_input("Initial Painting Cost (per Sq. Ft.)", min_value=10, value=35, step=5, key="tco_p_sq")
        dampproof_price_sqft = st.number_input("Damp proofing Cost (per Sq. Ft.)", min_value=5, value=25, step=5, key="tco_dp_sq")
        failure_years = st.slider("Projected Dampness in (Years)", min_value=2, max_value=12, value=8, key="tco_fail_y")
    
    # Mathematical Modeling Layer
    ext_area = floor_size * stories * 0.7   
    int_area = floor_size * stories * 2.8
    total_wall_area = ext_area + int_area
    roof_screed = floor_size
    
    def calc_bags(area, thick):
        return (area * (thick / 12.0) * 1.33 * 0.2) / 1.25
    
    t_bags = round(calc_bags(int_area, 0.5) + calc_bags(ext_area, 0.75) + calc_bags(roof_screed, 0.75))
    t_sand_cft = t_bags * 1.25 * 4.0
    
    # Financial Matrix Computations
    cost_cem_std = t_bags * local_brand_price
    cost_cem_hwp = t_bags * lh_premium_price
    cost_sand = t_sand_cft * sand_price_cft
    cost_initial_paint = total_wall_area * initial_paint_sqft
    
    initial_std_total = cost_cem_std + cost_sand + cost_initial_paint
    initial_hwp_total = cost_cem_hwp + cost_sand + cost_initial_paint
    
    upfront_extra_cost = initial_hwp_total - initial_std_total
    
    # Recurring Repair Costs (1/3 Paint Rework + 1/3 Dampproofing Area Treatment)
    recurring_paint_cost = cost_initial_paint / 3.0
    recurring_dampproof_cost = (total_wall_area * dampproof_price_sqft) / 3.0
    recurring_damage_shock = recurring_paint_cost + recurring_dampproof_cost
    
    lifetime_std_total = initial_std_total + recurring_damage_shock
    lifetime_hwp_total = initial_hwp_total
    
    total_net_savings = lifetime_std_total - lifetime_hwp_total
    
    # Annualized Savings & Annual ROI Calculations
    annual_net_savings = total_net_savings / failure_years
    total_roi_percentage = (total_net_savings / initial_hwp_total * 100) if initial_hwp_total > 0 else 0.0
    annual_roi_percentage = total_roi_percentage / failure_years

    # Custom Table Generator
    def render_custom_table(df):
        html = '<table class="custom-tco-table"><thead><tr>'
        for col in df.columns:
            html += f'<th>{col}</th>'
        html += '</tr></thead><tbody>'
        for _, row in df.iterrows():
            html += '<tr>'
            for val in row:
                html += f'td>{val}</td>'
            html += '</tr>'
        html += '</tbody></table>'
        return html.replace('td>', '<td>')

    # Breakdown Tables
    st.markdown("---")
    st.subheader("⚖️ 1. Initial Investment Comparison")
    
    col_std_header = "Traditional<br>(Local Brand)"
    col_hwp_header = "Premium<br>(Holcim Premium)"
    
    initial_comparison_df = pd.DataFrame({
        "Cost Element": ["Cement Cost", "Sand Cost", "Painting Cost", "Total Initial Cost"],
        col_std_header: [f"BDT {cost_cem_std:,.0f}", f"BDT {cost_sand:,.0f}", f"BDT {cost_initial_paint:,.0f}", f"BDT {initial_std_total:,.0f}"],
        col_hwp_header: [f"BDT {cost_cem_hwp:,.0f}", f"BDT {cost_sand:,.0f}", f"BDT {cost_initial_paint:,.0f}", f"BDT {initial_hwp_total:,.0f}"],
        "Premium Extra Cost": [f"+ BDT {upfront_extra_cost:,.0f}", "BDT 0", "BDT 0", f"+ BDT {upfront_extra_cost:,.0f}"]
    })
    st.markdown(render_custom_table(initial_comparison_df), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader(f"⏱️ 2. Lifecycle ROI (Year {failure_years})")
    
    lifecycle_df = pd.DataFrame({
        "Plan Options": ["Traditional (Local Brand)", "Holcim Premium Plan"],
        "Initial Cost": [f"BDT {initial_std_total:,.0f}", f"BDT {initial_hwp_total:,.0f}"],
        "Re-Painting Cost": [f"BDT {recurring_paint_cost:,.0f}", "BDT 0"],
        "Dampproofing Cost": [f"BDT {recurring_dampproof_cost:,.0f}", "BDT 0"],
        "Total Lifetime Cost": [f"BDT {lifetime_std_total:,.0f}", f"BDT {lifetime_hwp_total:,.0f}"]
    })
    st.markdown(render_custom_table(lifecycle_df), unsafe_allow_html=True)
    
    st.markdown("""
        <div style="font-size: 12px; color: #475569; margin-top: 8px; margin-bottom: 15px; background-color: #F1F5F9; padding: 10px; border-radius: 8px;">
            <b>** Note:</b> 1/3 of total paint cost is considered as repainting and 1/3 of surface area damp proofing cost is considered.
        </div>
    """, unsafe_allow_html=True)

    # Executive Summary Cards
    st.markdown("---")
    st.subheader("📈 Executive Summary")

    st.markdown(f"""
        <div class="tco-card" style="border-left: 6px solid #0284C7;">
            <div class="card-title" style="color: #0369A1;">TOTAL COST OF OWNERSHIP (HOLCIM PREMIUM)</div>
            <div class="card-value" style="color: #0284C7;">BDT {lifetime_hwp_total:,.0f}</div>
            <div class="card-sub">Total initial investment for Holcim Premium plan (Cement + Sand + Paint)</div>
        </div>
        
        <div class="tco-card" style="border-left: 6px solid #EF4444;">
            <div class="card-title" style="color: #991B1B;">ADDITIONAL COST OF OWNERSHIP (LOCAL BRAND)</div>
            <div class="card-value" style="color: #DC2626;">BDT {recurring_damage_shock:,.0f}</div>
            <div class="card-sub">Expected recurring dampness damage & repair cost by Year {failure_years}</div>
        </div>
        
        <div class="tco-card" style="border-left: 6px solid #10B981; background: linear-gradient(135deg, #FFFFFF 0%, #F0FDF4 100%);">
            <div class="card-title" style="color: #065F46;">ANNUAL NET SAVINGS (ROI)</div>
            <div class="card-value" style="color: #047857;">BDT {annual_net_savings:,.0f} / Year ({annual_roi_percentage:,.1f}% / Year)</div>
            <div class="card-sub">Total lifetime net savings: <b>BDT {total_net_savings:,.0f} ({total_roi_percentage:,.1f}%)</b> over {failure_years} years against total Holcim Premium plan investment of BDT {initial_hwp_total:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

    # Plotly Chart
    st.markdown("<br>", unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=['Traditional Plan', 'Premium Plan'], 
        x=[initial_std_total, initial_hwp_total], 
        name='Initial CapEx Base', 
        orientation='h', 
        marker=dict(color='#3B82F6')
    ))
    fig.add_trace(go.Bar(
        y=['Traditional Plan', 'Premium Plan'], 
        x=[recurring_damage_shock, 0], 
        name='1/3 Paint & Dampproof Repair Cost', 
        orientation='h', 
        marker=dict(color='#EF4444')
    ))
    
    fig.update_layout(
        barmode='stack',
        height=240,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5, font=dict(size=10)),
        xaxis=dict(title="Total Outflow (BDT)", tickformat=",.0f", tickfont=dict(size=9)),
        yaxis=dict(tickfont=dict(size=10))
    )
    st.plotly_chart(fig, use_container_width=True)

    with st.expander("🔍 Plaster and Paints Surface Area"):
        st.markdown(f"""
        * **Internal Wall Area:** {int_area:,.0f} Sq. Ft. (2.8x floor area per story).
        * **External Wall Area:** {ext_area:,.0f} Sq. Ft. (0.7x floor area per story).
        * **Total Wall Plaster Surface Area:** {total_wall_area:,.0f} Sq. Ft.
        * **Total Cement Bags Required:** {t_bags:,} bags.
        * **Sand Required:** {t_sand_cft:,.1f} CFT
        """)

# PAGE C: WALL & ROOF PLASTER MATERIAL QUANTIFICATION
elif st.session_state['current_page'] == "Plaster":
    st.markdown("<h4 style='text-align: center; color: #1E293B;'>Wall & Ceiling Plaster Calculator</h4>", unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    st.subheader("📋 Building Details")
    f_size = st.number_input("Floor Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="pl_f_sz")
    f_stories = st.number_input("Number of Stories", min_value=1, value=5, step=1, key="pl_st_n")
    s_ratio = st.number_input("Cement:Sand Ratio (1:X)", min_value=1.0, value=4.0, step=0.5, key="pl_s_rt")
    
    col_p1, col_p2 = st.columns(2)
    with col_p1:
        c_price = st.number_input("Cement Bag Price (BDT)", min_value=0, value=650, step=10, key="pl_c_pr")
    with col_p2:
        s_price = st.number_input("Sand Price per CFT (BDT)", min_value=0, value=45, step=5, key="pl_s_pr")
    
    # Plaster Calculation Layer
    b_up_area = f_size * f_stories
    a_out = b_up_area * 0.7
    a_in = b_up_area * 2.8
    a_rf = f_size
    
    def run_plaster_vol(area, thick):
        wet_vol = area * (thick / 12.0)
        dry_vol = wet_vol * 1.33
        return dry_vol
        
    dry_vol_out = run_plaster_vol(a_out, 0.75)
    dry_vol_in = run_plaster_vol(a_in, 0.5)
    dry_vol_rf = run_plaster_vol(a_rf, 0.5)
    total_dry_volume_all = dry_vol_out + dry_vol_in + dry_vol_rf
    
    total_parts = 1.0 + s_ratio
    total_cement_cft = total_dry_volume_all * (1.0 / total_parts)
    total_sand_cft = total_dry_volume_all * (s_ratio / total_parts)
    
    total_plaster_bags = math.ceil(total_cement_cft / 1.25)
    
    cost_cement_total = total_plaster_bags * c_price
    cost_sand_total = total_sand_cft * s_price
    gross_plaster_budget = cost_cement_total + cost_sand_total
    
    # 4-Card Grid
    row1_col1, row1_col2 = st.columns(2)
    with row1_col1:
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #DC2626;">
                <div class="metric-label">TOTAL CEMENT REQUIRED</div>
                <div class="metric-value">{total_plaster_bags:,} Bags</div>
            </div>
        """, unsafe_allow_html=True)
    with row1_col2:
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #2563EB;">
                <div class="metric-label">TOTAL SAND VOLUME</div>
                <div class="metric-value">{total_sand_cft:,.1f} CFT</div>
            </div>
        """, unsafe_allow_html=True)

    row2_col1, row2_col2 = st.columns(2)
    with row2_col1:
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #10B981;">
                <div class="metric-label">TOTAL CEMENT COST</div>
                <div class="metric-value">BDT {cost_cement_total:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)
    with row2_col2:
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #F59E0B;">
                <div class="metric-label">TOTAL SAND COST</div>
                <div class="metric-value">BDT {cost_sand_total:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)

    with st.expander("🔍 Material Details"):
        plaster_breakdown = {
            "Structural Part": ["Outside Walls Plaster", "Inside Walls Plaster", "Roof Screed Layer", "Total Volumetric Target"],
            "Surface Area Scope": [f"{a_out:,.0f} Sq. Ft.", f"{a_in:,.0f} Sq. Ft.", f"{a_rf:,.0f} Sq. Ft.", f"{a_out+a_in+a_rf:,.0f} Sq. Ft."],
            "Design Thickness": ['0.75 Inches', '0.50 Inches', '0.50 Inches', 'Composite Layout'],
            "Cement Sand Volume": [f"{dry_vol_out:,.1f} CFT", f"{dry_vol_in:,.1f} CFT", f"{dry_vol_rf:,.1f} CFT", f"{total_dry_volume_all:,.1f} CFT"]
        }
        st.table(pd.DataFrame(plaster_breakdown))
        st.markdown(f"""
        ### Material Calculation Details
        * **Dry Plaster Volume:** {total_dry_volume_all:,.1f} CFT.
        * **Cement Component:**  {total_cement_cft:,.1f} CFT based on 1 part of the 1:{s_ratio} mix ratio.
        * **Sand Component:** {total_sand_cft:,.1f} CFT based on {s_ratio} parts of the 1:{s_ratio} mix ratio.
        * **Total Plaster Bags Required:** {total_plaster_bags:,} bags.
        """)

# PAGE D: STRUCTURAL ELEMENTS COMPUTATION
elif st.session_state['current_page'] == "SlabColumn":
    st.markdown("<h4 style='text-align: center; color: #1E293B;'>Column/Slab Materials Volume Calculation</h4>", unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    el_choice = st.radio("Select Structure Elements:", ["Column", "Slab & Beam"], horizontal=True)
    st.markdown("---")
    
    if el_choice == "Column":
        st.subheader("🏛️ Column Details")
        cw = st.number_input("Column Width (Inches)", min_value=1.0, value=10.0, step=1.0, key="col_w")
        cl = st.number_input("Column Length (Inches)", min_value=1.0, value=12.0, step=1.0, key="col_l")
        ch = st.number_input("Height of Column (Feet)", min_value=1.0, value=10.0, step=0.5, key="col_h")
        c_num = st.number_input("Number of Columns", min_value=1, value=15, step=1, key="col_n")
        
        st.subheader("🧪 Concrete Mix Ratio & Pricing")
        csand = st.number_input("Sand Ratio Component (1 : X : Y)", min_value=0.5, value=1.5, step=0.5, key="col_sd_r")
        cagg = st.number_input("Aggregate Ratio Component (1 : X : Y)", min_value=0.5, value=3.0, step=0.5, key="col_ag_r")
        c_price = st.number_input("Cement Bag Price (BDT)", min_value=0, value=650, step=10, key="col_c_pr")
        
        # Volumetric Concrete Math Framework
        c_wet = ((cw / 12.0) * (cl / 12.0) * ch) * c_num
        c_dry = c_wet * 1.54 
        
        c_total_parts = 1.0 + csand + cagg
        c_cement_cft = c_dry * (1.0 / c_total_parts)
        c_sand_cft = c_dry * (csand / c_total_parts)
        c_agg_cft = c_dry * (cagg / c_total_parts)
        
        c_bags = math.ceil(c_cement_cft / 1.25)
        total_cement_budget = c_bags * c_price
        
        # 4-Card Grid
        col_r1_c1, col_r1_c2 = st.columns(2)
        with col_r1_c1:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #DC2626;">
                    <div class="metric-label">TOTAL CEMENT REQUIRED</div>
                    <div class="metric-value">{c_bags:,} Bags</div>
                </div>
            """, unsafe_allow_html=True)
        with col_r1_c2:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #2563EB;">
                    <div class="metric-label">SAND VOLUME</div>
                    <div class="metric-value">{c_sand_cft:,.1f} CFT</div>
                </div>
            """, unsafe_allow_html=True)

        col_r2_c1, col_r2_c2 = st.columns(2)
        with col_r2_c1:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #F59E0B;">
                    <div class="metric-label">COARSE AGGREGATE VOLUME</div>
                    <div class="metric-value">{c_agg_cft:,.1f} CFT</div>
                </div>
            """, unsafe_allow_html=True)
        with col_r2_c2:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #10B981;">
                    <div class="metric-label">TOTAL CEMENT COST</div>
                    <div class="metric-value">BDT {total_cement_budget:,.0f}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with st.expander("🔍 Volumetric Calculations Details"):
            st.markdown(f"""
            ### Column Concrete Material Details
            * **Wet Volume of Single Column:** Width × Length × Height = {((cw/12.0)*(cl/12.0)*ch):.3f} CFT.
            * **Total Wet Concrete Volume:** Combined volume for {c_num} columns is {c_wet:.2f} CFT.
            * **Total Dry Concrete Volume:** Wet volume multiplied by standard 1.54 concrete shrinkage factor yields {c_dry:.2f} CFT.
            * **Cement Component:**  {c_cement_cft:,.1f} CFT based on 1 part of the 1:{csand}:{cagg} mix ratio.
            * **Sand Component:** {c_sand_cft:,.1f} CFT based on {csand} parts of the mix.
            * **Aggregate Component:** {c_agg_cft:,.1f} CFT based on {cagg} parts of the mix.
            """)

    elif el_choice == "Slab & Beam":
        st.subheader("📐 Slab Dimensions")
        s_area = st.number_input("Floor Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="sb_a")
        s_thick = st.number_input("Slab Thickness (Inches)", min_value=1.0, value=5.0, step=0.5, key="sb_t")
        
        b_profile = st.radio("Select Beam Profile Style:", ["Concealed Beam", "Normal Hanging Beam"], horizontal=True)
        eff_thick = s_thick + 0.5 if b_profile == "Normal Hanging Beam" else s_thick
        if b_profile == "Normal Hanging Beam":
            st.info("💡 Added 0.5 inches thickness parameters globally to encompass physical beams allowances.")
            
        st.subheader("🧪 Concrete Mix Ratio & Pricing")
        ssand = st.number_input("Sand Ratio Component (1 : X : Y)", min_value=0.5, value=2.0, step=0.5, key="sb_sd_r")
        sagg = st.number_input("Aggregate Ratio Component (1 : X : Y)", min_value=0.5, value=4.0, step=0.5, key="sb_ag_r")
        s_price = st.number_input("Cement Bag Price (BDT)", min_value=0, value=650, step=10, key="sb_c_pr")
        
        s_wet = s_area * (eff_thick / 12.0)
        s_dry = s_wet * 1.54
        
        s_total_parts = 1.0 + ssand + sagg
        s_cement_cft = s_dry * (1.0 / s_total_parts)
        s_sand_cft = s_dry * (ssand / s_total_parts)
        s_agg_cft = s_dry * (sagg / s_total_parts)
        
        s_bags = math.ceil(s_cement_cft / 1.25)
        total_slab_cement_budget = s_bags * s_price
        
        # 4-Card Grid
        sb_r1_c1, sb_r1_c2 = st.columns(2)
        with sb_r1_c1:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #DC2626;">
                    <div class="metric-label">TOTAL CEMENT REQUIRED</div>
                    <div class="metric-value">{s_bags:,} Bags</div>
                </div>
            """, unsafe_allow_html=True)
        with sb_r1_c2:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #2563EB;">
                    <div class="metric-label">SAND VOLUME</div>
                    <div class="metric-value">{s_sand_cft:,.1f} CFT</div>
                </div>
            """, unsafe_allow_html=True)

        sb_r2_c1, sb_r2_c2 = st.columns(2)
        with sb_r2_c1:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #F59E0B;">
                    <div class="metric-label">COARSE AGGREGATE VOLUME</div>
                    <div class="metric-value">{s_agg_cft:,.1f} CFT</div>
                </div>
            """, unsafe_allow_html=True)
        with sb_r2_c2:
            st.markdown(f"""
                <div class="mobile-metric-card" style="border-left-color: #10B981;">
                    <div class="metric-label">TOTAL CEMENT COST</div>
                    <div class="metric-value">BDT {total_slab_cement_budget:,.0f}</div>
                </div>
            """, unsafe_allow_html=True)
        
        with st.expander("🔍 Volumetric Calculations Details"):
            st.markdown(f"""
            ### Slab and Beam Concrete Material Details
            * **Effective Slab Thickness:**  {eff_thick:.2f} Inches.
            * **Total Wet Concrete Volume:** Floor Area × (Slab Thickness / 12) = {s_wet:.2f} CFT.
            * **Total Dry Concrete Volume:** Wet volume multiplied by standard 1.54 concrete shrinkage multiplier yields {s_dry:.2f} CFT.
            * **Cement Component:**  {s_cement_cft:,.1f} CFT based on 1 part of the 1:{ssand}:{sagg} mix ratio.
            * **Sand Component:** {s_sand_cft:,.1f} CFT based on {ssand} parts of the mix.
            * **Aggregate Component:** {s_agg_cft:,.1f} CFT based on {sagg} parts of the mix.
            """)

# --- GLOBAL SYSTEM FOOTER BANNER ---
st.markdown(f"""
    <div class="dev-footer">
        <span style="font-size: 10px; color: #64748B; font-weight: 700; letter-spacing: 0.8px; text-transform: uppercase;">SYSTEM DEVELOPER & MAINTENANCE</span><br>
        <span style="font-size: 15px; font-weight: 800; color: #0F172A;">MD Abdullah Al Naim</span><br>
        <span style="font-size: 12px; color: #475569; font-weight: 500;">Assistant Engineer</span><br>
        <span style="font-size: 12px; color: #DC2626; font-weight: 600;">LafargeHolcim Bangladesh PLC</span>
    </div>
""", unsafe_allow_html=True)
