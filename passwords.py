
# add to lists for each type: upper, lower, num if they're in pwd and check if all lists are not empty
def min_pwd(pwd):
    asc_pwd = [ord(x) for x in pwd]
    up = [x for x in [y for y in range(ord('A'), ord('Z')+1)] if x in asc_pwd]
    low = [x for x in [y for y in range(ord('a'), ord('z')+1)] if x in asc_pwd]
    num = [x for x in [y for y in range(ord('0'), ord('9')+1)] if x in asc_pwd]
    return len(up) > 0 and len(low) > 0 and len(num) > 0

#add to lists for each type; if they're not empty, add to rate
def rate_strength(pwd):
    asc_pwd = [ord(x) for x in pwd]
    rate = 0;
    if [x for x in [y for y in range(ord('A'), ord('Z')+1)] if x in asc_pwd]:
        rate += 2
    if [x for x in [y for y in range(ord('a'), ord('z')+1)] if x in asc_pwd]:
        rate += 2
    if [x for x in [y for y in range(ord('0'), ord('9')+1)] if x in asc_pwd]:
        rate += 2
    if [x for x in [ord(x) for x in '.?!&#,;:-_*'] if x in asc_pwd]:
        rate+= 4
    return rate
    
print ""
print "CHECKING MIN THRESHOLD"
print "password: ABC"
print min_pwd('ABC')
print "password: ABC0"
print min_pwd('ABC0')
print "password: AbC0"
print min_pwd('AbC0')
print "password: AbC0#" #should be 10
print min_pwd('AbC0#')

print ""
print "CHECKING RATE"
print "password: ABC" #should be 2
print rate_strength('ABC')
print "password: ABC0" #should be 4
print rate_strength('ABC0')
print "password: AbC0" #should be 6
print rate_strength('AbC0')
print "password: AbC0#" #should be 10
print rate_strength('AbC0#')
print "password: AbC0#!" #should be 10
print rate_strength('AbC0#')
