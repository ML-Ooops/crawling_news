# crawling_news
new crawling, store in the NOSQL(mongoDB)

## 예시 출력 형식
'''json
  {
    "source": {
      "id": null,
      "name": "Tom's Hardware UK"
    },
    "author": "Anton Shilov",
    "title": "China plans state ownership for all of its rare earth metal resources — regulation comes into effect on Oct 1",
    "description": "New regulation in China prohibits any organization or individual from encroaching upon or destroying rare-earth resources.",
    "url": "https://www.tomshardware.com/tech-industry/china-plans-state-ownership-for-all-of-its-rare-earth-metal-resources-regulation-comes-into-effect-on-oct-1",
    "urlToImage": "https://cdn.mos.cms.futurecdn.net/qmLD6J8LgbFgNwEKpFUcmn-1200-80.jpg",
    "publishedAt": "2024-07-01T11:04:09Z",
    "content": "China has enacted a new regulation, effective October 1, asserting state ownership over its rare-earth materials required in semiconductor production, reports Nikkei. This move aims to secure nationa… [+2756 chars]"
  }
'''

뉴스 api
외국에 다양한 뉴스에 대해서 가져올 수 있다. 기존 문제인 키워드 검색 부분을 일차적으로 해결 
장점 : 
    무료
    빠른 성능


단점 : 
    언어 번역이 필요함

## remaining task
1. 일정시간마다 자동으로 api가 실행되어 정보를 수집
2. 수집된 정보 DB에 일괄적으로 업데이트
3. 업데이트 된 DB의 정보 카테고리화

