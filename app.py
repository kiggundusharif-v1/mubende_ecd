import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Mubende ECD Dashboard", layout="wide")
st.title("Mubende ECD Monitoring Dashboard")
st.caption("Interactive dashboard based on the Mubende ECD Termly Monitoring Report.")

# -----------------------------
# SOURCE NOTE
# -----------------------------
st.info(
    "This dashboard is based on the PDF monitoring report for Mubende District: "
    "430 submissions, 21 sub-counties/divisions, and 99 parishes."
)

# -----------------------------
# EXECUTIVE SUMMARY DATA
# -----------------------------
summary = {
    "Monitoring submissions": 430,
    "Unique centre names": 416,
    "Sub-counties/divisions": 21,
    "Parishes/wards": 99,
    "Enrollment": 36729,
    "Boys": 18010,
    "Girls": 18719,
    "Attendance": 28949,
    "Attendance rate": 0.788,
    "Caregivers": 1116,
    "Female caregivers": 1011,
    "Male caregivers": 105,
    "Learners per caregiver": 32.9,
    "Licensed centres": 115,
    "Registered centres": 45,
    "Not licensed centres": 270,
    "CMC centres": 222,
    "Hot meal centres": 360,
    "Attached to primary": 414,
    "Local language": 401,
    "Pay caregiver salaries": 413,
    "Zero attendance centres": 48,
}

# -----------------------------
# PAGE 4: CLASS TABLE
# -----------------------------
class_df = pd.DataFrame({
    "Class": ["Baby", "Middle", "Top", "Day care"],
    "Enrolled": [16665, 5335, 14494, 235],
    "Attending": [13207, 4125, 11582, 35],
    "Attendance Rate": [0.792, 0.773, 0.799, 0.149]
})

# -----------------------------
# PAGE 5 + 8: INCLUSION / SUBCOUNTIES
# -----------------------------
inclusion_df = pd.DataFrame({
    "Indicator": ["Orphans", "SNE learners", "Refugee learners"],
    "Count": [1302, 119, 2]
})

subcounty_df = pd.DataFrame({
    "Sub-county/Division": [
        "KIGANDO", "SOUTHERN DIVISION", "KITENGA", "KASAMBYA TOWN COUNCIL",
        "BUTOLOOGO", "EASTERN DIVISION", "WESTERN DIVISION",
        "KIYUNI", "KASAMBYA", "NABINGOOLA"
    ],
    "Centres": [47, 42, 37, 30, 30, 29, 28, 27, 24, 24],
    "Enrolled": [3959, 3137, 2644, 2935, 2745, 2410, 2180, 2411, 1919, 2046],
    "Attendance %": [32.6, 64.4, 91.1, 95.0, 90.6, 55.8, 87.1, 95.5, 99.9, 96.9],
    "Licensed/registered %": [38.3, 35.7, 67.6, 43.3, 26.7, 75.9, 39.3, 33.3, 0.0, 12.5],
    "Learners per caregiver": [32.5, 30.8, 35.7, 33.0, 34.3, 25.1, 29.9, 41.6, 32.0, 33.0]
})

# -----------------------------
# PAGE 3: LICENSING / FOUNDERS
# -----------------------------
licensing_df = pd.DataFrame({
    "Status": ["Not Licensed", "Licensed", "Registered"],
    "Centres": [270, 115, 45]
})

founder_df = pd.DataFrame({
    "Founder category": [
        "Entrepreneurs (Business people)",
        "COU / Protestant / Anglican",
        "Catholic",
        "Community",
        "Islamic",
        "SDA"
    ],
    "Centres": [303, 38, 33, 27, 16, 8]
})

profile_df = pd.DataFrame({
    "Indicator": [
        "Attached/affiliated to primary school",
        "Teach in local languages",
        "Provide hot midday meals",
        "Pay caregiver salaries"
    ],
    "Centres": [414, 401, 360, 413],
    "Percent": [0.963, 0.933, 0.837, 0.960]
})

# -----------------------------
# PAGE 5: CAREGIVER QUALIFICATIONS
# -----------------------------
qualification_df = pd.DataFrame({
    "Qualification / training": [
        "ECE diploma",
        "Nursery teaching certificate",
        "Bachelor or above",
        "Primary diploma (Grade V)",
        "Grade III teacher",
        "SNE trained teacher",
        "Other trainings"
    ],
    "Count": [20, 524, 0, 1, 12, 1, 33]
})

caregiver_sex_df = pd.DataFrame({
    "Sex": ["Female", "Male"],
    "Caregivers": [1011, 105]
})

