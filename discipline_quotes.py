import random
import datetime
import argparse
import os

quotes = [
    {
        "quote": "We do not need magic to transform our world. We carry all the power we need inside ourselves already.",
        "author": "J.K. Rowling"
    },
    {
        "quote": "Life is not easy for any of us. But what of that? We must have perseverance and above all confidence in ourselves.",
        "author": "Marie Curie"
    },
    {
        "quote": "Discipline is choosing between what you want now and what you want most.",
        "author": "Ada Lovelace"
    },
    {
        "quote": "The most courageous act is still to think for yourself. Aloud.",
        "author": "Coco Chanel"
    },
    {
        "quote": "Success is not final, failure is not fatal: It is the courage to continue that counts.",
        "author": "Angela Davis"
    },
    {
        "quote": "My philosophy is that not only are you responsible for your life, but doing the best at this moment puts you in the best place for the next moment.",
        "author": "Oprah Winfrey"
    },
    {
        "quote": "I am deliberate and afraid of nothing.",
        "author": "Audre Lorde"
    },
    {
        "quote": "If you want something said, ask a man; if you want something done, ask a woman.",
        "author": "Margaret Thatcher"
    },
    {
        "quote": "Freedom is to live one's life in a way that one's choices are not dictated by fear.",
        "author": "Simone de Beauvoir"
    }
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
    parser = argparse.ArgumentParser(description="Discipline quotes by female philosophers")
    parser.add_argument("--log", action="store_true", help="Log the quote to quote_log.txt")
    args = parser.parse_args()

    quote, date = show_quote()

    if args.log:
        log_quote(quote, date)
        print("📝 Quote logged to quote_log.txt")

if __name__ == "__main__":
    main()
