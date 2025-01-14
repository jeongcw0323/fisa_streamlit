import streamlit as st

# text를 입력하는 검색창 만들기
# anylist에 있는 글자가 일부라도 들어가면
# imglist에 있는 사진이 검색되되록 검색창을 만들기
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

ani_input= st.text_input("검색하실 애니메이션을 입력하세요")

dict={}
for i in range(len(ani_list)):
    dict[ani_list[i]] = img_list[i]

for ani in ani_list:
    if ani_input in ani:
        st.image(dict[ani], width=1000)