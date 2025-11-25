import folium
from folium.features import DivIcon

# --- SETUP ---
m = folium.Map(location=[37.0902, -95.7129], zoom_start=4, tiles='CartoDB positron')

# --- ADD TITLE & INSTRUCTIONS (Floating Overlay) ---
title_html = '''
     <div style="
         position: fixed; 
         top: 20px; left: 60px; width: 320px; 
         z-index: 9999; font-family: 'Segoe UI', Arial, sans-serif;
         ">
       <div style="
           background-color: white; 
           opacity: 0.95; 
           padding: 15px 20px; 
           border-radius: 8px; 
           box-shadow: 0 4px 15px rgba(0,0,0,0.15);
           border-left: 5px solid #0056b3;
       ">
         <h2 style="margin: 0; color: #333; font-size: 20px; font-weight: 700;">iRx Marketing Expansion</h2>
         <p style="margin: 8px 0 0; font-size: 13px; color: #555; line-height: 1.4;">
            <i class="fa fa-info-circle" aria-hidden="true" style="color: #0056b3;"></i> 
            &nbsp;<b>Instruction:</b> Click a colored pin on the map to view detailed market research, statistics, and pilot targets.
         </p>
       </div>
     </div>
'''
m.get_root().html.add_child(folium.Element(title_html))

# ==============================================================================
# PROFILE 1: Community Mental Health Centers (CMHCs)
# Locations: Chicago, Cleveland
# ==============================================================================

# 1. Cook County (Chicago)
cook_html = """
<div style="font-family: Arial; width: 340px; padding: 5px;">
    <h4 style="margin: 0; color: #1E90FF; border-bottom: 2px solid #1E90FF; padding-bottom: 5px;">Cook County, IL</h4>
    <div style="font-size: 11px; font-weight: bold; color: #1E90FF; margin-top: 4px;">PROFILE: Community Mental Health (CMHC)</div>
    <ul style="padding-left: 20px; font-size: 13px; line-height: 1.4; margin-top: 10px;">
        <li style="margin-bottom: 8px;">High concentration of Medicaid-funded CMHCs and large hospital systems creating volume efficiency.</li>
        <li style="margin-bottom: 8px;"><strong>1.2 Million residents</strong> (23% of county) needed behavioral health services in 2023.</li>
        <li style="margin-bottom: 8px;">Heavy prevalence of mental health and SUD diagnoses necessitates automated monitoring.</li>
        <li>Strong alignment for "enforcement" use cases driven by readmission penalty avoidance.</li>
    </ul>
</div>
"""

# 2. Cuyahoga County (Cleveland)
cuyahoga_html = """
<div style="font-family: Arial; width: 340px; padding: 5px;">
    <h4 style="margin: 0; color: #00008B; border-bottom: 2px solid #00008B; padding-bottom: 5px;">Cuyahoga County, OH</h4>
    <div style="font-size: 11px; font-weight: bold; color: #00008B; margin-top: 4px;">PROFILE: Community Mental Health (SUD Focus)</div>
    <ul style="padding-left: 20px; font-size: 13px; line-height: 1.4; margin-top: 10px;">
        <li style="margin-bottom: 8px;">Consistently ranks among the highest national overdose rates (<strong>78% involving Fentanyl</strong>).</li>
        <li style="margin-bottom: 8px;">Established behavioral health networks (MetroHealth, Cleveland Clinic) provide immediate pilot pathways.</li>
        <li>Existing iRx collaborator presence streamlines entry for SUD adherence pilots.</li>
    </ul>
</div>
"""


# ==============================================================================
# PROFILE 2: Hospital Transitional-Care Programs (HTPs)
# Locations: Phoenix, Miami, Los Angeles
# ==============================================================================

# 3. Maricopa County (Phoenix)
maricopa_html = """
<div style="font-family: Arial; width: 340px; padding: 5px;">
    <h4 style="margin: 0; color: #DC143C; border-bottom: 2px solid #DC143C; padding-bottom: 5px;">Maricopa County, AZ (Phoenix)</h4>
    <div style="font-size: 11px; font-weight: bold; color: #DC143C; margin-top: 4px;">PROFILE: Hospital Transitional-Care (HTP)</div>
    <ul style="padding-left: 20px; font-size: 13px; line-height: 1.4; margin-top: 10px;">
        <li style="margin-bottom: 8px;">One of the fastest-growing senior populations in the U.S.</li>
        <li style="margin-bottom: 8px;">High Medicare Advantage penetration (<strong>56% vs 54% nat'l avg</strong>) → hospitals strongly incentivized to improve adherence.</li>
        <li>Major health systems (Banner, Mayo, Dignity) actively running transitional-care and home-health pilots.</li>
    </ul>
</div>
"""

