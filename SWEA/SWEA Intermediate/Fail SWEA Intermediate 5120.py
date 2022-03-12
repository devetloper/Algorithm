n, m, k = map(int,input().split())
num_arr = list(map(int,input().split()))

def make_pw(arr, step, cnt, idx):
    if cnt == 0:
        return arr
    else:
        if idx + step <= len(arr):
            arr.insert(idx + step, arr[idx+2] + arr[idx+3])
            idx = idx + step
            cnt -= 1

        else:
            idx = idx % len(arr)
            arr.insert(idx, arr[idx -1] + arr[idx])
            cnt -= 1
        return make_pw(arr,step,cnt,idx)

print(make_pw(num_arr, m, k, 0))