# -----------------------------
# PAGE 6: WASH / ENVIRONMENT / SERVICES
# -----------------------------
water_source_df = pd.DataFrame({
    "Water source": [
        "Public borehole",
        "Piped water into the ECCE Centre",
        "Borehole in yard/plot",
        "Unprotected well/spring",
        "Public taps",
        "Protected well/spring",
        "Rain water",
        "Tanker Truck/Water Bowser"
    ],
    "Centres": [142, 107, 56, 39, 21, 20, 19, 13]
})

learning_space_df = pd.DataFrame({
    "Learning space": [
        "Permanent classrooms",
        "Temporary classrooms",
        "Under tree shade",
        "Open space"
    ],
    "Centres": [253, 174, 16, 12],
    "Percent": [0.588, 0.405, 0.037, 0.028]
})

water_access_df = pd.DataFrame({
    "Water access": [
        "Within ECCE premises",
        "Within 500m",
        "More than 500m"
    ],
    "Centres": [164, 189, 77]
})

environment_df = pd.DataFrame({
    "Feature": [
        "Lightning arrester",
        "Green grass",
        "Tree shades",
        "Flower garden",
        "Intruder-proof fence with gate",
        "Temporary fence"
    ],
    "Centres": [43, 284, 319, 89, 64, 81]
})

child_service_df = pd.DataFrame({
    "Service": ["Measles vaccine", "Rubella vaccine", "Polio vaccine", "Deworming", "Vitamin A"],
    "Centres": [212, 133, 222, 381, 347],
    "Share": [0.493, 0.309, 0.516, 0.886, 0.807]
})

parent_service_df = pd.DataFrame({
    "Service": ["Parenting education", "Community nutrition dialogue", "Child protection", "Birth registration"],
    "Centres": [228, 108, 237, 166],
    "Share": [0.530, 0.251, 0.551, 0.386]
})

# -----------------------------
# PAGE 7: GOVERNANCE / RECORDS
# -----------------------------
records_df = pd.DataFrame({
    "Record": [
        "Attendance register",
        "Assessment register",
        "Timetable",
        "Income & expenditure books",
        "Learning framework",
        "Minute book",
        "Children's personal files",
        "Scheme of work",
        "Lesson plans",
        "Correspondence book",
        "Inventory book",
        "Log book"
    ],
    "Percent": [0.888, 0.814, 0.809, 0.756, 0.653, 0.642, 0.584, 0.553, 0.535, 0.433, 0.274, 0.195]
})

cmc_df = pd.DataFrame({
    "Indicator": ["Centres with CMC", "CMC meetings held", "CMC members reported", "CMC members trained"],
    "Value": [222, 342, 1927, 1010]
})

# -----------------------------
# KPI ROW
# -----------------------------
k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("Centres", f"{summary['Monitoring submissions']:,}")
k2.metric("Enrollment", f"{summary['Enrollment']:,}")
k3.metric("Attendance", f"{summary['Attendance']:,}")
k4.metric("Attendance Rate", f"{summary['Attendance rate']:.1%}")
k5.metric("Caregivers", f"{summary['Caregivers']:,}")
k6.metric("Licensed %", f"{summary['Licensed centres'] / summary['Monitoring submissions']:.1%}")

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Executive Summary",
    "Enrollment & Attendance",
    "Centre Profile & Compliance",
    "Caregivers",
    "Infrastructure, WASH & Services",
    "Governance & Records"
])

with tab1:
    c1, c2 = st.columns(2)

    executive_df = pd.DataFrame({
        "Indicator": [
            "Attached to primary",
            "Local language",
            "Hot meals",
            "Pay caregiver salaries",
            "CMC availability"
        ],
        "Percent": [
            summary["Attached to primary"] / summary["Monitoring submissions"],
            summary["Local language"] / summary["Monitoring submissions"],
            summary["Hot meal centres"] / summary["Monitoring submissions"],
            summary["Pay caregiver salaries"] / summary["Monitoring submissions"],
            summary["CMC centres"] / summary["Monitoring submissions"],
        ]
    })

    fig = px.bar(executive_df, x="Indicator", y="Percent", text="Percent", title="Key Coverage Indicators")
    fig.update_yaxes(tickformat=".0%")
    fig.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    c1.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(licensing_df, x="Status", y="Centres", text="Centres", title="Licensing Status")
    fig2.update_traces(textposition="outside")
    c2.plotly_chart(fig2, use_container_width=True)

    st.subheader("Coverage and data quality")
    dq_df = pd.DataFrame({
        "Metric": [
            "Monitoring submissions",
            "Unique centre names",
            "Sub-counties/divisions",
            "Parishes/wards",
            "Zero-attendance centres"
        ],
        "Value": [430, 416, 21, 99, 48]
    })
    st.dataframe(dq_df, use_container_width=True)

