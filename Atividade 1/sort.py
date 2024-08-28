import re
# # a = [20,37,6,4,56,7,1,10]


# # for j in range(len(a)):
# #     for i in range(j+1,len(a)):
# #         if a[i] < a[j]:
# #             a[j],a[i] = a[i],a[j]

# # print(a)

# # a = []

# # if a:
# #     print('o array não está vazio')
# # else:
# #     print('o array está vazio')

# a = ['alves', 'jesus', 'luana', 'silva', 'silva', 'silva']

# # def removeRepeatedWords(arr):
# #     i=0
# #     while i < len(arr):
# #         # print(arr[i])
# #         for j in range(i+1,len(arr)):
# #             print(f'{i} e {j}')
# #             if arr[i] == arr[j]:
# #                 print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
# #         i+=1

# # def removeRepeatedWords(arr):
# #     i=0
# #     length = len(arr)
# #     while i <= length:
# #         print(f'{length} e {i+1}')
# #         for j in range(i+1,length):
# #             if arr[i] == arr[j]:
# #                 print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
# #                 length-=1
# #                 # arr.pop(j)
# #         i+=1
        
# #             # if arr[i] == arr[j]:
# #             #     print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
# #             #     arr.pop(j)

# # def removeRepeatedWords(arr):
# #     for i in range(len(arr)):
# #         for j in range(i+1,len(arr)):
# #             if arr[i] == arr[j]:
# #                 print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
# #                 arr.pop(j)
# #                 break
# #     return arr
    
# # def removeRepeatedWords(arr):
    
#     # for i in range(len(arr)):
#     #     for j in range(i-1,len(arr)):
#     #         indexArr = []
#     #         if arr[i] == arr[j]:
#     #             print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
#     #             indexArr.append(j)
#     #         if indexArr:
#     #             for y in indexArr:
#     #                 arr.pop(y)
#     # return arr

# # def removeRepeatedWords(arr):
# #     for i in range(len(arr)):
# #         j = -1
# #         while j > -len(arr):
# #             if arr[i] == arr[j]:
# #                 print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
# #                 arr.pop(j)
# #             i-=1
# #     return arr        
    
# def removeRepeatedWords(arr):
#     print(arr)
#     for i in range(len(arr)):
#         indexArr = []
#         for j in range(i+1,len(arr)):
#             if arr[i] == arr[j]:
#                 # print(f'{arr[i]} ind {i} = {arr[j]} ind {j}')
#                 indexArr.insert(0,j)
#         for b in indexArr:
#             arr.pop(b)
#     # print(arr)        
#     return arr

# a = 'uma frase com , . ! ? e outros sinais como , . ! ? () 876 9785 45687'



# print(re.findall(r'[\\d,.?!()0-9]', a))

# print(removeRepeatedWords(a))

def soma(a,b): return a+b

print(soma(1,3))


