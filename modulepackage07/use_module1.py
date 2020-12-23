#use_module1.py:모듈 module1.py를 import해서 사용하기
#이클립스로 작업시:Project메뉴->Properties->PyDev-PYTHONPATH->Add Source Folder클릭후 현재 패키지 추가
import module1#최초 import시 module1.py가 딱 한번만 실행됨
print('[모듈 불러오기 : import 모듈명(.py를 제외한 파일명)')

import module1#여러 번 import해도 최초 import시에만 실행됨 즉 한번만 import하면 된다
print('[모듈 module1의 이름공간 출력]')
print(dir(module1))
print('[모듈 module1의 변수 PI 사용하기 :모듈며.변수]')
print(module1.PI)

