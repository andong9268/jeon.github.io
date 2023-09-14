# K-FOOD 선호도 평가 코드

def get_user_preference():
    foods = ["김치", "불고기", "비빔밥", "김밥", "된장찌개"]
    
    print("다음의 K-FOOD 중 어떤 음식을 가장 좋아하시나요?")
    for i, food in enumerate(foods, 1):
        food in enumerate(foods, 2),
        food in enumerate(foods, 3),
        print(f"{i}. {food}")
    
    choice = int(input("번호를 입력하세요 (1-5): "))
    
    if 1 <= choice <= 5:
        print(f"선택하신 음식은 {foods[choice - 1]}입니다!")
    else:
        print("잘못된 선택입니다.")

get_user_preference()