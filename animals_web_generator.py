from data_fetcher import fetch_data


def main():
    '''
    '''
    inp_animal = input("Enter a name of an animal: ")
    data = fetch_data(inp_animal)
    print(data)

if __name__ == "__main__":
    main()