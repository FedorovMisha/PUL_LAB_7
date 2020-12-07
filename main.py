import re


text = "Baseball! Became@ popular in Japan after American soldiers introduced it during the occupation following World " \
       "War II. In the 1990s a Japanese player, Hideo Nomo, became a star pitcher for the Los Angeles Dodgers. " \
       "Baseball is also widely played in Cuba and other Caribbean nations. In the 1996 Olympics, it was a measure of " \
       "baseball’s appeal outside the United States that the contest for the gold medal was down to Japan and Cuba (" \
       "Cuba won). "

text = text.lower()
print(text)
# pattern = re.compile(r"[-.?!)(,:]")
pattern = re.compile(r"([.,\/#!$%\^&\*;:{}=\-_`~()])")
# new_pattern = re.compile(r"[ ^][aeiou][a-z]*[bcdfghjklmnpqrstvxz]")
result = re.findall(pattern, text)
result.append("".join(re.findall(r"\.{3,}", text)))


print(result)
