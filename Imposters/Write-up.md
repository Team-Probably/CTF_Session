## Imposters

### Description

Some things may pretend to be something they are not.

[re.py](./re.py)

Figure out what this atrocity of a code does to get the flag 

**Points**: 300

----------------------------------------------------

##### Hints to the Solution

> Several hints here

The first thing that comes to your mind ( hopefully ) is why in hell are there 3 definitions of **converts** . Look closely though! ( **Hint**: Even Github highlights them in different colours! )

The same mischief that is up wih **converts** is applied to the variables **flags** and **sr**

Don't overlook the self-XOR! Also remember that A ⊕ B ⊕ A = B

Oh! And those lists of numbers? Don't they look awfully similar to ASCII Codes?

##### Steps to the Solution
* Though all **converts** functions look the same to humans, they are different to the computer ( as one uses plain english letters, one uses an exotic (unicode) **s** and one uses an exotic **e**) . A good text editor can help you easily differentiate them.
* The same is the case with the variables **flags** and **sr**
* All 3 definitions of **converts** are executed (figure out in what order) with the output of one passed as input to the other. Though only one of these is actually doing something that persists.
* Which **coverts** is actually doing something? Use the understanding of **flags** and **sr** to figure this one out.
* The input **inp** is broken down into a list of digits.
* The self-xor and the above mentioned property of XOR should be a starting point to generate the values of **inp** list
* Once you calculate the correct value of inp, it will generate the flag for you