# 🎵 DLC_Project
[스파르타코딩클럽 내일배움캠프 AI 3기] A4팀 추천 시스템 프로젝트
## 프로젝트 소개
**DLC_Music**은 음악을 `좋아요` 했을 때, 좋아요 한 음악 리스트를 기반으로
**음악을 추천해주는 서비스** 입니다.
## 개발기간
2022.11.02 ~ 2022.11.08
## front-end github-address
[DLC_front](https://github.com/marinred/DLC_Front)
## 역할 파트
- **front-end** :
  - 임동근(노래 상세 페이지)
  - 염보미(노래 상세 페이지)
  - 이태규(메인 페이지, 리뷰 페이지)
  - 정진엽(리뷰 페이지)
  - 주세민(회원가입, 로그인, 회원 프로필 페이지)
- **back-end** :
  - 임동근(노래 리스트 조회, 노래 상세 페이지)
  - 염보미(노래 리스트 조회, 노래 상세 페이지)
  - 이태규(리뷰 페이지)
  - 정진엽(리뷰 페이지)
  - 주세민(회원가입, 로그인, 회원 프로필 페이지)
- **Machine Learning** :
  - 임동근(노래 추천 시스템)
  - 염보미(노래 추천 시스템)
## 주요 기능
1. 회원 가입 / 로그인
    - 회원 가입
    - 로그인
    - 프로필
    - 회원 정보 수정
2. 노래
    - 노래 목록 조회
        - top100
            - 멜론의 top100 리스트 크롤링
            - 곡명으로 spotipy api로 검색
            - db에 저장
        - my-list
        - recommend-llist
            - my-list에 있는 곡을 기반으로 노래 추천
            - 추천된 노래 db 저장
    - 노래 상세 조회
    - 노래 좋아요
3. 리뷰
    - 리뷰 작성
## 와이어프레임
1. 로그인 / 회원가입 페이지
![signin/signup](https://user-images.githubusercontent.com/113073974/200457719-a666049b-3a68-4d05-a9e7-02ff065d7493.png)
2. 메인 페이지
![main](https://user-images.githubusercontent.com/113073974/200458035-44b80ca1-08a7-4e1c-874e-170121bb93b8.png)
3. 노래 상세 페이지
![image](https://user-images.githubusercontent.com/113073974/200458106-51747628-3f1b-4d6c-91d5-cd15a9964eb9.png)
4. 프로필 상세 페이지


![image](https://user-images.githubusercontent.com/113073974/200458147-74b26a91-c646-443b-9d7a-b14c82bd036d.png)


## ERD 설계
![](https://velog.velcdn.com/images/marinred/post/3c1665f6-fd99-4732-b4e7-cc506e7d446f/image.jpg)
## API 설계
[API 명세서](https://documenter.getpostman.com/view/23810621/2s8Z73xATR)

## ⚠️ 트러블 슈팅

  - music의 review get 도중 이슈
  
  [Wiki로 이동](https://github.com/marinred/DLC_Project/wiki/TroubleShooting)

## 머신러닝 데이터셋
[![Spotify dataset](https://user-images.githubusercontent.com/113073974/200451893-73c26183-c753-444f-bcad-2628a2971d26.png)](https://www.kaggle.com/datasets/vatsalmavani/spotify-dataset)
## 프로젝트 시연영상

![Youtube](https://user-images.githubusercontent.com/113073974/200463994-934e4f53-0c73-47a4-ad76-df55e1c19c55.png)
