
import pandas as pd
import altair as alt
import json
###
import streamlit as st
from  PIL import Image
import numpy as np

# Name in the sidebar
st.set_page_config(page_title = '열린지방')
###################
def sidebar_bg():
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url("https://cdn.pixabay.com/photo/2013/09/26/00/21/swan-186551_1280.jpg")
               }}
      </style>
      """,
      unsafe_allow_html=True,
      )
sidebar_bg()
###############################################
###############################################
# NAVIGATION BAR 
#https://discuss.streamlit.io/t/the-navigation-bar-im-trying-to-add-to-my-streamlit-app-is-blurred/24104/3
# First clean up the bar 
st.markdown(
"""
<style>
header[data-testid="stHeader"] {
    background: none;
}
</style>
""",
    unsafe_allow_html=True,
)
# Then put the followings (Data Prof: https://www.youtube.com/watch?v=hoPvOIJvrb8)
# Background color에 붉은빛이 약간 들어간 #ffeded
# https://color-hex.org/color/ffeded
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #F8F8F8;">
  <a class="navbar-brand" href="https://digitalgovlab.com" target="_blank">Digital Governance Lab</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
    </ul>
  </div>
</nav>
<style>
    .navbar-brand{
    color: #89949F !important;
     }
    .nav-link disabled{
    color: #89949F !important;
     }
    .nav-link{
    color: #89949F !important;
     }
</style>
""", unsafe_allow_html=True)
##############################################################
#--- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
#########################################################################
# LOGO
#https://pmbaumgartner.github.io/streamlitopedia/sizing-and-images.html
image = Image.open('marketsentiment_v1.jpg')
st.image(image, caption='')
########################
st.markdown(""" <style> .font2 {
     font-size:30px ; font-family: 'Cooper Black'; color: #000000;} 
     </style> """, unsafe_allow_html=True)
#st.markdown('<p class="font2">InnoCase AI</p>', unsafe_allow_html=True) 
#st.markdown(""" <style> .font3 {
#     font-size:20px ; font-family: 'Cooper Black'; color: #000000;} 
#     </style> """, unsafe_allow_html=True)
#st.markdown("""
#열린지방에 대한 설명  \
#AI의 감성 이해 능력에 대한 연구목적으로 만들어졌으며, 현재는 미국의 7대 첨단기업 관련 주요 뉴스에 대한 분석만 실시하고 있습니다.
#""")
##########################################
#st.markdown("---")
metro_data = pd.read_csv("./data/metro_230624_final.csv", encoding='euc-kr')
govnames = metro_data.sort_values("CTP_KOR_NM").CTP_KOR_NM.unique().tolist()
varnames = metro_data.sort_values("cat").cat.unique().tolist()
years = metro_data.sort_values("year").year.unique().tolist()
##
with open('./data/TL_SCCO_CTPRVN.json', 'r', encoding="UTF-8") as f:
    geojson_lsoa = json.load(f)
geodata_lsoa = alt.Data(values=geojson_lsoa, format=alt.DataFormat(property="features", type="json"))
##
#tickers = pd.read_csv('data/nasdaq-listed.csv')
#indicators = tickers.sort_values("tickers").tickers.unique().tolist()
#st.markdown("광역자치단체(특별시/광역시/도)와 기초자치단체(시/군/구) 중 택일하세요.")
#level = st.selectbox(label="XX", label_visibility="collapsed", 
#                      options = ["광역자치단체(특별시/광역시/도)", "기초자치단체(시/군/구)"], index = 0)
#####
st.markdown("원하시는 분석을 선택하세요 (시계열과 횡단면 분석 중 택일)")
type = st.radio(label="XX", label_visibility="collapsed", 
                  options = ('연도별 변화 추세 분석', '특정 연도를 선택하여 지자체간 비교분석'), horizontal=True)
