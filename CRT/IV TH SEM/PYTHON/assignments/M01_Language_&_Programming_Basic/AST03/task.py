def student_grade_system(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3
    status = "Pass" if avg >= 50 else "Fail"
    return f"Average grade: {avg:.2f}, Status: {status}"


if __name__ == '__main__':
    name = input()
    n1, n2, n3 = map(int, input().split())
    print(student_grade_system(name, n1, n2, n3))
