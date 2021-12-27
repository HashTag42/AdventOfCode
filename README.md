# AdventOfCode
Solutions to the [Advent of Code](https://adventofcode.com/) puzzles

---
# [2021](https://adventofcode.com/2021)

### [2021-18](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-18): [Snailfish](https://adventofcode.com/2021/day/18)


### [2021-17](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-17): [Trick Shot](https://adventofcode.com/2021/day/17)


### [2021-16](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-16): [Packet Decoder](https://adventofcode.com/2021/day/16)


### [2021-15](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-15): [Chiton](https://adventofcode.com/2021/day/15)


### [2021-14](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-13): [Extended Polymerization](https://adventofcode.com/2021/day/14)

* An efficient solution is similar to that in 2021-06 (Lanternfish). Keep a list of buckets for the pairs, calculate the next step per bucket, and multiply the results per the number pairs in each bucket.
* Fully implemented the [.NET IEquatable interface](https://docs.microsoft.com/en-us/dotnet/api/system.iequatable-1.equals).


### [2021-13](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-13): [Transparent Origami](https://adventofcode.com/2021/day/13)

* Created a 'Point' class. Couldn't find an implementation on the .NET library.

### [2021-12](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-12): [Passage Pathing](https://adventofcode.com/2021/day/12)

* Created a 'Cave' class, including full support for the IEquatable interface.

### [2021-11](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-11): [Dumbo Octopus](https://adventofcode.com/2021/day/11)

* Created a DumboOctopus class and a DumboOctopusCell derived class.
* Thought out the problem could be solved using a Queue and no recursion.
* Designed the algorithm outling using a Excel spreadsheet.

### [2021-10](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-10): [Syntax Scoring](https://adventofcode.com/2021/day/10)

### [2021-09](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-09): [Smoke Basin](https://adventofcode.com/2021/day/9)

* Used recursion to find all locations in a basin.

### [2021-08](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-08): [Seven Segment Search](https://adventofcode.com/2021/day/8)
* Used chryptography fundaments to decode the inputs.

### [2021-07](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-07): [The Treachery of Whales](https://adventofcode.com/2021/day/7)

### [2021-06](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-06): [Lanternfish](https://adventofcode.com/2021/day/6)

* The key aspect for an efficient solution is that lanterfishes can be grouped by their number of days left, and the next day calculation needs only to be done on one instance per group.
* Used the [.NET Diagnostics.Stopwatch Class](https://docs.microsoft.com/en-us/dotnet/api/system.diagnostics.stopwatch) to measure how long it takes to find a solution.

### [2021-05](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-05): [Hydrothermal Venture](https://adventofcode.com/2021/day/5)

### [2021-04](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-04): [Giant Squid](https://adventofcode.com/2021/day/4)

### [2021-03](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-03): [Binary Diagnostic](https://adventofcode.com/2021/day/3)

### [2021-02](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-02): [Dive!](https://adventofcode.com/2021/day/2)

### [2021-01](https://github.com/HashTag42/AdventOfCode/tree/main/2021/2021-01): [ Sonar Sweep](https://adventofcode.com/2021/day/1)
---

# [2015](https://adventofcode.com/2015)

### 2015-07 [Some Assembly Required](https://adventofcode.com/2015/day/7)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-07).
* Using [C# Bitwise and shift operators](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/operators/bitwise-and-shift-operators).

### 2015-06: [Probably a Fire Hazard](https://adventofcode.com/2015/day/6)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-06).
* Classes created: Command, Instructions, and Grid. Used tuples for coordinates.

### 2015-05: [Doesn't He Have Intern-Elves For This?](https://adventofcode.com/2015/day/5)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-05).

### 2015-04: [The Ideal Stocking Stuffer](https://adventofcode.com/2015/day/4)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-04).

### 2015-03: [Perfectly Spherical Houses in a Vacuum](https://adventofcode.com/2015/day/3)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-03).

### 2015-02: [I Was Told There Would Be No Math](https://adventofcode.com/2015/day/2)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-02).

### 2015-01: [Not Quite Lisp](https://adventofcode.com/2015/day/1)

* [Solution](https://github.com/HashTag42/AdventOfCode/tree/main/2015/2015-01).

___

# Tips and Tricks

* Getting the length of a dimension in a multidimensional array:

  `anArray.GetLength(dimension)`

* Printing a list of chars:

  `List<char> myChars = new List<char>("abcde");`
  `Console.WriteLine(new string(myChars.ToArray()));`
