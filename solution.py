MIN_ALLOWED_RANGE_LENGTH = 2

def validate_list_of(arr, type):
    if not isinstance(arr, list):
        raise Exception("No list instance provided")
    for elem in arr:
        if not isinstance(elem, type):
            raise Exception("No list instance provided") 

def solution(arr):
    validate_list_of(arr, int)
    formatted = ''
    if not arr:
        return formatted
    
    index = 0
    length = len(arr)
    while(index < length):
        right = index
        while(right + 1 < length and arr[right + 1] - arr[right] == 1):
            right+=1
        elem = f'{arr[index]}-{arr[right]}' if right - index >= MIN_ALLOWED_RANGE_LENGTH else f'{arr[index]}'
        index = right + 1 if right - index >= MIN_ALLOWED_RANGE_LENGTH else index + 1
        if index < length - 1:
            elem += ','
        formatted += elem
    return formatted

def main():
    ordered_list = [-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]
    if solution(ordered_list) == '-6,-3-1,3-5,7-11,14,15,17-20':
        print("Solved")

    ordered_list = [-3,-2,-1,2,10,15,16,18,19,20]
    if solution(ordered_list) == '-3--1,2,10,15,16,18-20':
        print("Solved")

    ordered_list = [1,2,3,4,5]
    if solution(ordered_list) == '1-5':
        print("Solved")

    ordered_list = []
    if solution(ordered_list) == '':
        print("Solved")

    try:
        ordered_list = [1, 0.0, "122"]
        solution(ordered_list)
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
