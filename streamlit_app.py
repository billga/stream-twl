import streamlit as st
import twl
import random

st.title("Eldrow!")

words = [*twl.iterator()]
word5 = [w for w in words if len(w)==5]
# st.write(random.choice(word5))
bee = st.text_input(":bee:", help="center letter first, 7 letters total")

if len(bee)==7:
    candidates = sorted((w for w in words if set(w).issubset(bee) and bee[0] in w), key=len, reverse=True)
    pangrams = [w for w in candidates if set(bee).issubset(w)]
    st.badge(f"{len(candidates)} / {len(pangrams)}", color="blue")
    # st.markdown(pangrams)
    for w in candidates:
        st.write(f"{w+' <-:100:' if set(bee).issubset(w) else w}")
        