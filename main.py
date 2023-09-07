import opg


def main():
    while True:
        choice = int(input("What do you want to generate? (1 - NPC, 2 - MISSION)\n- "))

        match choice:
            case 1:
                print(opg.Generator().NPC())
            case 2:
                print(opg.Generator().MISSION())


if __name__ == '__main__':
    main()
