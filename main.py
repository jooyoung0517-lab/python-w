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

# 퀴즈 실행 부분
quizzes = [Quiz(q["question"], q["choices"], q["answer"]) for q in questions_data]

score = 0
print("--- 퀴즈 게임을 시작합니다! ---")

for i, quiz in enumerate(quizzes, 1):
    quiz.display(i)
    try:
        # 사용자에게 번호 입력 받기
        user_choice = int(input("정답 번호를 입력하세요: "))
        
        if quiz.check_answer(user_choice):
            print("정답입니다! 🎉")
            score += 1
        else:
            print(f"틀렸습니다. 정답은 {quiz.answer}번입니다. 😢")
    except ValueError:
        print("숫자만 입력해주세요! 이번 문제는 기회를 잃었습니다.")

# 최종 결과 출력
print(f"\n게임 종료! 당신의 점수는 {len(quizzes)}점 만점에 {score}점입니다.")
sys.exit()


