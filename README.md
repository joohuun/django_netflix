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
> - 유저 기반 협업필터링을 적용한 영화 추천 [[코드참조]](https://github.com/joohuun/django_netflix/blob/ad72b5da58e9cb07b6ec93a3b4834758d1b8556e/movie/collab_recommender.py#L1)   
> - 영화제목, 배우를 키워드로한 검색 기능   
### 3. 디테일 페이지   
> - 컨텐츠 기반 필터링을 적용한 영화 추천 [[코드참조]](https://github.com/joohuun/django_netflix/blob/main/movie/recommender_ml.py)   
> - 줄거리, 장르를 벡터화 시킴  
> - 댓글, 평점, 좋아요

📌 핵심 트러블 슈팅   
-   
### 1) 크롤링한 데이터 Dmup 하기  
> - 에러: 크롤링한 데이터를 DB에 Dump하는 과정에서 에러 발생
> - 원인: Data insert 하기 전에 전처리를 하지 않았다.
> - 해결: Data 전처리하여 Json형식으로 변환
> - [코드 참조](https://github.com/joohuun/django_netflix/blob/caf1a1a16c722bb532e27a1729735e628db4138c/data_insert/movie_insert.py#L1)


