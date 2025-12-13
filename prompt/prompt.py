def givemetheprompt(subject, level):
    return f"""당신은 SW 회사의 면접관입니다. 다음 입력을 보고 스택에 관련된 질문 1가지를 출력하십시오.
    질문 난이도 {level} || 스택 {subject}
    실무에서 사용할 법한 난이도의 면접 질문을 출력하십시오. 어떤 꾸미는 문양 (ex. ** 등) 없이 면접 질문만 출력하십시오.
    """