import sys

class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index):
        print(f"\nQ{index}. {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}) {choice}")

    def check_answer(self, user_input):
        return self.answer == user_input

questions_data = [
    {"question": "대한민국의 수도는 어디인가요?", "choices": ["부산", "서울", "인천", "대구"], "answer": 2},
    {"question": "사과를 영어로 무엇이라고 하나요?", "choices": ["Banana", "Grape", "Apple", "Orange"], "answer": 3},
    {"question": "1 + 1은 무엇인가요?", "choices": ["1", "2", "3", "4"], "answer": 2},
    {"question": "파이썬은 어떤 언어인가요?", "choices": ["프로그래밍 언어", "외국어", "몸짓 언어", "비밀 언어"], "answer": 1},
    {"question": "지구에서 가장 가까운 별은 무엇인가요?",
     "choices": ["달", "금성", "태양", "화성"], "answer": 3}
]

# 퀴즈 객체 생성
quizzes = [
    Quiz(q["question"], q["choices"], q["answer"])
    for q in questions_data
]


# 퀴즈 풀기
def play_quiz():
    score = 0
    print("\n--- 퀴즈 게임을 시작합니다! ---")

    for i, quiz in enumerate(quizzes, 1):
        quiz.display(i)

        while True:
            user_input = input("정답 번호를 입력하세요 (1~4): ").strip()

            if not user_input:
                print("입력값이 비어 있습니다. 다시 입력하세요.")
                continue

            try:
                user_choice = int(user_input)
            except ValueError:
                print("숫자만 입력해주세요.")
                continue

            if not 1 <= user_choice <= 4:
                print("1~4 사이의 숫자를 입력해주세요.")
                continue

            break

        if quiz.check_answer(user_choice):
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {quiz.answer}번입니다.")

    print(f"\n게임 종료! {len(quizzes)}문제 중 {score}문제 정답!")

# 게임 전체를 관리하는 클래스
class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.best_score = None

    def show_quiz_list(self):
        print("\n===== 등록된 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for i, quiz in enumerate(self.quizzes, 1):
            print(f"{i}. {quiz.question}")

    def show_best_score(self):
        print("\n===== 최고 점수 =====")

        if self.best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"최고 점수: {self.best_score}점")
            # QuizGame 객체 생성
game = QuizGame(quizzes)
# 메인 메뉴
def show_menu():
    while True:
        print("\n================================")
        print("       🎯 나만의 퀴즈 게임 🎯")
        print("================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 최고 점수 확인")
        print("5. 종료")
        print("================================")

        choice = input("메뉴를 선택하세요 (1~5): ").strip()

        if choice == "1":
            play_quiz()
        elif choice == "2":
            print("퀴즈 추가 기능은 다음 단계에서 구현합니다.")
        elif choice == "3":
            game.show_quiz_list()
        elif choice == "4":
            game.show_best_score()
        elif choice == "5":
            print("퀴즈 게임을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 1~5 사이의 숫자를 입력하세요.")


# 프로그램 시작
if __name__ == "__main__":
    try:
        show_menu()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")



