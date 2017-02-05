import md5
import sys 

def main():
    if len(sys.argv) < 2:
        print "%s [filename]" % sys.argv[0]
        exit()
    filename = sys.argv[1]
    file_object = open(filename, 'rb')   
    data = file_object.read()    

    m = md5.new()
    m.update(data)
    print m.hexdigest()
    
    file_object.close()    

if __name__ == "__main__":
    main()
