📌 Netflix
-   
- 추천시스템을 활용한 Netflix 클론 코딩

📌 Introduction
-    
- 프로젝트명: Netflix
- 기간: 2022.06.02 ~ 2022.06.14
- 핵심역할: 데이터 크롤링(dump data), 협업 필터링, 로그인, 회원가입, 검색기능
   
📌 핵심기능   
-   
### 1. 로그인/회원가입
> - 유효성 검사, 아이디 중복 검사 
### 2. 메인 페이지   
> - 유저 기반 협업필터링을 적용한 영화 추천   
> - 영화제목, 배우를 키워드로한 검색 기능   
### 3. 디테일 페이지   
> - 컨텐츠 기반 필터링을 적용한 영화 추천 
> - 줄거리, 장르를 벡터화 시킴  

📌 핵심 트러블 슈팅   
-   
### 1) 크롤링한 데이터 Dmup 하기  
> - 에러: 크롤링한 데이터를 DB에 Dump하는 과정에서 에러 발생
> - 원인: Data insert 하기 전에 전처리를 하지 않았다.
> - 해결: Data 전처리하여 Json형식으로 변환
> - [코드 참조](https://github.com/joohuun/Petrasche_back/blob/dfa374231cd39c9b53954e713b7d809d011a83aa/nginx/default.conf#L11)
### 2) 쿼리 최적화 진행   
> - 문제점: DB가 쌓이다 보니 서버가 느려지는 현상 발생
> - 원인: 불필요한 쿼리를 많이 날림
> - 해결: 쿼리디버거를 작성하여 모든 API에 적용시켜보며 전, 후를 비교해 보았다. prefetch_related, select_related를 사용하여 미리 입력된 캐시를 읽어와 불필요한 쿼리를 줄였다.
> - [블로그 참조](https://1q2w3ee.tistory.com/50)   

📌 피그마
-

- 회원가입/로그인
- ![img_5.png](/static/img_5.png) ![img_6.png](/static/img_6.png)


- 메인페이지 / 디테일 모달
![img_7.png](/static/img_7.png)
![img_8.png](/static/img_8.png)

- 애견월드컵 뽐뽐뽐
![img_9.png](/static/img_9.png)

- 산책매칭 / 디테일 모달
![img_10.png](/static/img_10.png)
![img_11.png](/static/img_11.png)

- 실시간 채팅 
![img_12.png](/static/img_12.png)

- 마이페이지
![img_13.png](/static/img_13.png)
