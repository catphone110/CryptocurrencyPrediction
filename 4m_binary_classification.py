
import json




def main():
    # read data
    text = json.load(open('reddit_data.json'))

    print(text['20180326'][0])

    fin = open("old_price.txt", "r")
    fout = open("price.txt", "w")

    for line in fin:
        fout.write(line.replace(',', ' '))





if __name__ == "__main__":
    main()