import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import math
import os

# --- BRANDING FILE CONFIGURATION ---
logo_filename = "logo.png"

# --- SYSTEM WIDE CONFIGURATION ---
st.set_page_config(
    page_title="Techno Commercial Suite Portal",
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
            
        st.header("আমার বাড়ি App Login")
        st.subheader("LafargeHolcim Bangladesh PLC")
        st.subheader("Developed By LHB Technical Team")    
        
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
                Assistant Engineer, LHB
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
    st.markdown(f'<div class="app-title">আমার বাড়ি Techno-Commercial Suite | Session: {st.session_state["user_id"]}</div>', unsafe_allow_html=True)
    st.markdown("---")
    
    st.subheader("Select Calculation toll")
    
    if st.button("📊 Total Cost of Ownership (TCO) & ROI Analyzer", use_container_width=True):
        go_to_page("TCO")
        
    if st.button("🧱 Wall & Ceiling Plaster Calculator", use_container_width=True):
        go_to_page("Plaster")
        
    if st.button("🏗️ Slab / Column material volume Estimator", use_container_width=True):
        go_to_page("SlabColumn")
        
    st.markdown("<br><br>", unsafe_allow_html=True)
    if st.button("🚪 System Log Out", use_container_width=True):
        st.session_state['authenticated'] = False
        st.rerun()

# PAGE B: TOTAL COST OF OWNERSHIP LCC ENGINE
elif st.session_state['current_page'] == "TCO":
    st.markdown('<div class="app-title">Total Cost of Ownership (TCO) & ROI Lifecycle Analyzer</div>', unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    st.subheader("🏢 Structural Dimensions")
    floor_size = st.number_input("Floor Footprint Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="tco_f_sz")
    stories = st.number_input("Number of Stories", min_value=1, value=5, step=1, key="tco_st_n")
    
    st.subheader("Input unit Pricing (BDT)")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        local_brand_price = st.number_input("Local Cement Price (per Bag)", min_value=300, value=560, step=10, key="tco_l_pr")
        lh_premium_price = st.number_input("Holcim Premium Price (per Bag)", min_value=400, value=680, step=10, key="tco_p_pr")
        sand_price_cft = st.number_input("Sand Market Price (per CFT)", min_value=10, value=40, step=5, key="tco_s_pr")
    with col_t2:
        initial_paint_sqft = st.number_input("Initial Paint & Putty Cost (per Sq. Ft.)", min_value=10, value=35, step=5, key="tco_p_sq")
        failure_years = st.slider("Projected Dampness in (Years)", min_value=2, max_value=10, value=5, key="tco_fail_y")
    
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
    
    # The 40% Painting Rework Rule application
    recurring_damage_shock = cost_initial_paint * 0.40
    
    lifetime_std_total = initial_std_total + recurring_damage_shock
    lifetime_hwp_total = initial_hwp_total
    
    net_roi_savings = lifetime_std_total - lifetime_hwp_total
    
    # ROI Percentage calculation
    roi_percentage = (net_roi_savings / upfront_extra_cost * 100) if upfront_extra_cost > 0 else 0.0
    
    # Upfront Extra Cost & ROI Cards
    st.markdown(f"""
        <div class="tco-card" style="background-color: #FFFBEB; border-left: 5px solid #F59E0B;">
            <div class="card-title" style="color: #92400E;">INITIAL PREMIUM INVESTMENT</div>
            <div class="card-value" style="color: #D97706;">BDT {upfront_extra_cost:,.0f}</div>
            <div class="card-sub">Premium protection additional cost at Day 1</div>
        </div>
        <div class="tco-card" style="background-color: #ECFDF5; border-left: 5px solid #10B981;">
            <div class="card-title" style="color: #065F46;">NET RETURN ON INVESTMENT (YEAR {failure_years})</div>
            <div class="card-value" style="color: #047857;">BDT {net_roi_savings:,.0f} ({roi_percentage:,.1f}%)</div>
            <div class="card-sub">Net Return of premium investment</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Horizontal Comparison Charts (Horizontal Layout Reverted)
    st.markdown("<br>", unsafe_allow_html=True)
    fig = go.Figure()
    fig.add_trace(go.Bar(y=['Traditional Plan', 'Premium Plan'], x=[initial_std_total, initial_hwp_total], name='Initial CapEx Base', orientation='h', marker=dict(color='#3B82F6')))
    fig.add_trace(go.Bar(y=['Traditional Plan', 'Premium Plan'], x=[recurring_damage_shock, 0], name='40% Paint Repair Shock', orientation='h', marker=dict(color='#EF4444')))
    
    fig.update_layout(
        barmode='stack',
        height=220,
        margin=dict(l=10, r=10, t=10, b=10),
        legend=dict(orientation="h", yanchor="bottom", y=1.1, xanchor="center", x=0.5, font=dict(size=9)),
        xaxis=dict(title="Total Outflow (BDT)", tickformat=",.0f", tickfont=dict(size=9)),
        yaxis=dict(tickfont=dict(size=9))
    )
    st.plotly_chart(fig, use_container_width=True)

    # Detailed Upfront Cost Table
    st.subheader("⚖️ 1. Initial Investment Comparison Breakdown")
    initial_comparison_data = {
        "Cost Element": ["Cement Cost", "Sand Cost", "Initial Paint & Putty Layer", "Total Initial Project Cost"],
        "Traditional (Local Brand)": [f"BDT {cost_cem_std:,.0f}", f"BDT {cost_sand:,.0f}", f"BDT {cost_initial_paint:,.0f}", f"BDT {initial_std_total:,.0f}"],
        "Premium (LHB Premium)": [f"BDT {cost_cem_hwp:,.0f}", f"BDT {cost_sand:,.0f}", f"BDT {cost_initial_paint:,.0f}", f"BDT {initial_hwp_total:,.0f}"],
        "Premium Cost": [f"+ BDT {upfront_extra_cost:,.0f}", "BDT 0", "BDT 0", f"+ BDT {upfront_extra_cost:,.0f}"]
    }
    st.table(pd.DataFrame(initial_comparison_data))

    # Comprehensive Lifecycle Cost Table
    st.subheader(f"⏱️ 2. Lifecycle ROI Breakdown (Year {failure_years})")
    lifecycle_data = {
        "Plan Strategy Options": ["Traditional Local Brand Plan", "Holcim Premium Plan"],
        "Initial Capital Cost": [f"BDT {initial_std_total:,.0f}", f"BDT {initial_hwp_total:,.0f}"],
        "Recurring Paint and Damp Proofing Cost": [f"BDT {recurring_damage_shock:,.0f}", "BDT 0 "],
        "Total Lifetime Cost": [f"BDT {lifetime_std_total:,.0f}", f"BDT {lifetime_hwp_total:,.0f}"]
    }
    st.table(pd.DataFrame(lifecycle_data))

    with st.expander("🔍 Deep Technical Engineering Log"):
        st.markdown(f"""
        ### Plaster and Paint Surface Areas
        * **Internal Wall Area:** Calculated as {int_area:,.0f} Sq. Ft. (based on 2.8x floor area per story).
        * **External Wall Area:** Calculated as {ext_area:,.0f} Sq. Ft. (based on 0.7x floor area per story).
        * **Total Wall Plaster Skin Area:** Combined internal and external wall surface area is {total_wall_area:,.0f} Sq. Ft.
        * **Total Cement Bags Required:** Sum of internal plaster, external plaster, and roof screed bag requirements totals {t_bags:,} bags.
        * **Sand Required:** Plaster sand requirements total {t_sand_cft:,.1f} CFT (calculated using the 1:4 layout ratio of 5 CFT of sand per bag of cement).
        """)

# PAGE C: WALL & ROOF PLASTER MATERIAL QUANTIFICATION
elif st.session_state['current_page'] == "Plaster":
    st.markdown('<div class="app-title">Wall & Ceiling Plaster Calculator</div>', unsafe_allow_html=True)
    
    nav_col1, nav_col2 = st.columns(2)
    with nav_col1:
        if st.button("⬅️ Back to Main Menu", use_container_width=True): go_to_page("Dashboard")
    with nav_col2:
        if st.button("🚪 Quick Logout", use_container_width=True): st.session_state['authenticated'] = False; st.rerun()
    st.markdown("---")
    
    st.subheader("📋 Design Dimensions & Unit Pricing Inputs")
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
    
    st.markdown(f"""
        <div class="mobile-metric-card" style="border-left-color: #DC2626;">
            <div class="metric-label">TOTAL PLASTER MATERIALS REQUIRED</div>
            <div class="metric-value">{total_plaster_bags:,} Cement Bags</div>
            <div style="font-size: 13px; color: #4B5563; margin-top: 4px;">Sand Volume: <b>{total_sand_cft:,.1f} CFT</b></div>
        </div>
        <div class="mobile-metric-card" style="border-left-color: #10B981;">
            <div class="metric-label">TOTAL MATERIALS ESTIMATED BUDGET</div>
            <div class="metric-value">BDT {gross_plaster_budget:,.0f}</div>
            <div style="font-size: 11px; color: #6B7280; margin-top: 2px;">Cement Share: BDT {cost_cement_total:,.0f} | Sand Share: BDT {cost_sand_total:,.0f}</div>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("🔍 Complete Material Breakdowns & Calculation Log"):
        plaster_breakdown = {
            "Structural Part": ["Outside Walls Plaster", "Inside Walls Plaster", "Roof Screed Layer", "Total Volumetric Target"],
            "Surface Area Scope": [f"{a_out:,.0f} Sq. Ft.", f"{a_in:,.0f} Sq. Ft.", f"{a_rf:,.0f} Sq. Ft.", f"{a_out+a_in+a_rf:,.0f} Sq. Ft."],
            "Design Thickness": ['0.75 Inches', '0.50 Inches', '0.50 Inches', 'Composite Layout'],
            "Dry Aggregate Volume": [f"{dry_vol_out:,.1f} CFT", f"{dry_vol_in:,.1f} CFT", f"{dry_vol_rf:,.1f} CFT", f"{total_dry_volume_all:,.1f} CFT"]
        }
        st.table(pd.DataFrame(plaster_breakdown))
        st.markdown(f"""
        ### Material Calculation Details
        * **Dry Plaster Volume:** Total dry plaster mix required for all areas is {total_dry_volume_all:,.1f} CFT.
        * **Cement Component:** Calculated as {total_cement_cft:,.1f} CFT based on 1 part of the 1:{s_ratio} mix ratio.
        * **Sand Component:** Calculated as {total_sand_cft:,.1f} CFT based on {s_ratio} parts of the 1:{s_ratio} mix ratio.
        * **Total Plaster Bags Required:** Total cement volume divided by standard bag volume yields {total_plaster_bags:,} bags.
        """)

# PAGE D: STRUCTURAL ELEMENTS STRUCTURAL COMPUTATION
elif st.session_state['current_page'] == "SlabColumn":
    st.markdown('<div class="app-title">Column/Slab Materials Volume Calculation</div>', unsafe_allow_html=True)
    
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
        
        st.markdown(f"""
            <div class="mobile-metric-card">
                <div class="metric-label">TOTAL COLUMN MATERIALS REQUIRED</div>
                <div class="metric-value">{c_bags:,} Cement Bags</div>
                <div style="font-size: 13px; color: #4B5563; margin-top: 4px;">
                    Sand Target Volume: <b>{c_sand_cft:,.1f} CFT</b><br>
                    Coarse Aggregate Target Volume: <b>{c_agg_cft:,.1f} CFT</b>
                </div>
            </div>
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
            * **Cement Component:** Calculated as {c_cement_cft:,.1f} CFT based on 1 part of the 1:{csand}:{cagg} mix ratio.
            * **Sand Component:** Calculated as {c_sand_cft:,.1f} CFT based on {csand} parts of the mix.
            * **Aggregate Component:** Calculated as {c_agg_cft:,.1f} CFT based on {cagg} parts of the mix.
            """)

    elif el_choice == "Slab & Beam":
        st.subheader("📐 Slab Dimensions")
        s_area = st.number_input("Floor  Area (Sq. Ft.)", min_value=100, value=2000, step=100, key="sb_a")
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
        
        st.markdown(f"""
            <div class="mobile-metric-card" style="border-left-color: #10B981;">
                <div class="metric-label">TOTAL SLAB & BEAM MATERIALS REQUIRED</div>
                <div class="metric-value">{s_bags:,} Cement Bags</div>
                <div style="font-size: 13px; color: #4B5563; margin-top: 4px;">
                    Sand Volume: <b>{s_sand_cft:,.1f} CFT</b><br>
                    Coarse Aggregate Volume: <b>{s_agg_cft:,.1f} CFT</b>
                </div>
            </div>
            <div class="mobile-metric-card" style="border-left-color: #2563EB;">
                <div class="metric-label">TOTAL CEMENT COST</div>
                <div class="metric-value">BDT {total_slab_cement_budget:,.0f}</div>
            </div>
        """, unsafe_allow_html=True)
        
        with st.expander("🔍 Volumetric Calculations Details"):
            st.markdown(f"""
            ### Slab and Beam Concrete Material Details
            * **Effective Slab Thickness:** Effective height of slab casting is {eff_thick:.2f} Inches.
            * **Total Wet Concrete Volume:** Floor Area × (Slab Thickness / 12) = {s_wet:.2f} CFT.
            * **Total Dry Concrete Volume:** Wet volume multiplied by standard 1.54 concrete shrinkage multiplier yields {s_dry:.2f} CFT.
            * **Cement Component:** Calculated as {s_cement_cft:,.1f} CFT based on 1 part of the 1:{ssand}:{sagg} mix ratio.
            * **Sand Component:** Calculated as {s_sand_cft:,.1f} CFT based on {ssand} parts of the mix.
            * **Aggregate Component:** Calculated as {s_agg_cft:,.1f} CFT based on {sagg} parts of the mix.
            """)

# --- GLOBAL SYSTEM FOOTER BANNER ---
st.markdown(f"""
    <div class="dev-footer">
        <span style="font-size: 10px; color: #6B7280; font-weight: bold; letter-spacing: 0.5px;">SYSTEM DEVELOPER & MAINTENANCE</span><br>
        <span style="font-size: 14px; font-weight: 700; color: #111827;">MD Abdullah Al Naim</span><br>
        <span style="font-size: 11px; color: #4B5563;">Assistant Engineer</span><br>
        <span style="font-size: 11px; color: #4B5563; font-style: italic;">LafargeHolcim Bangladesh PLC</span>
    </div>
""", unsafe_allow_html=True)
