import streamlit as st
import video_text

if 'count' not in st.session_state: 
	st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化

if 'video_count' not in st.session_state: 
	st.session_state.video_count = 0 #countがsession_stateに追加されていない場合，0で初期化

def create_text(video_count, i):
    st.header("提示方法")
    video = video_text.video_list[video_count]
    text = video_text.text_list[video][i]
    if len(text) > 20 :
        text_list = [text[x:x+20] for x in range(0, len(text), 20)]
        for t in text_list:
            st.markdown(t)

tab1, tab2 = st.tabs(["video", "questions"])

next_video = st.button("次のビデオ")
if next_video:
    st.session_state.video_count += 1
    st.session_state.count = 0 #countがsession_stateに追加されていない場合，0で初期化

col1, col2 = st.columns(2)
back, next = st.columns(2)


with tab1 :
    with col1:
        st.header("video")
        video_file = open('videos/' + video_text.video_list[st.session_state.video_count], 'rb')
        video_bytes = video_file.read()

        st.video(video_bytes)

    with col2:
        create_text(st.session_state.video_count, st.session_state.count)
        with back:
            back = st.button("戻る")
            if back:
                st.session_state.count -= 1
        with next:
            next = st.button("次へ")
            if next:
                st.session_state.count += 1


with tab2:
    st.header("評価")
    st.text_input("入力")
    hyouka = st.radio(
    "評価は妥当でしたか",
    ('ハイ', 'いいえ', 'どちらでもない'))


