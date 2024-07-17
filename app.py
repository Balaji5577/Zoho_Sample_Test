import streamlit as st

def cred_entered():
    if st.session_state["user"].strip() == "admin" and st.session_state["passwd"].strip() == "admin1234":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("please enter password")
        elif not st.session_state["user"]:
            st.warning("please enter user name")
        else:
            st.error("Invalid username or password")
     

def authenticated_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="username",value="",key="user",on_change=cred_entered)
        st.text_input(label="password",value="",key="passwd",type="password",on_change=cred_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="username",value="",key="user",on_change=cred_entered)
            st.text_input(label="password",value="",key="passwd",type="password",on_change=cred_entered)
            return False

if authenticated_user():
    st.set_page_config(page_title="Zoho Sample Test",page_icon="📁")
    st.title(":red[Web Page of Zoho]")
    st.write("Welcome to the Web Page of Zoho")
    st.button("Logout")
