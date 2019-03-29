# Cookies

### Description

[accounts.microsoft.com](https://accounts.microsoft.com)

[cookies.zip](./cookies.zip)

Given these links with no context, can you find the flag?

**Points**: 200

------------------------------------------------
##### Hints to the Solution
- The cookies zip (quite unsurprisingly) contains many .cookie files! Finding the relevant file though can feel like finding a needle in a haystack. 
- Once you find something interesting, use that to pretend to be someone who you are not to gain access to the site.
##### Steps to solve 
> I bet the guy who came up with the idiom "finding a needle in a haystack" would wish he had a tool like **grep** at his disposal. 
- Use grep to find the relevant cookie
- Inject the cookie to login to the site ( [This](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) may come in handy! )
- Once you so, you'll find the flag hiding in plain sight

