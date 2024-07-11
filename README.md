# SSAFY 스타트캠프
## git에 대해서 알아보자
### git의 역할
  * 코드의 버전(히스토리)를 관리
  * **분산버전관리시스템**
  *  **git** : local repository 로컬저장소
  * **github** : remote repository 원격저장소
### 기본개념
1. git (로컬저장소-업로드/다운로드) ——-github, gitlab( 원격저장소)
2. **Interface**(2종류) 
   1. GUI-graphic user interface  리모컨  
   2. TUI- text user interface : window GUI
    / CLI- command line interface : cmd → 윈도우 기반, powershell, bash→리눅스 기반

3. **IDE** : 통합 개발 환경 
   * **VScode** - IDE가 아님. but IDE처럼 사용 가능 → 텍스트 에디터(그렇지만 익스텐션을 이용하여 IDE처럼 사용 가능)
     * C# :  Visual studio
     * python: PyCharm, 쥬피터노트북
     * Java: IntelliJ
4. **URL**: “https://” 로 시작하는 웹주소
5. **API**: Application programming interface 도구
     * 클라이언트가 서버에게 요청하는 규칙
     * ex: 프론트 코드만 짜도 , 백엔드 GPT 서버를 사용할 수 있음.
## git 시작하기
  | git config --global [user.name](http://user.name/) 다희 |  |
| --- | --- |
| git config --global user.email [dlaekgml222@naver.com](mailto:dlaekgml222@naver.com) |  |
| git init | 컴퓨터에 git 생성 |
| git add .      (업데이트할때) | 모든 파일 add / .은 전체파일 이라는 뜻(띄어쓰기) |
| git status | commit 할 준비가 되어있나 확인 |
| git commit -m “first\_practice”      (업데이트할때) | 뒤에는 커밋 메세지 |
| git log | commit된 지 확인하기 |
| git remote add origin + 깃헙url | 로컬 저장소에서 원격 저장소의 주소를 추가하겠다   origin 은 원격 저장소의 별칭    |
| git remote -v | 잘 되었는 지 확인가능 / "verbose” |
| git push origin +master      (업데이트할때) | origin(전에 사용했던 별칭으로 작성)   +는 강제로 push 하겠다는 의미    |
| touch .gitignore | add하지 않을 파일명을 작성한다   (예 api key, 가상환경 등..)    |
| HOME |  |
| git clone + 깃헙url   git log (확인하기)    | git←-clone—github : 만약 새로운 환경에서 github에 있는 프로젝트를 받을 때   (집에서 프로젝트를 다시 처음 시작할 때)    |
| git pull origin +master | git←-pull—github: 이미 로컬에서 작업 중이고, 원격 저장소에 업데이트가 있는 경우 |

*gitignore 설정사이트(프레임워크 등)*
https://www.toptal.com/developers/gitignore/

## git 종료
  1. 숨긴항목 .git삭제하기
  2. rm -rg .git
## 프로그램 만드는 방법
   1. 처음부터 코딩
   2. 소스코드를 다운받아서 수정하는 방법 ⇒ **프레임워크Framework** : 이미 짜여진 소스코드
        * python : Django/ Flask
        * Java: Spring Boot/ Spring MVC(아시아권, 특히 한국에서 많이 씀)
        * C#: ASP NET Core(주로 미국에서 쓴다)
        * Javascript: Express(미국에서 엄청 많이 쓴다) 
        * nodeJs는 런타임
  ### 런타임
    * Javascript 만든 게임 App 런타임: Node.js
    * Python으로 만든 App 런타임: CPython / Pypy
      (CPython에서 속도를 올린 런타임)
    * Java로 만든 게임 App 런타임: JVM (Java virtual Machine)
    * C++, C로 만든 App 런타임 존재X
# MARK DOWN
  1. README.md 파일 만들기
  2. extension - mark down all in one 다운
  3. 공식문서 참고 https://www.markdownguide.org/basic-syntax/
  * github에 README.md(프로젝트의 설명 글) 파일로 활용 →자동으로 github에 올라옴→프로젝트에 대한 설명을 문서화→가독성,편의성 