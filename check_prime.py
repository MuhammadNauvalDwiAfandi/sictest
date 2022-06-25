knwn_prm = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,87,91,97)

class Prime:
    def __init__(self,low,up):
        self.low = low
        self.up = up

    def chk_conv_bound(self):
        '''
        Check the input is int
        '''
        try:
            int(self.low)
        except:
            return 'error: lower bound is not a number'
        else:
            self.low = int(self.low)

        try:
            int(self.up)
        except:
            return 'error: upper bound is not a number'
        else:
            self.up = int(self.up)
        
        '''
        Check upper bound and lower bound
        '''
        if self.low <= 0:
            return 'error: lower bound is less or equal 0'

        if self.up <= 0:
            return 'error: upper bound is less or equal 0'

        if self.low > self.up:
            return 'error: lower bound is larger than upper bound'
        
        return 'pass'

    def chk_prime(self):                    # Must run via start_list_check or start_single_check
        
        '''
        Check in list known prime
        '''
        if self.low in knwn_prm:
            return 'prime'

        '''
        Check modulo 2
        '''
        if self.low % 2 == 0 or self.low == 1:
            self.reason = 2
            return 'not prime'
        
        '''
        Check if number is not in the list known prime
        '''
        compare = range(3,int(self.low**0.5)+1)
        for l in compare:
            if self.low % l == 0:
                self.reason = l
                return 'not prime'
        
        return 'prime'

    def chk_list(self):                     # Must run via start_list_check
        prm = []
        '''
        Loop to check low bound is prime using chk_prime function
        '''
        for k in range(self.low,self.up+1):
            if self.chk_prime() == 'prime':
                prm.append(self.low)
            self.low += 1
        return prm

    def fctr_prm(self):                     # Must run via cnt_fctr_prm
        '''
        Check the divisibility of value self.up with all list of prime in self.chk_list
        '''
        for k in self.chk_list():
            while True:
                if self.up < k :
                    break

                if self.up % k == 0:
                    self.f_prime.append(k)
                    self.up = int(self.up / k)
                        
                    if self.up % k ==0:
                        continue
                    break
                break

            if self.up < k:
                break
                
        return self.f_prime

    def cnt_fctr_prm(self):                 # Must run via start_factor_prime
        fctr = self.fctr_prm()
        hold_prm_fctr = []
        prime_factor = {}
        '''
        Create separate list contained unique prime factor
        '''
        for k in fctr:
            if k not in hold_prm_fctr:
                hold_prm_fctr.append(k)

        '''
        Count how many each prime in fctr
        '''
        for k in hold_prm_fctr:
            jmlh = 0
            for i in fctr:
                if i == k:
                    jmlh += 1
            prime_factor[k] = jmlh

        return prime_factor

    def start_list_check(self):
        if self.chk_conv_bound() == 'pass':
            return self.chk_list()
        return self.chk_conv_bound()

    def start_single_check(self):
        self.up = self.low * 2
        if self.chk_conv_bound() == 'pass':
            return self.chk_prime()
        return self.chk_conv_bound()

    def start_factor_prime(self):
        self.up, self.low = self.low, 1
        if self.chk_conv_bound() == 'pass':
            self.low = self.up
            if self.chk_prime() == 'prime':
                return {self.up : 1}
            
            self.f_prime = [self.reason]
            self.up = int(self.up / self.reason)
            self.low = 1
            return self.cnt_fctr_prm()
        return self.chk_conv_bound()


# class GCD_LCM:
#     def __init__(self,f1,f2):
#         self.f1 = f1
#         self.f2 = f2

#     def chk_inp(self):
#         try:
#             int(self.f1)
#             int(self.f2)
#         except:
#             return 'error: one of the input is not a number'
#         else:
#             self.f1 = int(self.f1)
#             self.f2 = int(self.f2)
        
#         return 'pass'

#     def find_GCD(self):
#         if 'error' in self.chk_inp():
#             return self.chk_inp()
        
#         if self.f1 - self.f2 == 1 or self.f1 - self.f2 == -1:
#             return 1
            