#####
st.markdown("---")
if type == '연도별 변화 추세 분석':    
    #Two Dropdowns (https://discuss.streamlit.io/t/filter-dataframe-by-selections-made-in-select-box/6627/14)
    col1, col2 = st.columns([6, 4])
    with col1:
        st.markdown("지역 선택 (복수선택 가능)")
        var7 = st.multiselect(label="XX", label_visibility="collapsed", options = govnames, 
                                 default = ['강원도', '경기도'], key = "1")
    with col2:
        st.markdown("변수 선택")
        choice2 = st.selectbox(label="XX", label_visibility="collapsed", options = varnames, key = "2")
    
    import warnings
    warnings.filterwarnings('ignore')
    st.markdown("##")
    #st.markdown(f"선택하신 {var7}는 굵은 색으로 표시되어 있습니다")
    #metro_data = metro_data[metro_data.CTP_KOR_NM.isin([var7])]
    df32 = metro_data[metro_data.cat.isin([choice2])]

    df32["country2"] = df32["CTP_KOR_NM"].apply(lambda x: x if x in var7 else '나머지 지역') #country2 만들기     
    #df32= df32.sort_values(by=['CTP_KOR_NM', 'year'])
    df32 = df32.replace(0, np.nan)                   # 가장 최근연도 데이타가 0으로 되어 있으면 그래프가 이상함

    import plotly.express as px
    from itertools import cycle
    palette = cycle(px.colors.qualitative.Bold)
    colorcode = []                              # 이 4줄은 map(countrycode)를 만들기 위함 
    for j in range(len(var7)):                  # 이 4줄은 map(countrycode)를 만들기 위함
        colorcode.append(j+1)                   # 이 4줄은 map(countrycode)를 만들기 위함
    countrycode = dict(zip(var7, colorcode))    # 이 4줄은 map(countrycode)를 만들기 위함

    sorted_df32 = df32.copy()                                                               # sort the dataframe
    sorted_df32["order"] = sorted_df32["CTP_KOR_NM"].map(countrycode).fillna(len(var7)+1)  # map the value order. var2가 아니면 len(var2)+1
    sorted_df32.sort_values(by=["order", "year"], ascending=False, inplace=True)           # sort by this order

    fig34 = px.line(sorted_df32, x="year", y="var", color="country2", width=550, height=420)                         # sorted된 데이터로 그래프 그리기
    fig34.update_layout(
        xaxis=dict(
            showline=True, showgrid=False, showticklabels=True,
            linecolor='rgb(0, 0, 0)',
            #linecolor='rgb(169, 169, 169)',
            linewidth=1.5,
            ticks='inside',
            tickfont=dict(
               family='Arial',
               size=14,
               color='black'  # Black color for x-axis labels
           ),
           ),
        yaxis=dict(
            showgrid=False, zeroline=False, showline=True, showticklabels=True,
            linecolor='rgb(0, 0, 0)',  # Black color for y-axis
            #linecolor='rgb(169, 169, 169)',
            linewidth=1,
            tickfont=dict(
               family='Arial',
               size=14,
               color='black'
           ),
           ),
        autosize=False,
        margin=dict(
            autoexpand=True,
            l=0, r=65, t=0,               # t가 위쪽 여백. l은 왼쪽 여백.
        ),
        legend_title="",
        showlegend=True,  # Set to True to show the legend
        #showlegend=False, 
        legend=dict(yanchor="top", traceorder="reversed", y=0.99, xanchor="left", x=1.1,),
        font=dict(family="Arial", size=14, color='black',),
        plot_bgcolor='white'
        )
    fig34.update_traces(patch={"line":{"color":"rgb(220,220,220)", "width":0.9}})
    for i in var7:
        fig34.update_traces(patch={"line":{"color": next(palette), "width":3.6}}, selector={"legendgroup":i})
    #col1, col2, col3 = st.columns([1, 5, 1])
    #with col2:
    st.plotly_chart(fig34)
