# wordlist-similar-keyword

I wrote this code for optimizing my site's SEO.

You can use this repository for getting list of similar words by keyword.
And by these words list you'll get more relevant keywords, which user asked

#******************** Algorithm ********************#

Class based
- get keyword
- define lang (EN-RU)
- read file (EN-RU)
- find word, where word=keyword *
- find words (don't forget count), where word contains keyword, add results to array (by priority)*
	- find words, where word startswith keyword *
	- find words, where word endswith keyword *
	- find words, where word contains keyword (between, not included endswith & startswith) *
- find words, where word~=keyword (similar to keyword, differs with one letter)
return results array


*Don't need if we need only word's similar variants (because SQL LIKE operator solves these)

#******************** Algorithm finished ********************#

Special thanks to
-	Github user "Danakt", I used russian words list, which Danakt hosted to Github (https://github.com/danakt/russian-words)
-	Github user "dwyl", I used english words list, which dwyl hosted to Github (https://github.com/dwyl/english-words)
