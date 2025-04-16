# yoloTrainPC
yoloTrainPC
1. 폴더 만들고 yolo002_train
2. 폴더로 이동 후 code로 열기 
3. 터미널 에서 
4. 가상환경 만들기 
```
conda create -n yolo002 
```
5. shift+ctrl+p  가상환경 연결
6. yolov5 복사 해오기 
```
git clone https://github.com/ultralytics/yolov5
```
   git이 설치 안되어 있으면 설치 해야 한다. 
   https://git-scm.com/downloads
   git이 연결 안되면 VSCODE 껐다 켜야 한다고 지훈이가 얘기 했다. 
7. 터미널에서 requirements.txt 파일로 패키지 인스톨 하기 
```
pip install -r requirements.txt
```   
8. 데이터 세트 저장 폴더 만들기 
```
mkdir pothole
```
9. 다운로드 받은 데이터를 복사 해 넣는다. 또는
```
curl -L "https://public.roboflow.com/ds/AZZeoZCGOT?key=XFPYdCUU9Z"
```
10. data.yaml 파일을 수정한다. 
11. yolov5s.yaml을 custom_yolov5s.yaml로 복사하고 
12. 내용에서 nc를 수정 해준다.
13. 아래 2개의 코드를 makeDataList.py 파일로 만들어 실행 해준다. 
    13.1 dataset의 내용을 train.txt, test.txt, val.txt 파일로 만든다.
```
from glob import glob
train_img_list = glob('./pothole/train/images/*.jpg')
test_img_list = glob('./pothole/test/images/*.jpg')
valid_img_list = glob('./pothole/valid/images/*.jpg')
print(len(train_img_list), len(test_img_list), len(valid_img_list))
'''
    13.2 파일에 저장 
'''
import yaml
with open('./pothole/train.txt','w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('./pothole/test.txt','w') as f:
    f.write('\n'.join(test_img_list) + '\n')
with open('./pothole/val.txt','w') as f:
    f.write('\n'.join(valid_img_list) + '\n')
'''

14. 데이터 세트 준비가 끝났으므로 학습을 시작 할 수 있다. 
15. 학습은 터미널에서 다음과 같이 입력  
```
python train.py --img 640 --batch 32 --epochs 50 --data ./pothole/data.yaml --cfg ./models/custom_yolov5s.yaml --weights '' --name pothole_result --cache
```