##########################
else:
    #Two Dropdowns (https://discuss.streamlit.io/t/filter-dataframe-by-selections-made-in-select-box/6627/14)
    col3, col4 = st.columns([6, 4])
    with col3:
        st.markdown("년도 선택")
        choice3 = st.slider(label="XX", label_visibility="collapsed", min_value=2015, max_value=2020, value=2019, step=1, key = '3')
    with col4:
        st.markdown("변수 선택")
        choice4 = st.selectbox(label="XX", label_visibility="collapsed", options = varnames, key = "4")

    ##########################################
    #https://github.com/raqoon886/Local_HangJeongDong/blob/master/hangjeongdong_%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C.geojson
    #https://neurowhai.tistory.com/350
    #https://mapshaper.org/ #옵션란에 "'encoding=euc-kr'"
    #https://velog.io/@kjyeon1101/Django-%EC%A7%80%EB%8F%84-%EC%9C%84%EC%97%90-%EC%9A%B0%EB%A6%AC%EB%82%98%EB%9D%BC-%ED%96%89%EC%A0%95%EA%B5%AC%EC%97%AD-%EA%B2%BD%EA%B3%84-%EA%B7%B8%EB%A6%AC%EA%B8%B0
    st.markdown("##")
    st.markdown("관심있는 지역을 클릭하세요 (Shift 키를 누른 채 복수선택 가능; 지도 밖 클릭하면 전체 선택)")
    metro_data = metro_data[metro_data.year.isin([choice3])]
    metro_data = metro_data[metro_data.cat.isin([choice4])]
    lsoas_to_plot = list(metro_data.CTP_KOR_NM)

    def convert_string(s):
        try:
            return float(s.replace(',', ''))
        except ValueError:
            return s
    metro_data['var'] = metro_data['var'].apply(convert_string)

    #변수명 변경
    #color_lsoa = alt.Color("var:O", scale = alt.Scale(scheme="yellowgreenblue"), title="IDACI", legend = alt.Legend(orient="top"))
    color_lsoa = alt.Color("var:O", scale = alt.Scale(scheme="viridis"), title="IDACI", legend = None)
    choro_lsoa = alt.Chart(geodata_lsoa).mark_geoshape(
        stroke="black"
        ).transform_lookup(
            lookup="properties.CTP_KOR_NM",
            from_=alt.LookupData(metro_data,
            "CTP_KOR_NM",
            ["CTP_KOR_NM", "var"])
            ).transform_filter(
                alt.FieldOneOfPredicate(
                    field="properties.CTP_KOR_NM", oneOf=lsoas_to_plot
                    )).encode(color=color_lsoa,tooltip=[alt.Tooltip("CTP_KOR_NM:N", title="LSOA"), alt.Tooltip("var:O", title="IDACI")]).project(type="identity", reflectY=True).properties(width=500,height=500)

    choro_lsoa = choro_lsoa.configure_legend(
        labelLimit = 0,
        titleLimit = 0,
        titleFontSize = 13,
        labelFontSize = 13,
        symbolStrokeWidth = 1.5,
        symbolSize=150
        ).configure_view(
            strokeWidth = 0
            ).configure_axis(
                        labelLimit=0,
                        titleLimit=0)

    lsoa_select = alt.selection_point(fields=["CTP_KOR_NM"])
    lsoa_select_empty = alt.selection_point(fields=["CTP_KOR_NM"], empty = True)
    color_lsoa = alt.condition(lsoa_select, alt.Color("var:O", scale = alt.Scale(scheme="yellowgreenblue"), title="IDACI", legend = None), alt.value("lightgray"))

    choro_lsoa = (alt.Chart(geodata_lsoa).mark_geoshape(
        stroke="black"
        ).transform_lookup(
            lookup="properties.CTP_KOR_NM",
            from_=alt.LookupData(
                metro_data,
                "CTP_KOR_NM",
                ["CTP_KOR_NM", "var"]
                )).transform_filter(alt.FieldOneOfPredicate(field="properties.CTP_KOR_NM", oneOf=lsoas_to_plot)
                ).encode(
                    color=color_lsoa,
                    tooltip=[alt.Tooltip("CTP_KOR_NM:N", title="지역명"), alt.Tooltip("var:O", title=f"{choice4}")]).add_params(lsoa_select, lsoa_select_empty).project(type="identity", reflectY=True).properties(width=500,height=500))

    bar_chart = (alt.Chart(metro_data).mark_bar(color="#1f77b4").encode(
        x=alt.X("var:Q",
            title=f"{choice4}",
            axis=alt.Axis(tickMinStep=1, labelColor='black', titleColor='black')), # Modify color here
        y=alt.Y("CTP_KOR_NM:N", title="지역명", axis=alt.Axis(labelColor='black', titleColor='black')) # And here
        ).transform_filter(lsoa_select_empty).properties(width=400, height=500))
    
    #bar_charts_combined = bar_chart_york_average + bar_chart
    combined_charts = alt.vconcat(choro_lsoa, bar_chart, center=True).configure_legend(labelLimit=0,titleLimit=0,titleFontSize=13,labelFontSize=13,symbolStrokeWidth=1.5,symbolSize=150).configure_view(strokeWidth=0).configure_axis(labelLimit=0,titleLimit=0)
    ##
    #combined_charts.save("York_IDACI_map_and_bar_chart.html")
    st.altair_chart(combined_charts, use_container_width=True)
    ##

               
