# 累積和
#サイズNの配列Aに対して，N＋1の配列Sのこと
# S[0] = A[0]
# S[1] = A[0]+A[1]...
# 具体的な数値を当てはめると　
# A = [1,3,5,4,7]の時，S = [0,1,4,9,13,20]となる

# A =[]
# S = [0] * (N+1)
# for i in range(N):
#     S[i+1] = S[i] + A[i]

#for文使うと，順番に足していくので，O(N)の計算量．だけど，O(1)で求められる
# S[r]-S[l]でいけちゃう

#区間クエリだと，O(N)で累積話まとめて，O(Q)を足せばいける

###問題文ABC122C###
##区間を求めるものは累積和だと効率が良い
###例えば,s =[TTACTTACTT] a= [0001000100] 
###例外があるl=3,r=9の時，CTTACTで１個なんだけど，aでみると100010で２個になる
###なので，[l+1:r]の相和が答えである

N,Q = map(int,input().split())
S = input()

#総和を求める
cs = [0] *(N+1)
for i in range(1,N):
    cs[i+1] = cs[i] + (S[i-1:i+1] == "AC")

#各クエリに答える
for q in range(Q):
    l,r = map(int,input().split())

    # 添え字を0始まりとする
    l -= 1

    print(cs[r] - cs[l + 1])