#         obj1 = Prime(self.f1,1)
#         obj2 = Prime(self.f2,1)
#         fact1 = obj1.start_factor_prime()
#         fact2 = obj2.start_factor_prime()
#         gcd = 1
#         for k in fact1.keys():
#             if k in fact2:
#                 if fact1[k] < fact2[k]:
#                     gcd *= k**fact1[k]
#                     continue
#                 gcd *= k**fact2[k]

#         return gcd

#     def find_LCM(self):
#         if 'error' in self.chk_inp():
#             return self.chk_inp()
#         return int(self.f1 * self.f2 / self.find_GCD())

'''
use ctrl + / to comment or uncomment certain line
'''

'''
self.reason adalah bilangan prima terkecil yang habis membagi input
'''

class euclid_algo:
    def __init__(self,a1,a2):
        self.a1 = a1
        self.a2 = a2
        try:
            int(self.a1)
            int(self.a2)
        except:
            self.error = 'error: input is not a number'
        else:
            self.a1 = int(self.a1)
            self.a2 = int(self.a2)
            self.error = ''
        if self.a1 < self.a2:                           #self.a1 must bigger than self.a2
            self.a1, self.a2 = self.a2, self.a1
        
    def algo(self):
        if 'error' in self.error:
            return self.error
        if self.a1 - self.a2 == 1:                      #fact: gcd consecutive numbers always 1
            self.gcd = 1
            return 1

        if self.a1 % self.a2 == 0:                      #fact: if one number is divisible by other, then gcd is the other number
            self.gcd = self.a2
            return self.a2

        rmd = self.a1 % self.a2                         #pembagi
        bg = self.a2                                    #yang dibagi
        while rmd != 0:
            mdl = rmd
            if bg % mdl == 0:
                self.gcd = rmd
                return rmd
            rmd = bg % mdl
            bg = mdl

    def lcm(self):
        if 'error' in self.error:
            return self.error
        
        return int(self.a1 * self.a2 / self.gcd)


def check_prime(a,b):
    obj1 = Prime(a,b)
    hasil = obj1.start_single_check()
    print('-'*15)
    if hasil == 'prime':
        print(f'{a} is {hasil}')
    elif hasil == 'not prime':
        alasan = obj1.reason
        print(f'{a} is {hasil}. {a} is divisible by {alasan}')
    else:
        print(hasil)
    print('-'*15)
        

def list_prime(a,b):
    obj1 = Prime(a,b)
    hasil = obj1.start_list_check()
    print('-'*15)
    if 'error' in hasil:
        print(hasil)
    else:
        print(f'There are {len(hasil)} prime(s) in range {a}-{b}. List:')
        print(hasil)
    print('-'*15)

def factor_prime(a,b):
    obj1 = Prime(a,b)
    hasil = obj1.start_factor_prime()
    print('-'*15)
    if 'error' in hasil:
        print(hasil)
    else:
        print(f'Prime factor of {a}:')
        print(hasil)
        print('{prime:index}')
    print('-'*15)

def find_GCD_LCM(a,b):
    obj1 = euclid_algo(a,b)
    gcd = str(obj1.algo())
    lcm = str(obj1.lcm())
    print('-'*15)
    if 'error' in gcd:
        print(gcd)
    else:
        print(f'GCD: {gcd}, LCM: {lcm}')
    print('-'*15)

def start_program():
    print('='*15)
    print('Prime Tools')
    print('='*15)
    print('Available option:')
    print('1 Check single prime number')
    print('2 List prime number within spesific range')
    print('3 Find prime factor of a number')
    print('4 Find GCD and LCM from two numbers')
    act = input('Enter action: ')
    print('-'*15)
    if act == '1' or act == 'check':
        a = input('Enter prime number: ')
        b = 1
        check_prime(a,b)
    elif act == '2' or act == 'list':
        a = input('Enter lower bound: ')
        b = input('Enter upper bound: ')
        list_prime(a,b)
    elif act == '3' or act == 'factor':
        a = input('Enter number: ')
        b = 1
        factor_prime(a,b)
    elif act == '4' or act == 'gcd':
        a = input('Enter number: ')
        b = input('Enter number: ')
        find_GCD_LCM(a,b)
    else:
        print('Please enter number specified!')
        start_program()

start_program()