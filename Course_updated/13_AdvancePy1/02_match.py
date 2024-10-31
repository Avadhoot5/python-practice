n = int(input('Enter a number to check network status: '))

def httpStatus(n):
    match (n):
        case 100:
            return 'Informational status'
        case 200:
            return 'Sucess'
        case 300:
            return 'Redirectional Request'
        case 404:
            return 'Error NOT FOUND'
        case 500:
            return 'Server Error'
        case _:
            return 'Unknown status'
        
print(httpStatus(n))


