import os.path

if os.path.isfile("phones.txt"):
    print("동일한 이름의 파일이 이미 존재합니다.")
    
else :
    outfile = open("phones.txt", "w")
    outfile.write("홍길동 010-1234-5678\n")
    outfile.write("김철수 010-1234-5679\n")
    outfile.write("김영희 010-1234-5680\n")
    outfile.close()

infile = open("phones.txt","r")
for line in infile:
    line = line.rstrip()
    print(line)
infile.close()


