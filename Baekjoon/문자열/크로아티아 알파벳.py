st = input()
cnt = 0
alpha = ["c=", "c-", "d-", "lj", "nj", "s=", "dz=", "z="]
for i in range(len(alpha)):
    st = st.replace(alpha[i], "@")
print(len(st))
    