
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
          background: url("https://cdn.pixabay.com/photo/2017/06/14/08/20/map-of-the-world-2401458_1280.jpg")
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
image = Image.open('openlocal_muni_logo.jpg')
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
#Altair has a default limit of 5000 rows for a dataset. You can increase this limit
alt.data_transformers.disable_max_rows()
muni_data = pd.read_csv("./data/muni_230624_final.csv", encoding='euc-kr')
govnames = muni_data.sort_values("SIG_KOR_NM").SIG_KOR_NM.unique().tolist()
varnames = muni_data.sort_values("cat").cat.unique().tolist()
years = muni_data.sort_values("year").year.unique().tolist()
##
with open('./data/TL_SCCO_SIG.json', 'r', encoding="UTF-8") as f:
    geojson_lsoa = json.load(f)
geodata_lsoa = alt.Data(values=geojson_lsoa, format=alt.DataFormat(property="features", type="json"))
##
#tickers = pd.read_csv('data/nasdaq-listed.csv')
#indicators = tickers.sort_values("tickers").tickers.unique().tolist()
#st.markdown("광역자치단체(특별시/광역시/도)와 기초자치단체(시/군/구) 중 택일하세요.")
#level = st.selectbox(label="XX", label_visibility="collapsed", 
#                      options = ["광역자치단체(특별시/광역시/도)", "기초자치단체(시/군/구)"], index = 0)
#####

col1, col2 = st.columns([5, 5])
with col1:
    st.markdown("변수 선택 (3개까지 선택 가능)")
    choice2 = st.multiselect(label="XX", label_visibility="collapsed", default=["고령인구비율(%)"], options = varnames, key = "2")
with col2:
    st.markdown("년도 선택 (시계열 분석을 선택하지 않은 경우)")
    choice3 = st.slider(label="XX", label_visibility="collapsed", min_value=2000, max_value=2022, value=2019, step=1, key = '3')
    
col3, col4 = st.columns([5, 5])
with col3:
    st.markdown("시계열 분석 선택")
    timeseries = st.checkbox(label="연도별 추세분석")
with col4:
    st.markdown("분석 기간 (시계열 분석을 선택한 경우)")
    range = st.slider(label="XX", label_visibility="collapsed", min_value=2000, max_value =2022, value=[2015, 2021])

##########################################
#https://github.com/raqoon886/Local_HangJeongDong/blob/master/hangjeongdong_%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C.geojson
#https://neurowhai.tistory.com/350
#https://mapshaper.org/ #옵션란에 "'encoding=euc-kr'"
#https://velog.io/@kjyeon1101/Django-%EC%A7%80%EB%8F%84-%EC%9C%84%EC%97%90-%EC%9A%B0%EB%A6%AC%EB%82%98%EB%9D%BC-%ED%96%89%EC%A0%95%EA%B5%AC%EC%97%AD-%EA%B2%BD%EA%B3%84-%EA%B7%B8%EB%A6%AC%EA%B8%B0
st.markdown("---")
st.markdown("관심있는 지역을 클릭하세요 (Shift 키를 누른채 복수 선택 가능; 지도 바깥쪽을 클릭하면 전체 선택)")
lsoas_to_plot = list(muni_data.SIG_KOR_NM)

def convert_string(s):
    if isinstance(s, str):
        # perform string conversion logic
        try: 
            return float(s.replace(',', ''))
        except:
            return s
    else:
        # handle non-string values
        return s
#def convert_string(s):
#    try:
#        return float(s.replace(',', ''))
#    except ValueError:
#        return s
muni_data['var'] = muni_data['var'].apply(convert_string)

