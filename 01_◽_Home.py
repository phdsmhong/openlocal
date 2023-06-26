import streamlit as st
from  PIL import Image

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
image = Image.open('openlocal_logo.jpg')
st.image(image, caption='')
########################
#st.markdown(""" <style> .font2 {
#     font-size:30px ; font-family: 'Cooper Black'; color: #000000;} 
#     </style> """, unsafe_allow_html=True)
#st.markdown(""" <style> .font3 {
#     font-size:20px ; font-family: 'Cooper Black'; color: #13265C;} 
#     </style> """, unsafe_allow_html=True)
#st.markdown("##")
#st.markdown('<p class="font3">About us</p>', unsafe_allow_html=True)  
#st.markdown('<p class="font2">소개</p>', unsafe_allow_html=True) 
#st.markdown(""" <style> .font3 {
#     font-size:20px ; font-family: 'Cooper Black'; color: #000000;} 
#     </style> """, unsafe_allow_html=True)
st.markdown("""
열린지방에 오신 것을 환영합니다. \
본 플랫폼에서는 여러 웹사이트에 산재된 지역정보를 수집하여 제공하고 있습니다. \
2023년 7월에 공개된 본 플랫폼은 현재 베타버젼으로 프로그램 작동 과정에서 오류가 발생할 수 있으며 \
향후 적절한 시기에 수정할 예정입니다. 

데이터는 광역과 기초지자체 수준에서 따로 수집되었으며, 좌측 Side bar에서 메뉴를 선택하실 수 있습니다. \
모바일로 접속하신 방문자께서는 좌측 상단 화살표(<) 모양을 클릭하시기 바랍니다.

기초(시군구) 단위의 분석을 위한 프로그램 구동에는 상당한 시간이 시간이 소요됩니다. \
메뉴를 선택하신 후 약 30초 간 대기하시면 분석결과를 보실 수 있습니다.

관련 문의사항은 digitalgovlab@gmail.com으로 연락주시기 바랍니다.
""")
##
