import cv2


ABboxLocation1 = []
ABboxLocation2 = []
LocationGroup = []
BenchmarkGroup = []
result_file = 'C:/Users/mcdull/Desktop/Basketball/Basketball.txt'
benchmark_file = 'C:/Users/mcdull/Desktop/Basketball/groundtruth_rect.txt'

for line in open(result_file):           # preprocess the txt in order to fix four elements per row
    s = line.split(',')                  # without any other comma
    # s[3].rstrip('\n')
    for i in range(4):
        ABboxLocation1.append(float(s[i]))
    LocationGroup.append(ABboxLocation1)
    ABboxLocation1 = []

for line in open(benchmark_file):           # preprocess the txt in order to fix four elements per row
    s = line.split(',')                  # without any other comma
    # s[3].rstrip('\n')
    for i in range(4):
        ABboxLocation2.append(float(s[i]))
    BenchmarkGroup.append(ABboxLocation2)
    ABboxLocation2 = []

# print(group[0])
for j in range(725):
    k = str(j+1)
    ProcessingImageNum = k.zfill(4)
    Img = cv2.imread("C:\\Users\\mcdull\\Desktop\\Basketball\\img\\" + ProcessingImageNum + '.jpg')
    x11 = int(LocationGroup[j][0])
    y11 = int(LocationGroup[j][1])
    x12 = int(LocationGroup[j][0] + LocationGroup[j][2])
    y12 = int(LocationGroup[j][1] + LocationGroup[j][3])
    x21 = int(BenchmarkGroup[j][0])
    y21 = int(BenchmarkGroup[j][1])
    x22 = int(BenchmarkGroup[j][0] + BenchmarkGroup[j][2])
    y22 = int(BenchmarkGroup[j][1] + BenchmarkGroup[j][3])
    cv2.rectangle(Img, (x11, y11), (x12, y12), (255, 0, 0), 2)
    cv2.rectangle(Img, (x21, y21), (x22, y22), (0, 255, 0), 2)
    cv2.imwrite("C:\\Users\\mcdull\\Desktop\\Basketball\\result\\" + ProcessingImageNum + '.jpg', Img, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    print(j)