# 4. Miami-Dade & Broward (Florida)
miami_html = """
<div style="font-family: Arial; width: 340px; padding: 5px;">
    <h4 style="margin: 0; color: #20B2AA; border-bottom: 2px solid #20B2AA; padding-bottom: 5px;">Miami-Dade & Broward, FL</h4>
    <div style="font-size: 11px; font-weight: bold; color: #20B2AA; margin-top: 4px;">PROFILE: Hospital Transitional-Care (HTP)</div>
    <ul style="padding-left: 20px; font-size: 13px; line-height: 1.4; margin-top: 10px;">
        <li style="margin-bottom: 8px;">Florida has one of the oldest populations nationally (<strong>21%+ over age 65</strong>).</li>
        <li style="margin-bottom: 8px;">High chronic disease burden (hypertension, diabetes, CHF) → medication-heavy regimens.</li>
        <li>Strong telehealth adoption → aligns well with iRx’s app-centered workflow.</li>
    </ul>
</div>
"""

# 5. Los Angeles County (California)
la_html = """
<div style="font-family: Arial; width: 340px; padding: 5px;">
    <h4 style="margin: 0; color: #800080; border-bottom: 2px solid #800080; padding-bottom: 5px;">Los Angeles County, CA</h4>
    <div style="font-size: 11px; font-weight: bold; color: #800080; margin-top: 4px;">PROFILE: Hospital Transitional-Care (HTP)</div>
    <ul style="padding-left: 20px; font-size: 13px; line-height: 1.4; margin-top: 10px;">
        <li style="margin-bottom: 8px;">Largest county in the U.S. with highly complex care needs (<strong>1.7M safety-net patients</strong>).</li>
        <li style="margin-bottom: 8px;">Significant older adult population + major public hospital networks (LAC-USC, Kaiser, UCLA).</li>
        <li>California’s innovation-friendly digital health ecosystem ideal for pilot adoption.</li>
    </ul>
</div>
"""

# --- PIN LOGIC ---
locations = [
    # PROFILE 1: CMHCs (Blue Tones)
    {"coords": [41.8781, -87.6298], "label": "Chicago", "color": "#1E90FF", "popup": cook_html, "offset": "-240px", "align": "right"},
    {"coords": [41.4993, -81.6944], "label": "Cleveland", "color": "#00008B", "popup": cuyahoga_html, "offset": "50px", "align": "left"},
    
    # PROFILE 2: HTPs (Distinct Colors: Red, Teal, Purple)
    {"coords": [33.4484, -112.0740], "label": "Phoenix", "color": "#DC143C", "popup": maricopa_html, "offset": "-240px", "align": "right"},
    {"coords": [25.7617, -80.1918], "label": "Miami", "color": "#20B2AA", "popup": miami_html, "offset": "50px", "align": "left"},
    {"coords": [34.0522, -118.2437], "label": "Los Angeles", "color": "#800080", "popup": la_html, "offset": "50px", "align": "left"},
]

for loc in locations:
    folium.Marker(
        location=loc["coords"],
        popup=folium.Popup(loc["popup"], max_width=360),
        icon=DivIcon(
            icon_size=(0,0), icon_anchor=(0, 0),
            html=f"""
                <div style="position: relative;">
                    <i class="fa fa-map-marker" style="
                        position: absolute; left: -30px; top: -60px; 
                        color:{loc['color']}; font-size: 60px; 
                        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                    </i>
                    <div style="
                        position: absolute; top: -55px; left: {loc['offset']}; 
                        width: 220px; text-align: {loc['align']};">
                        <span style="
                            font-family: Arial; font-weight: 900; color: white; 
                            background-color: {loc['color']}; padding: 6px 12px; 
                            border-radius: 6px; box-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                            {loc['label']}
                        </span>
                    </div>
                </div>
            """
        )
    ).add_to(m)

m.save("index.html")
print("Map created successfully: index.html")
