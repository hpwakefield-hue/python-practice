# Crambox - turn messy notes into bite-sized revision Boxes
# Under 75 lines - beginner friendly

boxes = {}  # box_name -> {"notes": [], "cards": []}

def pick_box():
    name = input("Box name: ").strip()
    return name if name in boxes else None

def create_box():
    n = input("New box name (e.g. Biology Midterm): ").strip()
    if n and n not in boxes:
        boxes[n] = {"notes": [], "cards": []}
        print(f"Box '{n}' created!")
    else: print("Name taken or empty.")

def add_note():
    b = pick_box()
    if not b: print("Box not found."); return
    note = input("Paste/type your note: ").strip()
    if note: boxes[b]["notes"].append(note); print("Note added!")

def add_card():
    b = pick_box()
    if not b: print("Box not found."); return
    q = input("Question: ").strip(); a = input("Answer: ").strip()
    if q and a: boxes[b]["cards"].append((q, a)); print("Flashcard added!")

def view_box():
    b = pick_box()
    if not b: print("Box not found."); return
    print(f"\n--- {b} ---")
    for i, n in enumerate(boxes[b]["notes"], 1): print(f"{i}. {n}")
    for i, (q, a) in enumerate(boxes[b]["cards"], 1): print(f"Card {i}: Q: {q} | A: {a}")
    if not boxes[b]["notes"] and not boxes[b]["cards"]: print("(empty - add notes!)")

def study():
    b = pick_box()
    if not b: print("Box not found."); return
    cards = boxes[b]["cards"]
    if not cards: print("No flashcards in this box yet."); return
    score = 0
    for q, a in cards:
        print(f"\nQ: {q}")
        guess = input("Your answer: ").strip()
        print(f"Correct answer: {a}")
        if guess.lower() == a.lower():
            print("Nice!"); score += 1
        else: print("Keep cramming!")
    print(f"\nDone! Score: {score}/{len(cards)}")

def main():
    print("Welcome to Crambox! Make bite-sized revision Boxes.")
    while True:
        c = input("\n1:New Box 2:Add Note 3:Add Card 4:View 5:Study 6:Quit > ").strip()
        if c == "1": create_box()
        elif c == "2": add_note()
        elif c == "3": add_card()
        elif c == "4": view_box()
        elif c == "5": study()
        elif c == "6": print("Happy cramming!"); break
        else: print("Pick 1-6")

if __name__ == "__main__":
    main()
