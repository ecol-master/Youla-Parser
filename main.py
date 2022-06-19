from parser import Parser
import datetime


def get_format_date() -> str:
   format_date = datetime.datetime.now().strftime("%d_%m_%Y__%H_%M")
   return format_date

def main():
   format_date = get_format_date()
   parser = Parser(format_date=format_date)
   parser.run_parser()

if __name__ == "__main__":
    main()