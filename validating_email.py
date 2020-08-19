def fun(s):
    try:
        x=s.split('.')
        y=s.split('@')
        username=y[0]
        user=username.replace('_','t').replace('-','t')
        temp=y[1].split('.')
        web=temp[0]
    except:
        return False
    
    if(len(x)<2):
        return False
    
    elif(len(y)!=2):
        return False

    elif not(web.isalnum()):
        return False
    
    elif not(len(x[1])==3 or len(x[1])==2):
        return False

    elif not('@' in s):
        return False

    elif not(user.isalnum()):
        return False

    else:
        return True

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