with tab2:
    c1, c2 = st.columns(2)

    class_long = class_df.melt(id_vars="Class", value_vars=["Enrolled", "Attending"], var_name="Measure", value_name="Learners")
    fig = px.bar(class_long, x="Class", y="Learners", color="Measure", barmode="group", text="Learners",
                 title="Enrollment and Attendance by Class")
    fig.update_traces(textposition="outside")
    c1.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(class_df, x="Class", y="Attendance Rate", text="Attendance Rate", title="Attendance Rate by Class")
    fig2.update_yaxes(tickformat=".0%")
    fig2.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    c2.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)

    sex_df = pd.DataFrame({
        "Sex": ["Girls", "Boys"],
        "Learners": [summary["Girls"], summary["Boys"]]
    })
    fig3 = px.pie(sex_df, names="Sex", values="Learners", title="Enrollment by Sex")
    fig3.update_traces(textinfo="percent+label")
    c3.plotly_chart(fig3, use_container_width=True)

    fig4 = px.bar(inclusion_df, x="Indicator", y="Count", text="Count", title="Inclusion Indicators")
    fig4.update_traces(textposition="outside")
    c4.plotly_chart(fig4, use_container_width=True)

    st.subheader("Largest sub-counties/divisions")
    fig5 = px.bar(
        subcounty_df.sort_values("Attendance %"),
        x="Attendance %",
        y="Sub-county/Division",
        orientation="h",
        text="Attendance %",
        title="Attendance Rate in the 10 Largest Sub-counties/Divisions"
    )
    fig5.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
    st.plotly_chart(fig5, use_container_width=True)

    st.dataframe(subcounty_df, use_container_width=True)

with tab3:
    c1, c2 = st.columns(2)

    fig = px.bar(founder_df, x="Founder category", y="Centres", text="Centres", title="Founder Category")
    fig.update_traces(textposition="outside")
    c1.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(profile_df, x="Indicator", y="Percent", text="Percent", title="Centre Profile Indicators")
    fig2.update_yaxes(tickformat=".0%")
    fig2.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    c2.plotly_chart(fig2, use_container_width=True)

with tab4:
    c1, c2 = st.columns(2)

    fig = px.pie(caregiver_sex_df, names="Sex", values="Caregivers", title="Caregivers by Sex")
    fig.update_traces(textinfo="percent+label")
    c1.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(qualification_df, x="Qualification / training", y="Count", text="Count",
                  title="Caregiver Qualifications / Training")
    fig2.update_traces(textposition="outside")
    c2.plotly_chart(fig2, use_container_width=True)

    st.metric("Learners per caregiver", summary["Learners per caregiver"])

with tab5:
    c1, c2 = st.columns(2)

    fig = px.bar(water_source_df, x="Water source", y="Centres", text="Centres", title="Main Drinking Water Source")
    fig.update_traces(textposition="outside")
    c1.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(learning_space_df, x="Learning space", y="Centres", text="Centres", title="Learning Spaces")
    fig2.update_traces(textposition="outside")
    c2.plotly_chart(fig2, use_container_width=True)

    c3, c4 = st.columns(2)

    fig3 = px.bar(water_access_df, x="Water access", y="Centres", text="Centres", title="Water Access Distance")
    fig3.update_traces(textposition="outside")
    c3.plotly_chart(fig3, use_container_width=True)

    fig4 = px.bar(environment_df, x="Feature", y="Centres", text="Centres", title="Environment / Safety Features")
    fig4.update_traces(textposition="outside")
    c4.plotly_chart(fig4, use_container_width=True)

    st.subheader("Integrated child services")
    c5, c6 = st.columns(2)

    fig5 = px.bar(child_service_df, x="Service", y="Share", text="Share", title="Child Services")
    fig5.update_yaxes(tickformat=".0%")
    fig5.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    c5.plotly_chart(fig5, use_container_width=True)

    fig6 = px.bar(parent_service_df, x="Service", y="Share", text="Share", title="Parent / Community Services")
    fig6.update_yaxes(tickformat=".0%")
    fig6.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    c6.plotly_chart(fig6, use_container_width=True)

with tab6:
    c1, c2 = st.columns(2)

    fig = px.bar(records_df.sort_values("Percent"), x="Percent", y="Record", orientation="h", text="Percent",
                 title="Availability of Management and Teaching Records")
    fig.update_xaxes(tickformat=".0%")
    fig.update_traces(texttemplate="%{text:.1%}", textposition="outside")
    c1.plotly_chart(fig, use_container_width=True)

    fig2 = px.bar(cmc_df, x="Indicator", y="Value", text="Value", title="CMC Metrics")
    fig2.update_traces(textposition="outside")
    c2.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.caption("Source: Mubende ECD Termly Monitoring Report.")
