# 각 숫자를 적절한 위치에 삽입하는 방법
# 삽입 정렬은 '필요할 때만' 위치를 바꿈
# 실제로는 버블정렬과 선택정렬보다 더 빠르다
# 시간복잡도는 위 두개와 같지만 특정 상황에서 더 빠르기도 하고 더 좋다

# 이미 앞부분이 정렬이 되어있다고 가정
# 1은 건너뜀
# 10은 1앞과 1뒤 중에서 적절한 위치에 들어감
# 5는 _ 1 _ 10 _ 세 칸 중에서 적절한 위치에 들어감
# 8은 5와 10 사이에 들어감
# ...

# 중간에 낑겨넣는거는 이동이 연쇄적으로 일어나지 않나?
# --> 하나씩 앞으로 내려가면서 현재 원소가 더 작다면 바꿔줌

# 멈출 포인트를 알고 있기 때문에 앞의 두 정렬보다 더 효율적이다.

def main():
    array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    for i in range(len(array)-1):
        j = i
        while(array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
        print(array)

if __name__ == "__main__":
    main()

# CODE!!!
# '거의 정렬된' 상태라면 굉장히 효율적이다. 그냥 탐색도 안함. 
# 앞부분은 이미 정렬되어있다고 가정하기 때문에.
# '거의 정렬된' 상태에 한해서는 어떤 알고리즘보다 효율적.

# 일반적인 경우에서 O(n^2)