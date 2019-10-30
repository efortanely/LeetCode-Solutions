class Solution:
    def nextClosestTime(self, time: str) -> str:
        t1 = time[0]
        t2 = time[1]
        t3 = time[3]
        t4 = time[4]
        min_time = ''
        min_int = sys.maxsize
        for i in [t1, t2, t3, t4]:
            for j in [t1, t2, t3, t4]:
                #Same hour
                time = t1 + t2 + ':' + i + j
                new_int = int(i+j) - int(t3+t4)
                if new_int < min_int and new_int > 0 and int(i+j) < 60:
                    min_int = new_int
                    min_time = time
        
        for i in [t1, t2, t3, t4]:
            for j in [t1, t2, t3, t4]:
                for k in [t1, t2, t3, t4]:
                    #later hour
                    time = t1 + i + ':' + j + k
                    new_int = 60 * (int(t1+i) - int(t1+t2)) + int(j+k) - int(t3+t4)
                    if new_int < min_int and new_int > 0 and int(j+k) < 60 and int(t1+i) < 24:
                        min_int = new_int
                        min_time = time
        
        for i in [t1, t2, t3, t4]:
            for j in [t1, t2, t3, t4]:
                for k in [t1, t2, t3, t4]:
                    #earlier hour, next day
                    time = t1 + i + ':' + j + k
                    new_int = 60*int(t1+i) + 60*(24-int(t1+t2)) \
                    + int(j+k) - int(t3+t4)
                    if new_int < min_int and new_int > 0 and int(j+k) < 60 and int(t1+i) < 24:
                        min_int = new_int
                        min_time = time
        
        return min_time
