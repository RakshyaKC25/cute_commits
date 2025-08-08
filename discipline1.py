import random
import datetime
import argparse

quotes = [
    {"quote": "Discipline is choosing between what you want now and what you want most.", "author": "Ada Lovelace"},
    {"quote": "We carry all the power we need inside ourselves already.", "author": "J.K. Rowling"},
    {"quote": "The most courageous act is still to think for yourself. Aloud.", "author": "Coco Chanel"},
    # Add more quotes here...
]

def show_quote():
    selected = random.choice(quotes)
    today = datetime.date.today()
    print("\n🌱 Discipline Quote of the Day")
    print("-" * 40)
    print(f"\"{selected['quote']}\"")
    print(f"— {selected['author']}")
    print(f"📅 {today}\n")
    return selected, today

def log_quote(quote, date):
    with open("quote_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{date}: \"{quote['quote']}\" — {quote['author']}\n")

def main():
    import sys
    log = "--log" in sys.argv
    quote, date = show_quote()
    if log:
        log_quote(quote, date)
        print("📝 Quote logged to quote_log.txt")

if __name__ == "__main__":
    main()

