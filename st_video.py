import streamlit as st
import video_text
import pandas as pd
# import time
# from PIL import Image
# import image_path
if 'count' not in st.session_state:
    st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化
if 'video_count' not in st.session_state:
    st.session_state.video_count = 0 #countがsession_stateに追加されていない場合，0で初期化
my_bar = st.progress(st.session_state.video_count/15)
if 'question_bool' not in st.session_state:
    st.session_state.question_bool = True #countがsession_stateに追加されていない場合，0で初期化
if 'v_list' not in st.session_state:
    st.session_state.v_list = [] #countがsession_stateに追加されていない場合，0で初期化
def create_text(video_count, i):
    st.header("提示方法")
    video = video_text.video_list[video_count]
    text = video_text.text_list[video][i]
    text_detail = video_text.text_detail[video_count]
    if len(text) > 20 :
        # text_list = [text[x:x+20] for x in range(0, len(text), 20)]
        text_list = text.split("\n")
        text_detail_list = text_detail.split("\n")
        for t in text_list:
            # st.markdowm(t)
            st.write('<font size="5" color="black">' + t + '</font>', unsafe_allow_html=True)
        with st.expander("もっと見る"):
            for t_detail in text_detail_list:
                st.write('<font size="5" color="black">' + t_detail + '</font>', unsafe_allow_html=True)
# tab1, tab2 = st.tabs(["video", "questions"])
col1, col2 = st.columns(2)
back, next = st.columns(2)
# with tab1 :
print(st.session_state.video_count)
video_name = video_text.video_list[st.session_state.video_count]
if st.session_state.question_bool == True:
    with col1:
        st.header("video")
        video_file = open('videos/' + video_name, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        # img = Image.open("images/" + image_path.image_list[video_name])
        # st.image(img, caption='区間')
    with col2:
        with back:
            back = st.button("戻る")
            if back:
                st.session_state.count -= 1
        with next:
            next = st.button("次へ")
            if next:
                st.session_state.count += 1
                print("pushed")
                print(st.session_state.count)
        create_text(st.session_state.video_count, st.session_state.count)
    if st.session_state.count > 2:
        st.session_state.question_bool = False
else:
    st.markdown("妥当性評価　７段階")
    validity = st.slider("１：妥当でない　～　７：妥当である", 1, 7, 4)
    st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化
    check1 = st.checkbox('自分が普段考えていることと一緒だったか')
    check2 = st.checkbox('普段見ないポイントを思い出させてくれる提示だったか')
    if st.session_state.video_count < 15 :     #####################################変える
        next_video = st.button("次のビデオへ")
        if next_video:
            my_bar.progress(st.session_state.video_count/16)
            st.session_state.v_list.append([video_name, validity, check1, check2])
            st.session_state.question_bool = True
            st.session_state.video_count += 1
            print("pushsssss")
    else:
        csv = st.button("終了する")
        if csv :
            st.session_state.v_list.append([video_name, validity])
            q_df = pd.DataFrame(st.session_state.v_list)
            q_df.to_csv("test.csv")
            st.success("終了してください。ありがとうございました。")
            st.stop()
# with tab2:
#     q_list = []
#     st.header("評価")
#     st.text_input("入力")
#     hyouka = st.radio(
#     "評価は妥当でしたか",
#     ('ハイ', 'いいえ', 'どちらでもない'))
#     q_list.append(["評価", hyouka])
#     option = st.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone'))
#     q_list.append(["option", option])
#     st.write('You selected:', option)
#     csv = st.button("csvにする")
#     if csv :
#         q_df = pd.DataFrame(q_list)
#         q_df.to_csv("test.csv", encoding="shift-jis")