###############################
## muni_data와 muni_data2 분리 (muni_data2는 횡단면 분석용)
muni_data1 = muni_data[muni_data.cat.isin(choice2)] #시계열분석용
muni_data2 = muni_data[muni_data.year.isin([choice3])]
muni_data3 = muni_data2[muni_data2.cat.isin(choice2)] #횡단면분석용
#muni_data['year'] = muni_data['year'].astype(int)
###############################
#color_lsoa = alt.Color("var:O", scale = alt.Scale(scheme="yellowgreenblue"), title="IDACI", legend = alt.Legend(orient="top"))
zoom = alt.selection_interval(bind='scales', encodings=['x', 'y'])
color_lsoa = alt.Color("var:O", scale = alt.Scale(scheme="viridis"), title="IDACI", legend = None)
choro_lsoa = alt.Chart(geodata_lsoa).mark_geoshape(
    stroke="black"
    ).transform_lookup(
        lookup="properties.SIG_KOR_NM",
        from_=alt.LookupData(muni_data3,
        "SIG_KOR_NM",
        ["SIG_KOR_NM", "var"])
        ).transform_filter(
            alt.FieldOneOfPredicate(
                field="properties.SIG_KOR_NM", oneOf=lsoas_to_plot
                )).encode(color=color_lsoa,tooltip=[alt.Tooltip("SIG_KOR_NM:N", title="LSOA"), alt.Tooltip("var:O", title="IDACI")]).project(type="identity", reflectY=True).properties(width=500,height=500)

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
                    titleLimit=0).add_params(
                    zoom)

lsoa_select = alt.selection_point(fields=["SIG_KOR_NM"])
lsoa_select_empty = alt.selection_point(fields=["SIG_KOR_NM"], empty = True)
color_lsoa = alt.condition(lsoa_select, alt.Color("var:O", scale = alt.Scale(scheme="yellowgreenblue"), title="IDACI", legend = None), alt.value("lightgray"))

choro_lsoa = (alt.Chart(geodata_lsoa).mark_geoshape(
    stroke="black"
    ).transform_lookup(
        lookup="properties.SIG_KOR_NM",
        from_=alt.LookupData(
            muni_data3,
            "SIG_KOR_NM",
            ["SIG_KOR_NM", "var"]
            )).transform_filter(alt.FieldOneOfPredicate(field="properties.SIG_KOR_NM", oneOf=lsoas_to_plot)
            ).encode(
                color=color_lsoa,
                tooltip=[alt.Tooltip("SIG_KOR_NM:N", title="지역명"), alt.Tooltip("var:O", title=f"{choice2[0]}")]).add_params(lsoa_select, lsoa_select_empty).project(type="identity", reflectY=True).properties(width=500,height=500))

if timeseries:
    muni_data4 = muni_data1[(muni_data1['year'] >= range[0]) & (muni_data1['year'] <= range[1])]
    muni_data4 = muni_data4[muni_data4.cat.isin([choice2[0]])]
    #muni_data4.sort_values(by=['SIG_CD', 'year']).reset_index(drop=True)
    base = alt.Chart(muni_data4).encode(
        alt.Color("SIG_KOR_NM").legend(None)
    ).transform_filter(lsoa_select_empty).properties(
        width=500
    )
    line = base.mark_line().encode(
        x=alt.X("year:Q", title="", axis=alt.Axis(format="d")), 
        y=alt.Y("var:Q", scale=alt.Scale(zero=False))  # update this line
    )
    last_price = base.mark_circle().encode(
        alt.X("last_date['year']:T", title=""),
        alt.Y("last_date['var']:Q", title="")
    ).transform_aggregate(
        last_date = 'argmax(year)',
        groupby=["SIG_KOR_NM"]  #이것은 그래프 옆 레이블 
    )
    company_name = last_price.mark_text(align="left", dx=260).encode(text="SIG_KOR_NM")
    #line_chart = (line + last_price + company_name).encode( 
    line_chart = (line + company_name).encode( 
        x=alt.X().title(""), #그래프 위에 타이틀이 생겨서 별로
        y=alt.Y().title(f"{choice2[0]}")
    )
    combined_charts = alt.vconcat(choro_lsoa, line_chart, center=True).configure_legend(labelLimit=0,titleLimit=0,titleFontSize=15,labelFontSize=15,symbolStrokeWidth=1.5,symbolSize=150).configure_view(strokeWidth=0).configure_axis(labelColor='black', titleColor='black', labelLimit=0, titleLimit=0, labelFontSize=15)
    st.markdown("시계열 분석에서는 선택하신 첫 변수에 대한 분석결과만 표시됩니다")
    st.altair_chart(combined_charts, use_container_width=True)
