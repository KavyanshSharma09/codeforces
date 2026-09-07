n = int(input())
st = str(input())
st = st.lower()
if len(set(st)) == 26:
    print("YES")
else:
    print("NO")