# Look Closer

### Problem

>An image of an iphone homescreen is given and you have to find a way to capture the flag.
>This challenge is meant for you to find something wrong in everything that looks perfect.

------------------------------------------------
##### Hints to the Solution
- See the image carefully and find out what's odd in it.
- Check the source code of the webpage to find the solution.

##### Steps to solve 
- The QR code in the phone jpeg is to be scanned.
- On scanning you'll get a link where some random no. are apearing one after the other.
- Inspect the code in the inspect element tab and in the .js file you'll find an array of the nos that are being displayed.
- Each no. is the ASCII value of the alphabets.
- On decoding each no. you will be able to capture the flag that was hidden.
