from transliterate import translit
from num2words import num2words

text = """Ladies and gentlemen, I'm """ + translit(num2words(78),'ru') + """ years old and I finally got """ + translit(num2words(15),'ru') + """ minutes of fame once in a lifetime and I guess that this is mine. People have also told me to make these next few minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen.

More than """+ translit(num2words(3),'ru') + """ years ago I moved to Novo-Novsk, but worked on new Magnetic Storage for last """ + translit(num2words(40),'ru') +""". When I was"""+ translit(num2words(8),'ru') + """..."""

print(translit(text,'ru')) 