else: 
    muni_data5 = muni_data3 = muni_data3[muni_data3.cat.isin([choice2[0]])]
    bar_chart = (alt.Chart(muni_data5).mark_bar(color="#1f77b4").encode(
        x=alt.X("var:Q",
            title=f"{choice2[0]}",
            axis=alt.Axis(tickMinStep=1, labelColor='black', titleColor='black')), # Modify color here
        y=alt.Y("local:N", title="지역명", axis=alt.Axis(labelColor='black', titleColor='black')) # And here
        ).transform_filter(lsoa_select_empty).properties(width=400, height=1600))
    #bar_charts_combined = bar_chart_york_average + bar_chart
    combined_charts = alt.vconcat(choro_lsoa, bar_chart, center=True).configure_legend(labelLimit=0,titleLimit=0,titleFontSize=13,labelFontSize=13,symbolStrokeWidth=1.5,symbolSize=150).configure_view(strokeWidth=0).configure_axis(labelLimit=0,titleLimit=0).add_params(
                    zoom)
    #combined_charts.save("York_IDACI_map_and_bar_chart.html")
    st.altair_chart(combined_charts, use_container_width=True)
    ##############
    if len(choice2)==2:
        muni_data6 = muni_data2 = muni_data2[muni_data2.cat.isin([choice2[0], choice2[1]])]
        muni_data6 = pd.pivot(muni_data6, index=['year','local','SIG_KOR_NM'], columns='cat', values='var')
        muni_data6.reset_index(inplace=True) 
        scatterplot = alt.Chart(muni_data6).mark_point().encode(
            x=alt.X(f'{choice2[0]}:Q', title=choice2[0], scale=alt.Scale(zero=False), axis=alt.Axis(labelColor='black', titleColor='black')),
            y=alt.Y(f'{choice2[1]}:Q', title=choice2[1], scale=alt.Scale(zero=False), axis=alt.Axis(labelColor='black', titleColor='black'))
        )
        #text = scatterplot.mark_text(
        #    align='left',
        #    baseline='middle',
        #    dx=7,
        #    fontSize=11,
        #    color='black'
        #).encode(
        #    text='SIG_KOR_NM'
        #)
        #scatter = scatterplot + text
        st.markdown("##")
        st.markdown("선택하신 첫 두 변수 간 Scatterplot입니다 (문자변수 포함 시 나타나지 않음)")
        st.altair_chart(scatterplot, use_container_width=True)
        ##
    if len(choice2)>2:
        muni_data6 = muni_data2 = muni_data2[muni_data2.cat.isin([choice2[0], choice2[1], choice2[2]])]
        muni_data6 = pd.pivot(muni_data6, index=['year','local','SIG_KOR_NM'], columns='cat', values='var')
        muni_data6.reset_index(inplace=True) 
        scatterplot = alt.Chart(muni_data6).mark_point().encode(
            x=alt.X(f'{choice2[0]}:Q', title=choice2[0], scale=alt.Scale(zero=False), axis=alt.Axis(labelColor='black', titleColor='black')),
            y=alt.Y(f'{choice2[1]}:Q', title=choice2[1], scale=alt.Scale(zero=False), axis=alt.Axis(labelColor='black', titleColor='black')),
            size = f'{choice2[2]}:Q'
        )
        st.markdown("##")
        st.markdown("첫 두 변수 간 Scatterplot에 data point의 크기로 표현된 세번째 변수를 추가하였습니다 (문자변수 포함 시 나타나지 않음)")
        st.altair_chart(scatterplot, use_container_width=True)
        ## 


               
