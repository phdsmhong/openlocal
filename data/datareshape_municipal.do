clear 
clear matrix
set more off
set mem 500m
cd "C:\Users\phdsm\0. openlocal\data"
**
insheet using "muni_230624_stata.csv", comma names clear
replace var44=0 if var44==.
replace var47=0 if var47==.
tostring var44 var47, replace force
**
drop var40 var41 /*지역간 편차 없음 */
drop var28 var29 /*데이터 없음 */
drop var4 var5 var9 var10 /*거의 다 0임*/
**
reshape long var, i(year local sig_cd sig_eng_nm sig_kor_nm) j(imsi)
**
gen cat=""
replace cat="통합부채현황(A+B+C+D)(백만원)" if imsi==1
replace cat="자치단체부채(A)(백만원)" if imsi==2
replace cat="지방공공기관부채(B)(백만원)" if imsi==3
replace cat="교육재정부채(C)(백만원)" if imsi==4
replace cat="내(외)부거래(D)(백만원)" if imsi==5
replace cat="통합자산현황(A+B+C+D)(백만원)" if imsi==6
replace cat="자치단체자산(A)(백만원)" if imsi==7
replace cat="지방공공기관자산(B)(백만원)" if imsi==8
replace cat="교육재정자산(C)(백만원)" if imsi==9
replace cat="내(외)부거래(D)(백만원)" if imsi==10
replace cat="통합재정수지비율((A-(B+C))/D)*100" if imsi==11
replace cat="통합재정규모(D)(백만원)" if imsi==12
replace cat="세입(A)(백만원)" if imsi==13
replace cat="지출(B)(백만원)" if imsi==14
replace cat="순융자(C)(백만원)" if imsi==15
replace cat="총계 세출결산(A+B+C)(백만원)" if imsi==16
replace cat="일반회계 세출결산(A)(백만원)" if imsi==17
replace cat="공기업특별회계 세출결산(B)(백만원)" if imsi==18
replace cat="기타특별회계 세출결산(C)(백만원)" if imsi==19
replace cat="정책사업비중((A+B)/C)" if imsi==20
replace cat="자체사업비중(A/C)" if imsi==21
replace cat="보조사업비중(B/C)" if imsi==22
replace cat="자체사업(A)(백만원)" if imsi==23
replace cat="보조사업(B)(백만원)" if imsi==24
replace cat="일반회계예산(C)(백만원)" if imsi==25
replace cat="주민1인당 지방세부담액(천원)" if imsi==26
replace cat="지방세액(백만원)" if imsi==27
*replace cat="명목GRDP(시도)(백만원)" if imsi==28
*replace cat="실질GRDP(시도)(백만원)" if imsi==29
replace cat="일반회계중일반공공행정예산비중(A÷C×100)(%)" if imsi==30
replace cat="일반공공행정분야예산액(A)(백만원)" if imsi==31
replace cat="전체예산액(C)(백만원)" if imsi==32
replace cat="일반회계중사회복지예산비중{(D+E)÷C×100}(%)" if imsi==33
replace cat="사회복지분야예산액(D)(백만원)" if imsi==34
replace cat="보건분야예산액(E)(백만원)" if imsi==35
replace cat="재정자립도(%)" if imsi==36
replace cat="재정자주도(%)" if imsi==37
replace cat="고령인구비율(%)" if imsi==38
replace cat="인구(명)" if imsi==39
*replace cat="여당" if imsi==40
*replace cat="지방선거 회차" if imsi==41
replace cat="당선자" if imsi==42
replace cat="당선자 정당" if imsi==43
replace cat="당선자 득표율" if imsi==44
replace cat="차선자" if imsi==45
replace cat="차선자 정당" if imsi==46
replace cat="차선자 득표율" if imsi==47
drop imsi sig_eng_nm
rename sig_kor_nm SIG_KOR_NM
rename sig_cd SIG_CD
replace var="" if var=="-"
outsheet using "muni_230624_final.csv", comma names replace
**







