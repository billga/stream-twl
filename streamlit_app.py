import streamlit as st
import twl
from itertools import tee

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

# st.title(":bee: :email:")
st.title(":email:")

words = [*twl.iterator()]
word5 = [w for w in words if len(w)==5]
# st.write(random.choice(word5))
# bee = st.text_input(":bee:", help="center letter first, 7 letters total").strip().lower()
lb = st.text_input(":email:", help="12 letters total").strip().lower()

# if len(bee):
#     if len(bee)==7:
#         candidates = sorted((w for w in words if set(w).issubset(bee) and bee[0] in w), key=len, reverse=True)
#         pangrams = [w for w in candidates if set(bee).issubset(w)]
#         st.badge(f"{len(candidates)} / {len(pangrams)}", color="blue")
#         # st.markdown(pangrams)
#         for w in candidates:
#             st.write(f"{w+' <-:100:' if set(bee).issubset(w) else w}")
#     else:
#         if len(bee)>7:
#             "too many"
#         else:
#             "too few"
if len(lb):
    if len(lb)==12:
        # st.write(f"{lb} - pick starting letter")
        # start = st.pills("pick", [i for i in lb], selection_mode='single')
        cset = [lb[:3], lb[3:6], lb[6:9], lb[9:]]
        # start = st.pills("pill", cset, selection_mode='single')
        subset = sorted([w for w in words if
                    all([len(w) > 3,
                         set(w).issubset(lb)] + [not set(p).issubset(g) for p in pairwise(w) for g in cset])],
                   key=len, reverse=True)
        pangrams = [w for w in subset if set(w) == set(lb)]
        if len(pangrams) > 0:
            f"Pangram from word:{lb}={pangrams}"
        gamut = {w: {'next': [k for k in subset if k != w and k[0] == w[-1]],
                 'score': len(set(w)),
                 'needs': set(lb) - set(w)} for w in subset}
        
        for word, item in gamut.items():
            chk = len(item['needs'])
            for w in item['next']:
                if len(item['needs'].difference(w)) == 0:
                    st.markdown(f"{word} -> {w}")
    else:
        if len(lb)>12:
            "too many"
        else:
            "too few"
