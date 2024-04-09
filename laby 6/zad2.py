import cv2
image = cv2.imread('obraz.jpg')




naive_gray = image.copy()
row, col = naive_gray.shape[:2]
for i in range(row):
    for j in range(col):
        naive_gray[i, j] = sum(naive_gray[i, j]) / 3
cv2.imshow('image-naive', naive_gray)

better_gray = image.copy()
row, col = better_gray.shape[:2]
for i in range(row):
    for j in range(col):
        better_gray[i, j] = 0.299 * better_gray[i, j][0] + 0.587 * better_gray[i, j][1] + 0.114 * better_gray[i, j][2]
cv2.imshow('image-better', better_gray)
cv2.waitKey(0)