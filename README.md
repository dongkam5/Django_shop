# 간단한 쇼핑몰

## 구현 기능
- 상품 목록 표시 O
- 로그인/로그아웃 O  
- 회원별 개인 장바구니 확인/삭제/수정 기능 O
- 주문/ 주문현황확인 기능 --구현중--
- 개인 정보 확인 O
- 회원가입 O
 

## 문제
- buy에 관한 모델 생성

### 해결
- Cart.Stuffs 가 꼭 1개 이상의 필드를 가져야만 하는지? (Add Cart도 개선필요)
--> get 말고, filter를 사용해서 해결

- 장바구니 담을 때 개수 화면 출력
--> Cart에 quantity 필드를 추가하여 해결

- 유저 생성할때 같이 Cart 인스턴스도 생성 
--> Cart.create 함수를 통해 해결, Stuff는 Cart 생성 후 추가하는 방식으로 구현 --> 각 Cart별로 사용자, 물건 명, 개수를 담도록 설정

- 스태틱 폴더 제대로 인식 안됨 (css (body:100%) 랑 이미지)
--> html head에 블록을 생성하고, style.css를 해당 블록에 삽입 하여 구현
--> x축 방향으로 스크롤 생기는 것 : overflow-x: hidden; 을 통해 해결

- 스태틱 폴더 해결되면, models 개선해서 db에 이미지 저장 가능 구현
--> MEDIA 폴더를 통해, db에 이미지 저장 및 로드 기능 구현

- Register에 이미지 로드 기능 추가
--> Form의 Fileinput 기능을 통해 기능 구현

- 상품을 등록하고 나서, 홈 화면에 해당하는 url로 이동하지 않음 (새로고침 시 계속 register 작업 시행)
--> render을 사용하지 않고, redirect를 사용하여 views 에서 순환하게 하여 해결

- 업로드 시간 측정해서 화면에 출력
--> timezone을 이용하여, 마지막 수정시간을 화면에 출력하도록 해결 + timedelta를 이용하여 한국시간으로 설정

- 계정마다 하나의 db를 공유해서, 카트 목록이 같이 공유 됨 --> 사용자 별로 cart에 아이템 별 목록 리스트 생성 (JSONFIELD 이용 하려고 생각중)
--> 각 카트 인스턴스에 모든 물건 목록을 담는것이 아닌, (사용자,물건명,개수)를 담도록 변경

- 위 문제가 해결되면 각 유저별 카트(장바구니)에서 장바구니 목록 삭제
--> objects.delete()를 통해서 목록 삭제 구현

- views의 cart2 addcart2와 templates의 cart2.html 을 수정하여 완성
--> 이용하여 생성하고, 다시 원상태로 복귀 시킴

- 장고 template에서 곱셈 및 나눗셈
--> You can use widthratio builtin filter for multiplication and division.

To compute A*B: {% widthratio A 1 B %}

To compute A/B: {% widthratio A B 1 %}

- 위 문제가 해결되면 각 유저별 카트(장바구니)에서 장바구니 목록 개수 변경이 가능하도록 수정
--> 버튼을 이용하여 장바구니 목록 개수 수정 가능하도록 변경

- 장바구니 글자 세로 가운데 정렬
--> text align, vertical align 이용하여 해결

- 장바구니에서 목록별 체크박스 생성 
--> 체크박스 생성 (default=False)

- 주문 기능 구현 시, 홈 화면에서 buy 버튼 누르면 체크 되어 있게
--> 홈화면에서 buy를 클릭해서 들어가면 checked 되어있도록 설정

- 체크박스 활성/비활성 시, 총액에는 체크 된 상품들의 합만 출력 되도록
--> JS onclick 이벤트 리스너를 이용하여 해결

- 주문 현황 확인 기능
--> checked 된 목록을 info.html에 전달하여 표시

- buy 시 체크박스 체크여부도 전달
--> JS를 통해서 buy 버튼을 누를 시, 체크여부도 전달되도록 구성

- request.POST.get(uCart.stuffs.name)을 이용하면, 값이 없는경우에 오류를 반환하지 않고, None 값을 리턴함

- 버튼 클릭시 화면이 계속 reload 됨
--> JS를 통해 화면을 reload 하지 않고, 값을 변경하도록 수정