from services.qa import ask_question
from services.summarize import summarize_paper
from services.hypothesis import find_hypothesis
from services.methodology import find_methodology

from utils.json_parser import pretty_json, extract_json
from evaluation.evaluation import Evaluation

from rag.vector_store import create_vector_store


def upload_paper():

    path = input("\n请输入PDF路径:")

    create_vector_store(path)

    print("\n论文加载完成!")
    print("1. Upload Paper")
    print("2. Ask Question")
    print("3. Summarize Paper")
    print("4. Find Hypothesis")
    print("5. Find Methodology")
    print("6. Exit")


def show_menu():

    print("\n==============================")
    print(" AI Paper Assistant")
    print("==============================")
    print("1. Load Paper")
    print("2. Ask Question")
    print("3. Summarize Paper")
    print("4. Find Hypothesis")
    print("5. Find Methodology")
    print("6. Exit")


def main():

    evaluator = Evaluation()

    while True:

        show_menu()

        choice = input("\n选择功能：").strip()

        if choice == "1":

            upload_paper()

        elif choice == "2":

            question = input("\n请输入问题：")

            answer = ask_question(question)

            print("\n==============================")
            print("AI Answer")
            print("==============================\n")

            print(answer)
        elif choice == "3":

            print("\n正在总结论文...\n")

            answer = summarize_paper()

            print(answer)

        elif choice == "4":

            print("\n正在寻找假说...\n")

            answer = find_hypothesis()

            print(answer)

        elif choice == "5":

            print("\n正在分析研究方法...\n")

            answer = find_methodology()

            print("\n========== Methodology ==========\n")

            print(pretty_json(answer))

            data = extract_json(answer)

            if data:

                print("\n========== Evaluation ==========\n")

                result = evaluator.evaluate(data)

                print(f"JSON Valid       : {result['json_valid']}")
                print(f"Completeness     : {result['completeness']}%")
                print(f"Overall Score    : {result['overall_score']}")

            else:

                print("\nJSON解析失败，无法评估。")

        elif choice == "6":

            print("\nBye!")

            break

        else:

            print("\n请输入正确编号（1~6）")


if __name__ == "__main__":
    main()
