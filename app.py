from gsheet import read_gsheet

def main():
    print(read_gsheet('Feuille 1!A1:B2'))

if __name__ == '__main__':
    main()