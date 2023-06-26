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
drop var40 var41 /*������ ���� ���� */
drop var28 var29 /*������ ���� */
drop var4 var5 var9 var10 /*���� �� 0��*/
**
reshape long var, i(year local sig_cd sig_eng_nm sig_kor_nm) j(imsi)
**
gen cat=""
replace cat="���պ�ä��Ȳ(A+B+C+D)(�鸸��)" if imsi==1
replace cat="��ġ��ü��ä(A)(�鸸��)" if imsi==2
replace cat="������������ä(B)(�鸸��)" if imsi==3
replace cat="����������ä(C)(�鸸��)" if imsi==4
replace cat="��(��)�ΰŷ�(D)(�鸸��)" if imsi==5
replace cat="�����ڻ���Ȳ(A+B+C+D)(�鸸��)" if imsi==6
replace cat="��ġ��ü�ڻ�(A)(�鸸��)" if imsi==7
replace cat="�����������ڻ�(B)(�鸸��)" if imsi==8
replace cat="���������ڻ�(C)(�鸸��)" if imsi==9
replace cat="��(��)�ΰŷ�(D)(�鸸��)" if imsi==10
replace cat="����������������((A-(B+C))/D)*100" if imsi==11
replace cat="���������Ը�(D)(�鸸��)" if imsi==12
replace cat="����(A)(�鸸��)" if imsi==13
replace cat="����(B)(�鸸��)" if imsi==14
replace cat="������(C)(�鸸��)" if imsi==15
replace cat="�Ѱ� ������(A+B+C)(�鸸��)" if imsi==16
replace cat="�Ϲ�ȸ�� ������(A)(�鸸��)" if imsi==17
replace cat="�����Ư��ȸ�� ������(B)(�鸸��)" if imsi==18
replace cat="��ŸƯ��ȸ�� ������(C)(�鸸��)" if imsi==19
replace cat="��å�������((A+B)/C)" if imsi==20
replace cat="��ü�������(A/C)" if imsi==21
replace cat="�����������(B/C)" if imsi==22
replace cat="��ü���(A)(�鸸��)" if imsi==23
replace cat="�������(B)(�鸸��)" if imsi==24
replace cat="�Ϲ�ȸ�迹��(C)(�鸸��)" if imsi==25
replace cat="�ֹ�1�δ� ���漼�δ��(õ��)" if imsi==26
replace cat="���漼��(�鸸��)" if imsi==27
*replace cat="���GRDP(�õ�)(�鸸��)" if imsi==28
*replace cat="����GRDP(�õ�)(�鸸��)" if imsi==29
replace cat="�Ϲ�ȸ�����Ϲݰ��������������(A��C��100)(%)" if imsi==30
replace cat="�Ϲݰ��������о߿����(A)(�鸸��)" if imsi==31
replace cat="��ü�����(C)(�鸸��)" if imsi==32
replace cat="�Ϲ�ȸ���߻�ȸ�����������{(D+E)��C��100}(%)" if imsi==33
replace cat="��ȸ�����о߿����(D)(�鸸��)" if imsi==34
replace cat="���Ǻо߿����(E)(�鸸��)" if imsi==35
replace cat="�����ڸ���(%)" if imsi==36
replace cat="�������ֵ�(%)" if imsi==37
replace cat="����α�����(%)" if imsi==38
replace cat="�α�(��)" if imsi==39
*replace cat="����" if imsi==40
*replace cat="���漱�� ȸ��" if imsi==41
replace cat="�缱��" if imsi==42
replace cat="�缱�� ����" if imsi==43
replace cat="�缱�� ��ǥ��" if imsi==44
replace cat="������" if imsi==45
replace cat="������ ����" if imsi==46
replace cat="������ ��ǥ��" if imsi==47
drop imsi sig_eng_nm
rename sig_kor_nm SIG_KOR_NM
rename sig_cd SIG_CD
replace var="" if var=="-"
outsheet using "muni_230624_final.csv", comma names replace
**







