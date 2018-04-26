def minimumStrength(password):
    lower = [i for i in password if i.islower()]
    upper = [i for i in password if i.isupper()]
    number = [i for i in password if i.isdigit()]
    return (len(lower)>0 and len(upper)>0 and len(number)>0)

print minimumStrength("hello")
print minimumStrength("Hello")
print minimumStrength("H3ll0")

def strengthRating(password):
    if (not(minimumStrength(password))):
        return 1
    else:
        lower = [i for i in password if i.islower()]
        upper = [i for i in password if i.isupper()]
        number = [i for i in password if i.isdigit()]
        special = [i for i in password if i in ".?!&#,;:-_*"]
        strength = (len(special)+len(number))/len(password)+len(password)
        if (strength > 10):
            return 10
        else:
            return strength


print strengthRating("heLOw")
print strengthRating("Hell0ww/**")
