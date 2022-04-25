def spin_words(sentence):
        arr=  sentence.split( )
        for x in range(len(arr)):
            if(len(arr[x])>4):
                arr[x]=arr[x][::-1]

        return   " ".join(arr)