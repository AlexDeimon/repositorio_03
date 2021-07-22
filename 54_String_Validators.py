S=input();
if(any(s.isalnum() for s in S)):
    print('True')
else:
    print('False')
if(any(s.isalpha() for s in S)):
    print('True')
else:
    print('False')
if(any(s.isdigit() for s in S)):
    print('True')
else:
    print('False')
if(any(s.islower() for s in S)):
    print('True')
else:
    print('False')
if(any(s.isupper() for s in S)):
    print('True')
else:
    print('False')