# Turing Machines and Binary Code

Today we're going to look at some demystifying concepts in the world of software. Some of you might have done  coding in the past, but there's a lot going on behind the scenes that can make programming seem magical. The problem with that is we're not in the business of computer _magic_, we're in the business of computer _science_!

If we can understand how a computer works, we can understand how it works with our code. If we can understand how a computer works with our code, things don't seem as magical anymore.

Let's explore a few concepts and see if we can connect the dots with real code!

### Prerequisites

For this lesson you'll need to have _Python 2.7_ installed. If you're on Mac or Linux, this should already be preinstalled on your system. If you're on Windows, you may need to [download it](http://www.python.org/download/releases/2.7.6/).

## Part 1 - The Turing Machine

![Alan Turing](http://upload.wikimedia.org/wikipedia/en/c/c8/Alan_Turing_photo.jpg")

Time for a brief history lesson. [Alan Turing](http://en.wikipedia.org/wiki/Alan_Turing) was a highly influential British mathemetician. He is famous for breaking many of the German encryption codes during World War II. He was a crazy hacker over **70** years ago!

In 1936, Turing came up with a _hypothetical_ device that could run any **algorithm**. His device worked like an advanced _tape recorder_. He called it a "Logical Computing Machine," but we've come to know it as a **Turing Machine**. It's made up of the following parts.

* A **magnetic tape** divided into cells, one next to the other. Each cell can store a single symbol or **character**. Each character has to be a member of the machine's **alphabet**, but the alphabet can be any collection of symbols. Every alphabet contains a "blank" symbol, and when the machine is first activated, every cell on the tape is set to "blank." A Turing Machine needs at least enough tape to perform its computation, and so a theoretical Turing Machine is thought to have _infinite tape_.
* A **head** that can read and write symbols on the tape and move the tape left and right one (and only one) cell at a time.
* A **state register** that stores the **state** of the machine. State is an abstract concept, but think of it as the machine's "state of mind." For example, when you're doing a tough math problem you figure it out step by step. At each step, you know how much of the problem you've solved and you have a corresponding set of numbers floating in your mind. The Turing machine can do that too, it just uses its **state register** instead of a mind.
* An **action table** that tells the machine what to do next depending on the **state** and the position of the **head**. An **action** is always in this sequence:
	1. Erase, write, or keep the symbol on the tape that is under the head, _and then_
	2. Move the head one cell left, one cell right, or stay in place, _and then_
	3. Assume the same or a new state

Let's see an example of a Turing machine in action ([Jump to 3:19 in the video](http://www.youtube.com/embed/E3keLeMwfHY?t=3m19s))

## So... where can I get a Turing Machine?

Well, as you can see, an old-fashioned Turing Machine runs a bit slowly. Luckily, we've had decades of progress on top of Turing's original hypothesis, and modern computers have been designed with Turing's theories in mind. In order to make computers **faster**, and make using them **easier**, some changes were made to the design.

* Instead of a tape and a head, we now have a **hard disk**. They basically work the same way, with tons and tons of cells sitting next to each other, each cell storing a single character or **byte**. If you look up a picture of a hard drive, you'll see it has a head too that's used for reading and writing to a magnetic disk.
* Instead of a state register, we now have **random access memory** or **RAM**. RAM remembers the state of the computer, but it has the ability to remember the state of multiple programs at the same time.
* Instead of an action table we have a **program**. The program tells the **operating system** (That's Mac OS, Windows, Linux, etc) how to manipulate RAM, the hard disk, or any other hardware connected to the computer.

### Programming Example

Today we're going to be writing some simple scripts in _Python 2.7_ to demonstrate how these fundamental concepts relate to programming. Let's create a new file called `turing.py`.

```
# The Turing machine starts up, all cells are blank.

# Move the head to the first cell, write 1
cell_one = 1

# Move the head to the second cell, write 2
cell_two = 2

# Move to the first cell and read the value
print cell_one

# Move to the second cell and read the value
print cell_two
```

Now, let's open a **terminal** or **command prompt** window. A mentor can show you how to use `cd` to change to the directory you stured `turing.py` in. Now we're going to run `python turing.py` and see what happens.

```
1
2
```

What happened here? Let's start on the first line. All the lines that start with a `#` are called **comments**. The `#` tells Python to ignore the rest of the line, so we can type whatever we want after it. Comments are helpful for keeping track of what our code is doing, or leaving behind tips for other people who might end up reading it.

Then we wrote 1 into the first cell, and 2 into the second cell. But let's make a distinction here... The **cell** is actually what the computer is storing into at the hardware level. The program has an **operating system** between it and the hardware, so the program actually can't see the cell from its perspective. Behind the scenes, the **operating system** is storing the values in a **register**, which is basically a group of cells that can store any number of bytes. When we give the register a name in our program, like `cell_one` or `cell_two`, that is called a **variable**.

Then we told the program to **print** the values of those variables. In programming, **print** generally doesn't refer to spitting a piece of paper out of your computer, it is just a way to tell the program to display a given value. **Print** is called called **log** or **echo** in other languages.

So, are `cell_one` and `cell_two` actually being stored on the hard disk? Actually, your **operating system** is doing a lot of work behind the scenes to speed things up. RAM and the hard disk work in a very similar way, and your operating system figures out whether to store **registers** in RAM or on the hard disk. If you want your program to create a file on the hard disk that can be read later, that is possible too.

### Break time.

Any questions?

## Part 2 - Binary

We saw in the Turing machine example video an example of **binary code**, which is a series of `0`s and `1`s. We discussed how a modern computer can store a single character or **byte** in a cell. We might have heard before that everything on a computer operates in **binary**, but how do all of these concepts relate?

It all starts with the [transistor](http://en.wikipedia.org/wiki/Transistor). A transistor is a device in an electronic circuit that can both **switch** the signal path and **amplify** its input signal. This has some important implications:

1. The switch can either be on (`1`) or off (`0`)
2. Many transistors can be put in series and each can amplify the signal enough so that the signal flows to the next part of the circuit.

Because each transistor can reflect a `0` or `1`, or **binary** value, and because many transistors can be linked together without degrading the electrical signal, transistors have become useful as a means of storage. But how on earth can storing just `0`s and `1`s be useful?

### Double Base Breakdown

It turns out that by using a mathematical device called a [**change of base**](http://en.wikipedia.org/wiki/Radix), binary values can be combined and used to express more complex values than `0` and `1`.

#### Take a deep breath, it's time for some math!

Our natural counting system is more precisely called the **decimal system**, and it has a base of `10`. Bases work off of the position of the **digits** in the number. The number of potential digits in a base is equal to the value of the base, so base 10 has 10 possible digits it can express numbers with. The digits always include `0`. If you count how many numbers are between `0` and `9`, you'll find there are `10`, so `0 - 9` is the digit set for base 10.

To figure out the decimal value of a number in a different base, the value of each digit is multiplied by the base to the power of the digit's position, then all those are added together.

> "to the power of" just means multiplying a number by itself that many times. This is called an **exponent**.

Let's explain the decimal number `123`. We are going to convert it from base 10 to base 10, so the number won't actually change, but breaking it down will help explain the concept:

* 3 is in the 0th positon, 2 is in the 1st position, 1 is in the 2nd position.
* The value of the 0th digit is `3`, and the base is 10, so its decimal value is `3 * 10 ^ 0`, or `3 * 1`. Any number to the 0th power is `1`. `3 * 1` equals `3`
* The value of the 1st digit is `2`, so its decimal value is `2 * 10 ^ 1`, or `2 * 10`, which equals `20`.
* The value of the 2nd digit is `1`, so its decimal value is `1 * 10 ^ 2`, or `1 * 10 * 10`, which equals `100`.
* Now we add them all together, `3 + 20 + 100`, which equals `123`!

The **binary system** is base 2, which contains only 2 digits including `0`. That only leaves room for one more, the digit `1`. That's perfect for transistors!

Let's look at an example binary number, `101010`, and convert it to decimal:

* The value of the 0th digit is `1`, and the base is 2, so its decimal value is `0 * 2 ^ 0`, or `0 * 1`, which equals `0`.
* The value of the 1st digit is `1`, so its decimal value is `1 * 2 ^ 1`, or `1 * 2`, which equals `2`.
* The value of the 2nd digit is `0`, so its decimal value is `0 * 2 ^ 2`, or `0 * 2 * 2`, which equals `0`.
* The value of the 3rd digit is `1`, so its decimal value is `1 * 2 ^ 3`, or `1 * 2 * 2 * 2`, which equals `8`.
* The value of the 4th digit is `0`, which will equal `0` as well
* The value of the 5th digit is `1`, so its decimal value is `1 * 2 ^ 5`, or `1 * 2 * 2 * 2 * 2 * 2`, which equals `32`.
* Now we add them all together: `2 + 8 + 32` which equals `42`; the meaning of life, the universe and everything!

#### Bit by bit...

So now we know how we can use the **binary system** to express large numbers with just `1`s and `0`s. In computing, a single `1` or `0` is known as a **bit**. Well, even though numbers are useful and all, humans think in terms of words. Raw numbers don't leave us with a way to express readable text in a way that the computer can store.

Computer scientists were trying to solve this exact problem about 50 years ago. Computers needed to support the uppercase alphabet (26 characters), the lowercase alphabet (26 characters), numerals (10 characters), plus punctuation and special characters. Computers didn't have a lot of storage space at the time, so the scientists needed to figure out a way to fit a way to express those characters in the smallest amount of space per character.

It turned out that **8 bits** could store 256 different combinations (Binary `11111111` is equal to the decimal number 255), and so eventually **8 bits** became the compromise between space and flexibility for storing a single character. This became known as a **byte**.

Because individual bits tend to be cumbersome, most computer systems now don't store anything in units smaller than a **byte**. Good thing too, since computers have been skyrocketing into *kilobytes* (1024 bytes), *megabytes* (1024 kilobytes), *gigabytes* (1024 megabytes), and *terabytes* (1024 gigabytes) over the past few decades.

## Fun with Binary

Since computers don't store anything in units smaller than a **byte**, the registers behind our variables can't be smaller than 8 bits. Numbers in programming languages are expressed in decimal (base 10) by default, just because that is what is the most intuitive number system for people to understand. The operating system converts the numbers to and from binary behind the scenes. However, it is possible to manipulate the backing binary structure of a number. Let's start a new file `binary.py`.

```
num = 1          # Backing binary is 00000001
print num

# Shift num 1 bit to the left using <<
num = num << 1   # Backing binary is now 00000010
print num

# Keep shifting...
num = num << 1   # Backing binary is now 00000100
print num

num = num << 1   # Backing binary is now 00001000
print num

num = num << 1   # Backing binary is now 00010000
print num

num = num << 1   # Backing binary is now 00100000
print num

num = num << 1   # Backing binary is now 01000000
print num

num = num << 1   # Backing binary is now 10000000
print num

```

When we run `python binary.py`, we see the following output:
```
1
2
4
8
16
32
64
128
```

Can anybody figure out why? As we change the backing binary representation of the number,
it gets converted back into decimal using the change of base formula. 

### Break

Questions or comments about binary?

## Conclusion

Hopefully visiting the concepts of the Turing Machine and Binary Code helped you figure out how computers work on a deeper level. Everything in computing is designed by **abstraction**, which is the concept of smaller parts combining to make a bigger part that can be seen as its own unit. We have learned how our computers are an abstraction of a Turing Machine, and how the data in our computers is an abstraction of binary code.

Thanks for your participation!