import md5 

def main():
    filename = raw_input()    
    m = md5.new()
    m.update(filename)
    print m.hexdigest()    
        
                 







if __name__ == "__main__":
    main()
